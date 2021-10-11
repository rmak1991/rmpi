import os,sys,subprocess
from pathlib import Path
from PIL import Image,ImageFont, ImageDraw
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P

# status = os.system('systemctl is-active --quiet cron.service')
# img =Image.new('RGB',(900,900),'black')
# str1 = "Hello there"
# font = ImageFont.truetype("Piboto-Thin.ttf", 70)
# w,h=font.getsize(str1)
# draw=ImageDraw.Draw(img)
# draw.text(((900-w)/2,(900-h)/2),str1,font=font,fill="white")
# img.save(_P.PICS_PATH+"/err.jpg")
# 
# subprocess.run(["pcmanfm --set-wallpaper "+_P.PICS_PATH+"/err.jpg"],shell=True,check=True,cwd=PATH)
# 

