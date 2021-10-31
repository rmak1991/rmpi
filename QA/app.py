#! /usr/bin/python3
from tkinter import *
from tkinter import messagebox
from threading import *
from pathlib import Path
import subprocess, pexpect, math, types, time, os, sys, json, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from App.Lib.T_Global import PATHS as _P
from App.Lib.T_Global import COMMAND_LISTS as _CL
from App.Lib.T_Global import COMMANDS as _C
from App.Lib.T_Global import colors as _color
from App.Lib.T_Global import init as _init
from App.Lib.T_Global import layout as lout
from App.Lib.J_CheckAlerts import updatelights
import App.Lib.J_CheckServices as cs
import App.Lib.J_CheckAlerts as ca
import App.Lib.T_DB as db
import App.Lib.T_Hue as hue
#FRAMES
alerts_box=Frame
contents_box = Frame
F_main = Frame
F_services=Frame
F_lights=Frame
F_database=Frame
F_settings=Frame
close_btn = Button
home_btn = Button
light_btn = Button
service_btn = Button
database_btn = Button
setting_btn = Button
count=0
InstallMessageBox = Listbox
dic=_CL.dic
window = Tk
mylist= Listbox
t1=Thread
t2=Thread
t3=Thread
appconfig = Path(_P.APP_LIB_PATH+"/"+_P.JSON_APP_CONFIG)
photoimagewater=PhotoImage.subsample
photoimagepower=PhotoImage.subsample
photoimagetemp=PhotoImage.subsample
photoimagewatericon=PhotoImage.subsample
photoimagepowericon=PhotoImage.subsample
photoimagetempicon=PhotoImage.subsample
childroot = Toplevel
def getlogsize():
    totalsize=0
    path="/home/pi/Desktop/HueLighting/App/Logs/"
    obj = os.scandir(path)
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            file_size = os.stat(path+'/'+entry.name)
            totalsize+=file_size.st_size
    return totalsize/1024/1024
def resetbtnpage():
    home_btn.configure(bg = lout.BG_COLOR,activebackground="#ececec", activeforeground="#000000",fg="#0074D9")
    light_btn.configure(bg = lout.BG_COLOR,activebackground="#ececec", activeforeground="#000000",fg="#0074D9")
    service_btn.configure(bg = lout.BG_COLOR,activebackground="#ececec", activeforeground="#000000",fg="#0074D9")
    database_btn.configure(bg = lout.BG_COLOR,activebackground="#ececec", activeforeground="#000000",fg="#0074D9")
    setting_btn.configure(bg = lout.BG_COLOR,activebackground="#ececec", activeforeground="#000000",fg="#0074D9")
def raiseframe(frame,btn):
    resetbtnpage()
    btn.configure(bg = "#00a2ed",activebackground="#00adff", activeforeground="white",fg="white")
    frame.tkraise()    
def getservicestatus(service):
    args1 = "systemctl list-units --all "+service
    args2 = "systemctl is-active --quiet "+service
    txt=""
    popen = subprocess.Popen(args1,shell=True, stdout=subprocess.PIPE, universal_newlines=True)
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
    tempdic["Active"]=res[2]
    tempdic["Status"] = str(os.system(args2))
    return tempdic
def serviceaction(action,service):
    args = "sudo systemctl "+action+" "+service 
    return os.system(args)           
def window_close(window):
    window.destroy()
def createspace(txt,num):
    totalchar = num+3
    tlen = len(txt)
    offset = totalchar-tlen
    gentext=""
    for i in range(0,int(offset)):
        gentext=gentext+" "
    return gentext
def update_alerts():
    global mylist,alerts_box
    while True:
        TITLE= "#006400"
        SUCCESS= "#0000CD"
        mylist.delete(0,END)
        res = db.get_active_alerts()
        space=[5,12,5,8]
        count = 0
        for c in res:
            mylist.insert(count,c[0]+createspace(c[0],space[0])+c[2]+createspace(c[2],space[1])+c[3]+createspace(c[3],space[2])+c[7]+createspace(c[7],space[3])+c[1])
            mylist.pack(fill = BOTH )
            if count%2==0:
                mylist.itemconfig(count,{'fg':"#D0342C",'bg':"white"})
            else:
                mylist.itemconfig(count,{'fg':"white",'bg':"#D0342C"})
            count+=1
        time.sleep(5)
