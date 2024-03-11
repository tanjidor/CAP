from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.core.paginator import Paginator 
from django.db.models import Q
import pdfkit
from django.conf import settings
from django.http import Http404
from django.template.loader import get_template

from .models import (Klien, Kwitansi)
from INV.models import (Invoice)
from utilss.mainapp import (cek_status_pengguna, pt_detail)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success !")
            return redirect('MainApp:home')
        else:
            messages.error(request, "Login ERROR !")
            return redirect('MainApp:login')
    return render(request, 'MainApp/login.html', {})


@login_required
def home(request):
    user = request.user
    title = 'Home'
    status_pengguna = cek_status_pengguna(user)
    context = {
        'user': user,
        'title': title,
        'bredcum': 'Dashboard',
        'bredcum_head': 'Dashboard',
        'home_page': True,
    }
    context.update(status_pengguna)
    return render(request, 'MainApp/home.html', context)


@login_required
def klien_management(request, pk=None, tipe_req=None):
    user = request.user
    title = 'Manajemen Klien'
    klien_list = Klien.objects.all().order_by('-pk')
    status_pengguna = cek_status_pengguna(user)

    query = request.GET.get('q')
    if query:
        klien_list = klien_list.filter(
            Q(klien__icontains=query) |
            Q(kode__icontains=query)
        ).distinct()

    paginator = Paginator(klien_list, 10)
    page = request.GET.get('page')
    klien_list = paginator.get_page(page)

    context = {
        'user': user,
        'title': title,
        'klien_list': klien_list,
        'bredcum': 'Manajemen Klien',
        'bredcum_head': 'Klien',
        'klien_page': True,
        'query': query,
    }
    context.update(status_pengguna)
    
    if request.method == 'POST':
        aksi = request.POST['aksi']
        try:
            if request.POST['button_delete']:
                get_object_or_404(Klien, pk=pk).delete()
                messages.success(request, "Klien dihapus !")
                return redirect('MainApp:klien')
        except:pass

        if aksi == 'tambah_baru':
            nama = request.POST['nama'].upper()
            kode = request.POST['kode'].upper()
            kontak = request.POST['kontak']
            alamat = request.POST['alamat'].upper()
            email = request.POST['email']
            cp = request.POST['cp'].upper()
            if Klien.objects.filter(kode=kode).exists():
                messages.error(request, "Kode was exists !")
                return HttpResponse('<script>history.back();</script>')
            Klien.objects.create(klien=nama, kode=kode, telp=kontak, alamat=alamat, email=email, cp=cp)
            messages.success(request, "Klien ditambah !")
        else:
            a = get_object_or_404(Klien, pk=pk)
            a.klien = request.POST['nama'].upper()
            a.kode = request.POST['kode'].upper()
            a.telp = request.POST['kontak']
            a.alamat = request.POST['alamat'].upper()
            a.email = request.POST['email']
            a.cp = request.POST['cp'].upper()
            if Klien.objects.filter(kode=a.kode).exclude(pk=a.pk).exists():
                messages.error(request, "Kode was exists !")
                return HttpResponse('<script>history.back();</script>')
            a.save()
            messages.success(request, "Klien diupdate !")
        return redirect('MainApp:klien')

    if tipe_req == 'add':
        return render(request, 'MainApp/klien_post.html', context)
    elif tipe_req == 'update':
        klien = get_object_or_404(Klien, pk=pk)
        context.update({'klien': klien})
        return render(request, 'MainApp/klien_post.html', context)
    return render(request, 'MainApp/klien.html', context)


@login_required
def kwitansi_cetak(request, pk_src=None):
    try:
        instance_src = get_object_or_404(Invoice, pk=pk_src)
        instance = get_object_or_404(Kwitansi, sumber=instance_src.nomor)
    except:
        raise Http404("instance_src not found!!")

    context = {
        'instance': instance,
        'instance_src': instance_src,
        'css_src1': settings.CSS1_WKHTML,
        'css_src2': settings.CSS2_WKHTML,
        'css_src3': settings.CSS3_WKHTML,
    }
    context.update(pt_detail(instance_src.pt))

    # The name of your PDF file
    # filename = '{}.pdf'.format(invoice.uniqueId)
    filename = instance.nomor

    # HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('MainApp/kwitansi.html')
    

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
        # 'custom-footer': [
        #     ('footer-html', '/home/gili/Python/kbm/daki/templates/main1/cetak/footer.html')
        # ],
        # 'footer-html': "/home/gili/Python/kbm/daki/templates/main1/cetak/footer.html",
        # 'zoom': 0.9,
        # 'disable-smart-shrinking': False,
        # 'margin-top': '10',
        # 'margin-bottom': '10',
    }
    # Javascript delay is optional

    # Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=settings.GW_WKHTML)



    # config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    
    # config = pdfkit.configuration(wkhtmltopdf="/home/cannindica/wkhtml-install/usr/local/bin/wkhtmltopdf")

    

    # Create the file
    file_content = pdfkit.from_string(
        html, False, configuration=config, options=options)

    # Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    # Return
    return response

