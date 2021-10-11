#! /usr/bin/python3
from tkinter import *
from threading import *
from pathlib import Path
import subprocess, pexpect, math, types, time, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Automation.Lib.T_CronTab import CronTab
from Automation.Lib.T_Global import SETUP_COMMANDS as _S
count=0

opwin={}
R={}
cbox={}
var={}
arr={}
widget_h = 2
window = Tk()

web_folder=""
_web={"PWEB":"ws_pin_io","LWEB":"ws_library","EMPTY":"ws_empty"}
def wtlb(w,text,**kwargs):
    global count
    fg = kwargs.get('fg', None)
    bg = kwargs.get('bg', None)
    w.insert(END,text)
    w.itemconfig(count,{'fg':fg,'bg':bg})
    w.yview(END) 
    count+=1
def execute(args):
    '''Takes 4 arguments
        arg 0: cmd command
        arg 1: True -> use shell, false -> don't use shell
        arg 2: message to display
        arg 3: Listbox object
    '''
    wtlb(args[3],"Started: "+args[2],bg="",fg="#006400")
    if args[1]:
        popen = subprocess.Popen(args[0],shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            wtlb(args[3],stdout_line,fg="#0000CD")
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, args[0])
    else:
        popen = subprocess.Popen(args[0], stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            wtlb(args[3],stdout_line,fg="#0000CD")
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, args[0])
    wtlb(args[3],"Finished: "+args[2],bg="",fg="#006400")

def pre_installations(w):
    _RCPATH="/etc/rc.local"
    inst={}
    inst["PRE_INSTALLATION"]={}
    inst["PRE_INSTALLATION"][0] = [["sudo", "chmod","+x","/home/pi/Desktop/rmpi-master/"],False,w,"Change rmpi-master mode to execute"]
    inst["PRE_INSTALLATION"][1] = [["find", "/home/pi/Desktop/rmpi-master/","-executable"],False,w,"Check rmpi-master mode"]
    inst["PRE_INSTALLATION"][2] = [["sudo", "chown","pi","/var/spool/cron/crontabs/"],False,w,"Change crontabs owner to pi"]
    inst["PRE_INSTALLATION"][3] = [["sudo", "cp","/etc/rc.local","/etc/rc.local.orig"],False,w,"Change rc.local owner to root"]
    inst["PRE_INSTALLATION"][4] = [["sudo", "chown","pi",_RCPATH],False,w,"Change rc.local owner to pi"]
    inst["PRE_INSTALLATION"][5] = [["sudo", "chown","root",_RCPATH],False,w,"Change rc.local owner to root"]
    
    execute(inst["PRE_INSTALLATION"][0])
    execute(inst["PRE_INSTALLATION"][1])
    execute(inst["PRE_INSTALLATION"][2])
    wtlb(w,"Creating cronjob:  Daily Report",fg="#ff8c00")    
    CJ_1 = CronTab()
    CJ_1.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_DailyReport.py >> ~/cron.log 2>&1")
    CJ_1.comment("RUN DAILY REPORT AT 6:00 AM")
    CJ_1.on().minute(0)
    CJ_1.on().hour(6)
    CJ_1.schedule()
    wtlb(w,"Cronjob added:  Daily Report",fg="#ff8c00")
    wtlb(w,"Creating cronjob:   Pi Reboot",fg="#ff8c00")       
    CJ_3 = CronTab()
    CJ_3.command("/usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_PI_Reboot.py>> ~/cron.log 2>&1")
    CJ_3.comment("REBOOT MACHINE AT 12:00 AM EVERYDAY")
    CJ_3.on().minute(0)
    CJ_3.on().hour(0)
    wtlb(w,"Cronjob added:   Pi Reboot",fg="#ff8c00")       
    CJ_3.schedule()
    wtlb(w,"Creating cronjob:   autoprocess",fg="#ff8c00")       
    AUTOPROCESS_INTERVAL = 30
    RANGE=math.ceil(60/AUTOPROCESS_INTERVAL)
    for x in range(0,int(RANGE)):
        CJ_2 = CronTab()
        CMD = "sleep "+str((x*AUTOPROCESS_INTERVAL))+" ; /usr/bin/python3 /home/pi/Desktop/rmpi-master/automation/autoprocess.py >> ~/cron.log 2>&1"
        CJ_2.command(CMD)
        CJ_2.comment("RUN AUTOPROCESS AT SECOND "+str((x*AUTOPROCESS_INTERVAL)))
        CJ_2.schedule()    
    wtlb(w,"Cronjob added:   autoprocess",fg="#ff8c00")
    execute(inst["PRE_INSTALLATION"][3])
    execute(inst["PRE_INSTALLATION"][4])
    _FILE = Path(_RCPATH)
    _FILE_READ= open(_FILE, 'r')
    Lines = _FILE_READ.readlines()
    new_text = ""
    for line in Lines:
        line = line.replace("\n","")
        print(line)
        if line.startswith("exit 0"):
            new_text = new_text+"python3 /home/pi/Desktop/rmpi-master/automation/system/Jobs/J_PI_Reboot_After.py"+"\n"
            new_text = new_text+"exit 0"+"\n"
        else:
            new_text = new_text+line+"\n"
    _FILE_WRITE= open(_FILE, "w")        
    _FILE_WRITE.write(new_text)
    _FILE_WRITE.close()
    execute(inst["PRE_INSTALLATION"][5])
