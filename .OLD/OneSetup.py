#! /usr/bin/python3
import subprocess , math
import pexpect,os,sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Automation.Lib.T_CronTab import CronTab
from Automation.Lib.T_Thresholds import THRESHOLD_SET ,THRESHOLD_CODE_CHECK,THRESHOLD_CODE
from Automation.Lib.T_Logs import LOG as l
# SCRIPT = __file__.split(".")[0]

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
    
def install_updates_upgrades():
    #Update threshold number : 1
    #Upgrade threshold number : 2
    #Function threshold number : 3
    l(SCRIPT,install_updates_upgrades.__name__,"Installing updates and upgrades")
    l(SCRIPT,install_updates_upgrades.__name__,TTH(1)+" threshold is "+THRESHOLD_CODE(TTH(1)))
    l(SCRIPT,install_updates_upgrades.__name__,TTH(2)+" threshold is "+THRESHOLD_CODE(TTH(2)))
    l(SCRIPT,install_updates_upgrades.__name__,TTH(3)+" threshold is "+THRESHOLD_CODE(TTH(3)))
    if THRESHOLD_CODE_CHECK(TTH(3),0) or THRESHOLD_CODE_CHECK(TTH(3),1):
        THRESHOLD_SET(TTH(3),1)
        l(SCRIPT,install_updates_upgrades.__name__,TTH(3)+" threshold is set to 1")        
        if THRESHOLD_CODE_CHECK(TTH(1),0) or THRESHOLD_CODE_CHECK(TTH(1),1):
            THRESHOLD_SET(TTH(1),1)
            l(SCRIPT,install_updates_upgrades.__name__,TTH(1)+" threshold is set to 1")            
            l(SCRIPT,install_updates_upgrades.__name__,"Installing updates")
            subproc("sudo apt update","")
            l(SCRIPT,install_updates_upgrades.__name__,"Updates installed successfully")
            THRESHOLD_SET(TTH(1),2)
            l(SCRIPT,install_updates_upgrades.__name__,TTH(1)+" threshold is set to 2")
            subproc("shutdown -r now","")
        if THRESHOLD_CODE_CHECK(TTH(2),0) or THRESHOLD_CODE_CHECK(TTH(2),1):            
            THRESHOLD_SET(TTH(2),1)
            l(SCRIPT,install_updates_upgrades.__name__,TTH(2)+" threshold is set to 1")
            l(SCRIPT,install_updates_upgrades.__name__,"Installing upgrades")            
            subproc("sudo apt upgrade -y","")
            l(SCRIPT,install_updates_upgrades.__name__,"Upgrades installed successfully.")            
            THRESHOLD_SET(TTH(2),2)
            l(SCRIPT,install_updates_upgrades.__name__,TTH(2)+" threshold is set to 2")            
            subproc("shutdown -r now","")
        if THRESHOLD_CODE_CHECK(TTH(1),2) and THRESHOLD_CODE_CHECK(TTH(2),2):
            THRESHOLD_SET(TTH(3),2)
            l(SCRIPT,install_updates_upgrades.__name__,TTH(3)+" threshold is set to 2")
            l(SCRIPT,install_updates_upgrades.__name__,"Pi updated and upgraded")
# Install MariaDB
def install_MariaDB():
    #Function threshold number : 4
    l(SCRIPT,install_MariaDB.__name__,"Installing Maria database")
    l(SCRIPT,install_MariaDB.__name__,TTH(4)+" threshold is "+THRESHOLD_CODE(TTH(4)))
    if THRESHOLD_CODE_CHECK(TTH(4),0) or THRESHOLD_CODE_CHECK(TTH(4),1):
        THRESHOLD_SET(TTH(4),1)
        l(SCRIPT,install_MariaDB.__name__,TTH(4)+" threshold is set to 1")
        subproc("sudo apt install mariadb-server -y","")
        l(SCRIPT,install_MariaDB.__name__,"Maria database installed successfully")
        l(SCRIPT,install_MariaDB.__name__,"mysql_secure_installation")
        child = pexpect.spawn("sudo mysql_secure_installation")
        try:
            child.expect("password",timeout=3)
            child.sendline('Rayan1991')
            child.expect("password",timeout=3)
            child.sendline('yes')
            child.expect("password",timeout=3)
            child.sendline('Rayan1991')
            child.expect("password",timeout=3)
            child.sendline('Rayan1991')
            child.expect("anonymous",timeout=3)
            child.sendline('no')
            child.expect("remotely",timeout=3)
            child.sendline('no')
            child.expect("database",timeout=3)
            child.sendline('yes')
            child.expect("privilege",timeout=3)
            child.sendline('yes')
            print(str(child))
            l(SCRIPT,install_MariaDB.__name__,"mysql_secure_installation was successful")
            THRESHOLD_SET(TTH(4),2)
            l(SCRIPT,install_MariaDB.__name__,TTH(4)+" threshold is set to 2")
        except:
            print("Exception was thrown")
            print("debug information:")
            print(str(child))
            l(SCRIPT,install_MariaDB.__name__,"mysql_secure_installation failed")
    
