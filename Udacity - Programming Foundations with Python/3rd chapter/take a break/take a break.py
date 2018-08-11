" take a break"
import time
import webbrowser

count=0

print ("this program started on"+time.ctime())

while (count<3):
       time.sleep(10)
       webbrowser.open("https://www.youtube.com/watch?v=xpPc_Kfx97s")
       count+=1