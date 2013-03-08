
import lockfile
import time
import os
import subprocess
import sys

myport = 5020 
endport = 5050 

token = "/tmp/labwikitoken"

uname = sys.argv[1]

lock = lockfile.FileLock(token)
with lock:
    while (myport < endport):
        file_path = "/var/run/labwiki/labwiki" + str(myport) + ".pid"
        if os.path.exists(file_path):
            myport = myport + 1
        else:
            pid = subprocess.call(["/home/labwiki/GIMI/GIMIPortal/src/startLW.sh", str(myport), uname])
	    print myport
            time.sleep(3)
            break
 
