import requests

def get_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.HTTPError as errh:
        print("HTTP Hatası:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Bağlantı Hatası:", errc)
    except requests.exceptions.Timeout as errt:
        print("Zaman Aşımı Hatası:", errt)
    except requests.exceptions.RequestException as err:
        print("Bilinmeyen bir hata oluştu:", err)
        print("Detaylar:", response.text)  

#API  listesi için URL
api_list_url = "http://api.alquran.cloud/v1/edition/type"

#sorgu at ve çıktıyı al
api_data = get_api_data(api_list_url)

#çıktıyı ekrana yazdır
print(api_data)
