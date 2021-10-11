#! /usr/bin/python3
from tkinter import *
import tkinter.messagebox,os
from threading import *
from pathlib import Path
from Lib.T_FileHandler import *
from Lib.T_Logs import LOG as l
from Lib.T_Global import PATHS as _P

import subprocess, pexpect, math, types, time, os, sys
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   

def get_menu(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    return menubar

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
    #window.resizable(False, False)
    frame_left = Frame(window, bg="#001f3f")
    frame_left.pack(side=LEFT, fill="y")
    title_lable = Label(frame_left,font='Helvetica 18 bold', text="Header", fg="#80bfff",width=8,height=2).pack()
    title_lable.pack()
#     frame_left = Frame(window, bg="#001f3f")
#     frame_left.pack(side=LEFT,fill="y")
#     btn1 = Button(frame_left,text="Create")
#     btn1.pack()

    tkinter.messagebox.showinfo("Congratulations", "You won!")
    #window.overrideredirect(1)
    window.config(menu=get_menu(window))
    window.mainloop()
#run_main()

