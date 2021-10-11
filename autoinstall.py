#! /usr/bin/python3
from tkinter import *
from threading import *
from pathlib import Path
import subprocess, pexpect, math, types, time, os, sys, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Automation.Lib.T_CronTab import CronTab
from Automation.Lib.T_Global import PATHS as _P
from Automation.Lib.T_Global import COMMAND_LISTS as _CL
from Automation.Lib.T_Global import COMMANDS as _C
from Automation.Lib.T_Global import colors as _color
from Automation.Lib.T_Global import init as _init

import Automation.Lib.T_FileHandler as FH
close_btn = Button
start_btn = Button
count=0
InstallMessageBox = Listbox
dic=_CL.dic
opwin={}
R={}
cbox={}
var={}
arr={}
widget_h = 2
window = Tk
web_folder=""
#FH.FILE_WRITE_OVERWRITE(_P.JSON_SETUP_CONFIG,_P.RMPI_MASTER_PATH,json.dumps(_init.config_json(True)))
def gc(val1,val2):
    t = FH.FILE_READ(_P.JSON_SETUP_CONFIG,_P.RMPI_MASTER_PATH)
    res = json.loads(t)
    return res[val1][val2][0]
def gcv(val1,val2):
    t = FH.FILE_READ(_P.JSON_SETUP_CONFIG,_P.RMPI_MASTER_PATH)
    res = json.loads(t)
    return res[val1][val2][1]
def uc(val1,val2,valtoupdate):
    t = FH.FILE_READ(_P.JSON_SETUP_CONFIG,_P.RMPI_MASTER_PATH)
    res = json.loads(t)
    res[val1][val2][0]=valtoupdate
    FH.FILE_WRITE_OVERWRITE(_P.JSON_SETUP_CONFIG,_P.RMPI_MASTER_PATH,json.dumps(res))
def wtlb(text,**kwargs):
    global count
    fg = kwargs.get('fg', None)
    bg = kwargs.get('bg', None)
    InstallMessageBox.insert(END,text)
    InstallMessageBox.itemconfig(count,{'fg':fg,'bg':bg})
    InstallMessageBox.yview(END) 
    count+=1
def execute(args,var1,var2):
    if gc(var1,var2):
        wtlb("STARTED:: "+args[2],bg="",fg=_color.TITLE)
        if args[1]:
            popen = subprocess.Popen(args[0],shell=True, stdout=subprocess.PIPE, universal_newlines=True)
            for stdout_line in iter(popen.stdout.readline, ""):
                wtlb(stdout_line,fg=_color.SUCCESS)
            popen.stdout.close()
            return_code = popen.wait()
            if return_code:
                raise subprocess.CalledProcessError(return_code, args[0])
            else:
                uc(var1,var2,False)
        else:
            popen = subprocess.Popen(args[0], stdout=subprocess.PIPE, universal_newlines=True)
            for stdout_line in iter(popen.stdout.readline, ""):
                wtlb(stdout_line,fg=_color.SUCCESS)
            popen.stdout.close()
            return_code = popen.wait()
            if return_code:
                raise subprocess.CalledProcessError(return_code, args[0])
            else:
                uc(var1,var2,False)            
        wtlb("FINISHED:: "+args[2],bg="",fg=_color.TITLE)
    else:
        wtlb("SKIP:: "+gcv(var1,var2),bg="",fg=_color.SKIP)
def rclocalsetup():
    wtlb("STARTED:: "+gcv("NC","1"),fg=_color.PRE)
    _FILE = Path(_P.RCLOCALPATH)
    _FILE_READ= open(_FILE, 'r')
    Lines = _FILE_READ.readlines()
    new_text = ""
    for line in Lines:
        line = line.replace("\n","")
        if line.startswith("exit 0"):
            new_text = new_text+_C.RCLOCAL_TEXT
        else:
            new_text = new_text+line+"\n"
    _FILE_WRITE= open(_FILE, "w")        
    _FILE_WRITE.write(new_text)
    _FILE_WRITE.close()
    wtlb("FINISHED:: "+gcv("NC","1"),fg=_color.PRE)
