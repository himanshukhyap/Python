import pymongo
import requests
from logging import *

from DataModel import AssestManagercol




async def SingleGetData(api):
        
        response = requests.get(api,timeout=None)
        if response.status_code == 200:
            data = response.json()["data"]
            findQuery = AssestManagercol.find_one({ "AssestId": data["id"] })
            if findQuery == None:
                obj = {'AssestId':data['id'], 
                       'Symbol': data['symbol'], 
                       'Name': data['name']
                       }   
                AssestManagercol.insert_one(obj)
            else:
                return None
                #newvalues = {"$set": 
                #      {
                #       'Symbol': response.json()['symbol'], 
                #       'Name': response.json()['name'] 
                #      }}
                #mycol.update_one(findQuery, newvalues)
        else:
            warning(msg="Error in Api response code--"+str(response.status_code) +" --"+ response.url)
            print("error SingleGetData")

async def getAssestManagerCoincap(api):
            response = requests.get(f"{api}",timeout=None)
            #print(response.status_code)
            #print(response.json())
            # print(response.text)
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
         

