# import re

# # r"^\d*[.]?\d{0,2}$"
# # r"^\d*[.]?\d{0,2}$"
# # /^-?((100)|(\d{1,2}(\.\d*)?))%?$/
# mylist = ["232", "2%", "22.4%", "23.44%%%"]
# r = re.compile(r"^\d*[.]?\d{0,2}$|^(\d+(\.\d{0,2})?%)$")
# # newlist = list(filter(r.match, mylist)) # Read Note below
# newlist = list(filter(lambda v: not r.match(v), mylist))


# if newlist:
#     print('ada')


fak = [{'model': 'MyApp.klien', 'pk': 1, 'fields': {'klien': 'KLIEN1', 'kode': 'K-1', 'alamat': 'BOGOR', 'telp': '1122', 'email': '', 'cp': None}}, {'model': 'MyApp.klien', 'pk': 2, 'fields': {'klien': 'KLIEN2', 'kode': 'K-2', 'alamat': 'BGR', 'telp': '111', 'email': '', 'cp': 'ZACK'}}, {'model': 'MyApp.klien', 'pk': 3, 'fields': {'klien': 'SURYA ABADI', 'kode': 'SA', 'alamat': 'Workshop: Jl. Mayor Oking Jayaatmaja No.03 RT.01/03 Kel. Puspanegara - Citereup', 'telp': '-', 'email': 'aaa@gmail.com', 'cp': '-'}}, {'model': 'MyApp.klien', 'pk': 4, 'fields': {'klien': 'THE SENTRA HOTEL', 'kode': 'TSH', 'alamat': 'MINAHASA UTARA-MANADO', 'telp': '', 'email': '', 'cp': 'IBU SHIRLEY'}}, {'model': 'MyApp.klien', 'pk': 5, 'fields': {'klien': 'SENTRA MEDIKA CISALAK', 'kode': 'SMCSK ', 'alamat': 'JL. RAYA JAKARTA - BOGOR. KM 33, CISALAK - DEPOK', 'telp': '+62 878-8473-8941', 'email': '', 'cp': 'IBU RITA'}}, {'model': 'MyApp.klien', 'pk': 6, 'fields': {'klien': 'UNIVERSITAS INDONESIA', 'kode': 'UI', 'alamat': 'GEDUNG DEKANAT FEB UI KAMPUS WIDJOJO NITISASTRO, JL. PROF. DR. SUMITRO DJOJOHADIKUSUMO, KUKUSAN, KECAMATAN BEJI, KOTA DEPOK, JAWA BARAT 16424', 'telp': '', 'email': '', 'cp': ''}}, {'model': 'MyApp.klien', 'pk': 7, 'fields': {'klien': 'BMKG', 'kode': 'BMKG-BOGOR', 'alamat': 'BOGOR', 'telp': '', 'email': '', 'cp': ''}}, {'model': 'MyApp.klien', 'pk': 8, 'fields': {'klien': 'RS SENTRA MEDIKA CIBINONG', 'kode': 'SMCBN ', 'alamat': 'CIBINONG - BOGOR', 'telp': '', 'email': '', 'cp': ''}}, {'model': 'MyApp.klien', 'pk': 10, 'fields': {'klien': 'RS HARAPAN BUNDA', 'kode': 'RSHRB', 'alamat': 'JL. RAYA BOGOR KM 22 NO. 24 CIRACAS JAKARTA TIMUR, DKI JAKARTA, INDONESIA 13750', 'telp': '-', 'email': '-', 'cp': 'IBU SUJI'}}]

for i in fak:
    print(i['fields']['klien'])