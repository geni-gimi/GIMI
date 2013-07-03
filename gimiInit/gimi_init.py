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
import gimi_util
import omni
#import urllib
#import urllib2


# Set up working directory
print("Welcome to the GIMI initialization script, please make sure to install omni and set up your credential before running this script")
workdirectory = raw_input("Enter your preferred experiment path (please use absolute path, e.g., /home/geni/your/dir): \n")

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

# TODO: Get user information (experimenter name & organization)

experimenterName = raw_input("Tell us about yourself: enter your name: \n")

exp_org= raw_input ("Your organization: \n")

# Initialize iRODS
print("Initializing iRODS")

initialized=gimi_util.callIinit()

#irodsenv = subprocess.check_output(['ienv'])
#print irodsenv

#check_irods_login = subprocess.Popen('ils', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#check_irods_login_output, check_irods_login_error = check_irods_login.communicate()
#if not "CAT_INVALID_AUTHENTICATION" in check_irods_login_error:
#    print ("iRODS already logged in \n")
#else:
#    while True:
#        os.system("iinit")
#        p = subprocess.Popen('ils', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#        ilsoutput, ilserrors = p.communicate()
#    #    print errors
#        if not "CAT_INVALID_AUTHENTICATION" in ilserrors:
#            break
#        else:
#            print ("Well, wrong password, please try again")
            
print ("retrieving slice information...")

p = subprocess.Popen(['omni.py', 'listmyslices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
listmyslicesOutput, listmyslicesErrors = p.communicate()

# get username
username = gimi_util.get_user(listmyslicesErrors)
print ("Your user name is " + username + " \n")

# print listmyslicesErrors
(returned_projectAuthority, returned_projectID, returned_slicename) = gimi_util.listmyslices_output_parse(listmyslicesErrors) 

slicename = '\n'.join(str(x) for x in returned_slicename)

slicename = raw_input("Your active slice names:\n" + slicename + "\nPlease enter your preferred slice name for this experiment: \n")

while True:
    if slicename in returned_slicename:
        break
    else:
        slicename = raw_input("Please only enter the slice names listed above: \n")

slice_index = returned_slicename.index(slicename)    
projectID = ''.join(str(returned_projectID[slice_index]))# for x in returned_projectID)
proj_authority = ''.join(str(returned_projectAuthority[slice_index]))
print ("Your slice name is: " + slicename)

print ("Your project ID is: \n" + projectID)

expName = raw_input("Enter your experiment name: \n")

# Experiment ID = Experiment name + slice name + time (time stamp use time.time())
expTime = str(time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time())))
expId = str(username) + "-" + str(expName) + "-" + expTime

print ("derived experiment ID: " + expId)

# Retrieve manifest rspec
print ("retrieving the manifest rspec...")

manifestName="manifest-"+ expId + ".rspec"
manifest_workdirectory = workdirectory + "/manifests/"

gimi_util.getRspec(slicename, manifest_workdirectory, manifestName)

# This creates an example iRODS object & creates the XML files & makes a ticket
if (initialized==True):
    newRods = iRODS.iRODS(workdirectory, proj_authority, 'proj_name', projectID, 'PI', 'proj_individual_authority', 'proj_individual_user', 'proj_date_time_type', 'proj_start', 'exp_authority', expName, expId, 'experimenter', exp_org, username, 'iso8601', expTime)
    # Make an initial ticket with slice expiraion time 
    sliceExpTime=gimi_util.getExpire(slicename)
    myTicket=newRods.makeTicket(expire_time=sliceExpTime)
    while True:
        pushManifestOption = raw_input("Do you want to push manifest to iRODS? (Yes or No) \n")
        if (pushManifestOption in ("Yes", "Y", "yes", "y")):
            # Push to iRODS
            newRods.pushManifest(manifest_workdirectory, slicename)
            break
        elif (pushManifestOption in ("No", "N", "no", "n")):
            break
        else:
            print ("Please answer Yes or No")
else:
    print "iRODS was never initialized. No data has been pushed to iRODS."


restInt = gimiREST.REST("emmy9.casa.umass.edu", "8013", workdirectory, expId)
