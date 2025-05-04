import pymongo
import requests
import json
import shutil

from requests.models import Response # save img locally




imgurl = 'https://assets.coingecko.com/coins/images/12000/thumb/683JEXMN_400x400.png'
fileName = "D:\Python\Python\CoinImages.jpg"

response = requests.get(imgurl,stream = True,timeout=None)
print(response.text)
if response.status_code == 200:
    with open(fileName,'wb') as f:
        shutil.copyfileobj(response.raw, f)
    print('Image sucessfully Downloaded: ',fileName)
else:
    print('Image Couldn\'t be retrieved')