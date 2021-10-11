import pexpect
# child = pexpect.spawn("sudo mysql -u root -p -e \"CREATE USER 'RMPIDBU2'@'localhost' IDENTIFIED BY 'RMPI2021'\"")
# try:
#     child.expect("Enter password",timeout=3)
#     child.sendline("rmpi2021")
#     child.wait()
# except Exception as e:
#     print(e)
child = pexpect.spawn("sudo mysql -u root -p -e \"GRANT ALL PRIVILEGES ON *.* TO 'RMPIDBU'@'localhost'\"")
try:
    child.expect("Enter password",timeout=3)
    child.sendline("rmpi2021")
    child.wait()
except Exception as e:
    print(e)
    
child = pexpect.spawn("sudo mysql -u root -p -e \"FLUSH PRIVILEGES\"")
try:
    child.expect("Enter password",timeout=3)
    child.sendline("rmpi2021")
    child.wait()
except Exception as e:
    print(e)

