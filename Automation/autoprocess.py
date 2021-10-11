#!/usr/bin/python

import os, sys, time
from Lib.T_DateTime import getDateTime
from Lib.T_Thresholds import *
from Lib.T_FileHandler import *
from Lib.T_Logs import LOG as l
from Jobs.J_CheckServices import runServiceCheck
from subprocess import Popen, PIPE
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = __file__.split(".")[0]

def TTH():
    _THRESHOLDS={}
    _THRESHOLDS[0]="REBOOT"
    _THRESHOLDS[1]="IN_UPD"
    _THRESHOLDS[2]="IN_UPG"
    _THRESHOLDS[3]="IN_UPDG"
    _THRESHOLDS[4]="IN_MARIADB"
    _THRESHOLDS[5]="IN_WEBSER"
    _THRESHOLDS[6]="IN_GIT"
    _THRESHOLDS[7]="IN_CRON"
    _THRESHOLDS[8]="IN_PROMPTEXEC"
    _THRESHOLDS[9]="IN_RCLOCAL"
    _THRESHOLDS[10]="IN_INPROGRESS"
    return _THRESHOLDS

def RUN_TTH_CHECK():
    pass
#     PATH = os.path.dirname(os.path.abspath(__file__))+"/TTH"
#      for entry in os.scandir(PATH):
#          if entry.path.endswith(".TTH") and entry.is_file():
#              pass
#

def RUN_PROCESS():
    _DATE = getDateTime()
    runServiceCheck(_DATE)
    a = TTH()
    print("autoprocess ran")
#     if THRESHOLD_CODE_CHECK(a[10],2):
#         print(True)
#     else:
#         pass
#         run_setup()    
    #_DATE = getDateTime()
    #l(SCRIPT,RUN_PROCESS.__name__,"AUTOPROCESS RAN at "+str(_DATE))
    #print("auto process ran " +_DATE)
    #runServiceCheck(_DATE)
while True:
    time.sleep(30)
    RUN_PROCESS()



