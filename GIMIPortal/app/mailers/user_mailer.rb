class UserMailer < ActionMailer::Base
  default from: "labwiki@cs.umass.edu"

  def welcome_email(user)
    @user = user
    @url  = "http://emmy9.casa.umass.edu:3005"
    mail(:to => user.email, :subject => "Welcome to GIMI")
  end

  def new_user_waiting_for_approval(user)
    @user = user
    @url  = "http://emmy9.casa.umass.edu:3005"
    mail(:to => "johren@bbn.com", :subject => "GIMI account request")
  end

end