#mysql -u [username] -p [dbname] -e [query]
    
def pexpect_sendline(w,child,expect,sendline,tout):
    child.expect(expect,timeout=tout)
    child.sendline(sendline)
    print(str(child))
    wtlb(w,"mysql_secure_installation child : "+str(child),fg="#ff8c00")       
    

def commands_dictionary(w):
    dic={}
    dic["UP"]={}
    dic["MDB"]={}
    dic["WS"]={}
    dic["GIT"]={}

    #update and upgrade commands
    dic["UP"][0] = [["sudo", "apt","update"],False,w,"Installing updates"]
    dic["UP"][1] = [["sudo", "apt","upgrade","-y"],False,w,"Installing upgrades"]
    #webserver commands
    global web_folder
    dic["WS"][0] = [["sudo", "apt","install","apache2","-y"],False,w,"Installing apache2"]
    dic["WS"][1] = [["sudo", "apt","install","php","libapache2-mod-php","-y"],False,w,"Installing libapache2-mod-php"]
    dic["WS"][2] = ["echo 'www-data  ALL=NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo",True,w,"Enable php to run shell commands"]
    dic["WS"][3] = ["sudo touch /home/pi/Desktop/rmpi-master/"+web_folder+"/files/flag.flag",True,w,"Create empty flag file in html and orignal folder"]
    dic["WS"][4] = ["sudo rm -r /var/www/html/",True,w,"Clear default html folder"]
    dic["WS"][5] = ["sudo mkdir /var/www/html",True,w,"Create html folder"]
    dic["WS"][6] = ["sudo cp -r /home/pi/Desktop/rmpi-master/"+web_folder+"/files/* /var/www/html/",True,w,"Copy project files to html folder"]
    dic["WS"][7] = ["sudo rm /var/www/html/flag.flag /home/pi/Desktop/rmpi-master/"+web_folder+"/files/flag.flag",True,w,"Remove flag file from html and orignal folder"]
    dic["WS"][8] = ["sudo ln -s /var/www/html /home/pi/Desktop/html",True,w,"Create html folder shortcut on Desktop"]
    #GIT commands
    _USERNAME= "rmpi"
    _GMAIL= "ryanmakarem91@gmail.com"
    _KEYPI= "rmpi2021"
    _ORIGIN= "rmak1991/rmpi.git"
    _DIRNAME= "rmpi-master"
    _DESKTOP = "/home/pi/Desktop/"
    _PATH=_DESKTOP+_DIRNAME
    dic["GIT"][0] =[["sudo", "apt","install","git"],False,w,"Installing git"]
    dic["GIT"][1] =[["git", "config","--global","user.name","'"+_USERNAME+"'"],False,w,"Set GIT user.name to "+_USERNAME]
    dic["GIT"][2] =[["git", "config","--global","user.email","'"+_GMAIL+"'"],False,w,"Set GIT user.email to "+_GMAIL]
    dic["GIT"][3] =[["git", "config","--global","core.editor","nano"],False,w,"Set GIT core.editor to nano"]
    dic["GIT"][4] =[["mkdir", "-p",_PATH],False,w,"Create rmpi-master folder"]
    dic["GIT"][5] =[["git", "init",_PATH],False,w,"create a new repository in a directory"]
    dic["GIT"][6] =[["git", "add","--all",_PATH],False,w,"Add all files or changes to the repository"]
    dic["GIT"][7] =[["cd "+_PATH+" && git status"],True,w,"Check git status"]
    dic["GIT"][8] =[["sudo", "systemctl","enable","ssh"],False,w,"Enable SSH service"]
    dic["GIT"][9] =[["sudo", "systemctl","start","ssh"],False,w,"Start SSH service"]
    dic["GIT"][10] =[["sudo", "service","ssh","status"],False,w,"Check SSH service"]
    dic["GIT"][11] =[["cd "+_PATH+" && git remote add origin git@github.com:"+_ORIGIN],True,w,"Create remote origin"]
    dic["GIT"][12] =[["cd "+_PATH+" && git remote -v"],True,w,"Check remote origin"]
    dic["GIT"][13] =[["ssh-keygen","-t","rsa","-b","4096","-N",_KEYPI,"-f","/home/pi/.ssh/id_rsa"],False,w,"Create SSH key"]
    dic["GIT"][14] =[["ssh-keygen","-E","sha256","-lf","/home/pi/.ssh/id_rsa.pub"],False,w,"Generate a fingerprint for a public key"]
    dic["GIT"][15] =[["cat","/home/pi/.ssh/id_rsa.pub"],False,w,"Add this SSH key in git settings"]
    dic["MDB"][0] = [["sudo","apt","install","mariadb-server","-y"],False,w,"Installing Maria database"]
    dic["MDB"][1] = [["pip3","install","mariadb"],False,w,"Installing Maria database connector for python"]
     #sudo mysql -u root -p -e "CREATE USER 'RMPIDBU'@'localhost' IDENTIFIED BY 'RMPI2021'"
     #sudo mysql -u root -p -e "GRANT ALL PRIVILEGES ON *.* TO 'RMPIDBU'@'localhost'"
     #sudo mysql -u root -p -e "FLUSH PRIVILEGES"
    return dic
