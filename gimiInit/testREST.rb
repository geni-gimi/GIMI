require_relative 'gimiREST'

class Testnow
	def initialize
           @restURL = "emmy9.casa.umass.edu"
           @restPort = "8023"
           @user_name = "dbhat"
           @proj_name = "GEC18"
           @exp_name = "geni-dbhat-testop1-2013-10-06T16-50-14-04-00"
           @irods_path = "/home/gimiadmin/" + @user_name + @exp_name
           @itkt_valid = "10082013"
           @slice_name = "dbhattestopenfire"
           @manifest = "dbhattestopenfiremanifest.xml"           
           @clnew = RESTs.new(@restURL, @restPort,@user_name, @proj_name, @exp_name, @irods_path, @itkt_valid, @slice_name, @manifest)
 	end
   	def testinterface
	   @resproj = @clnew.postProject()
           @resexp = @clnew.postExperiment()
           @ressli = @clnew.postSlice()
           @resusr = @clnew.postUser()
 	end
end
testx = Testnow.new.testinterface
