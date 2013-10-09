require 'rest_client'
require 'json'
require 'base64'
require 'uuidtools'
require 'pp'
require 'execjs'
class Get_Rest
    def getProject(restURL_f,restPort_f)
        @restURL = restURL_f
        @restPort = restPort_f
        values = Array.new
        puts "#{@restURL} + #{@restPort}"
        @url = @restURL + ":" + @restPort + "/projects"
        puts "\nURL:  #{@url}"
        res = RestClient.get @url
        json_obj = JSON.parse(res)
        value_res = nestHash(json_obj, "projects", values)
        value_res.each do |val|
           puts "Project name : \n #{val}"
        end        
    end
    def getExperiment(restURL_f,restPort_f,projName_f)
        @restURL = restURL_f
        @restPort = restPort_f
        @proName = projName_f
        values = Array.new
        puts "#{@restURL} + #{@restPort}"
        @url = @restURL + ":" + @restPort + "/projects/" + @proName + "/experiments"
        puts "\nURL:  #{@url}"
        res = RestClient.get @url
        json_obj = JSON.parse(res)
        value_res = nestHash(json_obj, "experiments", values)
        value_res.each do |val|
           puts "Experiment name : \n #{val}"
        end
    end
    def getSlice(restURL_f,restPort_f,projName_f, expName_f)
        @restURL = restURL_f
        @restPort = restPort_f
        @proName = projName_f
        @expName = expName_f
        values = Array.new
        puts "#{@restURL} + #{@restPort}"
        @url = @restURL + ":" + @restPort + "/projects/" + @proName + "/experiments/" + @expName + "/slices"
        puts "\nURL:  #{@url}"
        res = RestClient.get @url
        json_obj = JSON.parse(res)
        value_res = nestHash(json_obj, "slices", values)
        value_res.each do |val|
           puts "Slice name : \n #{val}"
        end
    end
    def getUser(restURL_f,restPort_f,projName_f)
        @restURL = restURL_f
        @restPort = restPort_f
        @proName = projName_f
        values = Array.new
        puts "#{@restURL} + #{@restPort}"
        @url = @restURL + ":" + @restPort + "/projects/" + @proName + "/users"
        puts "\nURL:  #{@url}"
        res = RestClient.get @url
        json_obj = JSON.parse(res)
        value_res = nestHash(json_obj, "users", values)
        value_res.each do |val|
           puts "User name : \n #{val}"
        end
    end
    def nestHash(jsonobj, obj_type, val)
      v1 = Array.new
      v3 = Array.new
       @json_nat = jsonobj
       @objTyp = obj_type
       @val_act = val
       @json_nat.each do |k1, v1|
          if k1.to_s == @objTyp then
            if v1.kind_of?(Array) == true then
                  v1.each do |v2|
                      v3 = nestHash(v2, "name", @val_act)
             end
            else
                 @val_act << v1
            end
          end
      end
       return @val_act
    end      
testz = Get_Rest.new.getProject("http://emmy9.casa.umass.edu","8023")
testa = Get_Rest.new.getExperiment("http://emmy9.casa.umass.edu","8023", "GIMITesting")
testb = Get_Rest.new.getSlice("http://emmy9.casa.umass.edu","8023", "GIMiTesting","dbhatgeni-dbhat-testop1-2013-10-06T16-50-14-04-00")
testc = Get_Rest.new.getUser("http://emmy9.casa.umass.edu","8023", "GIMiTesting")
end



