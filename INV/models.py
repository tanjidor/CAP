from django.db import models
from MainApp.models import (Klien, Pt, Pengguna, Potongan)


class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    nomor = models.CharField(max_length=225, blank=False, null=False)
    nopospk = models.CharField(max_length=225, blank=False, null=False, default="")
    pt = models.ForeignKey(Pt, on_delete=models.CASCADE, related_name='pt_invoice', default="")
    klien = models.ForeignKey(Klien, on_delete=models.CASCADE, related_name='klien_invoice', default="")
    sub_total = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    pembulatan = models.IntegerField(default=0)
    potongan = models.ManyToManyField(Potongan, related_name='potongan_invoice')
    terbilang = models.CharField(max_length=255, default="")
    revisi = models.IntegerField(default=0) ###
    created_by = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='invoice_created_by') # created_by
    edited_by = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='invoice_edited_by', blank=True, null=True, default="") # latest edited_by
    notes = models.TextField(default="")
    proyek = models.CharField(max_length=225, blank=False, null=False, default="")
    status = models.BooleanField(default=False) # False = Pending/Rejected, True = Finished/Approved

    def __str__(self):
        return self.nomor 


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, default="", related_name='invoice_detail')

    nama_barang = models.CharField(max_length=225, blank=False, null=False)
    # qty = models.FloatField(default=0)
    qty = models.CharField(max_length=225, blank=False, null=False)
    satuan = models.CharField(max_length=30, blank=True, null=True, default="")
    keterangan = models.TextField(default="") ###
    harga_satuan = models.IntegerField(default=0)
    total_harga = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def __str__(self):
        return self.nama_barang