def checks():
    global F_home
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    v5 = StringVar()
    v6 = StringVar()
    color=_color.TITLE
    v6.set("DCLIGHTS.service")
    lbl1= Label(F_home,font='Helvetica 10 ',textvariable = v1, bg=lout.BG_COLOR, fg=color,width="40",height="2",anchor="w")
    lbl2=Label(F_home,font='Helvetica 10 ',textvariable = v2,  bg=lout.BG_COLOR, fg=color,width="40",height="2",anchor="w")
    lbl3=Label(F_home,font='Helvetica 10 ',textvariable = v3, bg=lout.BG_COLOR, fg=color,width="40",height="2",anchor="w")
    lbl4=Label(F_home,font='Helvetica 10 ',textvariable = v4, bg=lout.BG_COLOR, fg=color,width="40",height="2",anchor="w")
    lbl5=Label(F_home,font='Helvetica 10',textvariable = v5, bg=lout.BG_COLOR, fg=_color.TITLE,width="8",height="2",anchor="w")
    lbl6=Label(F_home,font='Helvetica 10 ',textvariable = v6, bg=lout.BG_COLOR, fg=_color.SUCCESS,width="18",height="2",anchor="w")
    lbl1.place(x=3,y=55)
    lbl2.place(x=3,y=95)
    lbl3.place(x=3,y=135)
    lbl4.place(x=3,y=175)
    lbl5.place(x=30,y=215)
    lbl6.place(x=92,y=215)
    while True:
        dbsize = db.getDBSize()
        color=_color.TITLE
        TEMP_COLOR=_color.TITLE
        TEMP_PMIC_COLOR=_color.TITLE
        service_color=_color.TITLE
        log_color=_color.TITLE
        t1=cs.getTemp()
        t2=cs.getTemp2()
        service = getservicestatus("DCLIGHTS.service")
        if dbsize >3000:
            color=_color.FAIL
        if float(t1) > 50.0:
            TEMP_COLOR = _color.FAIL
        if float(t2) > 50.0:
            TEMP_PMIC_COLOR = _color.FAIL
        if service["Status"]!="0":
            service_color=_color.FAIL
        logsize = getlogsize()
        if round(logsize,2) > 100.0:
            log_color = _color.FAIL    
        v1.set("DB size: "+str(dbsize)+" MB")
        lbl1.config(fg= color)
        v2.set("PI Temp: "+str(t1)+" 'C")
        lbl2.config(fg= TEMP_COLOR)
        v3.set("PMIC Temp: "+str(t2)+" 'C")
        lbl3.config(fg= TEMP_PMIC_COLOR)
        v4.set("Log files size: "+str(round(logsize,2))+" MB")
        lbl4.config(fg= log_color)
        v5.set(service["Active"])
        lbl5.config(fg= service_color)
        time.sleep(1)