def run_installs(d,w):
    w.delete(0,END)
    #pre_installations(w)
    global count
    count = 0
    ins = get_sel()
    dic=commands_dictionary(w)
    #child = pexpect.spawn("sudo apt install phpmyadmin")
    #print(child.expect("yes",timeout=3))
    #print(child.before)
   # print(child.after)
    for x in ins:
        if x =="UP":
            execute(dic["UP"][0])
            execute(dic["UP"][1])
        if x =="WS":
            print(1)
            execute(dic["WS"][0])
            execute(dic["WS"][1])
            execute(dic["WS"][2])
            execute(dic["WS"][3])
            execute(dic["WS"][4])
            execute(dic["WS"][5])
            execute(dic["WS"][6])
            execute(dic["WS"][7])
            execute(dic["WS"][8])
        if x =="GIT":
            execute(dic["GIT"][0])
            execute(dic["GIT"][1])
            execute(dic["GIT"][2])
            execute(dic["GIT"][3])
            execute(dic["GIT"][4])
            execute(dic["GIT"][5])
            execute(dic["GIT"][6])
            execute(dic["GIT"][7])
            execute(dic["GIT"][8])
            execute(dic["GIT"][9])
            execute(dic["GIT"][10])
            execute(dic["GIT"][11])
            execute(dic["GIT"][12])
            execute(dic["GIT"][13])
            execute(dic["GIT"][14])
            execute(dic["GIT"][15])
        if x =="MDB":
            execute(dic["MDB"][0])
            child = pexpect.spawn("sudo mysql_secure_installation")
            wtlb(w,"Started: mysql_secure_installation",fg="#ff8c00")
            try:
                pexpect_sendline(w,child,"password","Rayan1991",3)
                pexpect_sendline(w,child,"password","yes",3)
                pexpect_sendline(w,child,"password","Rayan1991",3)
                pexpect_sendline(w,child,"password","Rayan1991",3)
                pexpect_sendline(w,child,"anonymous","no",3)
                pexpect_sendline(w,child,"remotely","no",3)
                pexpect_sendline(w,child,"database","yes",3)
                pexpect_sendline(w,child,"privilege","yes",3)
            except:
                wtlb(w,"mysql_secure_installation installation error: Exception was thrown",fg="#ff8c00")
                wtlb(w,"mysql_secure_installation installation error : debug information:",fg="#ff8c00")       
                wtlb(w,"mysql_secure_installation installation error : "+str(child),fg="#ff8c00")       
            wtlb(w,"Finished: mysql_secure_installation",fg="#ff8c00")
            execute(dic["MDB"][1])
