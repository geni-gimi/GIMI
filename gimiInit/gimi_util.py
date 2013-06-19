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


import time

printtoscreen=1
dontprinttoscreen=0
debug = 0


def isRoot(username):
    if(username == 'root'):
        return True
    else:
        return False
    
def write_to_log(message,print_also):

    global LOGFILE_HANDLE
    global debug

    if (print_also or debug):
        print message+"\n"
    log_date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    LOGFILE_HANDLE.write(log_date +" :\t"+ message+"\n")

    return

def get_user(theOutput):
    indexOfUser=theOutput.find("User ")
    userInfo=theOutput[indexOfUser:]
    gettingUser=userInfo.split('\'')
    user=gettingUser[1]          ## user is your username
    return user

def listmyslices_output_parse(theOutput):
    moreSlices=True
    rev_slices=[]
    projects = []
    while(moreSlices==True):

        indexOfURN=theOutput.find('urn:')
        theOutput=theOutput[indexOfURN:]
        indexOfLineEnd=theOutput[2:].find('urn:')
        if indexOfLineEnd==-1:
            moreSlices=False
            indexOfLineEnd=theOutput[1:].find('INFO:omni')
        urnInfo=theOutput[:indexOfLineEnd]

        info=urnInfo.split(":")
        x=info[3].split('+')
        
        projectID=x[0]             ## project is the name of your project
        slicename=x[2]           ## slicename is the name of your slice
        rev_slices.append(slicename)
        projects.append(projectID)
        theOutput=theOutput[indexOfLineEnd-1:]
    slices = rev_slices[::-1]
    return projects, slices

def getRspecs(output):
    theOutput=output
    indexOfRspec=0
    rspecs=[]
    while(True):
        indexOfRspec=theOutput.find('<rspec')
        if indexOfRspec==-1:
            break
        theOutput=theOutput[indexOfRspec:]
        indexOfEnd=theOutput.find('</rspec>')
        oneRspec=theOutput[:indexOfEnd+8]
        rspecs.append(oneRspec)
        theOutput=theOutput[indexOfEnd:]
    return rspecs