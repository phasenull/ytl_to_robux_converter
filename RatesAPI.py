import string
import requests
import json
url = "https://api.genelpara.com/embed/para-birimleri.json"
def GetRates():
    request = requests.get(url)
    if request.status_code == 200:
        return json.loads(request._content)
def GetRate(currency:string):
    request = requests.get(url)
    if request.status_code == 200:
        j = json.loads(request.text)
        if j.keys().__contains__(currency.upper()):
            return j[currency.upper()]["alis"]
