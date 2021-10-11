#! /usr/bin/python3
import subprocess , math
import pexpect
from automation.lib.T_CronTab import CronTab
from automation.lib.T_Thresholds import THRESHOLD_SET ,THRESHOLD_CODE_CHECK,THRESHOLD_CODE
from automation.lib.T_Logs import LOG as l
from pathlib import Path
SCRIPT = __file__.split(".")[0]

#THRESHOLDS
#0 NOT STARTED
#1 STARTED-NOT COMPLETED
#2 COMPLETED
#*************************
#*************************
#*************************
#*************************
#FUNCTIONS
#install_updates_upgrades
#install_MariaDB
#install_WebServer
#install_Git
#add_CronJobs
#no_prompt_exec
#set_rc_local
#
#
def TTH(th):
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
    return _THRESHOLDS[th]
def subproc(cmd,directory):
    if directory=="":
        subprocess.run([cmd],shell=True,check=True)
    else:
        subprocess.run([cmd],shell=True,check=True,cwd=directory)
    
# def install_updates_upgrades():
#     #Update threshold number : 1
#     #Upgrade threshold number : 2
#     #Function threshold number : 3
#     if THRESHOLD_CODE_CHECK(TTH(3),0) or THRESHOLD_CODE_CHECK(TTH(3),1):
#         THRESHOLD_SET(TTH(3),1)
#         if THRESHOLD_CODE_CHECK(TTH(1),0) or THRESHOLD_CODE_CHECK(TTH(1),1):
#             THRESHOLD_SET(TTH(1),1)
#             subproc("sudo apt update","")
#             THRESHOLD_SET(TTH(1),2)
#             subproc("shutdown -r now","")
#         if THRESHOLD_CODE_CHECK(TTH(2),0) or THRESHOLD_CODE_CHECK(TTH(2),1):            
#             THRESHOLD_SET(TTH(2),1)
#             subproc("sudo apt upgrade -y","")
#             THRESHOLD_SET(TTH(2),2)
#             subproc("shutdown -r now","")
#         if THRESHOLD_CODE_CHECK(TTH(1),2) and THRESHOLD_CODE_CHECK(TTH(2),2):
#             THRESHOLD_SET(TTH(3),2)
# Install MariaDB
# def install_MariaDB():
#     #Function threshold number : 4
#     if THRESHOLD_CODE_CHECK(TTH(4),0) or THRESHOLD_CODE_CHECK(TTH(4),1):
#         THRESHOLD_SET(TTH(4),1)
#         subproc("sudo apt install mariadb-server -y","")
#         child = pexpect.spawn("sudo mysql_secure_installation")
#         try:
#             child.expect("password",timeout=3)
#             child.sendline('Rayan1991')
#             child.expect("password",timeout=3)
#             child.sendline('yes')
#             child.expect("password",timeout=3)
#             child.sendline('Rayan1991')
#             child.expect("password",timeout=3)
#             child.sendline('Rayan1991')
#             child.expect("anonymous",timeout=3)
#             child.sendline('no')
#             child.expect("remotely",timeout=3)
#             child.sendline('no')
#             child.expect("database",timeout=3)
#             child.sendline('yes')
#             child.expect("privilege",timeout=3)
#             child.sendline('yes')
#             print(str(child))
#             THRESHOLD_SET(TTH(4),2)
#         except:
#             print("Exception was thrown")
#             print("debug information:")
#             print(str(child))
#     
# Install Web Server
# def install_WebServer():
#     #Function threshold number : 5
#     if THRESHOLD_CODE_CHECK(TTH(5),0) or THRESHOLD_CODE_CHECK(TTH(5),1):
#         THRESHOLD_SET(TTH(5),1)
#         subproc("sudo apt install apache2 -y","")
#         subproc("sudo apt install php libapache2-mod-php -y","")
#         subproc("echo 'www-data  ALL=NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo","")
#         subproc("sudo rm /var/www/html/*","")
#         #_WEB="ws(library)"
#         _WEB="ws(pin_io)"
#         subproc("sudo cp -r /home/pi/Desktop/rmpi-master/setup/"+_WEB+"/files/* /var/www/html/","")
#         subproc("sudo ln -s /var/www/html /home/pi/Desktop/html","")
#         THRESHOLD_SET(TTH(5),2)
# Install git
# def install_Git():
#     #Function threshold number : 6
#     if THRESHOLD_CODE_CHECK(TTH(6),0) or THRESHOLD_CODE_CHECK(TTH(6),1):
#         THRESHOLD_SET(TTH(6),1)
#         _USERNAME= "rmpi"
#         _GMAIL= "ryanmakarem91@gmail.com"
#         _KEYPI= "rmpi2021"
#         _ORIGIN= "rmak1991/rmpi.git"
#         _DIRNAME= "rmpi-master"
#         PATH="/home/pi/Desktop/"+_DIRNAME
#         DESKTOP = "/home/pi/Desktop/"
#         subproc("sudo apt install git","")
#         subproc("git config --global user.name '"+_USERNAME+"'","")
#         subproc("git config --global user.email '"+_GMAIL+"'","")
#         subproc("git config --global core.editor nano","")
#         subproc("mkdir -p "+_DIRNAME,DESKTOP)
#         subproc("git init",PATH)
#         subproc("git add --all",PATH)
#         subproc("git status",PATH)
#         subproc("sudo systemctl enable ssh","")
#         subproc("sudo systemctl start ssh","")
#         subproc("git remote add origin git@github.com:"+_ORIGIN,PATH)
#         args=["ssh-keygen","-t","rsa","-b","4096","-C",_KEYPI]
#         childprocess = subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
#         child_out = childprocess.communicate(input=b'\n')
#         subproc("ssh-keygen -E sha256 -lf ~/.ssh/id_rsa.pub","")
#         print('*************************\nAdd the public key below to github\n*************************\n')
#         subproc("cat ~/.ssh/id_rsa.pub","")
#         THRESHOLD_SET(TTH(6),2)
    
