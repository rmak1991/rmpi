#!/usr/bin/python
from tkinter import *
import math,json
class PATHS():
    __APPPATH = "/home/pi/Desktop"
    RMPI_MASTER_PATH =__APPPATH+"/rmpi-master" 
    AUTOMATION_PATH =RMPI_MASTER_PATH+"/Automation"
    DATA_PATH = AUTOMATION_PATH+"/Data"
    DATA_ARCHIVE_PATH=AUTOMATION_PATH+"/Data/Archive"
    LIB_PATH=AUTOMATION_PATH+"/Lib"
    JOBS_PATH=AUTOMATION_PATH+"/Jobs"
    LOGS_PATH=AUTOMATION_PATH+"/Logs"
    LOGS_ARCHIVE_PATH=AUTOMATION_PATH+"/Logs/Archive"
    FLAGS_PATH=AUTOMATION_PATH+"/Flags"
    FLAGS_ARCHIVE_PATH=AUTOMATION_PATH+"/Flags/Archive"
    TTH_PATH=AUTOMATION_PATH+"/TTH"
    PICS_PATH=AUTOMATION_PATH+"/Pics"
    RCLOCALPATH="/etc/rc.local"
    RCLOCALORIGPATH="/etc/rc.local.orig"
    CRONTABPATH = "/var/spool/cron/crontabs/"
    WS_PIN_IO_PATH = "/home/pi/Desktop/rmpi-master/ws_pin_io/files"
    WS_LIBRARY_PATH = "/home/pi/Desktop/rmpi-master/ws_library/files"
    WS_EMPTY_PATH = "/home/pi/Desktop/rmpi-master/ws_empty/files"
    VARHTMLPATH = "/var/www/html/"
    DESKTOPHTMLPATH="/home/pi/Desktop/html"
    SSHPATH="/home/pi/.ssh"
    PYTHONPATH ="/usr/bin/python3"
    JSON_SETUP_CONFIG = "setup_config.json"
class Internalvars():
    FLAG="flag.flag"
    ID_RSA = "id_rsa"
    ID_RSAPUB = "id_rsa.pub"
    USERNAME= "rmpi"
    GMAIL= "ryanmakarem91@gmail.com"
    KEYPI= "rmpi2021"
    ORIGIN= "rmak1991/rmpi.git"
    DBUSER="RMPIDBU"
    DBPASSWORD="rmpi2021"
