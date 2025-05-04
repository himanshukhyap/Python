
import pymongo
import requests
from logging import *

from DataModel import AssestDetailscol



async def SingleGetData(api):
        
        response = requests.get(api,timeout=None)
        if response.status_code == 200:
            data = response.json()["data"]
            findQuery = AssestDetailscol.find_one({ "AssestId": data["id"] })
            if findQuery == None:
                obj = {'AssestId':data['id'], 
                        "Rank": "1",
                        "Supply": data['supply'],
                        "MaxSupply": data['maxSupply'],
                        "MarketCapUsd": data['marketCapUsd'],
                        "VolumeUsd24Hr": data['volumeUsd24Hr'],
                        "PriceUsd": data['priceUsd'],
                        "ChangePercent24Hr": data['changePercent24Hr'],
                        "vwap24Hr": data['vwap24Hr'],
                        "Explorer": data['explorer'],
                       }   
                AssestDetailscol.insert_one(obj)
            else:
                return None
                newvalues = {"$set": 
                      {
                        "Rank": "1",
                        "Supply": data['supply'],
                        "MaxSupply": data['maxSupply'],
                        "MarketCapUsd": data['marketCapUsd'],
                        "VolumeUsd24Hr": data['volumeUsd24Hr'],
                        "PriceUsd": data['priceUsd'],
                        "ChangePercent24Hr": data['changePercent24Hr'],
                        "vwap24Hr": data['vwap24Hr'],
                        "Explorer": data['explorer'],
                      }
                             }
                AssestDetailscol.update_one(findquery, newvalues)
        else:
            warning(msg="Error in Api response code--"+str(response.status_code) +" --"+ response.url)
            print("error SingleGetData")



async def getAssestDetailsCoincap(api):
            response = requests.get(f"{api}",timeout=None)
            if response.status_code == 200:
                    if response.json()["data"] != []:
                        print(api)
                        for x in response.json()["data"]:
                            print(x)
                            if x['id'] != "":
                                url= 'https://api.coincap.io/v2/assets/{}'.format(x['id'])
                                print(url)
                                await SingleGetData(url)
                            else:
                                warning(msg="Empty data --"+ response.url)
                                print("No Id "+response.url)
                    else:
                        warning(msg="No data in url --"+ response.url)
                        print("No data "+ response.url)  
            else:
                error(msg="Error in Api response code--"+str(response.status_code) +" --"+ response.url)
                print(response.status_code)

