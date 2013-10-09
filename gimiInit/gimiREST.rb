require 'rest_client'
require 'json'
require 'base64'
require 'uuidtools'

class RESTs
    def initialize(restURL, restPort,user_name, proj_name, exp_name, irods_path, itkt_valid, slice_name, manifest)
        @restURL = restURL
        @restPort = restPort
        @proj_name = proj_name
        @user_name = user_name
        @exp_name = exp_name
        @irods_path = irods_path
        @itkt_valid = itkt_valid
        @slice_name = slice_name
        @manifest = manifest
       # @uuidObj = UUID.new 
        #self.postProject()
        #self.postUser()
        #self.postExperiment()
        #self.postSlice()
        puts "Values: #{@user_name} #{@proj_name} #{@exp_name} #{@irods_path} #{@slice_name}" 
       # print('Pushed data to registry successfully\n')
    end
    def postProject()
        uuid = UUIDTools::UUID.md5_create(UUIDTools::UUID_DNS_NAMESPACE, @proj_name)
        @restURL_proj = @restURL + ":" + @restPort + "/projects"
        res = RestClient.post(
        @restURL_proj,
        {
          'name' => @proj_name,
          'uuid' => uuid.to_s
        }.to_json,
        :content_type => :json,
        :accept => :json
        )
        
    return res
    end
    def postExperiment()
        uuid = UUIDTools::UUID.md5_create(UUIDTools::UUID_DNS_NAMESPACE, @exp_name)  
        @restURL_exp = @restURL + ":" + @restPort + "/projects/" + @proj_name + "/experiments"         
        res= RestClient.post(
        @restURL_exp,
        {
          'name' => @exp_name,
          'uuid' => uuid.to_s,
          'path' => @irods_path
        }.to_json,
        :content_type => :json,
        :accept => :json
        )
     return res
    end
    def postSlice()
        uuid = UUIDTools::UUID.md5_create(UUIDTools::UUID_DNS_NAMESPACE, @slice_name)
        @restURL_sli = @restURL + ":" + @restPort + "/projects/" + @proj_name + "/experiments/" + @exp_name + "/slices"
        res = RestClient.post(
        @restURL_sli,
        {
          'name' => @slice_name,
          'uuid' => uuid.to_s,
          'urn'  => @slice_name,
          'manifest' => @manifest
        }.to_json,
        :content_type => :json,
        :accept => :json
        )
     return res
    end
    def postUser()
        @x = "geni-" + @user_name
        puts "User #{@x}"
        uuid = UUIDTools::UUID.md5_create(UUIDTools::UUID_DNS_NAMESPACE, @x)
        @restURL_usr = @restURL + ":" + @restPort + "/projects/" + @proj_name + "/users"
        res = RestClient.post(
        @restURL_usr,
        {
          'name' => @x,
          'uuid' => uuid.to_s
        }.to_json,
        :content_type => :json,
        :accept => :json
        ) 
     return res
   end
end
