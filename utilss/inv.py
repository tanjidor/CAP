from django.shortcuts import get_object_or_404
import datetime, roman
from django.db.models import F

from MainApp.models import (Klien, Pt, Kwitansi, Opsi)
from INV.models import (Invoice, InvoiceDetails)
from utilss.mainapp import (terbilang, kwitansi)



def invoice_create(data):
    sub_total = 0
    klien = get_object_or_404(Klien, klien=data['klien'])
    bulan = roman.toRoman(datetime.datetime.today().month)

    try:
        no_indicate = Opsi.objects.get(keterangan='nomor mulai')
        no = "CAP/INV/{}/{}/{}".format(no_indicate.nilai, bulan, datetime.datetime.today().strftime('%Y'))

    except:pass

    # try:
    #     no = Invoice.objects.filter(pt__kode='CAP').last().nomor
    #     no = no.split('/')[2]
    #     no = int(no) + 1
    #     no = "CAP/INV/{}/{}/{}".format(no, bulan, datetime.datetime.today().strftime('%Y'))
    # except:
    #     no = "CAP/INV/{}/{}/{}".format(Opsi.objects.filter(keterangan='tanggal mulai').last().nilai, bulan, datetime.datetime.today().strftime('%Y'))


    # no = "CAP/INV/{}/{}/{}".format(data['noinv'], bulan, datetime.datetime.today().strftime('%Y'))

    if Invoice.objects.filter(nomor=no).exists():
        return {'status_inv': False, 'message': 'Nomor invoice sudah ada !'}

    instance = Invoice.objects.create(
        nomor = no,
        nopospk = data['nopospk'],
        pt = get_object_or_404(Pt, kode='CAP'),
        klien = klien,
        created_by = data['user'].user_pengguna,
        proyek = data['proyek'],
    )

    for i in range(len(data['material'])):
        total_harga = data['qty'][i].split('%')
        tai = data['harga_satuan'][i]
        if tai == '':
            tai = 0
        if len(total_harga) == 1:
            total_harga = float(data['qty'][i]) * float(tai)
        else:
            total_harga = ( float(total_harga[0]) * float(tai) ) / 100

        sub_total +=total_harga
        InvoiceDetails.objects.create(
            invoice=instance,
            nama_barang=data['material'][i].capitalize(),
            qty=data['qty'][i],
            satuan=data['satuan'][i].capitalize(),
            total_harga=total_harga,
            harga_satuan=tai,
        )

    total = sub_total

    instance.sub_total, instance.total, instance.pembulatan = sub_total, total, round(total, -3)
    instance.terbilang = terbilang(total)
    instance.save()
    no_indicate.nilai = F("nilai") + 1
    no_indicate.save()

    kwitansi(instance)    

    return {'status_inv': True, 'message': 'Invoice added !'}

def invoice_edit(data):
    sub_total = 0
    klien = get_object_or_404(Klien, klien=data['klien'])

    if data['cb_revisi'] == 'revisi':
        no = data['instance'].nomor 
        data['instance'].revisi += 1 
        try:
            no = no.split('.')
            rev = ".Rev{}".format(data['instance'].revisi)
            no = no[0] + rev 
            data['instance'].nomor = no 
        except:
            rev = ".Rev{}".format(data['instance'].revisi)
            no = no.nomor.split('/')
            no = no + rev 
            data['instance'].nomor = no 
    
    try:
        data['instance'].invoice_detail.all().delete()
    except:
        print("ERROR reset invoice detail instance")
    
    for i in range(len(data['material'])):
        total_harga = data['qty'][i].split('%')
        tai = data['harga_satuan'][i]
        if tai == '':
            tai = 0
        if len(total_harga) == 1:
            total_harga = float(data['qty'][i]) * float(tai)
        else:
            total_harga = ( float(total_harga[0]) * float(tai) ) / 100

        sub_total +=total_harga
        InvoiceDetails.objects.create(
            invoice=data['instance'],
            nama_barang=data['material'][i].capitalize(),
            qty=data['qty'][i],
            satuan=data['satuan'][i].capitalize(),
            total_harga=total_harga,
            harga_satuan=tai,
        )

    total = sub_total

    data['instance'].sub_total, data['instance'].total, data['instance'].pembulatan = sub_total, total, round(total, -3)
    data['instance'].terbilang = terbilang(total)
    data['instance'].edited_by = data['user'].user_pengguna
    data['instance'].klien = klien
    data['instance'].nopospk = data['nopospk']
    data['instance'].save()

    ###
    kwitansi(data['instance'], get_object_or_404(Kwitansi, sumber=data['instance'].nomor))
    ###

    return data['instance'].pk