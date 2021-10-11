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
        print(c.cget("text"))
        print(c1)

B = tk.Button(text ="Submit",anchor="w",justify="left",width=100,pady=20,command=gettext)
B.pack()
B = tk.Button(text ="Delete",anchor="w",justify="left",width=100,pady=20)
B.pack()
window.mainloop()
