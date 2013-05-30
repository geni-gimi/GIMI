from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple project XML containing only the mandatory items
class Project:
   #Initializes variables
   def __init__(self, proj_id, title, PI_first_name, PI_last_name, PI_org):
      self.proj_id = proj_id
      self.title = title
      self.PI_first_name = PI_first_name
      self.PI_last_name = PI_last_name
      self.PI_org = PI_org

   #Creates XML file using ElementTree & writes it to file "project.xml"
   def makeXML(self):
      # </Project>
      TheProject =Element( 'Project')
      TheProject.attrib['xmlns']="http://geni.net/schema"
      TheProject.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
      TheProject.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"

      # <Project><ID/>
      ID = SubElement( TheProject, 'ProjectIdentifier')
      ID.text = self.proj_id

      # <Project><Title/>
      Title = SubElement( TheProject, 'Title')

      # <Project><Title><Title2/>
      Title2 = SubElement( Title, 'Title')
      Title2.attrib['xml:lang']="en-US"
      Title2.text = self.title

      # <Project><PrincipalInvestigator/>
      PrincipalInvestigator = SubElement( TheProject, 'PrincipalInvestigator')

      # <Project><PrincipalInvestigator><Person/>
      Person = SubElement( PrincipalInvestigator, 'Person')

      # <Project><PrincipalInvestigator><Person><FirstName/>
      FirstName = SubElement( Person, 'FirstName')
      FirstName.text = self.PI_first_name

      # <Project><PrincipalInvestigator><Person><LastName/>
      LastName = SubElement( Person, 'LastName')
      LastName.text = self.PI_last_name
  
      # <Project><PrincipalInvestigator><Organization/>
      Organization = SubElement( PrincipalInvestigator, 'Organization')
      Organization.text = self.PI_org

      #To print to file
      Test = ElementTree()
      Test._setroot(TheProject)
      Test.write('project.xml')

      ##To print to terminal
      #dump(TheProject)



##For testing purposes##
#newProject = Project('project_id', 'title', 'PI_first_name', 'PI_last_name', 'PI_org')
#newProject.makeXML()