# Install Web Server
def install_WebServer():
    #Function threshold number : 5
    l(SCRIPT,install_WebServer.__name__,"Installing Webserver")
    l(SCRIPT,install_WebServer.__name__,TTH(5)+" threshold is "+THRESHOLD_CODE(TTH(5)))
    if THRESHOLD_CODE_CHECK(TTH(5),0) or THRESHOLD_CODE_CHECK(TTH(5),1):
        THRESHOLD_SET(TTH(5),1)
        l(SCRIPT,install_WebServer.__name__,TTH(5)+" threshold is set to 1")
        l(SCRIPT,install_WebServer.__name__,"Installing apache2")
        subproc("sudo apt install apache2 -y","")
        l(SCRIPT,install_WebServer.__name__,"apache2 installed successfully")
        l(SCRIPT,install_WebServer.__name__,"Installing libapache2-mod-php")
        subproc("sudo apt install php libapache2-mod-php -y","")
        l(SCRIPT,install_WebServer.__name__,"libapache2-mod-php installed successfully")
        l(SCRIPT,install_WebServer.__name__,"Allowing php to run exec commands")
        subproc("echo 'www-data  ALL=NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo","")
        l(SCRIPT,install_WebServer.__name__,"Removing all files from html folder")
        subproc("sudo rm /var/www/html/*","")
        l(SCRIPT,install_WebServer.__name__,"Copying all the files from the ws folder to html folder")
        #_WEB="ws(library)"
        _WEB="ws(pin_io)"
        subproc("sudo cp -r /home/pi/Desktop/rmpi-master/setup/"+_WEB+"/files/* /var/www/html/","")
        l(SCRIPT,install_WebServer.__name__,"Creating a shortcut for html folder in the desktop")
        subproc("sudo ln -s /var/www/html /home/pi/Desktop/html","")
        THRESHOLD_SET(TTH(5),2)
        l(SCRIPT,install_WebServer.__name__,TTH(5)+" threshold is set to 2")
# Install git
def install_Git():
    #Function threshold number : 6
    l(SCRIPT,install_Git.__name__,"Installing Webserver")
    l(SCRIPT,install_Git.__name__,TTH(6)+" threshold is "+THRESHOLD_CODE(TTH(6)))
    if THRESHOLD_CODE_CHECK(TTH(6),0) or THRESHOLD_CODE_CHECK(TTH(6),1):
        THRESHOLD_SET(TTH(6),1)
        l(SCRIPT,install_Git.__name__,TTH(6)+" threshold is set to 1")
        _USERNAME= "rmpi"
        _GMAIL= "ryanmakarem91@gmail.com"
        _KEYPI= "rmpi2021"
        _ORIGIN= "rmak1991/rmpi.git"
        _DIRNAME= "rmpi-master"
        PATH="/home/pi/Desktop/"+_DIRNAME
        DESKTOP = "/home/pi/Desktop/"
        l(SCRIPT,install_Git.__name__,"Installing git")        
        #subproc("sudo apt install git","")
        l(SCRIPT,install_Git.__name__,"Git installed successfully")
        l(SCRIPT,install_Git.__name__,"Adding global user.name")        
        #subproc("git config --global user.name '"+_USERNAME+"'","")
        l(SCRIPT,install_Git.__name__,"Adding global user.email")
        #subproc("git config --global user.email '"+_GMAIL+"'","")
        l(SCRIPT,install_Git.__name__,"Adding global core.editor")
        #subproc("git config --global core.editor nano","")
        l(SCRIPT,install_Git.__name__,"Create folder " +_DIRNAME+" in "+DESKTOP)
        #subproc("mkdir -p "+_DIRNAME,DESKTOP)
        #subproc("git init",PATH)
        #subproc("git add --all",PATH)
        #subproc("git status",PATH)
        l(SCRIPT,install_Git.__name__,"Enable SSH")
        #subproc("sudo systemctl enable ssh","")
        l(SCRIPT,install_Git.__name__,"Start SSH")
        #subproc("sudo systemctl start ssh","")
        subproc("git remote add origin git@github.com:"+_ORIGIN,PATH)
        l(SCRIPT,install_Git.__name__,"Generate key")
        args=["ssh-keygen","-t","rsa","-b","4096","-C",_KEYPI]
        childprocess = subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        child_out = childprocess.communicate(input=b'\n')
        subproc("ssh-keygen -E sha256 -lf ~/.ssh/id_rsa.pub","")
        print('*************************\nAdd the public key below to github\n*************************\n')
        subproc("cat ~/.ssh/id_rsa.pub","")
        THRESHOLD_SET(TTH(6),2)
        l(SCRIPT,install_Git.__name__,TTH(6)+" threshold is set to 2")        
    
