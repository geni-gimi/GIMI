from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

#This class creates a simple artifact XML containing only the mandatory items
class Artifact:
    #Initializes variables
    def __init__(self, art_type_prime, interpretation_read_me, art_type_second='', art_type_version='', authority='', name='', keywords='', abstract='', notes='', link_to_interpretation='', prov_read_me='', prov_project='', prov_organization='', prov_individual_type='', prov_individual_authority='', prov_individual_user='', prov_individual_family='', prov_individual_given='', prov_individual_org='', prov_individual_org_dom='', prov_individual_contact_type='', prov_individual_contact_value='', prov_link_to_source='', prov_date_time_type='', prov_date_time_recieved='',justManditory=False):
        self.art_type_prime = art_type_prime
        self.art_type_second = art_type_second
        self.art_type_version = art_type_version
        self.authority = authority
        self.name = name
        self.keywords = keywords
        self.abstract = abstract
        self.notes= notes
        self.interpretation_read_me = interpretation_read_me
        self.link_to_interpretation = link_to_interpretation
        self.prov_read_me = prov_read_me
        self.prov_project = prov_project
        self.prov_organization = prov_organization
        self.prov_individual_type = prov_individual_type
        self.prov_individual_authority = prov_individual_authority
        self.prov_individual_user = prov_individual_user
        self.prov_individual_family = prov_individual_family
        self.prov_individual_given = prov_individual_given
        self.prov_individual_org = prov_individual_org
        self.prov_individual_org_dom = prov_individual_org_dom
        self.prov_individual_contact_type = prov_individual_contact_type
        self.prov_individual_contact_value = prov_individual_contact_value
        self.prov_link_to_source = prov_link_to_source
        self.prov_date_time_type = prov_date_time_type
        self.prov_date_time_recieved = prov_date_time_recieved
        self.justManditory = justManditory

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
        Primary.text = self.art_type_prime

        if self.justManditory==False:
            # <Artifact><Type><Secondary/>
            Secondary = SubElement( Type, 'Secondary')
            Secondary.text = self.art_type_second

            # <Artifact><Type><Version/>
            Version = SubElement( Type, 'Version')
            Version.text = self.art_type_version

            # <Artifact><Description/>
            Description = SubElement( TheArtifact, 'Description')

            # <Artifact><Description><Authority/>
            Authority = SubElement( Description, 'Authority')
            Authority.text = self.authority

            # <Artifact><Description><Name/>
            Name = SubElement( Description, 'Name')
            Name.text = self.name

            # <Artifact><Description><Keywords/>
            Keywords = SubElement( Description, 'Keywords')
            Keywords.text = self.keywords

            # <Artifact><Description><Abstract/>
            Abstract = SubElement( Description, 'Abstract')
            Abstract.text = self.abstract

            # <Artifact><Description><Notes/>
            Notes = SubElement( Description, 'Notes')
            Notes.text = self.notes


        # <Artifact><Interpretation/>
        Interpretation = SubElement( TheArtifact, 'Interpretation')
    
        # <Artifact><Interpretation><Interpretation_read_me_text/>
        Read_me_text = SubElement( Interpretation, 'Interpretation_read_me_text')
        Read_me_text.text = self.interpretation_read_me

        if self.justManditory==False:
            # <Artifact><Interpretation><Link_to_interpretation_resource/>
            Link_to_interpretation = SubElement( Interpretation, 'Link_to_interpretation_resource')
            Link_to_interpretation.text = self.link_to_interpretation

            # <Artifact><Provider/>
            Provider = SubElement( TheArtifact, 'Provider')
    
            # <Artifact><Provider><Interpretation_read_me_text/>
            Provider_read_me_text = SubElement( Provider, 'Provider_read_me_text')
            Provider_read_me_text.text = self.prov_read_me

            # <Artifact><Provider><Project/>
            Project = SubElement( Provider, 'Project')
            Project.text = self.prov_project

            # <Artifact><Provider><Organization/>
            Organization = SubElement( Provider, 'Organization')
            Organization.text = self.prov_organization

            # <Artifact><Provider><Individual/>
            Individual = SubElement( Provider, 'Individual')
 
            # <Artifact><Provider><Individual><Type/>
            Provider_type = SubElement( Individual, 'Type')
            Provider_type.text = self.prov_individual_type

            # <Artifact><Provider><Individual><Authority/>
            Provider_authority = SubElement( Individual, 'Authority')    
            Provider_authority.text = self.prov_individual_authority

            # <Artifact><Provider><Individual><User_name/>
            Provider_individual_user = SubElement( Individual, 'User_name')
            Provider_individual_user.text = self.prov_individual_user

            # <Artifact><Provider><Individual><Family_name/>
            Provider_individual_family = SubElement( Individual, 'Family_name')
            Provider_individual_family.text = self.prov_individual_family

            # <Artifact><Provider><Individual><Given_name/>
            Provider_individual_given = SubElement( Individual, 'Given_name')
            Provider_individual_given.text = self.prov_individual_given

            # <Artifact><Provider><Individual><Organization_name/>
            Provider_individual_org = SubElement( Individual, 'Organization_name')
            Provider_individual_org.text = self.prov_individual_org

            # <Artifact><Provider><Individual><Organization_domain/>
            Provider_individual_org_dom = SubElement( Individual, 'Organization_domain')
            Provider_individual_org_dom.text = self.prov_individual_org_dom

            # <Artifact><Provider><Individual><Contacts/>
            Provider_individual_contacts = SubElement( Individual, 'Contacts')

            # <Artifact><Provider><Individual><Contacts><Contact/>
            Provider_individual_contact = SubElement( Provider_individual_contacts, 'Contact')

            # <Artifact><Provider><Individual><Contacts><Contact><Type/>
            Provider_individual_contact_type = SubElement( Provider_individual_contact, 'Type')
            Provider_individual_contact_type.text = self.prov_individual_contact_type

            # <Artifact><Provider><Individual><Contacts><Contact><Value/>
            Provider_individual_contact_value = SubElement( Provider_individual_contact, 'Value')
            Provider_individual_contact_value.text = self.prov_individual_contact_value

            # <Artifact><Provider><Link_to_source/>
            Provider_link_to_source = SubElement( Provider, 'Link_to_source')
            Provider_link_to_source.text = self.prov_link_to_source

            # <Artifact><Provider><Date_and_time/>
            Provider_date_and_time = SubElement( Provider, 'Date_and_time')

            # <Artifact><Provider><Date_and_time><Date_time_type/>
            Provider_date_time_type = SubElement( Provider_date_and_time, 'Date_time_type')
            Provider_date_time_type.text = self.prov_date_time_type

            # <Artifact><Provider><Date_and_time><Date_time_recieved/>
            Provider_date_time_recieved = SubElement( Provider_date_and_time, 'Date_time_recieved')
            Provider_date_time_recieved.text = self.prov_date_time_recieved



        #To print to file
        Test = ElementTree()
        Test._setroot(TheArtifact)
        Test.write('artifact.xml')

        ##To print to terminal
        #dump(TheArtifact)



##For testing purposes##
#newArtifact = Artifact('GENI_AM_API_silver_manifest_rspec', "READ ME", 'The second artifact type', 'version 1.0', 'The authority', 'Artifact name', 'Artifact keywords', 'Artifact abstract', 'Artifact notes', 'The link', 'READ ME', 'The other project', 'Its organization', 'PI', 'His authority', 'geni_user2', 'His last name', 'His first name', 'His organization', 'His organization domain', 'email', 'geni_user2@geni.net', 'Its link', 'iso8601', '2013-06-05T09:30:01Z')
#newArtifact.makeXML()

#ArtifactWithManditory = Artifact('initialize_script', "READ ME", justManditory=True)
#ArtifactWithManditory.makeXML()

