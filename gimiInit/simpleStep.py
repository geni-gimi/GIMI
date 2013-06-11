from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple step XML containing only the mandatory items
class Step:
    #Initializes variables
    def __init__(self, prime_function, resource_type=None, resource_id=None):
        self.prime_function = prime_function 
        self.resource_type = resource_type
        self.resource_id = resource_id

    #Creates XML file using ElementTree & writes it to file "step.xml"
    def makeXML(self):
        # </Step>
        TheStep = Element( 'Step' )
        TheStep.attrib['xmlns']="http://geni.net/schema"
        TheStep.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
        TheStep.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"

        # <Step><Function/>
        Function = SubElement( TheStep, 'Function')

        # <Step><Function><Primary/>
        Primary = SubElement( Function, 'Primary')
        Primary.text = self.prime_function

        if self.resource_type!=None:
            # <Step><GENI_resources/>
            Resources = SubElement( TheStep, 'GENI_resources')

            # <Step><Resources><Resource/>
            Resource = SubElement( Resources, 'Resource')
  
            # <Step><Resources><Resource><ResourceID/>
            ResourceType = SubElement( Resource, 'GENI_resource_type')
            ResourceType.text =  self.resource_type
    
            # <Step><Resources><Resource><ResourceType/>
            ResourceID = SubElement( Resource, 'GENI_resource_identifier')
            ResourceID.text = self.resource_id

        #To print to file
        Test = ElementTree()
        Test._setroot(TheStep)
        root = Test.getroot()
        self.indent(root)
        Test.write('step.xml')

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
newStep = Step('design_experiment', 'slice', 'my_slice')
newStep.makeXML()