def lights_page():
    global contents_box,F_lights,photoimagewater,photoimagepower,photoimagetemp,photoimagewatericon,photoimagepowericon,photoimagetempicon
    F_lights= Frame(contents_box,bg=lout.BG_COLOR,height=55)
    F_lights.grid(row=0, column=0, sticky='news')
    frame_left = Frame(F_lights,bg=lout.BG_COLOR,width=lout.frame_leftwidth)
    frame_left.pack(side=LEFT,fill="y")
    frame_left.pack_propagate(0)
    frame_right = Frame(F_lights,bg=lout.BG_COLOR,width=lout.frame_rightwidth)
    frame_right.pack(side=RIGHT,fill="y")
    frame_right.pack_propagate(0)
    w = Canvas(frame_left, width=lout.frame_leftwidth-20, height=452-20,bg=lout.BG_COLOR)
    w.pack(fill="both",expand=True,padx=(10,10),pady=(10,10))
    photo = PhotoImage(file = r"/home/pi/Desktop/HueLighting/App/Pics/watericon.png")
    photoimagewater = photo.subsample(12, 12)
    photoimagewatericon = photo.subsample(15, 15)
    photo1 = PhotoImage(file = r"/home/pi/Desktop/HueLighting/App/Pics/powericon.png")
    photoimagepower = photo1.subsample(12, 12)
    photoimagepowericon = photo1.subsample(15, 15)
    photo2 = PhotoImage(file = r"/home/pi/Desktop/HueLighting/App/Pics/tempicon.png")
    photoimagetemp = photo2.subsample(12, 12)
    photoimagetempicon = photo2.subsample(15, 15)
    x1=17
    y1=17
    btnhw=45
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagewater,command=lambda:showlightopt(5)).place(x=x1, y=y1)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagetemp,command=lambda:showlightopt(11)).place(x=x1, y=y1+81)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagepower,command=lambda:showlightopt(6)).place(x=x1, y=y1+81*2)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagewater,command=lambda:showlightopt(12)).place(x=x1, y=y1+81*3)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagepower,command=lambda:showlightopt(26)).place(x=x1+91, y=y1)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagetemp,command=lambda:showlightopt(7)).place(x=x1+91, y=y1+81*3)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagetemp,command=lambda:showlightopt(24)).place(x=x1+91*2, y=y1)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagepower,command=lambda:showlightopt(10)).place(x=x1+91*2, y=y1+81*3)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagewater,command=lambda:showlightopt(25)).place(x=x1+91*3, y=y1)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagewater,command=lambda:showlightopt(9)).place(x=x1+91*3, y=y1+81*3)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagepower,command=lambda:showlightopt(8)).place(x=x1+80*4, y=138.5)
    Button(w, text = '',bg=lout.BG_COLOR,highlightthickness = 0,bd=0, image = photoimagetemp,command=lambda:showlightopt(4)).place(x=x1+80*5, y=y1)
    print ()
    Button(frame_right,text="Reset Power",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: reset("power")).pack()
    Button(frame_right,text="Reset Water",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: reset("water")).pack()
    Button(frame_right,text="Reset Temperature",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: reset("temp")).pack()
    Button(frame_right,text="Reset All",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: reset("all")).pack()
    Button(frame_right,text="Test lights",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: testlights()).pack()
    Button(frame_right,text="All lights ON",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: alllightson()).pack()
    Button(frame_right,text="All lights OFF",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: alllightsoff()).pack()
    x=429
    y=196
    Label(w,text ="", bg=lout.BG_COLOR, fg="black",image = photoimagewatericon, highlightthickness = 0,bd=0,anchor="w").place(x=x+5, y=y+5)
    Label(w,text ="", bg=lout.BG_COLOR, fg="black",image = photoimagepowericon, highlightthickness = 0,bd=0,anchor="w").place(x=x+5, y=y+45)
    Label(w,text ="", bg=lout.BG_COLOR, fg="black",image = photoimagetempicon, highlightthickness = 0,bd=0,anchor="w").place(x=x+5, y=y+85)
    Label(frame_left,font='Helvetica 12',text = "Water light", bg=lout.BG_COLOR, fg="black",height=1,anchor="w").place(x=x+65, y=y+20)
    Label(frame_left,font='Helvetica 12 ',text = "Power light", bg=lout.BG_COLOR, fg="black",height=1,anchor="w").place(x=x+65, y=y+60)
    Label(frame_left,font='Helvetica 12 ',text = "Temperature light", bg=lout.BG_COLOR, fg="black",height=1,anchor="w").place(x=x+65, y=y+100)

    w.create_rectangle(x, y, 195+x, 125+y, fill=lout.BG_COLOR,outline="#d0d0d0")
    
    
    
    
    def showlightopt(lightnumber):
        global childroot
        if type(childroot) != type:
            childroot.destroy()
        childroot = Toplevel(window)
        childroot.title("Light# "+str(lightnumber))
        childroot.configure(bg=lout.BG_COLOR)
        childroot.geometry("400x226+200+113")
        childroot.minsize(400,226)
        childroot.maxsize(400,226)
        container = Frame(childroot,bg=lout.BG_COLOR,height=400,width=226,highlightbackground="#431c5d", highlightthickness=1)
        container.pack(side=TOP,fill="both")
        container.pack_propagate(0)
        frametop = Frame(container,bg=lout.BG_COLOR,height=180,width=226)
        frametop.pack(side=TOP,fill="x")
        frametop.pack_propagate(0)
        framebottom = Frame(container,bg=lout.BG_COLOR,height=44,width=226)
        framebottom.pack(side=BOTTOM,fill="x")
        framebottom.pack_propagate(0)
        Button(framebottom,text="Turn off",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= "10",height=lout.control_btn_height,command= lambda: lightstate(lightnumber,False)).pack(side=LEFT)
        Button(framebottom,text="Turn on",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= "10",height=lout.control_btn_height,command= lambda: lightstate(lightnumber,True)).pack(side=LEFT)
        def lightstate(light,val):
            try:
                hue.Lightstate(light,val)
            except Exception as e:
                messagebox.showerror(title="Error", message=str(e),parent=F_lights)
    def reset(alert):
        if alert=="all":
            db.reset("power")
            db.reset("water")
            db.reset("temp")
            updatelights()
        else:
            db.reset(alert)
            updatelights()
    def testlights():
        hue.Testlights()
    def alllightson():
        hue.alllightson()
    def alllightsoff():
        hue.alllightsoff()
