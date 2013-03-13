class SessionsController < Devise::SessionsController

  before_filter :cleanup_labwiki!, :only => :destroy
 
  def cleanup_labwiki!
#    logger.debug "The session.username is #{session[:current_user_name]}"
    system("/home/labwiki/GIMI/GIMIPortal/src/stopLW.sh","#{session[:current_user_port]}", "#{session[:current_user_name]}")
  end

end
