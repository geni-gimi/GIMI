class SessionsController < Devise::SessionsController

  after_filter :cleanup_labwiki!, :only => :destroy
  def cleanup_labwiki!
    unless user_signed_in? # logout successful?
        system("/home/labwiki/src/stopLW.sh 5020")
    end
  end

end