def settings_page():
    global contents_box,F_settings,t3
    F_settings= Frame(contents_box,bg=lout.BG_COLOR,height=55)
    F_settings.grid(row=0, column=0, sticky='news')
    frame_right = Frame(F_settings,bg=lout.BG_COLOR,width=lout.frame_rightwidth)
    frame_right.pack(side=RIGHT,fill="y")
    frame_right.pack_propagate(0)
    frame_left = Frame(F_settings,bg=lout.BG_COLOR,width=500)
    frame_left.pack(side=LEFT,fill="y",padx=(10,0))
    frame_left.pack_propagate(0)
    Label(frame_left,font='Helvetica 14 bold',text = "Properties", bg=lout.BG_COLOR, fg="black",width=40,height="2",anchor="w").pack(side=TOP)
    frame_lm_left = Frame(frame_left,bg=lout.BG_COLOR,width=160)
    frame_lm_left.pack(side=LEFT,fill="y")
    frame_lm_left.pack_propagate(0)
    frame_lm_right = Frame(frame_left,bg=lout.BG_COLOR,width=240)
    frame_lm_right.pack(side=LEFT,fill="y")
    frame_lm_right.pack_propagate(0)    
    properties=db.allproperties()
    var={}
    var0 = StringVar()
    for x in properties:
        var1 = StringVar()
        var2 = StringVar()
        if x[0] !="APRUNNING":
            Radiobutton(frame_lm_left,font='Helvetica 10 ',textvariable=var1,bg=lout.BG_COLOR, variable=var0,value=x,width=20,height="1",  highlightthickness = 0,bd=0,anchor="w").pack(side=TOP)
            Label(frame_lm_right,font='Helvetica 10 ',textvariable = var2, bg=lout.BG_COLOR, fg="black",width=33,height="1",  highlightthickness = 0,bd=0,anchor="w").pack(side=TOP,padx=(5,0))
            var1.set(x[0])
            var2.set(db.property_value(x[0]))
            var[x[0]]=[var1,var2]
        else:
            Label(frame_lm_left,font='Helvetica 10 ',textvariable = var1, bg=lout.BG_COLOR, fg="black",width=20,height="1",  highlightthickness = 0,bd=0,anchor="w").pack(side=TOP,padx=(25,0))
            Label(frame_lm_right,font='Helvetica 10 ',textvariable = var2, bg=lout.BG_COLOR, fg="black",width=33,height="1",  highlightthickness = 0,bd=0,anchor="w").pack(side=TOP,padx=(5,0))
            var1.set(x[0])
            var2.set(db.property_value(x[0]))
            var[x[0]]=[var1,var2]          
    def refreshsettings():
        while True:
            for x in properties:
                var[x[0]][1].set(db.property_value(x[0]))
            time.sleep(1)
    Button(frame_right,text="Change value",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command=lambda:action()).pack()
    def action():
        if var0.get() =="":
            messagebox.showinfo(title="", message="Select a property first.",parent=F_services)
        else:
            global childroot
            if type(childroot) != type:
                childroot.destroy()
            var = var0.get()
            childroot = Toplevel(window)
            childroot.title(var)
            childroot.configure(bg=lout.BG_COLOR)
            childroot.geometry("400x226+200+113")
            childroot.minsize(400,226)
            childroot.maxsize(400,226)
            container = Frame(childroot,bg=lout.BG_COLOR,height=400,width=226,highlightbackground="#431c5d", highlightthickness=1)
            container.pack(side=TOP,fill="both")
            container.pack_propagate(0)
            frametop = Frame(container,bg=lout.BG_COLOR,height=180,width=226)
            frametop.pack(side=TOP,fill="x")
            frametop.pack_propagate(0)
            framebottom = Frame(container,bg=lout.BG_COLOR,height=44,width=226)
            framebottom.pack(side=BOTTOM,fill="x")
            framebottom.pack_propagate(0)
            Label(frametop,font='Helvetica 12 ',text ="Property name:  " +var, bg=lout.BG_COLOR, fg="black",width=33,height="1",  highlightthickness = 0,bd=0,anchor="w").pack(side=TOP,padx=(5,0))
            pvar=StringVar()
            Label(frametop,font='Helvetica 10 ',text ="value: ", bg=lout.BG_COLOR, fg="black",width=10,height="1",  highlightthickness = 0,bd=0,anchor="w").pack(side=LEFT,padx=(5,0))
            propval = Entry(frametop, textvariable =pvar ,bg=lout.BG_COLOR, font=('calibre',10, 'bold')).pack(side=LEFT)
            pvar.set(db.property_value(var))
            Button(framebottom,text="Update value",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= "10",height=lout.control_btn_height,command=lambda:changepval()).pack(side=LEFT)
            def changepval():
                db.property_insert(var,pvar.get())
                childroot.destroy()
    t3=Thread(target=refreshsettings)
    t3.start() 

