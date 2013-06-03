#!/usr/bin/env python
#
# GENIPUBLIC-COPYRIGHT
# Copyright (c) 2013 University of Massachusetts Amherst
# All rights reserved.
# 
# Permission to use, copy, modify and distribute this software is hereby
# granted provided that (1) source code retains these copyright, permission,
# and disclaimer notices, and (2) redistributions including binaries
# reproduce the notices in supporting documentation.
#
# THE UNIVERSITY OF MASSACHUSETTS AMHERST ALLOWS FREE USE OF THIS SOFTWARE IN ITS "AS IS"
# CONDITION.  THE UNIVERSITY OF MASSACHUSETTS DISCLAIMS ANY LIABILITY OF ANY KIND
# FOR ANY DAMAGES WHATSOEVER RESULTING FROM THE USE OF THIS SOFTWARE.
# ------------------------------------------------------------------------------


import os
import sys
import time
import subprocess
import iRODS

#import urllib
#import urllib2


#Set up working directory
print("Welcome to the GIMI initialization script, please make sure to install omni and set up your credential before running this script")
workdirectory = raw_input("Enter your preferred experiment path (please use absolute path, e.g., /home/geni/your/dir/): \n")

if (os.path.exists(workdirectory) == False):
    
    while True:
        createPathOption = raw_input("Path doesn't exist, do you want me to create directory for you? (Yes or No) \n")
        if (createPathOption in ("Yes", "Y", "yes", "y")):
            os.makedirs(workdirectory)
            break
        elif (createPathOption in ("No", "N", "no", "n")):
            print ("Please try again after creating the directory")
            sys.exit(1)
        else: 
            print ("Please answer Yes or No")

#Get user information (experimenter name & organization)
experimenterName = raw_input("Tell us about yourself: enter your name: \n")

exp_org= raw_input ("Your organization: \n")

#Initialize iRODS
print("Initializing iRODS")

os.system("iinit")

#while True:
#p = sub.Popen('iinit',stdout=sub.PIPE,stderr=sub.PIPE)
#output, errors = p.communicate()

#if "CAT_INVALID_AUTHENTICATION" in output:
#    print output

#else: 
#    continue

username = raw_input("Enter your GENI username: \n")

os.system("omni.py listmyslices " + username)

slicename = raw_input("Please enter your preferred slice name for this experiment: \n")

expName = raw_input("Enter your experiment name: \n")

#Experiment ID = Experiment name + slice name + time (time stamp use time.time())
expId = str(username) + "-" + str(expName) + "-" + str(time.strftime("%Y-%m-%dT%H-%M-%S",time.localtime(time.time())))

print ("derived experiment ID: " + expId)

#Retrieve manifest rspec
print ("retrieving the manifest rspec...")

manifestName="manifest-"+ expId + ".rspec"
os.system("omni.py listresources -a pg-utah " + slicename + " -o --outputfile=" + workdirectory + "/"+manifestName)
        
# This creates an example iRODS object & creates the XML files & makes a ticket

newExp = iRODS.iRODS('proj_id', 'proj_title', 'PI_first_name', 'PI_last_name', 'PI_org', expId, expName, experimenterName, 'exp_last_name', exp_org, 'exp_start', 'exp_end', 'step_name', 'step_seq_id', 'resource_id', slicename, 'artifact_name')


#make an initial ticket
#myTicket=newExp.makeTicket(['koneil2','koneil3'], '1372654800')

myTicket=newExp.makeTicket(expire_time='1379654800')
#myTicket=newExp.makeTicket()

while True:
    pushManifestOption = raw_input("Do you want to push manifest to iRODS? (Yes or No) \n")
 
    if (pushManifestOption in ("Yes", "Y", "yes", "y")):
    #Push to iRODS
        subprocess.check_output(['icd', expId])
        subprocess.check_output(['iput', workdirectory + "/" + manifestName])
        print ("Manefest " + manifestName + " has been pushed to iRODS")
        break
 
    elif (pushManifestOption in ("No", "N", "no", "n")):
        break
    else:
        print ("Please answer Yes or No")