#!/usr/bin/python

import os, sys
from pathlib import Path
from datetime import datetime
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P

LOGS_FILE = "/logs.log"
def LOG(script,function,data):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %I:%M:%S %p")
    arr1 = dt_string.split(" ")[0].split("/")
    arr2 = dt_string.split(" ")[1].split(":")
    AP = dt_string.split(" ")[2]
    constructDate = arr1[1]+"-"+arr1[0]+"-"+arr1[2]+"-"+arr2[0]+"-"+arr2[1]+"-"+arr2[2]+"-"+AP
    _DATA = constructDate +"@"+str(script)+"."+str(function)+": "+str(data)+"\n"
    _PATH = _P.LOGS_PATH+LOGS_FILE
    _FILE = Path(_PATH)
    _FILE_WRITE= open(_FILE, "a")
    _FILE_WRITE.write(_DATA)
    _FILE_WRITE.close()