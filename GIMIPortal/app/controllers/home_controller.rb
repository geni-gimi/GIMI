class HomeController < ApplicationController
  def index
    if user_signed_in?
      myport=`python /home/labwiki/GIMI/GIMIPortal/src/startLabwiki.py #{current_user.username}`
      # Set these values in the session so they can be used to cleanup after user signs out
      session[:current_user_port] = myport 
      session[:current_user_name] = "#{current_user.username}" 
#      redirect_to :controller=>'landing', :action => 'index'
#      redirect_to "http://pc257.emulab.net:#{current_user.url}"
       redirect_to "http://emmy9.casa.umass.edu:" + myport
    end
  end
end