class COMMAND_LISTS():
    __dic={}
    __dic["UP"]={}
    __dic["WS"]={}
    __dic["MDB"]={}
    __dic["GIT"]={}
    __dic["PRE"]={}
    __dic["PRE"]["0"] = [["sudo", "chmod","+x",PATHS.RMPI_MASTER_PATH],False,"Change rmpi-master mode to execute"]
    __dic["PRE"]["1"] = [["find", PATHS.RMPI_MASTER_PATH,"-executable"],False,"Check rmpi-master mode"]
    __dic["PRE"]["2"] = [["sudo", "chown","pi",PATHS.CRONTABPATH],False,"Change crontabs owner to pi"]
    __dic["PRE"]["3"] = [["sudo", "cp",PATHS.RCLOCALPATH,PATHS.RCLOCALORIGPATH],False,"Backup rc.local file"]
    __dic["PRE"]["4"] = [["sudo", "chown","pi",PATHS.RCLOCALPATH],False,"Change rc.local owner to pi"]
    __dic["PRE"]["5"] = [["sudo", "chown","root",PATHS.RCLOCALPATH],False,"Change rc.local owner to root"]
    __dic["UP"]["0"] = [["sudo", "apt","update"],False,"Installing updates"]
    __dic["UP"]["1"] = [["sudo", "apt","upgrade","-y"],False,"Installing upgrades"]
    __dic["WS"]["0"] = [["sudo", "apt","install","apache2","-y"],False,"Installing apache2"]
    __dic["WS"]["1"] = [["sudo", "apt","install","php","libapache2-mod-php","-y"],False,"Installing libapache2-mod-php"]
    __dic["WS"]["2"] = ["echo 'www-data  ALL=NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo",True,"Enable php to run shell commands"]
    __dic["WS"]["3"] = {}
    __dic["WS"]["3"]["PWEB"] = ["sudo touch "+PATHS.WS_PIN_IO_PATH+"/"+Internalvars.FLAG,True,"Create empty flag file in html"]
    __dic["WS"]["3"]["LWEB"] = ["sudo touch "+PATHS.WS_LIBRARY_PATH+"/"+Internalvars.FLAG,True,"Create empty flag file in html"]
    __dic["WS"]["3"]["EMPTY"] = ["sudo touch "+PATHS.WS_EMPTY_PATH+"/"+Internalvars.FLAG,True,"Create empty flag file in html"]
    __dic["WS"]["4"] = ["sudo rm -r "+PATHS.VARHTMLPATH,True,"Clear default html folder"]
    __dic["WS"]["5"] = ["sudo mkdir "+PATHS.VARHTMLPATH,True,"Create html folder"]
    __dic["WS"]["6"] = {}
    __dic["WS"]["6"]["PWEB"]=["sudo cp -r "+PATHS.WS_PIN_IO_PATH+"/* "+PATHS.VARHTMLPATH,True,"Copy project files to html folder"]
    __dic["WS"]["6"]["LWEB"]=["sudo cp -r "+PATHS.WS_LIBRARY_PATH+"/* "+PATHS.VARHTMLPATH,True,"Copy project files to html folder"]
    __dic["WS"]["6"]["EMPTY"]=["sudo cp -r "+PATHS.WS_EMPTY_PATH+"/* "+PATHS.VARHTMLPATH,True,"Copy project files to html folder"] 
    __dic["WS"]["7"] = {}
    __dic["WS"]["7"]["PWEB"] = ["sudo rm "+PATHS.VARHTMLPATH+"/"+Internalvars.FLAG+" "+PATHS.WS_PIN_IO_PATH+"/"+Internalvars.FLAG,True,"Remove flag file from html and orignal folder"]
    __dic["WS"]["7"]["LWEB"] = ["sudo rm "+PATHS.VARHTMLPATH+"/"+Internalvars.FLAG+" "+PATHS.WS_LIBRARY_PATH+"/"+Internalvars.FLAG,True,"Remove flag file from html and orignal folder"]
    __dic["WS"]["7"]["EMPTY"] = ["sudo rm "+PATHS.VARHTMLPATH+"/"+Internalvars.FLAG+" "+PATHS.WS_EMPTY_PATH+"/"+Internalvars.FLAG,True,"Remove flag file from html and orignal folder"]
    __dic["WS"]["8"] = ["sudo ln -s "+PATHS.VARHTMLPATH+" "+PATHS.DESKTOPHTMLPATH,True,"Create html folder shortcut on Desktop"]
    __dic["GIT"]["0"] =[["sudo", "apt","install","git"],False,"Installing git"]
    __dic["GIT"]["1"] =[["git", "config","--global","user.name","'"+Internalvars.USERNAME+"'"],False,"Set GIT user.name to "+Internalvars.USERNAME]
    __dic["GIT"]["2"] =[["git", "config","--global","user.email","'"+Internalvars.GMAIL+"'"],False,"Set GIT user.email to "+Internalvars.GMAIL]
    __dic["GIT"]["3"] =[["git", "config","--global","core.editor","nano"],False,"Set GIT core.editor to nano"]
    __dic["GIT"]["4"] =[["mkdir", "-p",PATHS.RMPI_MASTER_PATH],False,"Create rmpi-master folder"]
    __dic["GIT"]["5"] =[["git", "init",PATHS.RMPI_MASTER_PATH],False,"create a new repository in a directory"]
    __dic["GIT"]["6"] =[["git", "add","--all",PATHS.RMPI_MASTER_PATH],False,"Add all files or changes to the repository"]
    __dic["GIT"]["7"] =[["cd "+PATHS.RMPI_MASTER_PATH+" && git status"],True,"Check git status"]
    __dic["GIT"]["8"] =[["sudo", "systemctl","enable","ssh"],False,"Enable SSH service"]
    __dic["GIT"]["9"] =[["sudo", "systemctl","start","ssh"],False,"Start SSH service"]
    __dic["GIT"]["10"] =[["sudo", "service","ssh","status"],False,"Check SSH service"]
    __dic["GIT"]["11"] =[["cd "+PATHS.RMPI_MASTER_PATH+" && git remote add origin git@github.com:"+Internalvars.ORIGIN],True,"Create remote origin"]
    __dic["GIT"]["12"] =[["cd "+PATHS.RMPI_MASTER_PATH+" && git remote -v"],True,"Check remote origin"]
