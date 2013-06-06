from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple experiment XML containing only the mandatory items
class Experiment:
    #Initializes variables
    def __init__(self, exp_authority, name, individual_type, individual_authority, individual_user, date_time_type, start):
        self.exp_authority = exp_authority
        self.name = name
        self.individual_type = individual_type
        self.individual_authority = individual_authority
        self.individual_user = individual_user
        self.date_time_type = date_time_type
        self.start = start

    #Creates XML file using ElementTree & writes it to file "experiment.xml"
    def makeXML(self):
        # </Experiment>
        TheExperiment =Element( 'Experiment')
        TheExperiment.attrib['xmlns']="http://geni.net/schema"
        TheExperiment.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
        TheExperiment.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"


        # <Experiment><Name/>
        Name = SubElement( TheExperiment, 'Name')

        # <Experiment><Name><Authority/>
        Authority = SubElement( Name, 'Authority')
        Authority.text = self.exp_authority

        # <Experiment><Name><Name2/>
        Name2 = SubElement( Name, 'Name')
        Name2.attrib['xml:lang']="en-US"
        Name2.text = self.name

        # <Experiment><Individuals/>
        Individuals = SubElement( TheExperiment, 'Individuals')

        # <Experiment><Individuals><Individual/>
        Individual = SubElement( Individuals, 'Individual')

        # <Experiment><Individuals><Individual><Type/>
        Type = SubElement( Individual, 'Type')
        Type.text = self.individual_type

        # <Experiment><Individuals><Individual><Authority/>
        IndAuthority = SubElement( Individual, 'Authority')
        IndAuthority.text = self.individual_authority
  
        # <Experiment><Individuals><Individual><User_name/>
        User = SubElement( Individual, 'User_name')
        User.text = self.individual_user

        # <Experiment><Dates_and_times/>
        Dates_and_times = SubElement( TheExperiment, 'Dates_and_times')
    
        # <Experiment><Dates_and_times><Date_and_time/>
        Date_and_time = SubElement( Dates_and_times, 'Date_and_time')

        # <Experiment><Dates_and_times><Date_and_time><Date_time_type/>
        Date_time_type = SubElement( Date_and_time, 'Date_time_type')
        Date_time_type.text = self.date_time_type

        # <Experiment><Dates_and_times><Date_and_time><Date_time_start/>
        Start = SubElement( Date_and_time, 'Date_time_start')
        Start.text = self.start

        #To print to file
        Test = ElementTree()
        Test._setroot(TheExperiment)
        Test.write('experiment.xml')

        ##To print to terminal
        #dump(TheExperiment)



##For testing purposes##
#newExperiment = Experiment('exp_authority', 'myProject', 'experimenter', 'individual_authority', 'geni_user', 'iso8601', '2013-06-05T09:30:01Z')
#newExperiment.makeXML()

