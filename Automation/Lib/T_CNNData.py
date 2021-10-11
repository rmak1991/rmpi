
# importing the requests library
import requests, re, json, os, sys
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P

newarr = []
URL = "https://www.cnn.com/business/markets/premarkets"

def gs(index):
    return newarr[index]
def cnnjson():    
    r = requests.get(url = URL)
    data = r.text
    data2=data[data.find("<div name=\"anchor-futures\">"):data.find("<div class=\"Text-sc-1amvtpj-0 styles__StyledText-vox9kt-0 fDLFdz\">")]
    r = "<(“[^”]*”|'[^’]*’|[^'”>])*>"
    p = re.compile(r)
    newt=data2
    for m in p.finditer(data2):
       newt= newt.replace(m.group(), "\n")
    newt= newt.replace("amp;", "")   
    textarr=newt.split("\n")
    datajson = {}
    for i in range(len(textarr)):
        if textarr[i]!='':
            newarr.append(textarr[i])
    jsondow={}
    jsondow["DOW"]=gs(2)+"   "+gs(3)+""+gs(4)
    jsondow[gs(5)]=gs(6)
    jsondow[gs(7)]=gs(8)
    jsondow[gs(9)]=gs(10)
    datajson[gs(1)] = jsondow
    jsonsp={}
    jsonsp["S&P"]=gs(12)+"   "+gs(13)+""+gs(14)
    jsonsp[gs(15)]=gs(16)
    jsonsp[gs(17)]=gs(18)
    jsonsp[gs(19)]=gs(20)
    datajson[gs(11)] = jsonsp
    jsondnasdaq={}
    jsondnasdaq["Nasdaq"]=gs(22)+"   "+gs(23)+""+gs(24)
    jsondnasdaq[gs(25)]=gs(26)
    jsondnasdaq[gs(27)]=gs(28)
    jsondnasdaq[gs(29)]=gs(30)
    datajson[gs(21)] = jsondnasdaq
    json_data = json.dumps(datajson)
    return json_data