def services_page():
    global contents_box,F_services
    F_services= Frame(contents_box,bg=lout.BG_COLOR,height=55)
    F_services.grid(row=0, column=0, sticky='news')
    color=_color.TITLE
    frame_left = Frame(F_services,bg=lout.BG_COLOR,width=172)
    frame_left.pack(side=LEFT,fill="y")
    frame_left.pack_propagate(0)
    frame_middle = Frame(F_services,bg=lout.BG_COLOR,width=88)
    frame_middle.pack(side=LEFT,fill="y")
    frame_middle.pack_propagate(0)
    frame_right = Frame(F_services,bg=lout.BG_COLOR,width=lout.frame_rightwidth)
    frame_right.pack(side=RIGHT,fill="y")
    frame_right.pack_propagate(0)
    var0 = StringVar()
    Label(frame_left,font='Helvetica 12 bold',text = "Services", bg=lout.BG_COLOR, fg="black",width=16 ,height="2",anchor="w").pack()
    R1 = Radiobutton(frame_left,text="DCLIGHTS.service",textvariable="DCLIGHTS",bg=lout.BG_COLOR, variable=var0,value="DCLIGHTS.service",width=16,height=lout.widget_h,  highlightthickness = 0,bd=0,anchor="w")
    R2 = Radiobutton(frame_left,text="cron.service",textvariable="cron",bg=lout.BG_COLOR,  variable=var0,value="cron.service",width=16,height=lout.widget_h,  highlightthickness = 0,bd=0,anchor="w")
    R3 = Radiobutton(frame_left,text="mariadb.service",textvariable="mariadb",bg=lout.BG_COLOR,  variable=var0,value="mariadb.service",width=16,height=lout.widget_h,  highlightthickness = 0,bd=0,anchor="w")
    R1.pack()
    R2.pack()
    R3.pack()
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    Label(frame_middle,font='Helvetica 12 bold',text = "Status", bg=lout.BG_COLOR, fg="black",width=12,height="2",anchor="w").pack()
    lbl1=Label(frame_middle,font='Helvetica 10 ',textvariable = v1, bg=lout.BG_COLOR, fg=color,width=12,height="2",anchor="w")
    lbl2=Label(frame_middle,font='Helvetica 10 ',textvariable = v2,  bg=lout.BG_COLOR, fg=color,width=12,height="2",anchor="w")
    lbl3=Label(frame_middle,font='Helvetica 10 ',textvariable = v3, bg=lout.BG_COLOR, fg=color,width=12,height="2",anchor="w")
    lbl1.pack()
    lbl2.pack()
    lbl3.pack()
    def initview(lbl,v,serv):
        service_color=_color.TITLE
        service = getservicestatus(serv)
        if service["Status"]!="0":
            service_color=_color.FAIL
        v.set(service["Active"])
        lbl.config(fg= service_color)          
    initview(lbl1,v1,"DCLIGHTS.service")
    initview(lbl2,v2,"cron.service")
    initview(lbl3,v3,"mariadb.service")
    def action(act):
        if var0.get() =="":
            messagebox.showinfo(title="", message="Select a service first.",parent=F_services)
        elif var0.get() =="DCLIGHTS.service":
            serviceaction(act,var0.get())
            updateview(lbl1,v1)
        elif var0.get() =="cron.service":
            serviceaction(act,var0.get())
            updateview(lbl2,v2)
        elif var0.get() =="mariadb.service":
            serviceaction(act,var0.get())
            updateview(lbl3,v3)
    def updateview(lbl,v):
        service_color=_color.TITLE
        service = getservicestatus(var0.get())
        if service["Status"]!="0":
            service_color=_color.FAIL
        v.set(service["Active"])
        lbl.config(fg= service_color)
    stopser = Button(frame_right,text="Stop",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command=lambda:action("stop"))
    startpser = Button(frame_right,text="Start",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command=lambda:action("start"))
    restartpser = Button(frame_right,text="Restart",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command=lambda:action("restart"))
    stopser.pack()
    startpser.pack()
    restartpser.pack()
