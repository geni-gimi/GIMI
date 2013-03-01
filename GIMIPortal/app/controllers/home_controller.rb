class HomeController < ApplicationController
  def index
    if user_signed_in?
#      redirect_to :controller=>'landing', :action => 'index'
#      redirect_to "http://pc257.emulab.net:#{current_user.url}"
      myport=`python /home/labwiki/src/startLabwiki.py`
      redirect_to "http://emmy9.casa.umass.edu:" + myport
    end
  end
end
