import subprocess, os, sys
from pathlib import Path
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
class CronTab(object):
    def __init__(self):
        self.cron_freq = "* * * * *"
        self.cron_command =""
        self.cron_comment =""
    def every(self):
        return self._every(self)
    def on(self):
        return self._on(self)
    def getfreq(self):
        return self.cron_freq
    def command(self,cmd):
        self.cron_command = cmd
    def comment(self,cmnt):
        self.cron_comment=cmnt
    def setfreq(self,freq):
        self.cron_freq = freq
    class _on(object):
        def __init__(self, th):
            self.th = th
        def setfreq(self,ind,val):
            arr = self.th.cron_freq.split(" ")
            arr[ind] = str(val)
            newfreq=""
            for x in arr:
                newfreq = newfreq + str(x) +" "
            newfreq = newfreq.rstrip(newfreq[-1])
            self.th.cron_freq = newfreq
        def minute(self,minute):
            self.setfreq(0,minute)
        def hour(self,hour):
            self.setfreq(1,hour)            
        def dom(self,dom):
            self.setfreq(2,dom)
        def month(self,month):
            self.setfreq(3,month)
        def dow(self,dow):
            self.setfreq(4,dow)
    class _every(object):
        def __init__(self, th):
            self.th = th
        def setfreq(self,ind,val):
            arr = self.th.cron_freq.split(" ")
            arr[ind] = "*/"+str(val)
            newfreq=""
            for x in arr:
                newfreq = newfreq + str(x) +" "
            newfreq = newfreq.rstrip(newfreq[-1])
            self.th.cron_freq = newfreq
        def minute(self,minute):
            self.setfreq(0,minute)
        def hour(self,hour):
            self.setfreq(1,hour)            
        def dom(self,dom):
            self.setfreq(2,dom)
        def month(self,month):
            self.setfreq(3,month)
        def dow(self,dow):
            self.setfreq(4,dow)
    def schedule(self):
        crontxt = self.cron_freq+" "+self.cron_command
        _PATH= "/var/spool/cron/crontabs/pi"
        _FILE = Path(_PATH)
        _FILE_WRITE= open(_FILE, "a")
        if self.cron_comment !="":
            _FILE_WRITE.write("#"+str(self.cron_comment)+"\n")
        _FILE_WRITE.write(str(crontxt)+"\n")
        _FILE_WRITE.close()