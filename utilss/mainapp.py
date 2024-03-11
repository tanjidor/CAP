from MainApp.models import (RolesKaryawan, Kwitansi)
import roman
import datetime
from django.conf import settings



def cek_status_pengguna(user):
    status = {}

    for i in RolesKaryawan.objects.all():
        status['has_'+ i.roles.lower()] = user.user_pengguna.roles.filter(roles=i.roles).count() > 0
    
    return status 


def terbilang(bil):
    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
    "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bil)
    if n>= 0 and n <= 11:
        Hasil = angka[n]
    elif n <20:
        Hasil = terbilang (n-10) + " Belas "
    elif n <100:
        Hasil = terbilang (n/10) + " Puluh " + terbilang (n%10)
    elif n <200:
        Hasil = " Seratus " + terbilang (n-100)
    elif n <1000:
        Hasil = terbilang (n/100) + " Ratus " + terbilang (n%100)
    elif n <2000:
        Hasil = " Seribu " + terbilang (n-1000)
    elif n <1000000:
        Hasil = terbilang (n/1000) + " Ribu " + terbilang (n%1000)
    elif n <1000000000:
        Hasil = terbilang (n/1000000) + " Juta " + terbilang (n%1000000)
    elif n <1000000000000:
        Hasil = terbilang (n/1000000000) + " Milyar " + terbilang (n%1000000000)
    elif n <1000000000000000:
        Hasil = terbilang (n/1000000000000) + " Triliyun " + terbilang (n%1000000000000)
    elif n == 1000000000000000:
        Hasil = "Satu Kuadriliun"
    else:
        Hasil = "Angka Hanya Sampai Satu Kuadriliun"

    return Hasil


def kwitansi(instance_src, kwitansi_instance=None):
    if kwitansi_instance:
        kwitansi_instance.tujuan = instance_src.nopospk
        #instance.sumber = instance_src.nomor
        kwitansi_instance.sudahterimadari = instance_src.klien.klien
        kwitansi_instance.uangsejumlah = "{} Rupiah".format(instance_src.terbilang)
        kwitansi_instance.utkpembayaran = instance_src.proyek
        kwitansi_instance.nominal = instance_src.total

        kwitansi_instance.save()
        #return kwitansi_instance.pk
    else:
        bulan = roman.toRoman(datetime.datetime.today().month)

        if len(Kwitansi.objects.all()) == 0:
            no = "1"
        else:
            # no = len(Kwitansi.objects.all())
            # no+=1
            no = Kwitansi.objects.filter(pt=instance_src.pt).last()
            no = no.nomor.split('/')
            no = int(no[2])
            no += 1

        no = "KW/{}/{}/{}/{}".format(instance_src.pt.kode, no, bulan, datetime.datetime.today().strftime('%Y'))

        instance1 = Kwitansi.objects.create(
            nomor=no,
            tujuan=instance_src.nopospk,
            sumber=instance_src.nomor,
            sudahterimadari=instance_src.klien.klien,
            uangsejumlah="{} Rupiah".format(instance_src.terbilang),
            utkpembayaran=instance_src.proyek,
            nominal=instance_src.total,
            pt=instance_src.pt,
        )

       # return instance1.pk


def pt_detail(pt):
    if pt.kode == 'CAP':
        context = {
            'logo_src' : settings.LOGO_CAP,
            'ttd_src' : settings.TTD_CAP,
            'local_logo': 'pt_img/logo.jpg',
            'nama_pt' : 'PT. CIPTA ARTAKA PARAMESTI',
            'head' : 'General Contractor & Distribution',
            'ket' : 'Head Office : Jl. Raya KH. R Abdullah bin Nuh RT 01/011, Bubulak. Bogor, Jawa Barat 16117',
            'ket1' : 'Email: Ciptaartakaparamesti@gmail.com , Phone/whatsapp : 081385289879',
            'dirut' : 'Irfan Syah Chaerul',
            }
    elif pt.kode == 'PYD':
        context = {
            'logo_src' : '/home/gili/Python/kbm/accounting/static/pt_img/PyDevLogo.jpg',
            'ttd_src' : settings.TTD_PYDEVL,
            'local_logo': 'pt_img/PyDevLogo.jpg',
            'nama_pt' : 'PyDevL',
            'head' : 'IT Web Developer',
            'ket' : 'Perum. Budi Agung',
            'ket1' : 'dashaschisch@gmail.com -- 0857 159 80900',
            'dirut' : 'Aria Hanggara',
        }
    else:
        context = {
            'logo_src' : settings.LOGO_SA,
            'ttd_src' : settings.TTD_SA,
            'local_logo': '',
            'nama_pt' : 'CV. SURYA ABADI',
            'head' : 'Interior & Supplier',
            'ket' : 'Workshop: Jl. Mayor Oking Jayaatmaja No.03 RT.01/03 Kel. Puspanegara - Citereup',
            'ket1' : 'Email: cvsuryaabadi76@gmail.com , Telp : 0821 1112 9484 - 0812 8031 8676',
            'dirut' : 'Ujang Suryana',
        }
    return context

