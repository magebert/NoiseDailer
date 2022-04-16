import time
from fritzconnection.lib.fritzcall import FritzCall

fc = FritzCall(address='192.168.178.1', password="x")
fc.dial("x")
print("Anruf gestartet")
time.sleep(120)