#     __dic["GIT"]["13"] =[["ssh-keygen","-t","rsa","-b","4096","-N",Internalvars.KEYPI,"-f",PATHS.SSHPATH+"/"+Internalvars.ID_RSA],False,"Create SSH key"]
    __dic["GIT"]["13"] =[["ssh-keygen","-t","rsa","-b","4096","-C",Internalvars.KEYPI,"-f",PATHS.SSHPATH+"/"+Internalvars.ID_RSA],False,"Create SSH key"]
    __dic["GIT"]["14"] =[["ssh-keygen","-E","sha256","-lf",PATHS.SSHPATH+"/"+Internalvars.ID_RSAPUB],False,"Generate a fingerprint for a public key"]
    __dic["GIT"]["15"] =[["cat",PATHS.SSHPATH+"/"+Internalvars.ID_RSAPUB],False,"Add this SSH key in git settings"]
    __dic["MDB"]["0"] = [["sudo","apt","install","mariadb-server","-y"],False,"Installing Maria database"]
    __dic["MDB"]["1"] = "sudo mysql_secure_installation"
    __dic["MDB"]["2"] = "sudo mysql -u root -p -e \"CREATE USER '"+Internalvars.DBUSER+"'@'localhost' IDENTIFIED BY '"+Internalvars.DBPASSWORD+"'\""
    __dic["MDB"]["3"] = "sudo mysql -u root -p -e \"GRANT ALL PRIVILEGES ON *.* TO '"+Internalvars.DBUSER+"'@'localhost'\""
    __dic["MDB"]["4"] = "sudo mysql -u root -p -e \"FLUSH PRIVILEGES\""
    __dic["MDB"]["5"] = "sudo mysql -u root -p -e \"Create database RMPIDB\""
    __dic["MDB"]["6"] = [["pip3","install","mariadb"],False,"Installing Maria database connector for python"]
    
    dic=__dic
class COMMANDS():
    CRONJOB_DailyReport=PATHS.PYTHONPATH+" "+PATHS.JOBS_PATH+"/J_DailyReport.py >> ~/cron.log 2>&1"
    CRONJOB_PIReboot=PATHS.PYTHONPATH+" "+PATHS.JOBS_PATH+"/J_PI_Reboot.py>> ~/cron.log 2>&1"
    AUTOPROCESS_INTERVAL = 30
    RANGE=math.ceil(60/AUTOPROCESS_INTERVAL)
    CRONJOB_AutoProcess={}
    for x in range(0,int(RANGE)):
        CRONJOB_AutoProcess[x] = "sleep "+str((x*AUTOPROCESS_INTERVAL))+" ; "+PATHS.PYTHONPATH+" "+PATHS.AUTOMATION_PATH+"/autoprocess.py >> ~/cron.log 2>&1"
    RCLOCAL_TEXT ="python3 /home/pi/Desktop/rmpi-master/Automation/Jobs/J_PI_Reboot_After.py"+"\n"+"exit 0"+"\n"

