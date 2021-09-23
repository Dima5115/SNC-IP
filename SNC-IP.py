#!usr/bin/python
#Revisi: Dima

import requests, json, os

os.system('clear')
print("""
----------------------------------------------------------
                       [ SCN-IP ]
	           |CEK IP PUBLIK TOOL|
		------------------------
                    | DIMA OS GROUP |
      (LEARNED --> MADE --> DEFENCE SELF --> HELP OTHERS)
-----------------------------------------------------------
                     VERSION: 11.0.0


            |---------------------|     |------------------|
            |       SOLDUDO       |     | SOLDUDO?         |
            |  |---------------|  |     |------------------|
            |--|               |--|          .
                ----\\  // ----            .
                                         .
                 [--]     [--]        .

             \ \               / /
              \ \             / /
               \ \           / /
                \ \         / /
                 \ \       / /
                  \ \     / /
                   \ \   / /








""")
while True:
	try:
		r1=requests.get('https://ipapi.co/json/')
		print("Alamat IP anda:",r1.json()['ip'])
		ip=input("Masukan alamat IP:")
		r=requests.get('https://ipapi.co/'+ip+'/json')
		j=json.loads(r.text)
		print("""
Alamat Ip      : {}
Kota 	       : {}
Wilayah        : {}
Kode Wilayah   : {}
Negara	       : {}
Nama Negara    : {}
Kode Benua     : {}
Latitude       : {}
Longitude      : {}
Zona Waktu     : {}
Kode Telpon    : {}
Mata Uang      : {}
Bahasa	       : {}
Organisasi     : {}
""".format(j['ip'],j['city'],j['region'],j['region_code'],j['country'],j['country_name'],j['continent_code'],j['latitude'],j['longitude'],j['timezone'],j['country_calling_code'],j['currency'],j['languages'],j['org']))
	except KeyError:
		print("\nAlamat IP:",ip,"INVALID\n")
