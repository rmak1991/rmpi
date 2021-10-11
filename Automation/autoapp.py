#! /usr/bin/python3
from tkinter import *
import tkinter.messagebox
from threading import *
from pathlib import Path

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
    top = Toplevel()
    window.title("RMPIAPP")
    sc_h = window.winfo_screenheight()
    sc_w = window.winfo_screenwidth()
    win_h= int(sc_h)
    win_w=int(sc_w)
    #pos_x=int((sc_w-win_w)/2)
    #pos_y=int((sc_h-win_h)/2)
    window.geometry(str(win_w)+"x"+str(win_h))
    #window.resizable(False, False)
    frame_top = Frame(window, bg="#001f3f")
    frame_top.pack(side=TOP, fill="x")
    title_lable = Label(frame_top,font='Helvetica 18 bold', text="Header", fg="#80bfff",width=8,height=2).pack()
    frame_bottom = Frame(window, bg="#001f3f")
    frame_bottom.pack(side=BOTTOM, fill="x")
    title_lable = Label(frame_bottom,font='Helvetica 18 bold', text="Header", fg="#80bfff",width=8,height=2).pack()
    frame_left = Frame(window, bg="#001f3f")
    frame_left.pack(side=LEFT, fill="y")
    title_lable = Label(frame_left,font='Helvetica 18 bold', text="Header", fg="#80bfff",width=8,height=2).pack()
    frame_right = Frame(window, bg="#001f3f")
    frame_right.pack(side=RIGHT, fill="y")
    title_lable = Label(frame_right,font='Helvetica 18 bold', text="Header", fg="#80bfff",width=8,height=2).pack()
      
#     frame_left = Frame(window, bg="#001f3f")
#     frame_left.pack(side=LEFT,fill="y")
#     btn1 = Button(frame_left,text="Create")
#     btn1.pack()

    tkinter.messagebox.showinfo("Congratulations", "You won!")
    #window.overrideredirect(1)
    window.config(menu=get_menu(window))
    window.mainloop()
run_main()