from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.template.loader import get_template
from .models import (Invoice)
from django.contrib import messages
from django.http import HttpResponse
import re
import pdfkit
from django.conf import settings

from MainApp.models import (Klien)
from utilss.mainapp import (cek_status_pengguna, pt_detail)
from utilss.inv import (invoice_create, invoice_edit)


pattern_qty = re.compile(r"^\d*[.]?\d{0,2}$|^(\d+(\.\d{0,2})?%)$")
pattern_hs  = re.compile(r"^\d*$")

@login_required
def invoice_management(request, pk=None, tipe_req=None):
    user = request.user
    title = 'Manajemen Invoice'
    status_pengguna = cek_status_pengguna(user)

    kods = list([i.kode for i in user.user_pengguna.pt.all()])
    data_list = Invoice.objects.filter(pt__kode__in=kods).order_by('-id')

    query = request.GET.get('q')
    if query:
        data_list = data_list.filter(
            Q(nomor__icontains=query) |
            Q(klien__klien__icontains=query)
        ).distinct()

    paginator = Paginator(data_list, 15)
    page = request.GET.get('page')
    data_list = paginator.get_page(page)

    context = {
        'user': user,
        'title': title,
        'data_list': data_list,
        'bredcum': 'Manajemen Invoice',
        'bredcum_head': 'Invoice',
        'invoice_page': True,
        'query': query,
    }
    context.update(status_pengguna)

    if request.method == 'POST':
        aksi = request.POST['aksi']
        try:
            if request.POST['button_delete']:
                get_object_or_404(Invoice, pk=pk).delete()
                messages.success(request, "Invoice dihapus !")
                return redirect('MainApp:invoice')
        except:pass
        data_post = {
            'user': user,
            'klien': request.POST['konsumen'],
            'proyek': request.POST['pekerjaan'],
            # 'noinv': request.POST['noinv'],
            'nopospk': request.POST['nopospk'],
            'material' : request.POST.getlist('material'),
            'qty' : request.POST.getlist('qty'),
            'satuan' : request.POST.getlist('satuan'),
            'harga_satuan' : request.POST.getlist('harga_satuan'),
        }
        if list(filter(lambda v: not pattern_qty.match(v), data_post['qty'])):
            messages.error(request, "Qty must be number !")
            return HttpResponse('<script>history.back();</script>')
        if list(filter(lambda v: not pattern_hs.match(v), data_post['harga_satuan'])):
            messages.error(request, "Harga satuan must be number !")
            return HttpResponse('<script>history.back();</script>')
        if aksi == 'tambah_baru':
            hasil = invoice_create(data_post)
            if hasil['status_inv']:
                messages.success(request, "Invoice added !")
                return redirect('MainApp:invoice')
            else:
                messages.error(request, hasil['message'])
                return HttpResponse('<script>history.back();</script>')
        else:
            data_post.update({'cb_revisi': request.POST.get('revisi_cb'), 'instance': get_object_or_404(Invoice, pk=pk)})
            messages.success(request, "Invoice diupdate !")
            return redirect('MainApp:invoice_update', pk=invoice_edit(data_post))

    if tipe_req == 'add':
        context.update({'klien_list': Klien.objects.all().order_by('-pk')})
        return render(request, 'INV/inv_post.html', context)
    elif tipe_req == 'update':
        instance = get_object_or_404(Invoice, pk=pk)
        context.update({'instance': instance})
        context.update({'no_inv': instance.nomor.split('/')[2]})
        return render(request, 'INV/inv_post.html', context)
    return render(request, 'INV/inv.html', context)


@login_required
def invoice_cetak(request, pk=None):
    instance = get_object_or_404(Invoice, pk=pk)
    # potongan = {}
    # for i in instance.potongan.all():
    #     ea = instance.sub_total * (i.potongan/100)
    #     potongan[i.nama.capitalize()] = ea

    context = {
        'instance': instance,
        # 'notes' : NotesDict(instance.notes),
        # 'potongan': potongan,
        'row_span': str(len(instance.potongan.all())+2),
        'css_src1': settings.CSS1_WKHTML,
        'css_src2': settings.CSS2_WKHTML,
        'css_src3': settings.CSS3_WKHTML,
    }
    context.update(pt_detail(instance.pt))

    # The name of your PDF file
    # filename = '{}.pdf'.format(invoice.uniqueId)
    filename = instance.nomor

    # HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('INV/data_cetak.html')

    # Render the HTML
    html = template.render(context)

    # Options - Very Important [Don't forget this]
    options = {
        'encoding': 'UTF-8',
        'javascript-delay': '10',  # Optional
        'enable-local-file-access': None,  # To be able to access CSS
        'page-size': 'A4',
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
    }
    # Javascript delay is optional

    # Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=settings.GW_WKHTML)


    # Create the file
    file_content = pdfkit.from_string(
        html, False, configuration=config, options=options)

    # Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    # Return
    return response