def database_page():
    global contents_box,F_database,close_btn
    F_database= Frame(contents_box,bg=lout.BG_COLOR,height=55)
    F_database.grid(row=0, column=0, sticky='news')
    res = db.getrowcounts()
    res2 = db.getDBtables()
    frame_right = Frame(F_database,bg=lout.BG_COLOR,width=120)
    frame_right.pack(side=RIGHT,fill="y")
    frame_right.pack_propagate(0)
    frame_left = Frame(F_database,bg=lout.BG_COLOR,width=172)
    frame_left.pack(side=LEFT,fill="y",padx=(10,0))
    frame_left.pack_propagate(0)
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    color="black"
    Label(frame_left,font='Helvetica 12 bold',text = "Row Count", bg=lout.BG_COLOR, fg=color,width=13,height="2",anchor="w").pack()
    lbl1=Label(frame_left,font='Helvetica 10 ',textvariable = v1, bg=lout.BG_COLOR, fg=color,width=24,height="1",anchor="w")
    lbl2=Label(frame_left,font='Helvetica 10 ',textvariable = v2,  bg=lout.BG_COLOR, fg=color,width=24,height="1",anchor="w")
    lbl3=Label(frame_left,font='Helvetica 10 ',textvariable = v3, bg=lout.BG_COLOR, fg=color,width=24,height="1",anchor="w")
    lbl4=Label(frame_left,font='Helvetica 10',textvariable = v4, bg=lout.BG_COLOR, fg=color,width=24,height="1",anchor="w")
    lbl1.pack()
    lbl2.pack()
    lbl3.pack()
    lbl4.pack()
    v1.set("Alerts: "+str(res["alerts"]))
    v2.set("Logs: "+str(res["alertslog"]))
    v3.set("Total emails count: "+str(res["mids"]))
    v4.set("Errors: "+str(res["errors"]))
    frame_lm = Frame(frame_left,bg=lout.BG_COLOR,width=172,height=145)
    frame_lm.pack(side=TOP,fill="y")
    frame_lm.pack_propagate(0)
    Label(frame_lm,font='Helvetica 12 bold',text = "Table Size", bg=lout.BG_COLOR, fg=color,width=13,height="2",anchor="w").pack()
    frame_lm_left = Frame(frame_lm,bg=lout.BG_COLOR,width=86)
    frame_lm_left.pack(side=LEFT,fill="y")
    frame_lm_left.pack_propagate(0)
    frame_lm_right = Frame(frame_lm,bg=lout.BG_COLOR,width=86)
    frame_lm_right.pack(side=RIGHT,fill="y")
    frame_lm_right.pack_propagate(0)
    tarr={}
    for x in res2:
        v5 = StringVar()
        v6 = StringVar()
        lbl1=Label(frame_lm_left,font='Helvetica 10',textvariable = v5, bg=lout.BG_COLOR, fg=color,width=24,height="1",anchor="w")
        lbl2=Label(frame_lm_right,font='Helvetica 10',textvariable = v6, bg=lout.BG_COLOR, fg=color,width=24,height="1",anchor="w")
        lbl1.pack()
        lbl2.pack()
        v5.set(x)
        v6.set(str(res2[x])+" MB")
        tarr[x]=[v5,v6]
    vt = StringVar()
    frame_lb= Frame(frame_left,bg=lout.BG_COLOR,width=172,height=80)
    frame_lb.pack(side=TOP,fill="x")
    frame_lb.pack_propagate(0) 
    Label(frame_lb,font='Helvetica 12 bold',text = "Database Size", bg=lout.BG_COLOR, fg=color,width=13,height="2",anchor="w").pack()   
    lbldbs=Label(frame_lb,font='Helvetica 10 ',textvariable = vt, bg=lout.BG_COLOR, fg=color,width=24,height="1",anchor="w")
    lbldbs.pack()
    dbsize = db.getDBSize()
    vt.set(str(dbsize) + " MB")
    btn2=Button(frame_right,text="Test connection",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command=lambda:testconnection())
    btn3=Button(frame_right,text="Delete logs",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command=lambda : Thread(target=deletelogs).start())
    btn4=Button(frame_right,text="Rebuild OPSDB",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command=lambda : Thread(target=rebuilddb).start())
    btn2.pack()
    btn3.pack()
    btn4.pack()
    def refreshdata():
        while True:
            dbsize = db.getDBSize()
            res = db.getrowcounts()
            res2 = db.getDBtables()
            v1.set("Alerts: "+str(res["alerts"]))
            v2.set("Logs: "+str(res["alertslog"]))
            v3.set("Total emails count: "+str(res["mids"]))
            v4.set("Errors: "+str(res["errors"]))
            vt.set(str(dbsize) + " MB")
            for x in res2:
                arr= tarr[x]
                arr[0].set(x)
                arr[1].set(str(res2[x])+" MB")
            time.sleep(1)
    def testconnection():
        res = db.testconn()
        if res[0]==0:
            messagebox.showinfo(title="Success", message="Database connection was successfull.",parent=F_database)
        else:
            messagebox.showerror(title="Failure", message=res[1],parent=F_database)
    def deletelogs():
        res = messagebox.askquestion('Delete logs', 'Are you sure you want to delete the logs?')
        if res == 'yes':
            db.deletelogs()
            refreshdata()
    def rebuilddb():
        res = messagebox.askquestion('Rebuild OPSDB', 'Are you sure you want to rebuild OPSDB? All database data will be deleted and new data will be added. This process can take up to 5 minutes to finish.')
        if res == 'yes':
            if not aprunning():
                db.rebuildDB()
                messagebox.showinfo(title="", message="Database rebuilt successfull. Update progress will start soon.",parent=F_database)
            else:
                messagebox.showinfo(title="", message="Can not rebuild database. Update query is in progress.",parent=F_database)
    t1=Thread(target=refreshdata)
    t1.start()
