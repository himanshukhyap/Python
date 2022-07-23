import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["AssestCoin"]
AssestDetailscol = mydb["AssestDetails"] 
AssestManagercol = mydb["CoinApi_assestmanager"]  
