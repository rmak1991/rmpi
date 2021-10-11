#! /usr/bin/python3
from tkinter import *
import tkinter.messagebox,os,subprocess
from threading import *
from pathlib import Path
from Lib.T_FileHandler import *
from Lib.T_Logs import LOG as l
from Lib.T_Global import PATHS as _P

import subprocess, pexpect, math, types, time, os, sys
window = Tk
m = Menu
# def donothing():
#    filewin = Toplevel(root)
#    button = Button(filewin, text="Do nothing button")
#    button.pack()
#    

# def get_menu(root):
#     menubar = Menu(root)
#     filemenu = Menu(menubar, tearoff=0)
#     filemenu.add_command(label="New", command=donothing)
#     filemenu.add_command(label="Open", command=donothing)
#     filemenu.add_command(label="Save", command=donothing)
#     filemenu.add_command(label="Save as...", command=donothing)
#     filemenu.add_command(label="Close", command=donothing)
#     filemenu.add_separator()
#     filemenu.add_command(label="Exit", command=root.quit)
#     menubar.add_cascade(label="File", menu=filemenu)
#     editmenu = Menu(menubar, tearoff=0)
#     editmenu.add_command(label="Undo", command=donothing)
#     editmenu.add_separator()
#     editmenu.add_command(label="Cut", command=donothing)
#     editmenu.add_command(label="Copy", command=donothing)
#     editmenu.add_command(label="Paste", command=donothing)
#     editmenu.add_command(label="Delete", command=donothing)
#     editmenu.add_command(label="Select All", command=donothing)
#     menubar.add_cascade(label="Edit", menu=editmenu)
#     helpmenu = Menu(menubar, tearoff=0)
#     helpmenu.add_command(label="Help Index", command=donothing)
#     helpmenu.add_command(label="About...", command=donothing)
#     menubar.add_cascade(label="Help", menu=helpmenu)
#     return menubar
def jobmenu(job,x,y):
    global m
    m = Menu(window, tearoff = 0)
    m.add_command(label ="Start",command=lambda : startjob(job))

    #m.add_separator()
    m.add_command(label ="Rename")
    try:
        m.tk_popup(x, y)
    finally:
        m.grab_release()
def startjob(job):
    subprocess.run("/usr/bin/python3 /home/pi/Desktop/rmpi-master/Automation/Jobs/"+job,shell=True,check=True,cwd=_P.RMPI_MASTER_PATH)    
def rightclick(event):
    if type(event.widget) == type(Button()) and str(event.widget["textvariable"]).split(" ")[1] == "JOB":
        jobmenu(event.widget["text"], event.x_root, event.y_root)
    else:
        if type(m)!=type:
            if m.winfo_ismapped():
                m.destroy()
def leftclick(event):
    if type(m)!=type:
        if type(m)==type(Menu()):
            m.destroy()
def run_main():
    global window
    window=Tk()
    window.title("RMPIAPP")
    sc_h = window.winfo_screenheight()
    sc_w = window.winfo_screenwidth()
    win_h= int(sc_h)
    win_w=int(sc_w)
    #pos_x=int((sc_w-win_w)/2)
    #pos_y=int((sc_h-win_h)/2)
    window.geometry(str(win_w)+"x"+str(win_h))
    #window.resizable(False, False)
    frame_left = Frame(window, bg="#001f3f",width=300)
    frame_left.pack(side=LEFT, fill="y")
    frame_left.pack_propagate(0)
    files = FILES_NAME_PATTERN(_P.JOBS_PATH,starts_with="J_")
    for x in files:
        runTime = StringVar()
        Button(frame_left,text=x,width=230,textvariable=[runTime,"JOB"],anchor="w").pack()

    #tkinter.messagebox.showinfo("Congratulations", "You won!")
    #window.overrideredirect(1)
    window.bind("<Button-1>", leftclick)
    window.bind("<Button-3>", rightclick)
    window.focus() 
    #window.config(menu=get_menu(window))
    window.mainloop()
run_main()

