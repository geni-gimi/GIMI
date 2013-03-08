
import lockfile
import time
import os
import subprocess

myport = 5040 
endport = 5050 

token = "/tmp/labwikitoken"

lock = lockfile.FileLock(token)
with lock:
    while (myport < endport):
        file_path = "/var/run/labwiki/labwiki" + str(myport) + ".pid"
        if os.path.exists(file_path):
            myport = myport + 1
        else:
            pid = subprocess.call(["/home/johren/GIMI/GIMIPortal/src/startLW.sh", str(myport)])
	    print myport
            time.sleep(3)
            break
 
