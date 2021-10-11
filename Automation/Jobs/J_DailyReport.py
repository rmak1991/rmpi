#!/usr/bin/python
import os,sys
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_ReportHTML import constructhtml
from Lib.T_Email import send_email
def sendDailyReport():
    send_email("ryanmakarem91@gmail.com","Daily morning report","MorningEmail",constructhtml())        
sendDailyReport()