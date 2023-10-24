from ._anvil_designer import PatientLoginTemplate
from anvil import *
from ..Variables import AppState




class PatientLogin(PatientLoginTemplate):
  
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def doctor_signup_click(self, **event_args):
    open_form('PatientSignUp')
    pass

  def doctor_login_username_pressed_enter(self, **event_args):
    AppState.Ptypedu = self.patient_login_username.text
    pass

  def doctor_login_password_pressed_enter(self, **event_args):
    AppState.Ptypedp = self.patient_login_password.text
    pass

  def doctor_login_click(self, **event_args):

    print(AppState.Pusername)
    print(AppState.Ptypedu)
    print(AppState.Ppassword)
    print(AppState.Ptypedp)
      
    if AppState.Ptypedp == AppState.Ppassword and AppState.Ptypedu == AppState.Pusername:
      open_form('PatientUI')
    else:  
      print("no")
    
      
    pass

  