class colors():
    PRE= "#ff8c00"
    TITLE= "#006400"
    SUCCESS= "#0000CD"
    FAIL = "#c21000"
    SKIP = "#A6ACAF"

class init():
    def config_json(val):
        __dic={}
        __dic["UP"]={}
        __dic["WS"]={}
        __dic["MDB"]={}
        __dic["GIT"]={}
        __dic["PRE"]={}
        __dic["NC"]={}
        __dic["PRE"]["0"] = [val,"Change rmpi-master mode to execute"]
        __dic["PRE"]["1"] = [val,"Check rmpi-master mode"]
        __dic["PRE"]["2"] = [val,"Change crontabs owner to pi"]
        __dic["PRE"]["3"] = [val,"Backup rc.local file"]
        __dic["PRE"]["4"] = [val,"Change rc.local owner to pi"]
        __dic["PRE"]["5"] = [val,"Change rc.local owner to root"]
        __dic["UP"]["0"] = [val,"Installing updates"]
        __dic["UP"]["1"] = [val,"Installing upgrades"]
        __dic["WS"]["0"] = [val,"Installing apache2"]
        __dic["WS"]["1"] = [val,"Installing libapache2-mod-php"]
        __dic["WS"]["2"] = [val,"Enable php to run shell commands"]
        __dic["WS"]["3"] = [val,"Create empty flag file in html"]
        __dic["WS"]["4"] = [val,"Clear default html folder"]
        __dic["WS"]["5"] = [val,"Create html folder"]
        __dic["WS"]["6"] = [val,"Copy project files to html folder"]
        __dic["WS"]["7"] = [val,"Remove flag file from html and orignal folder"]
        __dic["WS"]["8"] = [val,"Create html folder shortcut on Desktop"]
        __dic["GIT"]["0"] = [val,"Installing git"]
        __dic["GIT"]["1"] = [val,"Set GIT user.name"]
        __dic["GIT"]["2"] = [val,"Set GIT user.email"]
        __dic["GIT"]["3"] = [val,"Set GIT core.editor to nano"]
        __dic["GIT"]["4"] = [val,"Create rmpi-master folder"]
        __dic["GIT"]["5"] = [val,"create a new repository in a directory"]
        __dic["GIT"]["6"] = [val,"Add all files or changes to the repository"]
        __dic["GIT"]["7"] = [val,"Check git status"]
        __dic["GIT"]["8"] = [val,"Enable SSH service"]
        __dic["GIT"]["9"] = [val,"Start SSH service"]
        __dic["GIT"]["10"] = [val,"Check SSH service"]
        __dic["GIT"]["11"] = [val,"Create remote origin"]
        __dic["GIT"]["12"] =[val,"Check remote origin"]
        __dic["GIT"]["13"] =[val,"Create SSH key"]
        __dic["GIT"]["14"] =[val,"Generate a fingerprint for a public key"]
        __dic["GIT"]["15"] =[val,"Add SSH key in git settings"]
        __dic["MDB"]["0"] = [val,"Installing Maria database"]
        __dic["MDB"]["1"] = [val,"mysql_secure_installation"]
        __dic["MDB"]["2"] = [val,"CREATE DB USER"]
        __dic["MDB"]["3"] = [val,"GRANT PRIVILEGES"]
        __dic["MDB"]["4"] = [val,"FLUSH PRIVILEGES"]
        __dic["MDB"]["5"] = [val,"CREATE DATABASE RMPIDB"]
        __dic["MDB"]["6"] = [val,"Installing Maria database connector for python"]
        __dic["NC"]["0"] = [val,"Adding crontab"]
        __dic["NC"]["1"] = [val,"Adding script path to RCLOCAL"]
        return __dic

# lambda x: f() if 2==2 else False
