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


########## ARTIFACTS ##########

    # Adds a new artifact with descriptor files to this experiment directory
    def addArtifact(self, artifact, artifactLocation, prime_function, resource_type, resource_id, art_type_prime, interpretation_read_me, directory_name=None):
        self.makeArtAndStepFiles(prime_function, resource_type, resource_id, art_type_prime, interpretation_read_me)
        self.makeArtifactDirectory(artifact,artifactLocation, directory_name)

    # Adds a new artifact to a specified arifact directory
    def addAnotherArtifact(self, artifact, artifactLocation, directory_name):
        subprocess.check_output(['icd'])
        subprocess.check_output(['icd', directory_name])
        subprocess.check_output(['iput', artifactLocation+'/'+artifact, '-r'])
        subprocess.check_output(['icd'])
        

    # Builds Artifact & Step XML files and writes them to files
    def makeArtAndStepFiles(self,prime_function, resource_type, resource_id, art_type_prime, interpretation_read_me):
        # makes step XML file
        newStep = simpleStep.Step(prime_function, resource_type, resource_id)
        newStep.makeXML(self.work_directory)
        # makes artifact XML file
        newArtifact = simpleArtifact.Artifact(art_type_prime, interpretation_read_me)
        newArtifact.makeXML(self.work_directory)

    # Creates all directories within iRODS for this experiment and put XML files into iRODS
    def makeArtifactDirectory(self, artifact, artifactLocation, directory_name):
        subprocess.check_output(['icd'])
        subprocess.check_output(['icd', self.exp_id])
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
        subprocess.check_output(['iput', self.work_directory+'/step.xml'])
        subprocess.check_output(['iput', self.work_directory+'/artifact.xml'])
        subprocess.check_output(['icd'])

    
    # Puts contents of manifest directory into iRODS
    def pushManifest(self, manifestLocation, slicename):
        directory_name='manifest_rspec'
        os.chdir(manifestLocation)
        #saves contents of manifestLocation directory folder as string
        files=subprocess.check_output(['ls'])
        #saves file names from manifestLocation into array
        manifests=files.split('\n')
        subprocess.check_output(['icd'])
        #adds first manifest rspec and creates descriptor files
        self.addArtifact(manifests[0], manifestLocation, 'obtain_resources', 'slice', slicename, 'GENI_AM_API_sliver_manifest_rspec', 'interpretation_read_me', directory_name)
        manifests=manifests[1:-1]
        #adds remaining manifest rspecs
        for rspec in manifests:
            self.addAnotherArtifact(rspec, manifestLocation, self.exp_id+"/"+directory_name+"-1")
        print "Manifest has been pushed to iRODS\n"


    # Puts intial OMF scripts into iRODS
    def pushOMFs(self):
        subprocess.check_output(['icd'])
        # check if experimentTemplates directory already exists
        try:
            print 'turtle'
            subprocess.check_output(['icd', 'experimentTemplates'])
            print "OMF template scripts already exist in iRODS\n"
            subprocess.check_output(['icd'])
        # if experimentTemplates directory does not exist
        except:
            #copy OMF scripts from gimiadmin to user directory
            subprocess.check_output(['icp', '-r', '/geniRenci/home/gimiadmin/experimentTemplates', 'experimentTemplates'])
            subprocess.check_output(['icd'])
            print "OMF template scripts have been pushed to iRODS\n"

      
########## TICKETS ##########
    
    # Creates tickets for the experiment directory taking in user restrictions & an expiration time
    def makeTicket(self, users=None, expire_time=0):
        ticket = subprocess.check_output(['iticket', 'create', 'write', self.exp_id])
        ticket = ticket.replace("ticket:","")
        ticket = ticket.replace("\n","")
        print "Ticket for new directory: " + ticket
        # Restricts users
        if users is None:
            users=[]
        for x in users:
            subprocess.check_output(['iticket', 'mod', ticket, 'add', 'user', x])
        # Sets expiration time
        if expire_time != 0:
            self.extendTicket(ticket, expire_time)
        return ticket 

    # Postpones the time at which the iticket expires.
    # expire_time must be UNIX timestamp
    def extendTicket(self, ticket, expire_time):
        subprocess.check_output(['iticket', 'mod', ticket, 'expire', expire_time])
        print "Ticket expiration date is set to: " + expire_time
        return ticket

    # Adds user to list of users with access to ticket
    def addTicketUser (self, ticket, user):
        subprocess.check_output(['iticket', 'mod', ticket, 'add', 'user', user])
        print "Ticket access granted to: " + user
        return ticket
  ####################################
        


#### TEST CODE ####

# This creates an example iRODS object & creates the XML files
#newExp = iRODS('/home/koneil/iRODSstuff/tmp', "Project Authority", "My Project", 'proj_id', 'PI', 'Her authority', 'geni_user', 'iso8601', '2013-06-05T09:30:01Z', 'exp_authority', 'myProject2', 'myExperiment', 'experimenter', 'individual_authority', 'geni_user', 'iso8601', '2013-06-05T09:30:01Z')
#To Push manifest
#newExp.pushManifest('/home/koneil/iRODSstuff/manifests','my_slice')
#newExp.pushOMFs()

#make initial tickets
#myTicket=newExp.makeTicket(['koneil2','koneil3'])
#myTicket=newExp.makeTicket(expire_time='1372654800')
#myTicket=newExp.makeTicket()




