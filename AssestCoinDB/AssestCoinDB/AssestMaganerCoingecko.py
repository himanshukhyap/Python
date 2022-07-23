import pymongo
import requests
from logging import *
import shutil
import json
from DataModel import AssestManagercol


async def ImageGet(imgurl,fileName):
    res = requests.get(imgurl,stream = True)
    if res.status_code == 200:
                        with open(fileName,'wb') as f:
                            shutil.copyfileobj(res.raw, f)
                        print('Image sucessfully Downloaded: ',fileName)
    else:
                        print('Image Couldn\'t be retrieved')


async def SingleGetData(api):
        
        response = requests.get(api,timeout=None)
        if response.status_code == 200:
            data = response.json()
            findQuery = AssestManagercol.find_one({ "AssestId": data["id"] })
            if findQuery == None:
                for x in response.json()['image']:
                    imgurl = str(response.json()['image'][x])
                    print(type(imgurl))
                    fileName = "D:\Python\Python\{}\{}.jpg".format(response.json()['id'],x)
                    await ImageGet(imgurl,fileName)


                obj = {'AssestId':response.json()['id'], 
                       'Symbol': response.json()['symbol'], 
                       'Name': response.json()['name'] , 
                       'ThumbImage':response.json()['image']["thumb"] ,
                       'SmallImage':response.json()['image']["small"] ,
                       'LargeImage':response.json()['image']["large"]       
                       }   
                AssestManagercol.insert_one(obj)
            else:
                newvalues = {"$set": 
                      {'ThumbImage':response.json()['image']["thumb"] ,
                       'SmallImage':response.json()['image']["small"] ,
                       'LargeImage':response.json()['image']["large"] ,
                       'Symbol': response.json()['symbol'], 
                       'Name': response.json()['name'] 
                      }}
                AssestManagercol.update_one(findQuery, newvalues)
        else:
            warning(msg="Error in Api--"+str(response.status_code) +" --"+ response.url)
            print("error SingleGetData")

async def getAssestManagerDataCoingecko(api):
            response = requests.get(f"{api}",timeout=None)
            # print(response.status_code)
            # print(response.json())
            # print(response.text)
            if response.status_code == 200:
                if response.json() != []:
                    for x in response.json():
                        if x['id'] != "":
                            url= 'https://api.coingecko.com/api/v3/coins/{}'.format(x['id'])
                            print(url)
                            await SingleGetData(url)
                        else:
                            warning(msg="Empty data  --"+ response.url)
                            print("No Id "+response.url)
                else:
                    warning(msg="No data in url --"+ response.url)
                    print("No data "+ response.url)
                    
            else:
                error(msg="Error in Api response code--"+str(response.status_code) +" --"+ response.url)
                print(response.status_code)


#asyncio.run(getAssestManagerDataCoincap(coingecko))