#sudo DEBIAN_FRONTEND=noninteractive apt-get -y install phpmyadmin

def get_sel():
    sel={}
    for x in arr:
        if type(x) is type(Checkbutton()):
            if arr[x].get() > 0:
                if str(x["textvariable"])=="WS":
                    for y in arr:
                        if type(y) is type(Radiobutton()):
                            if str(arr[y].get()) == str(y["value"]):
                                global web_folder
                                web_folder = _web[str(y["textvariable"])]
                                sel[str(x["textvariable"])] = "Install"
                else:
                    sel[str(x["textvariable"])] = "Install"
    return sel
                
def btn_winlist():
    window.withdraw()
    info_window = Tk()
    opwin[1]=info_window
    #info_window.configure(bg='#001f3f')
    sc_h = info_window.winfo_screenheight()
    sc_w = info_window.winfo_screenwidth()
    win_h= int(sc_h/2)
    win_w=int(sc_w/2)
    pos_x=int((sc_w-win_w)/2)
    pos_y=int((sc_h-win_h)/2)
    info_window.geometry(str(win_w)+"x"+str(win_h)+"+"+str(pos_x)+"+"+str(pos_y))
    info_window.overrideredirect(1)
    frame_bottom = Frame(info_window)
    frame_top = Frame(info_window,bg='#001f3f')
    frame_bottom.pack(side=BOTTOM,fill="x")
    frame_top.pack(side=TOP,fill="both")
    w = Listbox (frame_top,width=win_w,height=win_h)
    w.pack()
    btn_start = Button(frame_bottom,text="Start",width= 10,height=2,command=lambda:start())
    btn_close = Button(frame_bottom,text="Close",width= 10,height=2,command=lambda:close())
    btn_start.pack(side=RIGHT)
    btn_close.pack(side=LEFT)
    def start():
        t1=Thread(target=run_installs, args=("",w))
        t1.start()
    def close():
        del opwin[1]
        info_window.destroy()
        window.deiconify()
    info_window.mainloop()

def _enradio(val):
    for x in arr:
        if type(x) is type(Radiobutton()):
            x.select()
            if val:
                x.configure(state=NORMAL)
                x.select()
            else:
                x.configure(state=DISABLED)
            x.update() 
def enradio(self):
    if self.get()==1:
        _enradio(True)
    else:
        _enradio(False)   
def btn_close():
    for x in opwin:
        opwin[x].destroy()
def btn_selall():
    for x in arr:
        if type(x) is type(Checkbutton()):
            x.select()
    _enradio(True)
def btn_dselall():
    for x in arr:
        if type(x) is type(Checkbutton()):
            x.deselect()
    _enradio(False)
