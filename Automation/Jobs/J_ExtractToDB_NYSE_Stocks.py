
# importing the requests library
import requests,json,sys,os,time
_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_PATH)
import Lib.T_FileHandler as fw
import Lib.T_DateTime as dt
from Lib.T_Global import PATHS as _P
from Lib.T_DB import *

def ExtracttoDB():
    start = time.time()
    FILE= fw.FILE_NAME_PATTERN(_P.DATA_PATH,starts_with="nyse_stocks_")
    data = json.loads(fw.FILE_READ(FILE,_P.DATA_PATH))
    for c in data:
        text  = "INSERT INTO stocks_NYSE (symbol,name,lastsale,netchange,pctchange,volume,marketCap,country,ipoyear,industry,sector,url) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        param = (c["symbol"], c["name"], c["lastsale"], c["netchange"], c["pctchange"], c["volume"], c["marketCap"], c["country"], c["ipoyear"], c["industry"], c["sector"], c["url"])
        dbinsert_param(text,param)
    finish = time.time()
    runtime = int((finish - start)/60)
    print(runtime)
ExtracttoDB()
