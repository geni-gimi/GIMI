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
import gimiRest_GET
import gimi_util
import omni
#import urllib
#import urllib2

# Set up working directory
print("Welcome to the GIMI initialization script, please make sure to install omni and set up your credential before running this script")
p = subprocess.Popen(['omni.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
omniOut, omniErrors = p.communicate()
if "ERROR:omni: Could not find an omni configuration file in local directory" in omniErrors:
    print omniErrors
    sys.exit(1)

while True:
    newExpOption = raw_input("Are you creating a new experiment? \n")
    if (newExpOption in ("Yes", "Y", "yes", "y")):
        break
    elif (newExpOption in ("No", "N", "no", "n")):
        workdirectory = raw_input("Enter your preferred experiment path (please use absolute path, e.g., /home/geni/your/dir): \n")        
        if (os.path.exists(workdirectory) == False):
            while True:
                createPathOption = raw_input("Path doesn't exist, do you want me to create directory for you? (Yes or No) \n")
                if (createPathOption in ("Yes", "Y", "yes", "y")):
                    try:
                        os.makedirs(workdirectory)
                        break
                    except:
                        print ("Was unable to make directory. Please try again after creating the directory")
                        sys.exit(1)
                elif (createPathOption in ("No", "N", "no", "n")):
                    print ("Please try again after creating the directory")
                    sys.exit(1)
                else: 
                    print ("Please answer Yes or No")
            
        print ("Updating existing experiment...")
        p = subprocess.Popen(['omni.py', 'listmyslices'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        listmyslicesOutput, listmyslicesErrors = p.communicate()
        # get username
        username = gimi_util.get_user(listmyslicesErrors)
        print username
        
        (returned_projectAuthority, returned_projectID, returned_slicename) = gimi_util.listmyslices_output_parse(listmyslicesErrors) 

        slicenames = '\n'.join(str(x) for x in returned_slicename)

        slicename = raw_input("Your active slice names:\n" + slicenames + "\nPlease enter your preferred slice name for this experiment: \n")
        
        while True:
            if slicename in returned_slicename:
                break
            else:
                slicename = raw_input("Please only enter the slice names listed above: \n")

        projectName = raw_input("Please enter your project name: \n")
        expList = gimiRest_GET.getExperiment("http://emmy9.casa.umass.edu", "8002", projectName)
        print("Your existing experiments: \n")
        print "\n".join(expList)
        expId = raw_input("Please enter the experiment ID you are updating: \n")
        #projectName = gimiRest_GET.getProject("http://emmy9.casa.umass.edu", "8002")
        
        initialized = gimi_util.callIinit()
        
        sliceExpTime=gimi_util.getExpire(slicename, projectName)
        myTicket=gimi_util.makeTicket(expId, expire_time=sliceExpTime)
        
        manifestName="manifest-"+ expId + ".rspec"
        expTime = str(time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time())))
        manifest_workdirectory = workdirectory + "/manifests-" + expTime
        os.makedirs(manifest_workdirectory)
        gimi_util.getRspec(slicename, projectName, manifest_workdirectory, manifestName)
        
        if (initialized==True):
            itkt_create_time = str(time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time())))
            sliceExpTime=gimi_util.getExpire(slicename, projectName)
            myTicket=gimi_util.makeTicket(expId, expire_time=sliceExpTime)
            while True:
                pushManifestOption = raw_input("Do you want to push the new manifest to iRODS? (Yes or No) \n")
                if (pushManifestOption in ("Yes", "Y", "yes", "y")):
                    # Push to iRODS
                    gimi_util.pushManifest(expId, manifest_workdirectory, slicename)
                    break
                elif (pushManifestOption in ("No", "N", "no", "n")):
                    break
                else:
                    print ("Please answer Yes or No")
        else:
            print "iRODS was never initialized. No data has been pushed to iRODS."
        sys.exit(1)
    else: 
        print ("Please answer Yes or No")


workdirectory = raw_input("Enter your preferred experiment path (please use absolute path, e.g., /home/geni/your/dir): \n")

if (os.path.exists(workdirectory) == False):
    while True:
        createPathOption = raw_input("Path doesn't exist, do you want me to create directory for you? (Yes or No) \n")
        if (createPathOption in ("Yes", "Y", "yes", "y")):
            try:
                os.makedirs(workdirectory)
                break
            except:
                print ("Was unable to make directory. Please try again after creating the directory")
                sys.exit(1)
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
            
print ("retrieving slice information...")

p = subprocess.Popen(['omni.py', 'listmyslices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
listmyslicesOutput, listmyslicesErrors = p.communicate()

# get username
username = gimi_util.get_user(listmyslicesErrors)
print ("Your user name is " + username + " \n")

(returned_projectAuthority, returned_projectID, returned_slicename) = gimi_util.listmyslices_output_parse(listmyslicesErrors) 

slicename = '\n'.join(str(x) for x in returned_slicename)

slicename = raw_input("Your active slice names:\n" + slicename + "\nPlease enter your preferred slice name for this experiment: \n")

while True:
    if slicename in returned_slicename:
        sliceurn = gimi_util.getSlices(slicename, listmyslicesErrors)
        print("SliceURN is: " + str(sliceurn) + "\n")
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

print ("Derived experiment ID: " + expId)

# Retrieve manifest rspec
print ("Retrieving the manifest rspec...")

manifestName="manifest-"+ expId + ".rspec"
manifest_workdirectory = workdirectory + "/manifests-" + expTime

os.makedirs(manifest_workdirectory)

gimi_util.getRspec(slicename, projectID, manifest_workdirectory, manifestName)

# This creates an example iRODS object & creates the XML files & makes a ticket
if (initialized==True):
    newRods = iRODS.iRODS(workdirectory, proj_authority, 'proj_name', projectID, 'PI', 'proj_individual_authority', 'proj_individual_user', 'proj_date_time_type', 'proj_start', 'exp_authority', expName, expId, 'experimenter', exp_org, username, 'iso8601', expTime)
    # Make an initial ticket with slice expiraion time 
    sliceExpTime = gimi_util.getExpire(slicename, projectID)
    itkt_create_time = str(time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time())))
    myTicket=gimi_util.makeTicket(expId, expire_time=sliceExpTime)
    while True:
        pushManifestOption = raw_input("Do you want to push manifest to iRODS? (Yes or No) \n")
        if (pushManifestOption in ("Yes", "Y", "yes", "y")):
            # Push to iRODS
            gimi_util.pushManifest(expId, manifest_workdirectory, slicename)
            break
        elif (pushManifestOption in ("No", "N", "no", "n")):
            break
        else:
            print ("Please answer Yes or No")
else:
    print "iRODS was never initialized. No data has been pushed to iRODS."
    
print ("Pushing experiment information to GIMI Experiment Registry...")

manifest = manifestName + ".xml"

irodsHome = gimi_util.ienvParse()

irods_path = irodsHome + "/manifests-" + expTime
restInt = gimiREST.REST("http://emmy9.casa.umass.edu", "8002", workdirectory, username, projectID, expId, myTicket, irods_path, itkt_create_time, sliceExpTime, slicename, manifest)
