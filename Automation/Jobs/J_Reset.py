import random,json
from datetime import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Lib.T_FileHandler import *


PATH_TTH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/TTH"
def _DELETE_ALL_THRESHOLDS():
    dir = PATH_TTH
    for file in os.scandir(dir):
        os.remove(file.path)
    
def _CREATE_ALL_THRESHOLDS():
    _THRESHOLDS={}
    _THRESHOLDS["REBOOT"]=0
    _THRESHOLDS["IN_UPD"]=0
    _THRESHOLDS["IN_UPG"]=0
    _THRESHOLDS["IN_UPDG"]=0
    _THRESHOLDS["IN_MARIADB"]=0
    _THRESHOLDS["IN_WEBSER"]=0
    _THRESHOLDS["IN_GIT"]=0
    _THRESHOLDS["IN_CRON"]=0
    _THRESHOLDS["IN_PROMPTEXEC"]=0
    _THRESHOLDS["IN_RCLOCAL"]=0
    _THRESHOLDS["IN_INPROGRESS"]=0   
    for file in _THRESHOLDS:
        FILE_WRITE_OVERWRITE(file+".TTH",PATH_TTH,_THRESHOLDS[file])
def reset():
    _DELETE_ALL_THRESHOLDS()
    _CREATE_ALL_THRESHOLDS()
reset()    