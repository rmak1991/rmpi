#! /usr/bin/python3

import tkinter as tk
from pathlib import Path

window = tk.Tk()

# Using readlines()
file1 = open('/var/spool/cron/crontabs/pi', 'r')
Lines = file1.readlines()
count = 0
cbox={}
for line in Lines:
    if len(line.strip())!=0:
        if line.strip()[0] !="#":
            cb = tk.IntVar()
            c1 = tk.Checkbutton(window, text=line.strip(),variable=cb,anchor="w",justify="left",width=100,pady=20, onvalue=1, offvalue=0)
            cbox[c1]=cb
            c1.pack()
            count = count +1
def gettext():
    for c in cbox:
        c1= cbox[c]
def CMD_reboot():
    reboot()
def CMD_gitpush():
    gitPush()   
def CMD_sendemail():
    sendDailyReport()    
def CMD_reset():
    CMD_reset()    
B = tk.Button(text ="Reboot",anchor="w",justify="left",width=100,pady=20,command=CMD_reboot)
B.pack()
B = tk.Button(text ="Send Email",anchor="w",justify="left",width=100,pady=20,command=CMD_sendemail)
B.pack()
B = tk.Button(text ="GitPush",anchor="w",justify="left",width=100,pady=20,command=CMD_gitpush)
B.pack()
B = tk.Button(text ="Reset",anchor="w",justify="left",width=100,pady=20,command=CMD_reset)
B.pack()
window.mainloop()
