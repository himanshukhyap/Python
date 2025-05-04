
import pymongo
import requests
from logging import *

from DataModel import AssestDetailscol



async def SingleGetData(api):
        
        response = requests.get(api,timeout=None)
        if response.status_code == 200:
            data = response.json()
            findQuery = AssestDetailscol.find_one({ "AssestId": data["id"] })
            if findQuery == None:
                obj = {'AssestId':response.json()['id'], 
                        "HashingAlgorithm": response.json()['hashing_algorithm'], 
                        "Categories": response.json()["categories"],
                        "Localization": response.json()["localization"]["en"],
                        "Description": response.json()["description"]["en"],
                        "Homepage": response.json()["links"]["homepage"][0],
                        "Genesis_date": response.json()["genesis_date"], 
                        "sentiment_votes_up_percentage": response.json()["sentiment_votes_up_percentage"],
                        "sentiment_votes_down_percentage": response.json()["sentiment_votes_down_percentage"],
                        "market_cap_rank": response.json()["market_cap_rank"],
                        "coingecko_rank": response.json()["coingecko_rank"],
                        "coingecko_score":response.json()["coingecko_score"],
                        "developer_score": response.json()["developer_score"],
                        "community_score": response.json()["community_score"],
                        "liquidity_score":response.json()["liquidity_score"],
                        "public_interest_score": response.json()["public_interest_score"],
                        "Last_Updated": response.json()["last_updated"],
                        "Social_data" : response.json()["community_data"]
                       }   
                AssestDetailscol.insert_one(obj)
            else:
                newvalues = {"$set": 
                      {
                        "HashingAlgorithm": response.json()['hashing_algorithm'], 
                        "Categories": response.json()["categories"],
                        "Localization": response.json()["localization"]["en"],
                        "Description": response.json()["description"]["en"],
                        "Homepage": response.json()["links"]["homepage"][0],
                        "Genesis_date": response.json()["genesis_date"], 
                        "sentiment_votes_up_percentage": response.json()["sentiment_votes_up_percentage"],
                        "sentiment_votes_down_percentage": response.json()["sentiment_votes_down_percentage"],
                        "market_cap_rank": response.json()["market_cap_rank"],
                        "coingecko_rank": response.json()["coingecko_rank"],
                        "coingecko_score":response.json()["coingecko_score"],
                        "developer_score": response.json()["developer_score"],
                        "community_score": response.json()["community_score"],
                        "liquidity_score":response.json()["liquidity_score"],
                        "public_interest_score": response.json()["public_interest_score"],
                        "Last_Updated": response.json()["last_updated"],
                        "Social_data" : response.json()["community_data"] 

                      }}
                AssestDetailscol.update_one(findQuery, newvalues)
        else:
            warning(msg="Error in Api--"+str(response.status_code) +" --"+ response.url)
            print("error SingleGetData")

async def getAssestDetailsCoingecko(api):
            response = requests.get(f"{api}",timeout=None)
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
