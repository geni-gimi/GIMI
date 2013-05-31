from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple experiment XML containing only the mandatory items
class Experiment: 
    #Initializes variables
    def __init__(self, exp_id, title, first_name, last_name, exp_org):
        self.exp_id = exp_id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.exp_org = exp_org

    #Creates XML file using ElementTree & writes it to file "experiment.xml"
    def makeXML(self):
        # </Experiment>
        TheExperiment = Element( 'Experiment')
        TheExperiment.attrib['xmlns']="http://geni.net/schema"
        TheExperiment.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
        TheExperiment.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"

        # <Experiment><ID/>
        ID = SubElement( TheExperiment, 'ExperimentIdentifier')
        ID.text = self.exp_id

        # <Experiment><Title/>
        Title = SubElement( TheExperiment, 'Title')

        # <Experiment><Title><Title/>
        Title2 = SubElement( TheExperiment, 'Title')
        Title2.text = self.title

        # <Experiment><Duration/>
        Duration = SubElement( TheExperiment, 'Duration')

        # <Experiment><Duration><Start/>
        Start = SubElement( Duration, 'Start')
        Start.text = 'NOW'
  
        # <Experiment><Duration><End/>
        End = SubElement( Duration, 'End')
        End.text = '9013-01-01T00:00:01'

        # <Experiment><Experimenter/>
        Experimenter = SubElement( TheExperiment, 'Experimenter')

        # <Experiment><Experimenter><Person/>
        Person = SubElement( Experimenter, 'Person')

        # <Experiment><Experimenter><Person><FirstName/>
        FirstName = SubElement( Person, 'FirstName')
        FirstName.text = self.first_name

        # <Experiment><Experimenter><Person><LastName/>
        LastName = SubElement( Person, 'LastName')
        LastName.text = self.last_name
  
        # <Experiment><Experimenter><Organization/>
        Organization = SubElement( Experimenter, 'Organization')
        Organization.attrib['xml:lang']="en-US"
        Organization.text = self.exp_org

        #To print to file
        Test = ElementTree()
        Test._setroot(TheExperiment)
        Test.write('experiment.xml')
  
        ##To print to terminal
        #dump(TheExperiment)



##For testing purposes##
#newExperiment = Experiment('exp_id', 'title', 'first_name', 'last_name', 'exp_org')
#newExperiment.makeXML()

