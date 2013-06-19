import json
import sys
import os

class REST:
    def __init__(self, restURL, restPort, workdirectory, exp_name):
        self.restURL = restURL      #"http://emmy9.casa.umass.edu"
        self.restPort = restPort    #8002
        self.exp_name = exp_name
        self.workdirectory = workdirectory
        
        data = {'name': exp_name}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
        #data=json.dumps(data)
        json_filename = workdirectory + "/experiment.json"
        print ("Saving JSON to file: " + json_filename)
        jsonf = open(json_filename,'w')
        data = json.dumps(data)
        jsonf.write(data)
        jsonf.close()
        
        os.system('curl -X POST -H "Content-Type: application/json" --data-binary @'+ json_filename +' ' + restURL + ':' + str(restPort) + '/projects/projectB/experiments')