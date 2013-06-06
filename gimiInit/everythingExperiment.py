from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple experiment XML containing only the mandatory items
class Experiment:
    #Initializes variables
    def __init__(self, exp_authority, name, keywords='', abstract='', notes='', individual_type='', individual_authority='', individual_user='', individual_family='', individual_given='', individual_org='', individual_org_dom='', individual_contact_type='', individual_contact_value='', date_time_type='', start='', end='', justManditory=False):
        self.exp_authority = exp_authority
        self.name = name
        self.keywords = keywords
        self.abstract = abstract
        self.notes = notes
        self.individual_type = individual_type
        self.individual_authority = individual_authority
        self.individual_user = individual_user
        self.individual_family = individual_family
        self.individual_given = individual_given
        self.individual_org = individual_org
        self.individual_org_dom = individual_org_dom
        self.individual_contact_type = individual_contact_type
        self.individual_contact_value = individual_contact_value
        self.date_time_type = date_time_type
        self.start = start
        self.end = end
        self.justManditory = justManditory

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

        # <Experiment><Name><Name/>
        Name2 = SubElement( Name, 'Name')
        Name2.attrib['xml:lang']="en-US"
        Name2.text = self.name

        if self.justManditory==False:
            # <Experiment><Name><Keywords/>
            Keywords = SubElement( Name, 'Keywords')
            Keywords.text = self.keywords

            # <Experiment><Name><Abstract/>
            Abstract = SubElement( Name, 'Abstract')
            Abstract.text = self.abstract

            # <Experiment><Name><Notes/>
            Notes = SubElement( Name, 'Notes')
            Notes.text = self.notes

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
  
            # <Experiment><Individuals><Individual><UserName/>
            User = SubElement( Individual, 'UserName')
            User.text = self.individual_user


            # <Experiment><Individuals><Individual><Family_name/>
            Individual_family = SubElement( Individual, 'Family_name')
            Individual_family.text = self.individual_family

            # <Experiment><Individuals><Individual><Given_name/>
            Individual_given = SubElement( Individual, 'Given_name')
            Individual_given.text = self.individual_given

            # <Experiment><Individuals><Individual><Organization_name/>
            Individual_org = SubElement( Individual, 'Organization_name')
            Individual_org.text = self.individual_org

            # <Experiment><Individuals><Individual><Organization_domain/>
            Individual_org_dom = SubElement( Individual, 'Organization_domain')
            Individual_org_dom.text = self.individual_org_dom

            # <Experiment><Individuals><Individual><Contacts/>
            Individual_contacts = SubElement( Individual, 'Contacts')

            # <Experiment><Individuals><Individual><Contacts><Contact/>
            Individual_contact = SubElement( Individual_contacts, 'Contact')

            # <Experiment><Individuals><Individual><Contacts><Contact><Type/>
            Individual_contact_type = SubElement( Individual_contact, 'Type')
            Individual_contact_type.text = self.individual_contact_type

            # <Experiment><Individuals><Individual><Contacts><Contact><Value/>
            Individual_contact_value = SubElement( Individual_contact, 'Value')
            Individual_contact_value.text = self.individual_contact_value

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

            # <Experiment><Dates_and_times><Date_and_time><Date_time_end/>
            End = SubElement( Date_and_time, 'Date_time_end')
            End.text = self.end

        #To print to file
        Test = ElementTree()
        Test._setroot(TheExperiment)
        Test.write('experiment.xml')

        ##To print to terminal
        #dump(TheExperiment)



##For testing purposes##
#newExperiment = Experiment('Authority of this experiment', 'My experiment', 'My keywords', 'My abstract', 'My notes', 'experimenter', ' My authority', 'geni_user', 'My last name', 'My first name', 'My org', 'My org domain', 'email', 'geni_user@geni.net', 'iso8601', '2013-06-05T09:30:01Z', '2014-06-05T09:30:01Z')
#newExperiment.makeXML()

#ExperimentWithManditory = Experiment('Authority of this experiment', 'My experiment', justManditory=True)
#ExperimentWithManditory.makeXML()
