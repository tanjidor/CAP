from django.db import models
from django.contrib.auth.models import User 


class Potongan(models.Model): # diskon, dll
	nama = models.CharField(max_length=65, blank=False, null=False)
	potongan = models.FloatField(default=0)
	jenis = models.CharField(max_length=15, blank=False, null=False, default="")

	def __str__(self):
		return "{} - {}".format(self.nama, self.potongan)


class Penambahan(models.Model): # ppn, dll
	nama = models.CharField(max_length=65, blank=False, null=False)
	penambahan = models.FloatField(default=0)
	jenis = models.CharField(max_length=15, blank=False, null=False, default="")

	def __str__(self):
		return "{} - {}".format(self.nama, self.penambahan)


class Klien(models.Model):
    klien = models.CharField(max_length=225, blank=False, null=False)
    kode = models.CharField(max_length=30, blank=False, null=False, unique=True)
    alamat = models.TextField(default="", blank=True, null=True)
    telp = models.CharField(max_length=15, default="", blank=True, null=True)
    email = models.EmailField(max_length=125, blank=True, null=True, default="")
    cp = models.CharField(max_length=65, blank=True, null=True)

    def __str__(self):
        return self.klien


class Pt(models.Model):
    nama = models.CharField(max_length=125, blank=False, null=False)
    kode = models.CharField(max_length=15, blank=False, null=False)
    telp = models.CharField(max_length=15, default="", blank=False, null=False)
    email = models.EmailField(max_length=125, blank=True, null=True, default="")
    cp = models.CharField(max_length=65, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.pk, self.nama)


class Vendor(models.Model):
    nama = models.CharField(max_length=125, blank=False, null=False)
    kode = models.CharField(max_length=15, blank=False, null=False, unique=True)
    telp = models.CharField(max_length=15, default="", blank=False, null=False)
    alamat = models.TextField(default="", blank=True, null=True)
    email = models.EmailField(max_length=125, blank=True, null=True, default="")
    cp = models.CharField(max_length=65, blank=True, null=True)
    norek = models.CharField(max_length=65, blank=False, null=False, default="")
    an = models.CharField(max_length=125, blank=False, null=False, default="")

    def __str__(self):
        return self.nama


class RolesKaryawan(models.Model):
	roles = models.CharField(max_length=60, blank=False, null=False)

	def __str__(self):
		return self.roles


class Pengguna(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_pengguna')
    roles = models.ManyToManyField(RolesKaryawan, related_name='roles_pengguna')
    status = models.IntegerField(default=1) # 1 active 0 deactive
    telp = models.CharField(max_length=15, default="")
    pt = models.ManyToManyField(Pt, related_name='pt_roles_karyawan')
    email = models.EmailField(max_length=125, blank=True, null=True, default="")

    def __str__(self):
        return self.user.first_name


class Kwitansi(models.Model):
    nomor = models.CharField(max_length=225, blank=False, null=False)
    tujuan = models.CharField(max_length=225, blank=False, null=False) # untuk pembayaran apa kwitansi ini (nopospk)
    sumber = models.CharField(max_length=225, blank=False, null=False) # dari mana kwitansi ini keluar (no inv, dll)

    sudahterimadari = models.CharField(max_length=225, blank=False, null=False)
    uangsejumlah = models.CharField(max_length=225, blank=False, null=False)
    utkpembayaran = models.CharField(max_length=225, blank=False, null=False)
    nominal = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    pt = models.ForeignKey(Pt, on_delete=models.CASCADE, related_name='pt_kwitansi', null=True)

    def __str__(self):
        return self.nomor
    

class Opsi(models.Model):
    keterangan = models.CharField(max_length=225, blank=False, null=False) # ex: "nomor mulai"
    nilai = models.SmallIntegerField(default=0) # ex: 1
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    createdBy = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='opsi_created_by')

    def __str__(self):
        return self.keterangan
