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
import subprocess
import omni
import os
import simpleStep
import simpleArtifact

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
    slices=[]
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
        slices.append(slicename)
        projects.append(projectID)
        authorities.append(proj_authority)
        theOutput=theOutput[indexOfLineEnd-1:]
#    slices = rev_slices[::-1]
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
        print p.before, p.after
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

#get expiration date & time for specified slice  
def getExpire(slicename, project):
    p= subprocess.Popen(['omni.py', 'print_slice_expiration', slicename, '-r', project], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    slice_expirationOutput, slice_expirationErrors = p.communicate()
    output=slice_expirationErrors
    indexOfExpire=output.find('expires on')
    if indexOfExpire!=-1:
        expireDate=output[indexOfExpire+11:indexOfExpire+21]
        expireTime=output[indexOfExpire+22:indexOfExpire+30]
    else:
        indexOfExpire=output.find('expires within 1 day on')
        expireDate=output[indexOfExpire+24:indexOfExpire+34]
        expireTime=output[indexOfExpire+35:indexOfExpire+44]
    expiration=expireDate+'.'+expireTime
    return expiration

def getRspec(slicename, project, manifest_workdirectory, manifestName):
    print "Checking resources from aggregates... (this might take some time)"
    aggregates = ['https://pgeni.gpolab.bbn.com:12369/protogeni/xmlrpc/am/2.0', 'https://www.emulab.net:12369/protogeni/xmlrpc/am/2.0', 'https://www.uky.emulab.net:12369/protogeni/xmlrpc/am/2.0', 'https://bbn-hn.exogeni.net:11443/orca/xmlrpc', 'https://rci-hn.exogeni.net:11443/orca/xmlrpc', 'https://geni.renci.org:11443/orca/xmlrpc', 'https://boss.utah.geniracks.net:12369/protogeni/xmlrpc/am/2.0', 'https://boss.instageni.gpolab.bbn.com:12369/protogeni/xmlrpc/am/2.0', 'https://boss.lan.sdn.uky.edu:12369/protogeni/xmlrpc/am/2.0', 'https://geni.kettering.edu:12369/protogeni/xmlrpc/am', 'https://instageni.northwestern.edu:12369/protogeni/xmlrpc/am']
    for am in aggregates:
        bigString = "--outputfile=" + manifest_workdirectory + "/" + am + "-" + manifestName

        checkOutput = subprocess.Popen(['omni.py', 'listresources', slicename, '-r', project, '-a', am], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        checkOut, checkErrors = checkOutput.communicate()
        if "No resource listing returned" in checkErrors:
            continue
        else:
            p= subprocess.Popen(['omni.py', 'listresources', slicename, '-r', project, '-a', am, '-o', bigString], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, errors = p.communicate()
            print ("Found resource in aggregate: " + am + ", manifest stored as " + manifest_workdirectory + "/" + am + "-" + manifestName)


#Check iRODS environment settings
def ienvParse():
    ienvOut = subprocess.check_output(['ienv'])
    for item in ienvOut.split("\n"):
        if "irodsHome=" in item:
            ienvOutLine = item.strip()

    indexOfIrodsHome = ienvOutLine.find("irodsHome")
    irodsHomeInfo = ienvOutLine[indexOfIrodsHome:]
    gettingIrodsHome = irodsHomeInfo.split('=')
    irodsHome = gettingIrodsHome[1]
    
    return irodsHome



############ iRODS.py stuff ###############

########## ARTIFACTS ##########

# Adds a new artifact with descriptor files to this experiment directory
def addArtifact(exp_id, artifact, artifactLocation, prime_function, resource_type, resource_id, art_type_prime, interpretation_read_me, directory_name=None):
    makeArtAndStepFiles(artifactLocation, prime_function, resource_type, resource_id, art_type_prime, interpretation_read_me)
    makeArtifactDirectory(exp_id, artifact,artifactLocation, directory_name)

# Adds a new artifact to a specified arifact directory
def addAnotherArtifact(artifact, artifactLocation, directory_name):
    subprocess.check_output(['icd'])
    subprocess.check_output(['icd', directory_name])
    subprocess.check_output(['iput', artifactLocation+'/'+artifact, '-r'])
    subprocess.check_output(['icd'])
        

# Builds Artifact & Step XML files and writes them to files
def makeArtAndStepFiles(artifactLocation, prime_function, resource_type, resource_id, art_type_prime, interpretation_read_me):
    # makes step XML file
    newStep = simpleStep.Step(prime_function, resource_type, resource_id)
    newStep.makeXML(artifactLocation)
    # makes artifact XML file
    newArtifact = simpleArtifact.Artifact(art_type_prime, interpretation_read_me)
    newArtifact.makeXML(artifactLocation)

# Creates all directories within iRODS for this experiment and put XML files into iRODS
def makeArtifactDirectory(exp_id, artifact, artifactLocation, directory_name):
    subprocess.check_output(['icd'])
    subprocess.check_output(['icd', exp_id])
    # name directory uniquely
    if directory_name==None:
        directory_name = artifact
    run=1
    directory_name_run = directory_name+'-'+str(run)
    newDirectory=False
    while newDirectory==False :
        try:
            subprocess.check_output(['imkdir', directory_name_run])
            newDirectory=True
            break
        except:
            run+=1
            directory_name_run = directory_name+'-'+str(run)
    subprocess.check_output(['icd', directory_name_run])
    #add artifact & xml files to directory
    subprocess.check_output(['iput', artifactLocation+'/'+artifact, '-r'])
    subprocess.check_output(['iput', artifactLocation+'/step.xml'])
    subprocess.check_output(['iput', artifactLocation+'/artifact.xml'])
    subprocess.check_output(['icd'])

    
# Puts contents of manifest directory into iRODS
def pushManifest(exp_id, manifestLocation, slicename):
    directory_name='manifest_rspec'
    os.chdir(manifestLocation)
    #manifestLocation=manifestLocation[:-1]
    #saves contents of manifestLocation directory folder as string
    files=subprocess.check_output(['ls'])
    #saves file names from manifestLocation into array
    manifests=files.split('\n')
    subprocess.check_output(['icd'])
    if manifests==['']:
        print "WARNING: No manifest rspecs were found."
        return
    #adds first manifest rspec and creates descriptor files
    addArtifact(exp_id, manifests[0], manifestLocation, 'obtain_resources', 'slice', slicename, 'GENI_AM_API_sliver_manifest_rspec', 'interpretation_read_me', directory_name)
    manifests=manifests[1:-1]
    #adds remaining manifest rspecs
    for rspec in manifests:
        addAnotherArtifact(rspec, manifestLocation, exp_id+"/"+directory_name+"-1")
    print "Manifest has been pushed to iRODS\n"



########## TICKETS ##########
    
# Creates tickets for the experiment directory taking in user restrictions & an expiration time
def makeTicket(exp_id, users=None, expire_time=0):
    ticket = subprocess.check_output(['iticket', 'create', 'write', exp_id])
    ticket = ticket.replace("ticket:","")
    ticket = ticket.replace("\n","")
    print "Ticket for new directory: " + ticket
    subprocess.check_output(['iticket', 'mod', ticket, 'write-files', '0'])
    # Restricts users
    if users is None:
        users=[]
    for x in users:
        subprocess.check_output(['iticket', 'mod', ticket, 'add', 'user', x])
    # Sets expiration time
    if expire_time != 0:
        extendTicket(ticket, expire_time)
    return ticket 

# Postpones the time at which the iticket expires.
# expire_time must be UNIX timestamp
def extendTicket(ticket, expire_time):
    subprocess.check_output(['iticket', 'mod', ticket, 'expire', expire_time])
    print "Ticket expiration date is set to: " + expire_time
    return ticket

# Adds user to list of users with access to ticket
def addTicketUser (ticket, user):
    subprocess.check_output(['iticket', 'mod', ticket, 'add', 'user', user])
    print "Ticket access granted to: " + user
    return ticket
####################################


