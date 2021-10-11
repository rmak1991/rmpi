#!/usr/bin/python
#******THRESHOLDS******
#REBOOT (0 = NO ACTIONS, 1 = RUN AFTER REBOOT SCRIPT)

import os, sys
from pathlib import Path
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
from Lib.T_FileHandler import *
from Lib.T_Logs import LOG as l
SCRIPT = __file__.split(".")[0]
def THRESHOLD_EXISTS(threshold):
    l(SCRIPT,THRESHOLD_EXISTS.__name__,"function called")
    THRESHOLD_NAME = threshold+".TTH"
    l(SCRIPT,THRESHOLD_EXISTS.__name__,"THRESHOLD: "+str(threshold))
    return FILE_EXISTS(THRESHOLD_NAME,_P.TTH_PATH)
def THRESHOLD_CODE(threshold):
    l(SCRIPT,THRESHOLD_CODE.__name__,"function called")
    THRESHOLD_NAME = threshold+".TTH"
    l(SCRIPT,THRESHOLD_CODE.__name__,"THRESHOLD: "+str(threshold))
    return FILE_READ(THRESHOLD_NAME,_P.TTH_PATH)
def THRESHOLD_CODE_CHECK(threshold,code):
    l(SCRIPT,THRESHOLD_CODE_CHECK.__name__,"function called")
    THRESHOLD_NAME = threshold+".TTH"
    l(SCRIPT,THRESHOLD_CODE_CHECK.__name__,"check CODE:"+str(code)+",THRESHOLD: "+str(threshold))
    return FILE_CONTENT_CHECK(THRESHOLD_NAME,_P.TTH_PATH,code)
def THRESHOLD_SET(threshold,code):
    l(SCRIPT,THRESHOLD_SET.__name__,"function called")
    THRESHOLD_NAME = threshold+".TTH"
    l(SCRIPT,THRESHOLD_SET.__name__,"SET CODE "+str(code)+",THRESHOLD: "+ str(threshold))
    return FILE_WRITE_OVERWRITE(THRESHOLD_NAME,_P.TTH_PATH,code)
def THRESHOLD_DELETE(threshold):
    l(SCRIPT,THRESHOLD_DELETE.__name__,"function called")
    THRESHOLD_NAME = threshold+".TTH"
    l(SCRIPT,THRESHOLD_SET.__name__,"REMOVE THRESHOLD: "+ str(threshold))
    return FILE_DELETE(THRESHOLD_NAME,_P.TTH_PATH)
