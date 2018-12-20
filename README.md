# Hotel_API

Muhammad Fata Nurrahman
18216014

API Documentation

<strong> 1.	Overview </strong>
Sebuah API untuk mendapatkan data hotel hasil dari scraping web pada TripAdvisor. Data yang tersedia adalah id, nama, harga, jumlah review, dan lokasi. Hotel juga sementara hanya yang terletak di kota/provinsi dengan turis terbanyak, yaitu Medan, NTT, Yogyakarta, Bandung, Jakarta, dan Bali.

2.	Purpose
Selain untuk keperluan akademik, API dapat dimanfaatkan oleh agen travel atau startup yang lebih ingin mendapatkan hotel dengan lebih banyak opsi. ( Namun pada kenyataanya yang saya buat hanya pilot version, dan belum terintegrasi antara hasil scrapping web dengan database. Sehingga database yang ada adalah masukan secara manual sebagian hasil scraping web )

3.	Tools & Framework
Bahasa : Python
Framework : Django
Web Scraping : Requests & BeautifulSoup4
Text Editor : Visual Studio Code & Pycharm
API : RESTFUL API & JSON
Frontend : HTML & CSS ( Bootstrap )

4.	Accessing API
API hanya bisa dengan method “GET”. Dan karena kode disimpan di local host, mengakses API bisa melalui. Localhost:8000/hotel_api/. Dan berikut hasil keluarannya. ( Lebih jelasnya pada folder API Documentation )

5.	Content
Field	Type	Description
Nama	Varchar (250)	Nama hari hotel
Harga	Int (11)	Harga sewa per malam
Jumlah_review	Int (11)	Jumlah orang yang melakukan review pada hotel tersebut di website TripAdvisor.co
Lokasi	Varchar (250)	Kota atau Provinsi dari hotel tersebut berada