def crontabsetup():
    wtlb("STARTED:: "+gcv("NC","0"),fg=_color.PRE)
    wtlb("STARTED:: Creating cronjob Daily Report",fg=_color.PRE)    
    CJ_1 = CronTab()
    CJ_1.command(_C.CRONJOB_DailyReport)
    CJ_1.comment("RUN DAILY REPORT AT 6:00 AM")
    CJ_1.on().minute(0)
    CJ_1.on().hour(6)
    CJ_1.schedule()
    wtlb("FINISHED:: Cronjob added Daily Report",fg=_color.PRE)
    
    wtlb("STARTED:: Creating cronjob Pi Reboot",fg=_color.PRE)       
    CJ_3 = CronTab()
    CJ_3.command(_C.CRONJOB_PIReboot)
    CJ_3.comment("REBOOT MACHINE AT 12:00 AM EVERYDAY")
    CJ_3.on().minute(0)
    CJ_3.on().hour(0)
    wtlb("FINISHED:: Cronjob added Pi Reboot",fg=_color.PRE)       
    CJ_3.schedule()
    
    wtlb("STARTED:: Creating cronjob:   autoprocess",fg=_color.PRE)       
    for c in _C.CRONJOB_AutoProcess:
        CJ_2 = CronTab()
        CJ_2.command(str(_C.CRONJOB_AutoProcess[c]))
        CJ_2.comment("RUN AUTOPROCESS AT SECOND "+str((c*_C.AUTOPROCESS_INTERVAL)))
        CJ_2.schedule()
    wtlb("FINISHED:: Cronjob added:   autoprocess",fg=_color.PRE)
    wtlb("FINISHED:: "+gcv("NC","0"),fg=_color.PRE)
def PRE_INSTALLATION():
    global dic
    execute(dic["PRE"]["0"],"PRE","0")
    execute(dic["PRE"]["1"],"PRE","1")
    execute(dic["PRE"]["2"],"PRE","2")

    if gc("NC","0"):
        crontabsetup()
        uc("NC","0",False)
    else:
        wtlb("SKIP:: "+gcv("NC","0"),fg=_color.SKIP)
    execute(dic["PRE"]["3"],"PRE","3")
    execute(dic["PRE"]["4"],"PRE","4")
    if gc("NC","1"):
        rclocalsetup()
        uc("NC","1",False)
    else:
        wtlb("SKIP:: "+gcv("NC","1"),fg=_color.SKIP)              
    execute(dic["PRE"]["5"],"PRE","5")
