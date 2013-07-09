import json
import sys
import os
import urllib2
class REST:
    def getProject(self, restURL, restPort):
        print('retrieving projects...')
        jsonurl = urllib2.urlopen(self.restURL + ':' + self.restPort + '/projects')
        decoded_json = json.load(jsonurl)
        name = []
        projects = decoded_json['projects']
        for i in range(len(projects)):
            dict = projects[i]
            name.append(str(dict['name']))
        return name


    def getExperiment(self,restURL, restPort, proj_name):
        print('retrieving experiments...')
        jsonurl = urllib2.urlopen(self.restURL + ':' + self.restPort + '/projects/' + self.proj_name + '/experiments')
        decoded_json = json.load(jsonurl)
        name = []
        experiments = decoded_json['experiments']
        for i in range(len(experiments)):
            dict = experiments[i]
            name.append(str(dict['name']))
        return name
   
    def getSlice(self, restURL, restPort, proj_name, exp_name):
        print('retrieving slices...')
        jsonurl = urllib2.urlopen(self.restURL + ':' + self.restPort + '/projects/' + self.proj_name + '/experiments/' + self.exp_name + '/slices')
        decoded_json = json.load(jsonurl)
        name = []
        experiments = decoded_json['experiments']
        for i in range(len(experiments)):
            dict = experiments[i]
            name.append(str(dict['name']))
        return name

    def postUser(self, restURL, restPort, proj_name):
        print('retrieving users...')
        jsonurl = urllib2.urlopen(self.restURL + ':' + self.restPort + '/projects/' + self.proj_name + '/users')
        decoded_json = json.load(jsonurl)
        name = []
        users = decoded_json['users']
        for i in range(len(users)):
            dict = users[i]
            name.append(str(dict['name']))
        return name

