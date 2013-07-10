#!/usr/bin/python

import sys, os
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
    def __init__(self, work_directory, proj_authority, proj_name, proj_id, proj_individual_type, proj_individual_authority, proj_individual_user, proj_date_time_type, proj_start, exp_authority, exp_name, exp_id, exp_individual_type, exp_individual_authority, exp_individual_user, exp_date_time_type, exp_start):
        #set variables
        # project variables
        self.proj_authority = proj_authority
        self.proj_name = proj_name
        self.proj_id = proj_id
        self.proj_individual_type = proj_individual_type
        self.proj_individual_authority = proj_individual_authority
        self.proj_individual_user = proj_individual_user
        self.proj_date_time_type = proj_date_time_type
        self.proj_start = proj_start
        # experiment variables
        self.exp_authority = exp_authority
        self.exp_name = exp_name
        self.exp_id = exp_id
        self.exp_individual_type = exp_individual_type
        self.exp_individual_authority = exp_individual_authority
        self.exp_individual_user= exp_individual_user
        self.exp_date_time_type = exp_date_time_type
        self.exp_start = exp_start
        self.work_directory = work_directory

        # write XML files
        self.makeProjAndExpFiles()

        # create directories and include initial XML files
        self.makeExpDirectory()
        self.pushOMFs()
        print 'iRODS intial collection setup was successful\n'


    # Builds Porject & Experiment XML files and writes them to files
    def makeProjAndExpFiles(self):
        # makes project XML file
        newProject = simpleProject.Project(self.proj_authority, self.proj_name, self.proj_id, self.proj_individual_type, self.proj_individual_authority, self.proj_individual_user, self.proj_date_time_type, self.proj_start)
        newProject.makeXML(self.work_directory)
        # makes experiment XML file
        newExperiment = simpleExperiment.Experiment(self.exp_authority, self.exp_name, self.exp_id, self.exp_individual_type, self.exp_individual_authority, self.exp_individual_user, self.exp_date_time_type, self.exp_start)
        newExperiment.makeXML(self.work_directory)


    # Creates directory within iRODS for this experiment and put XML files into iRODS
    def makeExpDirectory(self):
        subprocess.check_output(['icd'])
        #make experiment directory
        subprocess.check_output(['imkdir', self.exp_id])  
        subprocess.check_output(['icd', self.exp_id])
        #add xml files to directory
        subprocess.check_output(['iput', self.work_directory+'/project.xml'])
        subprocess.check_output(['iput', self.work_directory+'/experiment.xml'])
        subprocess.check_output(['icd'])



    # Puts intial OMF scripts into iRODS
    def pushOMFs(self):
        subprocess.check_output(['icd'])
        # check if experimentTemplates directory already exists
        try:
            subprocess.check_output(['icd', 'experimentTemplates'])
            print "OMF template scripts already exist in iRODS\n"
            subprocess.check_output(['icd'])
        # if experimentTemplates directory does not exist
        except:
            #copy OMF scripts from gimiadmin to user directory
            subprocess.check_output(['icp', '-r', '/geniRenci/home/gimiadmin/experimentTemplates', 'experimentTemplates'])
            subprocess.check_output(['ichmod', '-r', 'write', 'public', 'experimentTemplates'])
            subprocess.check_output(['icd'])
            print "OMF template scripts have been pushed to iRODS\n"



#### TEST CODE ####

# This creates an example iRODS object & creates the XML files
#newExp = iRODS('/home/koneil/iRODSstuff/tmp', "Project Authority", "My Project", 'proj_id', 'PI', 'Her authority', 'geni_user', 'iso8601', '2013-06-05T09:30:01Z', 'exp_authority', 'myProject2', 'testExperiment', 'experimenter', 'individual_authority', 'geni_user', 'iso8601', '2013-06-05T09:30:01Z')
#To Push manifest
#newExp.pushManifest('/home/koneil/iRODSstuff/manifests','my_slice')


#make initial tickets
#myTicket=newExp.makeTicket(['koneil2','koneil3'])
#myTicket=newExp.makeTicket(expire_time='1372654800')
#myTicket=newExp.makeTicket()




