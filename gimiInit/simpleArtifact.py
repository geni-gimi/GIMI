from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple artifact XML containing only the mandatory items
class Artifact:
    #Initializes variables
    def __init__(self, art_type, read_me_text):
        self.art_type = art_type
        self.read_me_text = read_me_text

    #Creates XML file using ElementTree & writes it to file "artifact.xml"
    def makeXML(self):
        # </Artifact>
        TheArtifact = Element( 'Artifact')
        TheArtifact.attrib['xmlns']="http://geni.net/schema"
        TheArtifact.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
        TheArtifact.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"

        # <Artifact><Type/>
        Type = SubElement( TheArtifact, 'Type')

        # <Artifact><Type><Primary/>
        Primary = SubElement( Type, 'Primary')
        Primary.text = self.art_type

        # <Artifact><Interpretation/>
        Interpretation = SubElement( TheArtifact, 'Interpretation')
    
        # <Artifact><Interpretation><Read_me_text/>
        Read_me_text = SubElement( Interpretation, 'Read_me_text')
        Read_me_text.text = self.read_me_text

        #To print to file
        Test = ElementTree()
        Test._setroot(TheArtifact)
        Test.write('artifact.xml')

        ##To print to terminal
        #dump(TheArtifact)



##For testing purposes##
#newArtifact = Artifact('GENI_AM_API_silver_manifest_rspec', 'read_me_text')
#newArtifact.makeXML()

