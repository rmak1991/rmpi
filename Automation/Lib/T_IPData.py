
# importing the requests library
import requests,json, os, sys
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
def ip_info():
    URL = "https://freegeoip.app/json/"
    r = requests.get(url = URL)
    data = r.json()
    URL2 = "https://ipinfo.io/"+data["ip"]+"/geo"
    r2 = requests.get(url = URL2)
    data2 = r2.json()
    datajson = {}
    jsonIPData1={}
    jsonIPData2={}
    for a in data:
        jsonIPData1[a]=data[a]
    datajson["IPD1"]=jsonIPData1
    for a in data2:
        jsonIPData2[a]=data2[a]
    datajson["IPD2"]=jsonIPData2
    json_data = json.dumps(datajson)
    return json_data

