
# importing the requests library
import requests,json,sys,os

_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_PATH)
import Lib.T_FileHandler as fw
import Lib.T_DateTime as dt
from Lib.T_Global import PATHS as _P

#GLOBAL VARIABLES
_FILENAME ="nasdaq_stocks_"+dt.getDateTime()+".data"
#****************
def nasdaq_stocks_download():
    if not fw.FILE_EXISTS_PATTERN(_P.DATA_PATH,starts_with="nasdaq_stocks_"):  
        URL = "https://api.nasdaq.com/api/screener/stocks"
        PARAMS = {"tableonly": "true", "limit": "25","exchange":"NASDAQ","download":"true"}
        user_agent = {"user-agent":"Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36"}
        r = requests.get(url = URL,params = PARAMS, headers=user_agent)
        data = json.dumps(r.json()["data"]["rows"])
        fw.FILE_WRITE_OVERWRITE(_FILENAME,_P.DATA_PATH,data)
nasdaq_stocks_download()