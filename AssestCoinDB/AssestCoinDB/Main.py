import pymongo
import asyncio
from logging import *
from AssestDetailsCoincap import getAssestDetailsCoincap
from AssestDetailsCoingecko import getAssestDetailsCoingecko
from AssestMaganerCoingecko import  getAssestManagerDataCoingecko
from AssestMangerCoincap import getAssestManagerCoincap


LogFormat = '%(asctime)s -- %(levelname)s -- %(message)s - %(lineno)d --%(filename)s '
basicConfig(filename='D:\Python\Python\LogginData\Coin.log',force=True,level=DEBUG,filemode="w",format=LogFormat)
#debug(msg="ApI Call.ipynb") 
#info(msg="ApI Call.ipynb")  
#warning(msg="ApI Call.ipynb")
#error(msg="ApI Call.ipynb")

coingecko = 'https://api.coingecko.com/api/v3/coins/list?include_platform=false'
coincap1 =   'https://api.coincap.io/v2/assets?limit=2000&offset=0'
coincap2 =   'https://api.coincap.io/v2/assets?limit=1000&offset=2000'

async def getAssest():
     await getAssestManagerDataCoingecko(coingecko)
     await getAssestManagerCoincap(coincap1) 
     await getAssestManagerCoincap(coincap2)
     await getAssestDetailsCoincap(coincap1)
     await getAssestDetailsCoincap(coincap2)
     await getAssestDetailsCoingecko(coingecko)
     
     

asyncio.run(getAssest())