def home_page():
    global contents_box,alerts_box,mylist,t1,t2,F_home
    FG_LIST_COLOR="#001f3f"
    F_home= Frame(contents_box,bg=lout.BG_COLOR,height=55)
    F_home.grid(row=0, column=0, sticky='news')
    alerts_box = Frame(F_home,bg=lout.BG_COLOR,height=300,width=500,highlightbackground="#0074D9", highlightthickness=1)
    alerts_box.pack(side=RIGHT)
    alerts_box.pack_propagate(0)
    title_lable = Label(alerts_box,font='Helvetica 12 bold', text="Active Alerts", bg="#0074D9", fg="white",height="3").pack(fill="x")
    scrollbar = Scrollbar(alerts_box)
    scrollbar.pack(side = RIGHT, fill = BOTH)
    mylist = Listbox(alerts_box,height=500,width =600)
    mylist.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = mylist.yview)
    t1=Thread(target=update_alerts)
    t2=Thread(target=checks)
    t1.start()
    t2.start()

def run_main():
    global window,mylist,contents_box,p1,F_home,close_btn
    FG_LIST_COLOR="#001f3f"
    window = Tk()
    window.title("OPS Hue Lighting")
    window.configure(bg=lout.BG_COLOR)
    window.geometry("800x452")
    window.minsize( 800,452)
    window.maxsize( 800,452)
    title_box= Frame(window,bg=lout.BG_COLOR,height=55)
    title_box.pack(side=TOP,fill="x")
    title_box.pack_propagate(0)
    contents_box= Frame(window,bg=lout.BG_COLOR)
    contents_box.pack(fill="both",expand=True)
    contents_box.grid_rowconfigure(0, weight=1)
    contents_box.grid_columnconfigure(0, weight=1)
    pages_box = Frame(window,bg=lout.BG_COLOR,height=55)
    pages_box.pack(side=BOTTOM,fill="x")
    pages_box.pack_propagate(0)
    title_lable = Label(title_box,font='Helvetica 18 bold', text="OPS Hue Lighting", bg=lout.BG_COLOR, fg="#0074D9",height="3").pack()
    close_btn = Button(pages_box,text="Close",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= lout.control_btn_width,height=lout.control_btn_height,command= lambda: window_close(window))
    global home_btn,light_btn,service_btn,database_btn,setting_btn
    home_btn = Button(pages_box,text="Home",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= 8,height=lout.widget_h,command=lambda:raiseframe(F_home,home_btn))
    light_btn = Button(pages_box,text="Lights",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= 8,height=lout.widget_h,command=lambda:raiseframe(F_lights,light_btn))
    service_btn = Button(pages_box,text="Services",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= 8,height=lout.widget_h,command=lambda:raiseframe(F_services,service_btn))
    database_btn = Button(pages_box,text="Database",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= 8,height=lout.widget_h,command=lambda:raiseframe(F_database,database_btn))
    setting_btn = Button(pages_box,text="Settings",bg=lout.BG_COLOR,fg="#0074D9",highlightthickness = 1,bd=0,width= 8,height=lout.widget_h,command=lambda:raiseframe(F_settings,setting_btn))
    close_btn.pack(side=RIGHT,padx=4)
    home_btn.pack(side=LEFT,padx=4)
    light_btn.pack(side=LEFT,padx=4)
    service_btn.pack(side=LEFT,padx=4)
    database_btn.pack(side=LEFT,padx=4)
    setting_btn.pack(side=LEFT,padx=4)
    services_page()
    settings_page()
    lights_page()
    database_page()
    home_page()
    home_btn.configure(bg = "#00a2ed",activebackground="#00adff", activeforeground="white",fg="white")
    window.mainloop()
    exit()
run_main()
