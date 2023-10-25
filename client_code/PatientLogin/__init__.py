from ._anvil_designer import PatientLoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState




class PatientLogin(PatientLoginTemplate):
  
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def doctor_signup_click(self, **event_args):
    open_form('PatientSignUp')
    pass

  def doctor_login_click(self, **event_args):

    AppState.Ptypedu = self.patient_login_username.text
    AppState.Ptypedp = self.patient_login_password.text
      
    if anvil.server.call('checkPAccount', AppState.Ptypedu, AppState.Ptypedp) :
      open_form('PatientUI')
    else:  
      print("no")
    
      
    pass

  