def add_CronJobs():
    #Function threshold number : 7
    l(SCRIPT,add_CronJobs.__name__,"Adding Cron jobs")
    l(SCRIPT,add_CronJobs.__name__,TTH(7)+" threshold is "+THRESHOLD_CODE(TTH(7)))
    if THRESHOLD_CODE_CHECK(TTH(7),0) or THRESHOLD_CODE_CHECK(TTH(7),1):
        THRESHOLD_SET(TTH(7),1)
        l(SCRIPT,add_CronJobs.__name__,TTH(7)+" threshold is set to 1")
        l(SCRIPT,add_CronJobs.__name__,"Changind mode to executable")
        subproc("sudo chmod +x /home/pi/Desktop/rmpi-master/","")
        CJ_1 = CronTab()
        CJ_3 = CronTab()
        CJ_1.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_DailyReport.py >> ~/cron.log 2>&1")
        CJ_3.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_PI_Reboot.py>> ~/cron.log 2>&1")
        CJ_1.comment("RUN DAILY REPORT AT 6:00 AM")
        CJ_3.comment("REBOOT MACHINE AT 12:00 AM EVERYDAY")
        CJ_1.on().minute(0)
        CJ_1.on().hour(6)
        CJ_3.on().minute(0)
        CJ_3.on().hour(0)
        CJ_1.schedule()
        l(SCRIPT,add_CronJobs.__name__,"Adding J_DailyReport job")
        CJ_3.schedule()
        l(SCRIPT,add_CronJobs.__name__,"Adding J_PI_Reboot job")
        AUTOPROCESS_INTERVAL = 30
        RANGE=math.ceil(60/AUTOPROCESS_INTERVAL)
        for x in range(0,int(RANGE)):
            CJ_2 = CronTab()
            CMD = "sleep "+str((x*AUTOPROCESS_INTERVAL))+" ; /usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/autoprocess.py >> ~/cron.log 2>&1"
            CJ_2.command(CMD)
            CJ_2.comment("RUN AUTOPROCESS AT SECOND "+str((x*AUTOPROCESS_INTERVAL)))
            CJ_2.schedule()
        l(SCRIPT,add_CronJobs.__name__,"Adding autoprocess jobs")
        THRESHOLD_SET(TTH(7),2)
        l(SCRIPT,add_CronJobs.__name__,TTH(7)+" threshold is set to 2")   
def no_prompt_exec():
    #Function threshold number : 8
    l(SCRIPT,no_prompt_exec.__name__,"Enabling don't ask options on launch executable file")
    l(SCRIPT,no_prompt_exec.__name__,TTH(8)+" threshold is "+THRESHOLD_CODE(TTH(8)))
    if THRESHOLD_CODE_CHECK(TTH(8),0) or THRESHOLD_CODE_CHECK(TTH(8),1):
        THRESHOLD_SET(TTH(8),1)
        l(SCRIPT,no_prompt_exec.__name__,TTH(8)+" threshold is set to 1")
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
        l(SCRIPT,no_prompt_exec.__name__,"Don't ask options on launch executable file enabled")
        THRESHOLD_SET(TTH(8),2)
        l(SCRIPT,no_prompt_exec.__name__,TTH(8)+" threshold is set to 2")           
