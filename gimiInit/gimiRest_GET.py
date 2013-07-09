import json
import urllib2

def getProject(restURL, restPort):
    print('retrieving projects...')
    jsonurl = urllib2.urlopen(restURL + ':' + restPort + '/projects')
    decoded_json = json.load(jsonurl)
    projectName = []
    projects = decoded_json['projects']
    for i in range(len(projects)):
        dicti = projects[i]
        projectName.append(str(dicti['name']))
    return projectName


def getExperiment(restURL, restPort, proj_name):
    print('retrieving experiments...')
    jsonurl = urllib2.urlopen(restURL + ':' + restPort + '/projects/' + proj_name + '/experiments')
    decoded_json = json.load(jsonurl)
    expName = []
    experiments = decoded_json['experiments']
    for i in range(len(experiments)):
        dicti = experiments[i]
        expName.append(str(dicti['name']))
    return expName

def getSlice(restURL, restPort, proj_name, exp_name):
    print('retrieving slices...')
    jsonurl = urllib2.urlopen(restURL + ':' + restPort + '/projects/' + proj_name + '/experiments/' + exp_name + '/slices')
    decoded_json = json.load(jsonurl)
    sliceName = []
    experiments = decoded_json['experiments']
    for i in range(len(experiments)):
        dicti = experiments[i]
        sliceName.append(str(dicti['name']))
    return sliceName

def postUser(restURL, restPort, proj_name):
    print('retrieving users...')
    jsonurl = urllib2.urlopen(restURL + ':' + restPort + '/projects/' + proj_name + '/users')
    decoded_json = json.load(jsonurl)
    userName = []
    users = decoded_json['users']
    for i in range(len(users)):
        dicti = users[i]
        userName.append(str(dicti['name']))
    return userName

