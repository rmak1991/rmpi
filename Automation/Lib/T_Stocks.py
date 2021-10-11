
# importing the requests library
import requests,os,sys
import re
import json
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
def stock_json(stock):
    URL = "https://finance.yahoo.com/quote/"+stock+"/"
    r = requests.get(url = URL)
    data = r.text
    #print(r.status_code)
    r = "(<span class=\"Trsdu\(0\.3s\) Fw\(b\) Fz\(36px\) Mb\(-4px\) D\(ib\)\" data-reactid=\"49\">)(.+?)<\/span>"
    p = re.compile(r)
    data2=""
    for m in p.finditer(data):
        data2=m.group()
    STOCK_PRICE = data2.replace("<span class=\"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)\" data-reactid=\"49\">","").replace("</span>","")
    datajson = {}
    datajson["Stock"]=stock
    datajson["Price"]=STOCK_PRICE
    json_data = json.dumps(datajson)
    return json_data
