from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple project XML containing only the mandatory items
class Project:
    #Initializes variables
    def __init__(self, proj_authority, name, proj_id, individual_role, individual_authority, individual_user, date_time_type, start):
        self.proj_authority = proj_authority
        self.name = name
        self.proj_id = proj_id
        self.individual_role = individual_role
        self.individual_authority = individual_authority
        self.individual_user = individual_user
        self.date_time_type = date_time_type
        self.start = start

    #Creates XML file using ElementTree & writes it to file "project.xml"
    def makeXML(self, work_directory):
        # </Project>
        TheProject =Element( 'Project')
        TheProject.attrib['xmlns']="http://geni.net/schema"
        TheProject.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
        TheProject.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"


        # <Project><Name/>
        Name = SubElement( TheProject, 'Name')

        # <Project><Name><Authority/>
        Authority = SubElement( Name, 'Authority')
        Authority.text = self.proj_authority

        # <Project><Name><Name2/>
        Name2 = SubElement( Name, 'Name')
        Name2.attrib['xml:lang']="en-US"
        Name2.text = self.name

        # <Project><GENI_project_identifier/>
        Proj_id = SubElement( TheProject, 'GENI_project_identifier')
        Proj_id.text = self.proj_id

        # <Project><Individuals/>
        Individuals = SubElement( TheProject, 'Individuals')

        # <Project><Individuals><Individual/>
        Individual = SubElement( Individuals, 'Individual')

        # <Project><Individuals><Individual><Role/>
        Role = SubElement( Individual, 'Role')
        Role.text = self.individual_role

        # <Project><Individuals><Individual><Authority/>
        IndAuthority = SubElement( Individual, 'Authority')
        IndAuthority.text = self.individual_authority
  
        # <Project><Individuals><Individual><UserName/>
        User = SubElement( Individual, 'UserName')
        User.text = self.individual_user

        # <Project><Dates_and_times/>
        Dates_and_times = SubElement( TheProject, 'Dates_and_times')

        # <Project><Dates_and_times><Date_and_time/>
        Date_and_time = SubElement( Dates_and_times, 'Date_and_time')

        # <Project><Dates_and_times><Date_and_time><Date_time_type/>
        Date_time_type = SubElement( Date_and_time, 'Date_time_type')
        Date_time_type.text = self.date_time_type

        # <Project><Dates_and_times><Date_and_time><Date_time_start/>
        Start = SubElement( Date_and_time, 'Date_time_start')
        Start.text = self.start


        #To print to file
        Test = ElementTree()
        Test._setroot(TheProject)
        root = Test.getroot()
        self.indent(root)
        Test.write(work_directory+'/project.xml')

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
#newProject = Project('proj_authority', 'myProject', 'proj_id', 'PI', 'individual_authority', 'geni_user', 'iso8601', '2013-06-05T09:30:01Z')
#newProject.makeXML('/home/koneil/iRODSstuff/tmp')

