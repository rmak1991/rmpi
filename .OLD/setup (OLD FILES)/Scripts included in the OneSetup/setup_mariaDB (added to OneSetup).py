#! /usr/bin/python3
import subprocess
import pexpect
#subprocess.run(["sudo apt update"],shell=True,check=True)
#subprocess.run(["sudo apt upgrade -y"],shell=True,check=True)
#subprocess.run(["sudo apt install mariadb-server -y"],shell=True,check=True)
child = pexpect.spawn("sudo mysql_secure_installation")
try:
    child.expect("password",timeout=3)
    child.sendline('Rayan1991')
    child.expect("password",timeout=3)
    child.sendline('yes')
    child.expect("password",timeout=3)
    child.sendline('Rayan1991')
    child.expect("password",timeout=3)
    child.sendline('Rayan1991')
    child.expect("anonymous",timeout=3)
    child.sendline('no')
    child.expect("remotely",timeout=3)
    child.sendline('no')
    child.expect("database",timeout=3)
    child.sendline('yes')
    child.expect("privilege",timeout=3)
    child.sendline('yes')
    print(str(child))
except:
    print("Exception was thrown")
    print("debug information:")
    print(str(child))   
