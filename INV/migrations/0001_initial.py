# Generated by Django 5.0.2 on 2024-03-06 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MainApp', '0002_alter_klien_kode_alter_vendor_kode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nomor', models.CharField(max_length=225)),
                ('nopospk', models.CharField(default='', max_length=225)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('pembulatan', models.IntegerField(default=0)),
                ('terbilang', models.CharField(default='', max_length=255)),
                ('revisi', models.IntegerField(default=0)),
                ('notes', models.TextField(default='')),
                ('proyek', models.CharField(default='', max_length=225)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_created_by', to='MainApp.pengguna')),
                ('edited_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_edited_by', to='MainApp.pengguna')),
                ('klien', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='klien_invoice', to='MainApp.klien')),
                ('potongan', models.ManyToManyField(related_name='potongan_invoice', to='MainApp.potongan')),
                ('pt', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pt_invoice', to='MainApp.pt')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=225)),
                ('qty', models.CharField(max_length=225)),
                ('satuan', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('keterangan', models.TextField(default='')),
                ('harga_satuan', models.IntegerField(default=0)),
                ('total_harga', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('invoice', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='invoice_detail', to='INV.invoice')),
            ],
        ),
    ]