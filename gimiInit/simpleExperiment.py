from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple experiment XML containing only the mandatory items
class Experiment:
    #Initializes variables
    def __init__(self, exp_authority, name, exp_id, individual_role, individual_authority, individual_user, date_time_type, start):
        self.exp_authority = exp_authority
        self.name = name
        self.exp_id = exp_id
        self.individual_role = individual_role
        self.individual_authority = individual_authority
        self.individual_user = individual_user
        self.date_time_type = date_time_type
        self.start = start

    #Creates XML file using ElementTree & writes it to file "experiment.xml"
    def makeXML(self, work_directory):
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

        # <Experiment><GENI_experiment_identifier/>
        Exp_id = SubElement( TheExperiment, 'GENI_experiment_identifier')
        Exp_id.text = self.exp_id

        # <Experiment><Individuals/>
        Individuals = SubElement( TheExperiment, 'Individuals')

        # <Experiment><Individuals><Individual/>
        Individual = SubElement( Individuals, 'Individual')

        # <Experiment><Individuals><Individual><Role/>
        Role = SubElement( Individual, 'Role')
        Role.text = self.individual_role

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
        root = Test.getroot()
        self.indent(root)
        Test.write(work_directory+'/experiment.xml')

        ##To print to terminal
        #dump(root)


    # ElementTree code to indent for pretty printing
    def indent(self,elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i




##For testing purposes##
#newExperiment = Experiment('exp_authority', 'myProject', 'exp_id', 'experimenter', 'individual_authority', 'geni_user', 'iso8601', '2013-06-05T09:30:01Z')
#newExperiment.makeXML('/home/koneil/iRODSstuff/tmp')