# def add_CronJobs():
#     #Function threshold number : 7
#     if THRESHOLD_CODE_CHECK(TTH(7),0) or THRESHOLD_CODE_CHECK(TTH(7),1):
#         THRESHOLD_SET(TTH(7),1)
# #         subproc("sudo chmod +x /home/pi/Desktop/rmpi-master/","")
#         CJ_1 = CronTab()
#         CJ_3 = CronTab()
#         CJ_1.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_DailyReport.py >> ~/cron.log 2>&1")
#         CJ_3.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_PI_Reboot.py>> ~/cron.log 2>&1")
#         CJ_1.comment("RUN DAILY REPORT AT 6:00 AM")
#         CJ_3.comment("REBOOT MACHINE AT 12:00 AM EVERYDAY")
#         CJ_1.on().minute(0)
#         CJ_1.on().hour(6)
#         CJ_3.on().minute(0)
#         CJ_3.on().hour(0)
#         CJ_1.schedule()
#         CJ_3.schedule()
#         AUTOPROCESS_INTERVAL = 30
#         RANGE=math.ceil(60/AUTOPROCESS_INTERVAL)
#         for x in range(0,int(RANGE)):
#             CJ_2 = CronTab()
#             CMD = "sleep "+str((x*AUTOPROCESS_INTERVAL))+" ; /usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/autoprocess.py >> ~/cron.log 2>&1"
#             CJ_2.command(CMD)
#             CJ_2.comment("RUN AUTOPROCESS AT SECOND "+str((x*AUTOPROCESS_INTERVAL)))
#             CJ_2.schedule()
#         THRESHOLD_SET(TTH(7),2)
def no_prompt_exec():
    #Function threshold number : 8
    if THRESHOLD_CODE_CHECK(TTH(8),0) or THRESHOLD_CODE_CHECK(TTH(8),1):
        THRESHOLD_SET(TTH(8),1)
        _PATH="/home/pi/.config/libfm/libfm.conf"
        _FILE = Path(_PATH)
        _FILE_READ= open(_FILE, 'r')
        Lines = _FILE_READ.readlines()
        new_text = ""
        for line in Lines:
            if line.startswith("quick_exec"):
                new_text = new_text+"quick_exec=1"+"\n\n"
            else:
                new_text = new_text+line+"\n"
        _FILE_WRITE= open(_FILE, "w")        
        _FILE_WRITE.write(new_text)
        _FILE_WRITE.close()
        THRESHOLD_SET(TTH(8),2)
# def set_rc_local():
#     #Function threshold number : 9
#     if THRESHOLD_CODE_CHECK(TTH(9),0) or THRESHOLD_CODE_CHECK(TTH(9),1):
#         THRESHOLD_SET(TTH(9),1)
#         _PATH="/etc/rc.local"
#         subproc("sudo chown pi "+_PATH,"")
#         _FILE = Path(_PATH)
#         _FILE_READ= open(_FILE, 'r')
#         Lines = _FILE_READ.readlines()
#         new_text = ""
#         for line in Lines:
#             if line.startswith("exit 0"):
#                 new_text = new_text+"python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_PI_Reboot_After.py"+"\n\n"
#                 new_text = new_text+"exit 0"+"\n\n"
#             else:
#                 new_text = new_text+line+"\n"
#         _FILE_WRITE= open(_FILE, "w")        
#         _FILE_WRITE.write(new_text)
#         _FILE_WRITE.close()
#         subproc("sudo chown root "+_PATH,"")
#         THRESHOLD_SET(TTH(9),2)    
def run():
    #Function threshold number :10
    if THRESHOLD_CODE_CHECK(TTH(10),0) or THRESHOLD_CODE_CHECK(TTH(10),1):
        THRESHOLD_SET(TTH(10),1)
        set_rc_local()
        no_prompt_exec()
        install_updates_upgrades()
        install_WebServer() 
        install_MariaDB()
        install_Git()    
        add_CronJobs()
        THRESHOLD_SET(TTH(10),2)
run()