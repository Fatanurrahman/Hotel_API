import requests
import bs4
#from models import Hotel


def url(kota):
    if (kota=="Bali") :
        return ("https://www.tripadvisor.com/Hotels-g294226-", "Bali-Hotels.html", 3)
    elif (kota=="NTT"):
        return ("https://www.tripadvisor.com/Hotels-g297728-", "East_Nusa_Tenggara-Hotels.html",3)
    elif (kota == "Jakarta"):
        return ("https://www.tripadvisor.com/Hotels-g294229-", "Jakarta_Java-Hotels.html",3)
    elif (kota == "Bandung"):
        return ("https://www.tripadvisor.com/Hotels-g297704-", "Bandung_West_Java_Java-Hotels.html",3)
    elif (kota == "Medan"):
        return ("https://www.tripadvisor.com/Hotels-g297725-", "Medan_North_Sumatra_Sumatra-Hotels.html",3)
    elif (kota == "Yogyakarta"):
        return ("https://www.tripadvisor.com/Hotels-g294230-", "Yogyakarta_Region_Java-Hotels.html",3)

def get_url(url_awal,url_akhir, page) :
    if ( page==0 ) :
        url_final = url_awal + url_akhir
    else :
        url_final = url_awal + 'oa' + str(page*30) + '-' + url_akhir
    return (url_final)

def ambil_data(sumber, city) :
    for a in sumber:
        nama_hotel = str(a.find('a', attrs={"class": 'property_title'}).text)
        harga_hotel = a.find('div', attrs={"class": 'price-wrap'}).find('div', attrs={"class": 'price'}).text.replace('IDR\xa0','')
        jumlah_review_hotel = a.find('a', attrs={"class": 'review_count'}).text.replace(' reviews', '')
        print("Nama : ", nama_hotel)
        print("Harga : ",str(harga_hotel))
        print("Jumlah Review : ", str(jumlah_review_hotel))
        print(city)
        print()

kota = "Jakarta"


url1, url2, pages = url(kota)
for i in range(0, pages):
    url = get_url(url1, url2, i)
    res = requests.get(url)
    data = bs4.BeautifulSoup(res.text, 'lxml')
    daftar = data.find_all('div', class_="allowEllipsis")
    ambil_data(daftar, kota)


# simpen database
    #ringo = Person.objects.create(name="Ringo Starr")
# Bikin login
# Bikin template
# RESTFUL API