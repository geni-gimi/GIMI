from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple step XML containing only the mandatory items
class Step:
   #Initializes variables
   def __init__(self, step_seq_id, title, resource_id, slice_name):
      self.title = title 
      self.step_seq_id = step_seq_id
      self.resource_id = resource_id
      self.slice_name = slice_name

   #Creates XML file using ElementTree & writes it to file "step.xml"
   def makeXML(self):
      # </Step>
      TheStep = Element( 'Step' )
      TheStep.attrib['xmlns']="http://geni.net/schema"
      TheStep.attrib['xmlns:xsi']="http://www.w3.org/2001/XMLSchema-instance"
      TheStep.attrib['xsi:schemaLocation']="http://geni.net/schema GENIObject.xsd"

      # <Step><Primary/>
      Primary = SubElement( TheStep, 'Primary')
      Primary.text = 'Manifest'
  
      # <Step><Sequence/>
      Sequence = SubElement( TheStep, 'StepSequenceID')
      Sequence.text = self.step_seq_id

      # <Step><Title/>
      Title = SubElement( TheStep, 'Title')

      # <Step><Title><Title/>
      Title2 = SubElement( TheStep, 'Title')
      Title2.text = self.title

      # <Step><Resources/>
      Resources = SubElement( TheStep, 'Resources')

      # <Step><Resources><Resource/>
      Resource = SubElement( Resources, 'Resource')
  
      # <Step><Resources><Resource><ResourceID/>
      ResourceID = SubElement( Resource, 'ResourceID')
      ResourceID.text =  self.resource_id
    
      # <Step><Resources><Resource><ResourceType/>
      ResourceType = SubElement( Resource, 'ResourceType')
      ResourceType.text = 'Slice'

      #To print to file
      Test = ElementTree()
      Test._setroot(TheStep)
      Test.write('step.xml')


      ##To print to terminal
      #dump(TheStep)



##For testing purposes##
#newStep = Step('step_seq_id', 'title', 'resource_id', 'slice_name')
#newStep.makeXML()

