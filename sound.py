import os
import time
import subprocess

def clear(): os.system('clear')

def measure():
    rtime=60*30
    restart=time.time()+rtime
    while True:
        proc = subprocess.Popen(['soundmeter --trigger +550 20 --action exec --exec trigger.sh'], shell=True)
        time.sleep(120) # <-- sleep for 12''
        proc.terminate()
        print("Restart process")
        if time.time()>restart:
            break

while True:      
    os.system("echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind")
    time.sleep(30)
    os.system("echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/bind")
    time.sleep(30)
    print("Starte Messung")
    measure()
    time.sleep(1830)
    clear()
    

# <-- terminate the process
