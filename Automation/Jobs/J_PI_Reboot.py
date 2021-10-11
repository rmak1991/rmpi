#!/usr/bin/python

import os, sys, time
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_DateTime import getDateTime
from Lib.T_Thresholds import *
from Lib.T_Global import PATHS as _P
def reboot():
    _TTH = "REBOOT"
    _TTH_CODE=1
    filename = _P.FLAGS_PATH+"/SystemReboot_"+str(getDateTime())+".flg"
    f = open(filename, "a")
    f.write("")
    f.close()
    THRESHOLD_SET(_TTH,_TTH_CODE)
    if THRESHOLD_CODE_CHECK(_TTH,_TTH_CODE):
        os.system('sudo shutdown -r now')
reboot()