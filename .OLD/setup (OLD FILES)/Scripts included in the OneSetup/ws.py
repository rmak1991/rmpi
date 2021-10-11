#! /usr/bin/python3
import subprocess

subprocess.run(["sudo apt install apache2 -y"],shell=True,check=True)
subprocess.run(["sudo apt install php libapache2-mod-php -y"],shell=True,check=True)
#    uncomment the line below to allow php run exec commands
subprocess.run(["echo 'www-data  ALL=NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo"],shell=True,check=True)
subprocess.run(["sudo rm /var/www/html/*"],shell=True,check=True)
subprocess.run(["sudo cp -r /home/pi/Desktop/rmpi-master/setup/ws/files/* /var/www/html/"],shell=True,check=True)
subprocess.run(["sudo ln -s /var/www/html /home/pi/Desktop/html"],shell=True,check=True)
