from ._anvil_designer import DoctorLoginTemplate
from anvil import *
from ..Variables import AppState




class DoctorLogin(DoctorLoginTemplate):
  
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def doctor_signup_click(self, **event_args):
    open_form('DoctorSignUp')
    pass

  def doctor_login_username_pressed_enter(self, **event_args):
    AppState.Dtypedu = self.doctor_login_username.text
    pass

  def doctor_login_password_pressed_enter(self, **event_args):
    AppState.Dtypedp = self.doctor_login_password.text
    pass

  def doctor_login_click(self, **event_args):
    
    if AppState.Dtypedp == AppState.Dpassword and AppState.Dtypedu == AppState.Dusername:
      open_form('DoctorUI')
    else:  
      print("no")
    
      
    pass






