class SessionsController < Devise::SessionsController

  before_filter :cleanup_labwiki!, :only => :destroy
 
  def cleanup_labwiki!
    system("/home/labwiki/src/stopLW.sh #{session[:current_user_port]}")
  end

end
