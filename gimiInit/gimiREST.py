import json
import sys
import os
import uuid

class REST:
    def __init__(self, restURL, restPort, workdirectory, user_name, proj_name, exp_name, itkt_token, irods_path, itkt_create, itkt_valid, slice_name, manifest):
        self.restURL = restURL
        self.restPort = restPort
        self.workdirectory = workdirectory
        self.proj_name = proj_name
        self.user_name = user_name
        self.exp_name = exp_name
        self.itkt_token = itkt_token
        self.irods_path = irods_path
        self.itkt_create = itkt_create
        self.itkt_valid = itkt_valid
        self.slice_name = slice_name
        self.manifest = manifest

        self.postProject()
        self.postUser()
        self.postExperiment()
        self.postSlice()
        print("Values:" + user_name + ' ' + proj_name + ' ' +  exp_name + ' ' + itkt_token + ' ' + irods_path + ' ' + slice_name + ' ' )
        print('Pushed data to registry successfully\n')

    def postProject(self):
        UUID = uuid.uuid3(uuid.NAMESPACE_DNS, self.proj_name)
        data = [{'name': self.proj_name, 'uuid': str(UUID)}]
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
        #data=json.dumps(data)
        json_filename = self.workdirectory + "/proj.json"
        print ("Saving JSON to file: " + json_filename)
        jsonf = open(json_filename,'w')
        data = json.dumps(data)
        jsonf.write(data)
        jsonf.close()
        
        os.system('curl -X POST -H "Content-Type: application/json" --data-binary @'+ json_filename +' ' + self.restURL + ':' + str(self.restPort) + '/projects')

    def postExperiment(self):
        UUID = uuid.uuid3(uuid.NAMESPACE_DNS, self.exp_name)
        data = [{'name': self.exp_name,'uuid': str(UUID), 'iticket' :{'token': self.itkt_token, 'path': self.irods_path, 'created_at': self.itkt_create, 'valid_until': self.itkt_valid}}]
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
        #data=json.dumps(data)
        json_filename = self.workdirectory + "/experiment.json"
        print ("Saving JSON to file: " + json_filename)
        jsonf = open(json_filename,'w')
        data = json.dumps(data)
        jsonf.write(data)
        jsonf.close()
        
        os.system('curl -X POST -H "Content-Type: application/json" --data-binary @'+ json_filename +' ' + self.restURL + ':' + str(self.restPort) + '/projects/' + self.proj_name + '/experiments')
   
    def postSlice(self):
        UUID = uuid.uuid3(uuid.NAMESPACE_DNS, self.slice_name)
        data = [{'name': self.slice_name,'uuid': str(UUID), 'urn': self.slice_name,'manifest': self.manifest}]
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
        #data=json.dumps(data)
        json_filename = self.workdirectory + "/slice.json"
        print ("Saving JSON to file: " + json_filename)
        jsonf = open(json_filename,'w')
        data = json.dumps(data)
        jsonf.write(data)
        jsonf.close()
        
        os.system('curl -X POST -H "Content-Type: application/json" --data-binary @'+ json_filename +' ' + self.restURL + ':' + str(self.restPort) + '/projects/' + self.proj_name + '/experiments/' + self.exp_name + '/slices')

    def postUser(self):
        x="geni-" + self.user_name
        UUID = uuid.uuid3(uuid.NAMESPACE_DNS, x)
        data = [{'name': "geni-" + self.user_name, 'uuid': str(UUID)}]
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        #data=json.dumps(data)
        json_filename = self.workdirectory + "/user.json"
        print ("Saving JSON to file: " + json_filename)
        jsonf = open(json_filename,'w')
        data = json.dumps(data)
        jsonf.write(data)
        jsonf.close()

        os.system('curl -X POST -H "Content-Type: application/json" --data-binary @'+ json_filename +' ' + self.restURL + ':' + str(self.restPort) + '/projects/' + self.proj_name + '/users')

