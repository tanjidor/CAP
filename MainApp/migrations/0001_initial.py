# Generated by Django 5.0.2 on 2024-02-29 10:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Klien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klien', models.CharField(max_length=225)),
                ('kode', models.CharField(max_length=30)),
                ('alamat', models.TextField(blank=True, default='', null=True)),
                ('telp', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=125, null=True)),
                ('cp', models.CharField(blank=True, max_length=65, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Penambahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=65)),
                ('penambahan', models.FloatField(default=0)),
                ('jenis', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Potongan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=65)),
                ('potongan', models.FloatField(default=0)),
                ('jenis', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=125)),
                ('kode', models.CharField(max_length=15)),
                ('telp', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(blank=True, default='', max_length=125, null=True)),
                ('cp', models.CharField(blank=True, max_length=65, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RolesKaryawan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=125)),
                ('kode', models.CharField(max_length=15)),
                ('telp', models.CharField(default='', max_length=15)),
                ('alamat', models.TextField(blank=True, default='', null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=125, null=True)),
                ('cp', models.CharField(blank=True, max_length=65, null=True)),
                ('norek', models.CharField(default='', max_length=65)),
                ('an', models.CharField(default='', max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Kwitansi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor', models.CharField(max_length=225)),
                ('tujuan', models.CharField(max_length=225)),
                ('sumber', models.CharField(max_length=225)),
                ('sudahterimadari', models.CharField(max_length=225)),
                ('uangsejumlah', models.CharField(max_length=225)),
                ('utkpembayaran', models.CharField(max_length=225)),
                ('nominal', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pt_kwitansi', to='MainApp.pt')),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('telp', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(blank=True, default='', max_length=125, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_pengguna', to=settings.AUTH_USER_MODEL)),
                ('pt', models.ManyToManyField(related_name='pt_roles_karyawan', to='MainApp.pt')),
                ('roles', models.ManyToManyField(related_name='roles_pengguna', to='MainApp.roleskaryawan')),
            ],
        ),
    ]
