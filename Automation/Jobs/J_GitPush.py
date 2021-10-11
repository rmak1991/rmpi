#! /usr/bin/python3
import subprocess,pexpect,os,sys
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
def gitPush():
    try:
        subprocess.run(["git add --all"],shell=True,check=True,cwd=_P.RMPI_MASTER_PATH)
        subprocess.run(["git status"],shell=True,check=True,cwd=_P.RMPI_MASTER_PATH)
        subprocess.run(["git commit -am 'add --all'"],shell=True,check=True,cwd=_P.RMPI_MASTER_PATH)
        #subprocess.run(["git push -u origin master"],shell=True,check=True,cwd=_P.RMPI_MASTER_PATH)
#         subprocess.run(["git push -f origin master"],shell=True,check=True,cwd=_P.RMPI_MASTER_PATH)
        try:
            child = pexpect.spawn("git push -u origin master")
            child.wait()
            print(child)
            i= child.expect(["Are you sure you want to continue connecting","Enter passphrase",""],timeout=5)
            print(child.after)
            child.sendline("yes")
            v= child.expect(["Are you sure you want to continue connecting","Enter passphrase"],timeout=5)
            print(i)
            child.wait()
        except:
            print("hi")
            subprocess.run(["git push -u origin master"],shell=True,check=True,cwd=_P.RMPI_MASTER_PATH)
    except Exception as e:
        print(e)
gitPush()
