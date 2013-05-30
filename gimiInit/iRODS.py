#!/usr/bin/python

import sys
import subprocess
import simpleProject
import simpleExperiment
import simpleStep
import simpleArtifact

# Things I need to write XML files:
# -Experiment id
# -Experiment name, 
# -Experimenter name & organization
# -Slicename

# Assumptions: 
# -iinit has been called and was successful
# -exp_id is unique for the user
# 
class iRODS:
   # This creates the iRODS experiment directory with initial XML files 
   # and returns a ticket for read/write access to the directory
   def __init__(self, exp_id, exp_title, exp_first_name, exp_last_name, exp_org, slice_name):
      #set variables
      self.proj_id = "Project ID"
      self.proj_title = "Project title"
      self.PI_first_name = "PI firstName"
      self.PI_last_name = "PI lastName"
      self.PI_org = "PI organization"
      self.exp_id = exp_id+""
      self.exp_title = exp_title
      self.exp_first_name = exp_first_name
      self.exp_last_name = exp_last_name
      self.exp_org = exp_org
      self.step_name = "Step title" 
      self.step_seq_id = "First"
      self.resource_id = "1234567"
      self.slice_name = slice_name
      self.artifact_name = "Filename"
      #write XML files
      self.makeFiles()
      #create directories and include initial XML files
      self.makeDirectories()
      print 'iRODS setup was successful\n'
      #make an initial ticket
      myTicket=self.makeTicket()
      print "Ticket for new directory: " + myTicket
      

   # Builds XML files and writes them to files
   def makeFiles(self):
      # makes project XML file
      newProject = simpleProject.Project(self.proj_id, self.proj_title, self.PI_first_name, self.PI_last_name, self.PI_org)
      newProject.makeXML()
      # makes experiment XML file
      newExperiment = simpleExperiment.Experiment(self.exp_id, self.exp_title, self.exp_first_name, self.exp_last_name, self.exp_org)
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
    

   # Creates tickets for the experiment directory
   def makeTicket(self):
      ticket = subprocess.check_output(['iticket', 'create', 'write', self.exp_id])
      ticket = ticket.replace("ticket:","")
      ticket = ticket.replace("\n","")
      return ticket
      


# This creates an example iRODS object & creates the XML files & makes a ticket
newiRODS = iRODS('exp_id14', 'exp_title', 'exp_first_name', 'exp_last_name', 'exp_org', "slice_name")