def run_main():
    window.title("RMAPP Setup")
    sc_h = window.winfo_screenheight()
    sc_w = window.winfo_screenwidth()
    win_h= int(sc_h/2)
    win_w=int(sc_w/2)
    pos_x=int((sc_w-win_w)/2)
    pos_y=int((sc_h-win_h)/2)
    window.geometry(str(win_w)+"x"+str(win_h)+"+"+str(pos_x)+"+"+str(pos_y))
    window.resizable(False, False)
    title_lable = Label(window,font='Helvetica 18 bold', text="RMAPP", bg="#001f3f", fg="#80bfff",width=win_w,height="3").pack()
    #frames
    frame_empty= Frame(window)
    frame_bottom = Frame(window)
    frame_left = Frame(window)
    frame_right = Frame(window)
    frame_empty.pack(fill="x")
    frame_bottom.pack(side=BOTTOM,fill="x")
    frame_left.pack(side=LEFT,fill="y")
    frame_right.pack(side=RIGHT,fill="y")
    #header title
    lbl_empty = Label(frame_empty,text="",width= 55,height=widget_h, fg="#9B2335", anchor="w")
    lbl_empty.pack()
    #checkbox and radio
    var0 = IntVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()

    chk1 = Checkbutton(frame_left, text="Install updates and upgrades",textvariable="UP", variable=var1,width=50,height=widget_h,  highlightthickness = 0,anchor="w")
    chk2 = Checkbutton(frame_left, text="Install Maria database",textvariable="MDB", variable=var2,width=50,height=widget_h,  highlightthickness = 0,anchor="w")
    chk3 = Checkbutton(frame_left, text="Install webserver",textvariable="WS", variable=var3,width=50,height=widget_h,  highlightthickness = 0,anchor="w",command= lambda: enradio(var3))
    R1 = Radiobutton(frame_left,text="Add pinio website",textvariable="PWEB", variable=var0,value="1",width=40,height=widget_h,  highlightthickness = 0,anchor="w",state="disabled")
    R2 = Radiobutton(frame_left,text="Add library website",textvariable="LWEB", variable=var0,value="2",width=40,height=widget_h,  highlightthickness = 0,anchor="w",state="disabled")
    R3 = Radiobutton(frame_left,text="Empty project",textvariable="EMPTY", variable=var0,value="3",width=40,height=widget_h,  highlightthickness = 0,anchor="w",state="disabled")
    chk4 = Checkbutton(frame_left, text="Install Git",textvariable="GIT", variable=var4,width= 50,height=widget_h,  highlightthickness = 0,anchor="w")
    chk1.pack()
    chk2.pack()
    chk3.pack()
    R1.pack()
    R2.pack()
    R3.pack()
    chk4.pack()
    #Labels
    lbl1 = Label(frame_right,text="updates and upgrades are not installed",width= 55,height=widget_h, fg="#9B2335", anchor="w")
    lbl2 = Label(frame_right,text="Maria database is not installed",width= 55,height=widget_h, fg="#9B2335",anchor="w")
    lbl3 = Label(frame_right,text="Webserver is not installed",width= 55,height=widget_h, fg="#9B2335",anchor="w")
    lbl4 = Label(frame_right,text="pinio website is not installed",width= 55,height=widget_h, fg="#9B2335",anchor="w")
    lbl5 = Label(frame_right,text="library website is not installed",width= 55,height=widget_h, fg="#9B2335",anchor="w")
    lbl6 = Label(frame_right,text="Empty Project is not installed",width= 55,height=widget_h, fg="#9B2335",anchor="w")
    lbl7 = Label(frame_right,text="Git is not installed",width= 55,height=widget_h, fg="#9B2335", anchor="w")
    lbl1.pack()
    lbl2.pack()
    lbl3.pack()
    lbl4.pack()
    lbl5.pack()
    lbl6.pack()
    lbl7.pack()
    # Buttons
    btn1 = Button(frame_bottom,text="Close",width= 10,height=widget_h,command= lambda: btn_close())
    btn2 = Button(frame_bottom,text="Select All",width= 10,height=widget_h,command = lambda:btn_selall())
    btn3 = Button(frame_bottom,text="Deselect All",width= 10,height=widget_h,command=lambda:btn_dselall())
    btn4 = Button(frame_bottom,text="Install",width= 10,height=widget_h,command=lambda:btn_winlist())
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=RIGHT)
    #init arrays
    arr[chk1]=var1
    arr[chk2]=var2
    arr[chk3]=var3
    arr[chk4]=var4
    arr[R1]=var0
    arr[R2]=var0
    arr[R3]=var0
    opwin[0]=window
    window.overrideredirect(1)
    window.mainloop()
run_main()