def set_rc_local():
    #Function threshold number : 9
    l(SCRIPT,add_CronJobs.__name__,"Enabling don't ask options on launch executable file")
    l(SCRIPT,add_CronJobs.__name__,TTH(9)+" threshold is "+THRESHOLD_CODE(TTH(9)))
    if THRESHOLD_CODE_CHECK(TTH(9),0) or THRESHOLD_CODE_CHECK(TTH(9),1):
        THRESHOLD_SET(TTH(9),1)
        l(SCRIPT,add_CronJobs.__name__,TTH(9)+" threshold is set to 1")
        _PATH="/etc/rc.local"
        l(SCRIPT,set_rc_local.__name__,"Change rc.local owner to pi")
        subproc("sudo chown pi "+_PATH,"")
        _FILE = Path(_PATH)
        _FILE_READ= open(_FILE, 'r')
        Lines = _FILE_READ.readlines()
        new_text = ""
        for line in Lines:
            if line.startswith("exit 0"):
                new_text = new_text+"python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_PI_Reboot_After.py"+"\n\n"
                new_text = new_text+"exit 0"+"\n\n"
            else:
                new_text = new_text+line+"\n"
        _FILE_WRITE= open(_FILE, "w")        
        _FILE_WRITE.write(new_text)
        _FILE_WRITE.close()
        l(SCRIPT,set_rc_local.__name__,"J_PI_Reboot_After is added to rc.local")
        l(SCRIPT,set_rc_local.__name__,"Change rc.local owner to root")
        subproc("sudo chown root "+_PATH,"")
        THRESHOLD_SET(TTH(9),2)
        l(SCRIPT,no_prompt_exec.__name__,TTH(9)+" threshold is set to 2")
    
def run():
    l(SCRIPT,run.__name__,"Started")
    #Function threshold number :10
    l(SCRIPT,run.__name__,TTH(10)+" threshold is "+THRESHOLD_CODE(TTH(10)))
    if THRESHOLD_CODE_CHECK(TTH(10),0) or THRESHOLD_CODE_CHECK(TTH(10),1):
        l(SCRIPT,run.__name__,TTH(10)+" threshold set to 1")
        THRESHOLD_SET(TTH(10),1)
        l(SCRIPT,run.__name__,"Starting setup")
        
        l(SCRIPT,run.__name__,"Adding startup script to rc.local")
        set_rc_local()
        l(SCRIPT,run.__name__,"Startup script added sccessfully")
        
        l(SCRIPT,run.__name__,"Disabling execution prompt")                
        no_prompt_exec()
        l(SCRIPT,run.__name__,"Execution prompt disabled successfully")

#         l(SCRIPT,run.__name__,"Installing updates and upgrades")
#         install_updates_upgrades()
#         l(SCRIPT,run.__name__,"Updates and upgrades installation finished")
#         
#         l(SCRIPT,run.__name__,"Installing webserver")
#         install_WebServer()
#         l(SCRIPT,run.__name__,"Webserver installation finished")
#         
#         l(SCRIPT,run.__name__,"Installing MariaDB")
#         install_MariaDB()
#         l(SCRIPT,run.__name__,"MariaDB installation finished")
# 
#         l(SCRIPT,run.__name__,"Installing Git")
        install_Git()
#         l(SCRIPT,run.__name__,"Git installation finished")
#         
#         l(SCRIPT,run.__name__,"Adding Cron jobs")        
#         add_CronJobs()
#         l(SCRIPT,run.__name__,"Cron jobs added successfully")
#
#         l(SCRIPT,run.__name__,"Setup completed")
#         THRESHOLD_SET(TTH(10),2)
#         l(SCRIPT,no_prompt_exec.__name__,TTH(10)+" threshold is set to 2")

def add_CronJobs2():
    #Function threshold number : 7
    subproc("sudo chmod +x /home/pi/Desktop/rmpi-master/","")
    CJ_1 = CronTab()
    CJ_3 = CronTab()
    CJ_1.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_DailyReport.py >> ~/cron.log 2>&1")
    CJ_3.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_PI_Reboot.py>> ~/cron.log 2>&1")
    CJ_1.comment("RUN DAILY REPORT AT 6:00 AM")
    CJ_3.comment("REBOOT MACHINE AT 12:00 AM EVERYDAY")
    CJ_1.on().minute(0)
    CJ_1.on().hour(6)
    CJ_3.on().minute(0)
    CJ_3.on().hour(0)
    CJ_1.schedule()
    CJ_3.schedule()
    AUTOPROCESS_INTERVAL = 30
    RANGE=math.ceil(60/AUTOPROCESS_INTERVAL)
    for x in range(0,int(RANGE)):
        CJ_2 = CronTab()
        CMD = "sleep "+str((x*AUTOPROCESS_INTERVAL))+" ; /usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/autoprocess.py >> ~/cron.log 2>&1"
        CJ_2.command(CMD)
        CJ_2.comment("RUN AUTOPROCESS AT SECOND "+str((x*AUTOPROCESS_INTERVAL)))
        CJ_2.schedule()
add_CronJobs2()