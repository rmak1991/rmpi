#! /usr/bin/python3
import subprocess
#username = rmpi
#gmail = ryanmakarem91@gmail.com
#keypi = rmpi2021
#subprocess.run(["sudo apt install git"],shell=True,check=True)
#subprocess.run(["git config --global user.name 'rmpi'"],shell=True,check=True)
#subprocess.run(["git config --global user.email 'ryanmakarem91@gmail.com'"],shell=True,check=True)
#subprocess.run(["git config --global core.editor nano"],shell=True,check=True)
#    uncomment the line below to allow php run exec commands
#subprocess.run(["echo 'www-data  ALL=NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo"],shell=True,check=True)
#subprocess.run(["mkdir rmpi-master"],shell=True,check=True,cwd="/home/pi/Desktop/")
subprocess.run(["git init"],shell=True,check=True,cwd="/home/pi/Desktop/rmpi-master")
subprocess.run(["git add --all"],shell=True,check=True,cwd="/home/pi/Desktop/rmpi-master")
subprocess.run(["git status"],shell=True,check=True,cwd="/home/pi/Desktop/rmpi-master")
subprocess.run(["pwd"],shell=True,check=True)
####subprocess.run(["ssh-keygen -t rsa -b 4096 -C rmpi@2021"],shell=True,check=True)
