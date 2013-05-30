from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple artifact XML containing only the mandatory items
class Artifact:
   #Initializes variables
   def __init__(self, name):
      self.name=name

   #Creates XML file using ElementTree & writes it to file "artifact.xml"
   def makeXML(self):
      # </Artifact>
      TheArtifact = Element( 'Artifact')
      TheArtifact.attrib['xmlns']="http://geni.net/schema"
      TheArtifact.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
      TheArtifact.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"

      # <Artifact><Name/>
      Name = SubElement( TheArtifact, 'Name')
      Name.text = self.name

      # <Artifact><Type/>
      Type = SubElement( TheArtifact, 'Type')

      # <Artifact><Type><Primary/>
      Primary = SubElement( Type, 'Primary')
      Primary.text = 'Manifest'

      # <Artifact><Interpretation/>
      Interpretation = SubElement( TheArtifact, 'Interpretation')
    
      # <Artifact><Interpretation><Description/>
      Description = SubElement( Interpretation, 'Description')
      Description.text = self.name

      #To print to file
      Test = ElementTree()
      Test._setroot(TheArtifact)
      Test.write('artifact.xml')

      ##To print to terminal
      #dump(TheArtifact)



##For testing purposes##
#newArtifact = Artifact('name')
#newArtifact.makeXML()