def run_installs():
    global close_btn,start_btn,count,dic
    count=0
    close_btn["state"] = "disabled"
    start_btn["state"] = "disabled"
    ins = get_sel()
    try:
        InstallMessageBox.delete(0,END)
        PRE_INSTALLATION()
        
        for x in ins:
            if x =="UP":
                execute(dic["UP"]["0"],"UP","0")
                execute(dic["UP"]["1"],"UP","1")
            if x =="WS":
                execute(dic["WS"]["0"],"WS","0")
                execute(dic["WS"]["1"],"WS","1")
                execute(dic["WS"]["2"],"WS","2")
                execute(dic["WS"]["3"][web_folder],"WS","3")
                execute(dic["WS"]["4"],"WS","4")
                execute(dic["WS"]["5"],"WS","5")
                execute(dic["WS"]["6"][web_folder],"WS","6")
                execute(dic["WS"]["7"][web_folder],"WS","7")
                execute(dic["WS"]["8"],"WS","8")
            if x =="GIT":
                execute(dic["GIT"]["0"],"GIT","0")
                execute(dic["GIT"]["1"],"GIT","1")
                execute(dic["GIT"]["2"],"GIT","2")
                execute(dic["GIT"]["3"],"GIT","3")
                execute(dic["GIT"]["4"],"GIT","4")
                execute(dic["GIT"]["5"],"GIT","5")
                execute(dic["GIT"]["6"],"GIT","6")
                execute(dic["GIT"]["7"],"GIT","7")
                execute(dic["GIT"]["8"],"GIT","8")
                execute(dic["GIT"]["9"],"GIT","9")
                execute(dic["GIT"]["10"],"GIT","10")
                execute(dic["GIT"]["11"],"GIT","11")
                execute(dic["GIT"]["12"],"GIT","12")
                execute(dic["GIT"]["13"],"GIT","13")
                execute(dic["GIT"]["14"],"GIT","14")
                execute(dic["GIT"]["15"],"GIT","15")
            if x =="MDB":
                execute(dic["MDB"]["0"],"MDB","0")
                exp0_1=["password","Rayan1991",3]
                exp0_2=["password","yes",3]
                exp0_3=["password","Rayan1991",3]
                exp0_4=["password","Rayan1991",3]
                exp0_5=["anonymous","no",3]
                exp0_6=["remotely","no",3]
                exp0_7=["database","yes",3]
                exp0_8=["privilege","yes",3]
                execute_pexpect(dic["MDB"]["1"],"MDB","1","mysql_secure_installation",exp0_1,exp0_2,exp0_3,exp0_4,exp0_5,exp0_6,exp0_7,exp0_8)
                execute_pexpect(dic["MDB"]["2"],"MDB","2","mysql create user",["Enter password","rmpi2021",3])
                execute_pexpect(dic["MDB"]["3"],"MDB","3","mysql grant all privileges",["Enter password","rmpi2021",3])
                execute_pexpect(dic["MDB"]["4"],"MDB","4","mysql flush privileges",["Enter password","rmpi2021",3])
                execute_pexpect(dic["MDB"]["5"],"MDB","5","CREATE DATABASE RMPIDB",["Enter password","rmpi2021",3])
                execute(dic["MDB"]["6"],"MDB","6")
        close_btn["state"] = "normal"
        start_btn["state"] = "normal"
    except Exception as e:
        wtlb("ERROR:: "+str(e),fg=_color.FAIL)
        close_btn["state"] = "normal"
        start_btn["state"] = "normal"
        
def execute_pexpect(child_command,var1,var2,message,*args):
    if gc(var1,var2):
        wtlb("STARTED:: "+message,fg=_color.PRE)       
        child = pexpect.spawn(child_command)    
        for a in args:
            try:
                child.expect(a[0],timeout=a[2])
                child.sendline(a[1])
                uc(var1,var2,False)
            except Exception as e:
                wtlb("ERROR:: "+str(e),fg=_color.FAIL)     
        wtlb("FINISHED:: "+message,fg=_color.PRE)       
    else:
        wtlb("SKIP:: "+gcv(var1,var2),fg=_color.SKIP)       
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
                                web_folder = str(y["textvariable"])
                                sel[str(x["textvariable"])] = "Install"
                else:
                    sel[str(x["textvariable"])] = "Install"
    return sel
                
def btn_winlist():
    window.withdraw()
    global start_btn,close_btn
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
    global InstallMessageBox
    InstallMessageBox = Listbox (frame_top,width=win_w,height=win_h)
    InstallMessageBox.pack()
    start_btn = Button(frame_bottom,text="Start",width= 10,height=2,command=lambda:start())
    close_btn = Button(frame_bottom,text="Close",width= 10,height=2,command=lambda:close())
    start_btn.pack(side=RIGHT)
    close_btn.pack(side=LEFT)
    def start():
        t1=Thread(target=run_installs)
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
    
# def showPosEvent(event):
#     print ('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
#     
# def onRightClick(event):
#     print ('Got right mouse button click:')
#     showPosEvent(event)

    
def run_main():
    global window
    window = Tk()
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
#     window.bind('<Button-3>',  onRightClick)        
#     window.focus()                                    

    opwin[0]=window
    window.overrideredirect(1)
    window.mainloop()
run_main()
