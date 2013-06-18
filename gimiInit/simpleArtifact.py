from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple artifact XML containing only the mandatory items
class Artifact:
    #Initializes variables
    def __init__(self, art_type_prime, interpretation_read_me):
        self.art_type_prime = art_type_prime
        self.interpretation_read_me = interpretation_read_me

    #Creates XML file using ElementTree & writes it to file "artifact.xml"
    def makeXML(self, work_directory):
        # </Artifact>
        TheArtifact = Element( 'Artifact')
        TheArtifact.attrib['xmlns']="http://geni.net/schema"
        TheArtifact.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
        TheArtifact.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"

        # <Artifact><Type/>
        Type = SubElement( TheArtifact, 'Type')

        # <Artifact><Type><Primary/>
        Primary = SubElement( Type, 'Primary')
        Primary.text = self.art_type_prime

        # <Artifact><Interpretation/>
        Interpretation = SubElement( TheArtifact, 'Interpretation')
    
        # <Artifact><Interpretation><Interpretation_read_me_text/>
        Read_me_text = SubElement( Interpretation, 'Interpretation_read_me_text')
        Read_me_text.text = self.interpretation_read_me

        #To print to file
        Test = ElementTree()
        Test._setroot(TheArtifact)
        root = Test.getroot()
        self.indent(root)
        Test.write(work_directory+'/artifact.xml')

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
#newArtifact = Artifact('GENI_AM_API_silver_manifest_rspec', 'read_me_text')
#newArtifact.makeXML('/home/koneil/iRODSstuff/tmp')

