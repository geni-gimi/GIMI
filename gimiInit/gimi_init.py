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
import gimiREST

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

#TODO: get project name from urn
experimenterName = raw_input("Tell us about yourself: enter your name: \n")

exp_org= raw_input ("Your organization: \n")

#Initialize iRODS
print("Initializing iRODS")

irodsenv = subprocess.check_output(['ienv'])
print irodsenv

while True:
    os.system("iinit")
    p = subprocess.Popen('ils', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ilsoutput, ilserrors = p.communicate()
#    print errors
    if not "CAT_INVALID_AUTHENTICATION" in ilserrors:
        break
    else:
        print ("Well, wrong password, please try again")

username = raw_input("Enter your GENI username: \n")

p = subprocess.Popen(['omni.py', 'listmyslices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
listmyslicesOutput, listmyslicesErrors = p.communicate()

print listmyslicesErrors


slicename = raw_input("Please enter your preferred slice name for this experiment: \n")

expName = raw_input("Enter your experiment name: \n")

#Experiment ID = Experiment name + slice name + time (time stamp use time.time())
expTime = str(time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time())))
expId = str(username) + "-" + str(expName) + "-" + expTime

print ("derived experiment ID: " + expId)

#Retrieve manifest rspec
print ("retrieving the manifest rspec...")

manifestName="manifest-"+ expId + ".rspec"
os.system("omni.py listresources " + slicename + " -a pg-utah -o --outputfile=" + workdirectory + "/"+manifestName)
        
# This creates an example iRODS object & creates the XML files & makes a ticket

newRods = iRODS.iRODS('proj_authority', 'proj_name', 'proj_id', 'PI', 'proj_individual_authority', 'proj_individual_user', 'proj_date_time_type', 'proj_start', 'exp_authority', expName, expId, 'experimenter', exp_org, username, 'iso8601', expTime)
#make an initial ticket

myTicket=newRods.makeTicket(expire_time='1379654800')

while True:
    pushManifestOption = raw_input("Do you want to push manifest to iRODS? (Yes or No) \n")
 
    if (pushManifestOption in ("Yes", "Y", "yes", "y")):
        #Push to iRODS
        newRods.pushManifest(manifestName, workdirectory, slicename)
#        subprocess.check_output(['icd', expId])
#        subprocess.check_output(['iput', workdirectory + "/" + manifestName])
#        print ("Manifest " + manifestName + " has been pushed to iRODS")
        break
 
    elif (pushManifestOption in ("No", "N", "no", "n")):
        break
    else:
        print ("Please answer Yes or No")
        
restInt = gimiREST.REST("emmy9.casa.umass.edu", "8002", workdirectory, expId)