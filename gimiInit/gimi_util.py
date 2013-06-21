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
import pexpect
import getpass

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
    user=gettingUser[1]           ## user is your username
    return user

def listmyslices_output_parse(theOutput):
    moreSlices=True
    rev_slices=[]
    projects = []
    authorities = []
    while(moreSlices==True):
        indexOfURN=theOutput.find('urn:')
        theOutput=theOutput[indexOfURN:]
        indexOfLineEnd=theOutput[2:].find('urn:')
        if indexOfLineEnd==-1:
            moreSlices=False
            indexOfLineEnd=theOutput[1:].find('INFO:omni')
        urnInfo=theOutput[:indexOfLineEnd]

        info=urnInfo.split(":")
        auth=info[2].split('+')
        proj_authority=auth[1]
        x=info[3].split('+')
        
        projectID=x[0]            ## project is the name of your project
        slicename=x[2]            ## slicename is the name of your slice
        rev_slices.append(slicename)
        projects.append(projectID)
        authorities.append(proj_authority)
        theOutput=theOutput[indexOfLineEnd-1:]
    slices = rev_slices[::-1]
    return authorities, projects, slices

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

# Initializes iRODS
def callIinit():
    #checks if iRODS is already intialized
    try:
        p=pexpect.spawn('ils')
    #returns False if iRODS isn't installed 
    #or there is no path to the icommands
    except: 
        print "ERROR: unable to access iRODS icommands"
        return False
    j=p.expect(['USER_RODS_HOST_EMPTY', pexpect.EOF])
    #returns True if user has already intialized iRODS
    if j==1:
        print "iRODS already initialized"
        return True
    p=pexpect.spawn('iinit')
    i=p.expect(['Enter your current iRODS password:','.*One or more fields in your iRODS.*', pexpect.TIMEOUT])
    #returns false if the call to iinit timesout
    if i==2:
        print 'ERROR!'
        print 'iRODS could not login. Here is what iRODS said:'
        print child.before, child.after
        return False
    #gives user setup information to iRODS
    if i==1:
        hostname = raw_input("Hostname of server:")
        p.sendline(hostname)
        p.expect(['Enter the port number:'])
        port = raw_input("Port number:")
        p.sendline(port)
        p.expect(['Enter your irods user name:'])
        username = raw_input("iRODS username:")
        p.sendline(username)
        p.expect(['Enter your irods zone:'])
        zone = raw_input("iRODS zone:")
        p.sendline(zone)
        p.expect(['Those values will.*'])
    #passes password to iRODS
    password = getpass.getpass('iRODS Password: ')
    p.sendline(password)
    #checks for errors 
    i=p.expect(['CAT_INVALID_AUTHENTICATION', 'USER_RODS_HOSTNAME_ERR', 'USER_SOCK_CONNECT_ERR', 'SYS_AGENT_INIT_ERR', pexpect.EOF])
    if i==0:
        print "Your password was incorrect."
        again = raw_input("Would you like to try again?(Yes or No)")
        if (again in ("Yes", "Y", "yes", "y")):
            return callIinit()
        elif (again in ("No", "N", "no", "n")):
            return False
        else:
            print ("Please answer Yes or No")
    elif i==1:
        print "Your hostname was incorrect."
        again = raw_input("Would you like to try again?(Yes or No)")
        if (again in ("Yes", "Y", "yes", "y")):
            return callIinit()
        elif (again in ("No", "N", "no", "n")):
            return False
        else:
            print ("Please answer Yes or No")
    elif i==2:
        print "Your port number was incorrect or the server is down."
        again = raw_input("Would you like to try again?(Yes or No)")
        if (again in ("Yes", "Y", "yes", "y")):
            return callIinit()
        elif (again in ("No", "N", "no", "n")):
            return False
        else:
            print ("Please answer Yes or No")
    elif i==3:
        print "Your username, zone, or password was incorrect."
        again = raw_input("Would you like to try again?(Yes or No)")
        if (again in ("Yes", "Y", "yes", "y")):
            return callIinit()
        elif (again in ("No", "N", "no", "n")):
            return False
        else:
            print ("Please answer Yes or No")
    else:
        print "iRODS login was successful"
        return True

