
import pymongo
import requests
import json
import shutil

imgurl = 'https://assets.coingecko.com/coins/images/12000/thumb/683JEXMN_400x400.png?1596690527'
fileName = "D:\Python\Python\CoinImages.jpg"
print(type(imgurl))
response = requests.get(imgurl,stream = True)
if response.status_code == 200:
    with open(fileName,'wb') as f:
        shutil.copyfileobj(response.raw, f)
    print('Image sucessfully Downloaded: ',fileName)
else:
    print('Image Couldn\'t be retrieved')
