import time
import os
choice=int(input(""))
if choice == 1:  
    t = int(input(""))
    time.sleep(t)
    os.system("shutdown -r -t 0")
    exit()
elif choice==2:
    t = int(input(""))
    time.sleep(t)
    os.system("taskkill /f /im wps.exe")
    exit()
else:
    t = int(input(""))
    time.sleep(t)
    for i in range(1,10):
        os.system("ipconfig")
    exit()
    
