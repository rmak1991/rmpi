#! /usr/bin/python3
from tkinter import *
import tkinter.messagebox,os,sys
from threading import *
from pathlib import Path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lib.T_FileHandler import *
from Lib.T_Logs import LOG as l
from Lib.T_Global import PATHS as _P

import subprocess, pexpect, math, types, time, os, sys

def run_main():
    window=Tk()
    window.title("RMPIAPP")
    sc_h = window.winfo_screenheight()
    sc_w = window.winfo_screenwidth()
    win_h= int(sc_h)
    win_w=int(sc_w)
    #pos_x=int((sc_w-win_w)/2)
    #pos_y=int((sc_h-win_h)/2)
    window.geometry(str(win_w)+"x"+str(win_h))
    window.resizable(False, False)
    frame_top = Frame(window, bg="",height=80)
    frame_top.pack(fill="x")
    frame_top.pack_propagate(0)
    
    variable = StringVar(window)
    variable.set("one")
    optionmenu = OptionMenu(frame_top,variable, "one", "two", "three")
    optionmenu.config(width=30)
    optionmenu.config(height=200)

    optionmenu.pack(side=LEFT,padx=(10,10),pady=(10,10))

    Entry(frame_top).pack(side=LEFT,padx=(30,30),pady=(30,30))


    #tkinter.messagebox.showinfo("Congratulations", "You won!")
    #window.overrideredirect(1)
    window.mainloop()
run_main()

