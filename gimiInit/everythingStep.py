from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple step XML containing only the mandatory items
class Step:
    #Initializes variables
    def __init__(self, prime_function, second_function='', index_type='', index_value='', date_time_type='', start='', end='', keywords='', abstract='', notes='', resource_type='', resource_id='', justManditory=False):
        self.prime_function = prime_function 
        self.second_function = second_function 
        self.index_type = index_type
        self.index_value = index_value
        self.date_time_type = date_time_type
        self.start = start
        self.end = end
        self.keywords = keywords
        self.abstract = abstract
        self.notes = notes
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.justManditory = justManditory

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

        if self.justManditory==False:
	        # <Step><Function><Secondary/>
    	    Secondary = SubElement( Function, 'Secondary')
    	    Secondary.text = self.second_function

    	    # <Step><Index/>
    	    Index = SubElement( TheStep, 'Index')
	
    	    # <Step><Function><Type/>
    	    Index_type = SubElement( Index, 'Type')
    	    Index_type.text = self.index_type

    	    # <Step><Function><Value/>
    	    Index_value = SubElement( Index, 'Value')
    	    Index_value.text = self.index_value

	        # <Step><Dates_and_times/>
    	    Dates_and_times = SubElement( TheStep, 'Dates_and_times')

    	    # <Step><Dates_and_times><Date_and_time/>
    	    Date_and_time = SubElement( Dates_and_times, 'Date_and_time')

    	    # <Step><Dates_and_times><Date_and_time><Date_time_type/>
    	    Date_time_type = SubElement( Date_and_time, 'Date_time_type')
    	    Date_time_type.text = self.date_time_type

    	    # <Step><Dates_and_times><Date_and_time><Date_time_start/>
    	    Start = SubElement( Date_and_time, 'Date_time_start')
    	    Start.text = self.start

    	    # <Step><Dates_and_times><Date_and_time><Date_time_end/>
    	    End = SubElement( Date_and_time, 'Date_time_end')
    	    End.text = self.end

    	    # <Step><Description/>
    	    Description = SubElement( TheStep, 'Description')

    	    # <Step><Description><Keywords/>
    	    Keywords = SubElement( Description, 'Keywords')
    	    Keywords.text = self.keywords

    	    # <Step><Description><Abstract/>
    	    Abstract = SubElement( Description, 'Abstract')
    	    Abstract.text = self.abstract

    	    # <Step><Description><Notes/>
    	    Notes = SubElement( Description, 'Notes')
    	    Notes.text = self.notes

    	    # <Step><GENI_resources/>
    	    Resources = SubElement( TheStep, 'GENI_resources')

    	    # <Step><GENI_resources><Resource/>
    	    Resource = SubElement( Resources, 'Resource')
  
	      	# <Step><GENI_resources><Resource><ResourceID/>
            ResourceType = SubElement( Resource, 'GENI_resource_type')
            ResourceType.text =  self.resource_type
    
	        # <Step><GENI_resources><Resource><ResourceType/>
    	    ResourceID = SubElement( Resource, 'GENI_resource_identifier')
    	    ResourceID.text = self.resource_id

        #To print to file
        Test = ElementTree()
        Test._setroot(TheStep)
        Test.write('step.xml')
  
  
        ##To print to terminal
        #dump(TheStep)



##For testing purposes##
#newStep = Step('design_experiment', 'My second function', 'run', '1', 'iso8601', '2013-06-05T09:30:01Z', '2014-06-05T09:30:01Z', 'My keywords', 'My abstract', 'My notes', 'slice', 'my_slice')
#newStep.makeXML()

#StepWithManditory = Step('design_experiment', justManditory=True)
#StepWithManditory.makeXML()

