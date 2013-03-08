class HomeController < ApplicationController
  def index
    if user_signed_in?
      myport=`python /home/labwiki/src/startLabwiki.py #{current_user.username}`
      session[:current_user_port] = myport 
#      redirect_to :controller=>'landing', :action => 'index'
#      redirect_to "http://pc257.emulab.net:#{current_user.url}"
       redirect_to "http://emmy9.casa.umass.edu:" + myport
    end
  end
end
