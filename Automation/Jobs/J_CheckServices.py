import os,sys,re
import subprocess
from pathlib import Path
from PIL import Image,ImageFont, ImageDraw
import tkinter as tk
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
from Lib.T_Global import colors as _cc

dic={}
dic["apache2.service"] = {}
dic["apt-daily-upgrade.service"] = {}
dic["apt-daily.service"] = {} 
dic["cron.service"] = {}
dic["mariadb.service"] = {}
dic["rc-local.service"] = {}
dic["rsyslog.service"] = {}
dic["ssh.service"] = {}
dic["systemd-sysctl.service"] = {}
def getserviceStatus():
    global dic
    for x in dic:
        args = "systemctl list-units --all "+x
        txt=""
        popen = subprocess.Popen(args,shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        count=0
        for stdout_line in iter(popen.stdout.readline, ""):
            if count==1:
                txt=re.sub(' +', ' ', stdout_line)
                count+=1
            else:
                count+=1
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, args)
        res=txt.replace(chr(9679),"").strip().split(" ", 4)
        tempdic={}
        tempdic["UNIT"]=res[0]
        tempdic["DESCRIPTION"]=res[4]
        tempdic["Status"] = os.system("systemctl is-active --quiet "+x)
        dic[x]=tempdic
    return dic
def getTemp():
    popen = subprocess.Popen("sudo vcgencmd measure_temp",shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    txt=""
    for stdout_line in iter(popen.stdout.readline, ""):
        txt=stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, args)    
    return txt.replace("temp=","").split("'")[0]
def getTemp2():
    popen = subprocess.Popen("vcgencmd measure_temp pmic",shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    txt=""
    for stdout_line in iter(popen.stdout.readline, ""):
        txt=stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, args)    
    return txt.replace("temp=","").split("'")[0]

def runServiceCheck(date): 
    str1 = "Autoprocess last ran at : "+str(date)      
    setBackground(str1)            
def setBackground(APlastrun):
    img =Image.new('RGB',(1920,1080),"#1b1e23")
    font = ImageFont.truetype("Piboto-Bold.ttf", 30)
    font2 = ImageFont.truetype("Piboto-Regular.ttf", 18)
    temp = ImageFont.truetype("Piboto-Regular.ttf", 16)
    draw=ImageDraw.Draw(img)
    draw.rectangle((1500, 550, 500, 20),fill=("#FFFFFF"),outline=("#FFFFFF"))
    START = 430
    w,h=font.getsize(APlastrun)
    screen_width=(1920-w)/2
    screen_height =((1080-h)/2)-h-START
    draw.text((screen_width,screen_height),APlastrun,font=font,fill=_cc.TITLE)
    TEMP_COLOR=_cc.TITLE
    TEMP_PMIC_COLOR=_cc.TITLE
    if float(getTemp()) > 38.0:
        TEMP_COLOR = _cc.FAIL
    if float(getTemp2()) > 38.0:
        TEMP_PMIC_COLOR = _cc.FAIL
    draw.text((screen_width+w+20,screen_height+5),"Temp = "+str(getTemp())+"'C",font=temp,fill=TEMP_COLOR)
    draw.text((screen_width+w+20,screen_height+30),"PMIC = "+str(getTemp2())+"'C",font=temp,fill=TEMP_PMIC_COLOR)
    START = START-60
    dic=getserviceStatus()
    for x in dic:
        STATUS="ACTIVE"
        COLOR=_cc.TITLE
        if dic[x]["Status"]!=0:
            STATUS="INACTIVE"
            COLOR=_cc.FAIL           
        h=40
        screen_height =((1080-h)/2)-h-START
        w=0
        draw.text((screen_width,screen_height),STATUS,font=font2,fill=COLOR)
        draw.text((screen_width+100,screen_height),dic[x]["UNIT"],font=font2,fill="#000000")
        draw.text((screen_width+320,screen_height),dic[x]["DESCRIPTION"],font=font2,fill="#000000")
        START = START-40
    img.save(_P.PICS_PATH+"/noerr.jpg")    
    env = os.environ.copy()
    env["DISPLAY"] = ":0"
    env["XAUTHORITY"] = "/root/.Xauthority"
    env["XDG_RUNTIME_DIR"] = "/run/user/1000"
    subprocess.run(["pcmanfm --set-wallpaper "+_P.PICS_PATH+"/noerr.jpg"],env=env, shell=True,check=True)        
def showMessage():
    if os.environ.get('DISPLAY','') == '':
        os.environ.__setitem__('DISPLAY', ':0.0')
    master = tk.Tk()
    master.title("Notification")
    master.geometry("300x100")
    label1 = tk.Label(master, text='System will reboot soon.')
    label1.pack()
    master.mainloop()