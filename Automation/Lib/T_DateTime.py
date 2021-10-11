#!/usr/bin/python
import os, sys
from datetime import datetime
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
from Lib.T_Logs import LOG as ___l
SCRIPT = __file__.split(".")[0]
def getDateTime():
    '''returns date and time in the following format:  MM-DD-YYYY-HH-MM-SS-12 '''
    ___l(SCRIPT,getDateTime.__name__,"getDateTime function called")
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %I:%M:%S %p")
    ___l(SCRIPT,getDateTime.__name__,"dt_String :"+dt_string)
    constructDate = dt_string.replace("/","-").replace(":","-").replace(" ","-")
    ___l(SCRIPT,getDateTime.__name__,"constructDate: "+constructDate)
    return constructDate

def getDate():
    '''returns date in the following format:  MM-DD-YYYY'''
    ___l(SCRIPT,getDateTime.__name__,"getDateTime function called")
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y")
    ___l(SCRIPT,getDateTime.__name__,"dt_String :"+dt_string)
    constructDate = dt_string.replace("/","-").replace(" ","-")
    ___l(SCRIPT,getDateTime.__name__,"constructDate: "+constructDate)
    return constructDate
def getTime_12():
    '''returns date in the following format:  HH-MM-SS-12'''
    ___l(SCRIPT,getDateTime.__name__,"getDateTime function called")
    now = datetime.now()
    dt_string = now.strftime("%I:%M:%S %p")
    ___l(SCRIPT,getDateTime.__name__,"dt_String :"+dt_string)
    constructDate = dt_string.replace(":","-").replace(" ","-")
    ___l(SCRIPT,getDateTime.__name__,"constructDate: "+constructDate)
    return constructDate
def getTime_24():
    '''returns date in the following format:  HH-MM-SS-24'''
    ___l(SCRIPT,getDateTime.__name__,"getDateTime function called")
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    ___l(SCRIPT,getDateTime.__name__,"dt_String :"+dt_string)
    constructDate = dt_string.replace(":","-").replace(" ","-")
    ___l(SCRIPT,getDateTime.__name__,"constructDate: "+constructDate)
    return constructDate