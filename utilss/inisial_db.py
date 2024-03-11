from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
from MainApp.models import (Pt, RolesKaryawan, Pengguna, Opsi, Klien)


fak = [{'model': 'MyApp.klien', 'pk': 1, 'fields': {'klien': 'KLIEN1', 'kode': 'K-1', 'alamat': 'BOGOR', 'telp': '1122', 'email': '', 'cp': None}}, {'model': 'MyApp.klien', 'pk': 2, 'fields': {'klien': 'KLIEN2', 'kode': 'K-2', 'alamat': 'BGR', 'telp': '111', 'email': '', 'cp': 'ZACK'}}, {'model': 'MyApp.klien', 'pk': 3, 'fields': {'klien': 'SURYA ABADI', 'kode': 'SA', 'alamat': 'Workshop: Jl. Mayor Oking Jayaatmaja No.03 RT.01/03 Kel. Puspanegara - Citereup', 'telp': '-', 'email': 'aaa@gmail.com', 'cp': '-'}}, {'model': 'MyApp.klien', 'pk': 4, 'fields': {'klien': 'THE SENTRA HOTEL', 'kode': 'TSH', 'alamat': 'MINAHASA UTARA-MANADO', 'telp': '', 'email': '', 'cp': 'IBU SHIRLEY'}}, {'model': 'MyApp.klien', 'pk': 5, 'fields': {'klien': 'SENTRA MEDIKA CISALAK', 'kode': 'SMCSK ', 'alamat': 'JL. RAYA JAKARTA - BOGOR. KM 33, CISALAK - DEPOK', 'telp': '+62 878-8473-8941', 'email': '', 'cp': 'IBU RITA'}}, {'model': 'MyApp.klien', 'pk': 6, 'fields': {'klien': 'UNIVERSITAS INDONESIA', 'kode': 'UI', 'alamat': 'GEDUNG DEKANAT FEB UI KAMPUS WIDJOJO NITISASTRO, JL. PROF. DR. SUMITRO DJOJOHADIKUSUMO, KUKUSAN, KECAMATAN BEJI, KOTA DEPOK, JAWA BARAT 16424', 'telp': '', 'email': '', 'cp': ''}}, {'model': 'MyApp.klien', 'pk': 7, 'fields': {'klien': 'BMKG', 'kode': 'BMKG-BOGOR', 'alamat': 'BOGOR', 'telp': '', 'email': '', 'cp': ''}}, {'model': 'MyApp.klien', 'pk': 8, 'fields': {'klien': 'RS SENTRA MEDIKA CIBINONG', 'kode': 'SMCBN ', 'alamat': 'CIBINONG - BOGOR', 'telp': '', 'email': '', 'cp': ''}}, {'model': 'MyApp.klien', 'pk': 10, 'fields': {'klien': 'RS HARAPAN BUNDA', 'kode': 'RSHRB', 'alamat': 'JL. RAYA BOGOR KM 22 NO. 24 CIRACAS JAKARTA TIMUR, DKI JAKARTA, INDONESIA 13750', 'telp': '-', 'email': '-', 'cp': 'IBU SUJI'}}]

role_karyawan = ['GM', 'Manajer', 'Karyawan']

username = ['cap']

firstname = ['Irvan']

pt = ['Cipta Artaka Paramesti']

pt_kode = ['CAP']


def RolesKaryawanInit():
	try:
		for i in role_karyawan:
			RolesKaryawan.objects.get_or_create(
				roles=i
			)
	except:
		print("Initial RolesKaryawan Error!")


def PenggunaInit():
	try:
		karyawan = get_object_or_404(RolesKaryawan, roles="Karyawan")
		manajer = get_object_or_404(RolesKaryawan, roles="Manajer")
		gm = get_object_or_404(RolesKaryawan, roles="GM")
	except:
		print("Cant get RolesKaryawan!")

	for i in range (len(username)):
		try:
			obj = User.objects.create_user(
				username[i], '', 'user12345'
			)
			obj.first_name = firstname[i]
			obj.save()
		except:
			obj = User.objects.get(username=username[i])

		obj1, created = Pengguna.objects.get_or_create(
			user = obj,
		)
		obj1.roles.add(gm, manajer)
		obj1.save()


def PtInit():
    for i in range (len(pt)):
        Pt.objects.get_or_create(
        nama=pt[i],
        kode=pt_kode[i],
    )
		
def OpsiInit():
	try:
		a = User.objects.get(username='irvan').user_pengguna
		Opsi.objects.get_or_create(
			keterangan='nomor mulai',
			nilai=1,
			createdBy = a
		)
	except:
		print("Initial Opsi Error!")

def KlienInit():
	for i in fak:
		Klien.objects.get_or_create(
			klien=i['fields']['klien'],
			kode=i['fields']['kode'],
			alamat=i['fields']['alamat'],
			telp=i['fields']['telp'],
			email=i['fields']['email'],
			cp=i['fields']['cp']
		)

def GAS():
	RolesKaryawanInit()
	PenggunaInit()
	PtInit()
	OpsiInit()
	KlienInit()