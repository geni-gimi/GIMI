#!/usr/bin/python

import sys
import subprocess
import simpleProject
import simpleExperiment
import simpleStep
import simpleArtifact

# Assumptions: 
# -iinit has been called and was successful
# -exp_id is unique for the user
# 
class iRODS:
    # This creates the iRODS experiment directory with initial XML files 
    def __init__(self, proj_id, proj_title, PI_first_name, PI_last_name, PI_org, exp_id, exp_title, exp_first_name, exp_last_name, exp_org, exp_start, exp_end, step_name, step_seq_id, resource_id, slice_name, artifact_name):
        #set variables
        self.proj_id = proj_id
        self.proj_title = proj_title
        self.PI_first_name = PI_first_name
        self.PI_last_name = PI_last_name
        self.PI_org = PI_org
        self.exp_id = exp_id
        self.exp_title = exp_title
        self.exp_first_name = exp_first_name
        self.exp_last_name = exp_last_name
        self.exp_org = exp_org
        self.exp_start = exp_start
        self.exp_end = exp_end
        self.step_name = step_name 
        self.step_seq_id = step_seq_id
        self.resource_id = resource_id
        self.slice_name = slice_name
        self.artifact_name = artifact_name
        #write XML files
        self.makeFiles()
        #create directories and include initial XML files
        self.makeDirectories()
        print 'iRODS setup was successful\n'
             

    # Builds XML files and writes them to files
    def makeFiles(self):
        # makes project XML file
        newProject = simpleProject.Project(self.proj_id, self.proj_title, self.PI_first_name, self.PI_last_name, self.PI_org)
        newProject.makeXML()
        # makes experiment XML file
        newExperiment = simpleExperiment.Experiment(self.exp_id, self.exp_title, self.exp_first_name, self.exp_last_name, self.exp_org, self.exp_start, self.exp_end)
        newExperiment.makeXML()
        # makes step XML file
        newStep = simpleStep.Step(self.step_seq_id, self.step_name, self.resource_id, self.slice_name)
        newStep.makeXML()
        # makes artifact XML file
        newArtifact = simpleArtifact.Artifact(self.artifact_name)
        newArtifact.makeXML()


    # Creates all directories within iRODS for this experiment and put XML files into iRODS
    def makeDirectories(self):
        subprocess.check_output(['icd'])
        #make experiment directory
        subprocess.check_output(['imkdir', self.exp_id])  
        subprocess.check_output(['icd', self.exp_id])
        #add xml files to directory
        subprocess.check_output(['iput', 'project.xml'])
        subprocess.check_output(['iput', 'experiment.xml'])
        subprocess.check_output(['iput', 'step.xml'])
        subprocess.check_output(['imkdir', 'artifact'])
        #make artifact directory within the experiment directory
        subprocess.check_output(['icd', 'artifact'])
        subprocess.check_output(['iput', 'artifact.xml'])
        subprocess.check_output(['icd'])
      
########## TICKETS ##########

    # Creates tickets for the experiment directory
#    def makeTicket(self):
#        subprocess.check_output(['icd'])
#        ticket = subprocess.check_output(['iticket', 'create', 'write', self.exp_id])
#        ticket = ticket.replace("ticket:","")
#        ticket = ticket.replace("\n","")
#        return ticket  
 ##########   NEW CODE    #########     
    # Creates tickets for the experiment directory taking in user restrictions & an expiration time
    def makeTicket(self, users=None, expire_time=0):
        ticket = subprocess.check_output(['iticket', 'create', 'write', self.exp_id])
        ticket = ticket.replace("ticket:","")
        ticket = ticket.replace("\n","")
        if users is None:
            users=[]
        for x in users:
            subprocess.check_output(['iticket', 'mod', ticket, 'add', 'user', x])
        if expire_time != 0:
            subprocess.check_output(['iticket', 'mod', ticket, 'expire', expire_time])
        print "Ticket for new directory: " + ticket
        return ticket 

    # Postpones the time at which the iticket expires
    # expire_time must be UNIX timestamp
    def extendTicket(self, ticket, expire_time=0):
        if expire_time != 0:
            subprocess.check_output(['iticket', 'mod', ticket, 'expire', expire_time])
            print "Expiration date is now set to" + expire_time
        return ticket 
  ####################################

    # Puts manifest into iRODS
    def pushManifest(self, manifest):
        subprocess.check_output(['icd', self.exp_id])
        subprocess.check_output(['iput', manifest])
        #newArtifact = simpleArtifact.Artifact(manifest)
        #newArtifact.makeXML()
        #subprocess.check_output(['iput', 'artifact.xml'])
        print "Manifest has been pushed to iRODS"


#    def pushOMlScripts(self, OML):
#        subprocess.check_output(['icd', self.exp_id])
#        for x in OML:
#            subprocess.check_output(['iput', OML])
            #newArtifact = simpleArtifact.Artifact(manifest)
            #newArtifact.makeXML()
            #subprocess.check_output(['iput', 'artifact.xml'])
#        print "OML scripts have been pushed to iRODS"
        


#### SAMPLE CODE ####

## This creates an example iRODS object & creates the XML files & makes a ticket
#newExp = iRODS('proj_id', 'proj_title', 'PI_first_name', 'PI_last_name', 'PI_org', 'exp_id24', 'exp_title', 'exp_first_name', 'exp_last_name', 'exp_org', 'exp_start', 'exp_end', 'step_name', 'step_seq_id', 'resource_id', 'slice_name', 'artifact_name')

#make an initial tickets
#myTicket=newExp.makeTicket(['koneil2','koneil3'])
#myTicket=newExp.makeTicket(expire_time='1372654800')
#myTicket=newExp.makeTicket()

##To Push manifest
#newExp.pushManifest('TwoVMs')


