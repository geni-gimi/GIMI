from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple step XML containing only the mandatory items
class Step:
    #Initializes variables
    def __init__(self, prime_function, resource_type, resource_id):
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
        Test.write('step.xml')
  
  
        ##To print to terminal
        #dump(TheStep)



##For testing purposes##
#newStep = Step('design_experiment', 'slice', 'my_slice')
#newStep.makeXML()

