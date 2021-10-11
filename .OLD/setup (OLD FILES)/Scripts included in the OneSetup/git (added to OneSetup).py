#! /usr/bin/python3
import subprocess
_USERNAME= "rmpi"
_GMAIL= "ryanmakarem91@gmail.com"
_KEYPI= "rmpi2021"
_ORIGIN= "rmak1991/rmpi.git"
_DIRNAME= "rmpi-master"
PATH="/home/pi/Desktop/"+_DIRNAME
DESKTOP = "/home/pi/Desktop/"
subprocess.run(["sudo apt install git"],shell=True,check=True)
subprocess.run(["git config --global user.name '"+_USERNAME+"'"],shell=True,check=True)
subprocess.run(["git config --global user.email '"+_GMAIL+"'"],shell=True,check=True)
subprocess.run(["git config --global core.editor nano"],shell=True,check=True)
subprocess.run(["mkdir -p "+_DIRNAME],shell=True,check=True,cwd=DESKTOP)
subprocess.run(["git init"],shell=True,check=True,cwd=PATH)
subprocess.run(["git add --all"],shell=True,check=True,cwd=PATH)
subprocess.run(["git status"],shell=True,check=True,cwd=PATH)
subprocess.run(["sudo systemctl enable ssh"],shell=True,check=True)
subprocess.run(["sudo systemctl start ssh"],shell=True,check=True)
subprocess.run(["git remote add origin git@github.com:"+_ORIGIN],shell=True,check=True,cwd=PATH)
args=["ssh-keygen","-t","rsa","-b","4096","-C",_KEYPI]
childprocess = subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
child_out = childprocess.communicate(input=b'\n')
subprocess.run(["ssh-keygen -E sha256 -lf ~/.ssh/id_rsa.pub"],shell=True,check=True)
print('*************************\nAdd the public key below to github\n*************************\n')
subprocess.run(["cat ~/.ssh/id_rsa.pub"],shell=True,check=True)

