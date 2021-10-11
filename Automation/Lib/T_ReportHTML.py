#!/usr/bin/python

import os,sys,json ,time
from datetime import datetime
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
from Lib.T_CNNData import cnnjson
from Lib.T_IPData import ip_info
from Lib.T_Stocks import stock_json

SCRIPT = __file__.split(".")[0]

def p(n):
    print(n)
def _jsondict(jsonstr):
    if _isJson(jsonstr):
        return json.loads(jsonstr)
    else:
        return jsonstr

def _isJson(jsonstr):
    try:
        json_object = json.loads(jsonstr)
        return True
    except Exception:
        return False
def _cnnhtml():
    html=""
    json_dict= _jsondict(cnnjson())
    html=html+"<div style=\"font-family: sans-serif;\"><ul>"
    for item in json_dict:
       sub_json = _jsondict(json_dict[item])
       html=html+"<li style=\"margin-bottom:30px;\"><span style=\"font-weight:bold;\">"+item+"</span>"
       html=html+"<ul>"
       for item2 in sub_json:
           html=html+"<li>"
           html=html+"<p style=\"margin:0;\"><span style=\"font-weight:bold;color:#3D9970;\">"+item2+": </span><span style=\"font-weight:bold;color:#FF4136;\">"+str(sub_json[item2])+"</span></p>"
           html=html+"</li>"
       html=html+"</ul>"
       html=html+"</li>"
    html=html+"</ul></div>"
    return html
def _ipinfohtml():
    html=""
    json_dict= _jsondict(ip_info())
    html=html+"<div style=\"font-family: sans-serif;\"><ul>"
    for item in json_dict:
       sub_json = _jsondict(json_dict[item])
       html=html+"<li style=\"margin-bottom:30px;\"><span style=\"font-weight:bold;\">"+item+"</span>"
       html=html+"<ul>"
       for item2 in sub_json:
           html=html+"<li>"
           html=html+"<p style=\"margin:0;\"><span style=\"font-weight:bold;color:#3D9970;\">"+item2+": </span><span style=\"font-weight:bold;color:#FF4136;\">"+str(sub_json[item2])+"</span></p>"
           html=html+"</li>"
       html=html+"</ul>"
       html=html+"</li>"
    html=html+"</ul></div>"
    return html
def _stockhtml(stock):
    html=""
    json_dict= _jsondict(stock_json(stock))
    html=html+"<div style=\"font-family: sans-serif;\"><ul>"
    for item in json_dict:
       html=html+"<li>"
       html=html+"<p style=\"margin:0;\"><span style=\"font-weight:bold;color:#3D9970;\">"+item+": </span><span style=\"font-weight:bold;color:#FF4136;\">"+str(json_dict[item])+"</span></p>"
       html=html+"</li>"
    html=html+"</ul></div>"
    return html
def constructhtml():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    header = "<h1>Report data as of <span style=\"color:#707070;\">"+dt_string+"</span></h1>"
    html=""
    html=html+header
    html=html+_cnnhtml()
    html=html+_stockhtml("RCL")
    html=html+_ipinfohtml()
    return html
