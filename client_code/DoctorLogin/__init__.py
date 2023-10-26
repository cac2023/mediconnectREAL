from ._anvil_designer import DoctorLoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState




class DoctorLogin(DoctorLoginTemplate):
  
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def doctor_signup_click(self, **event_args):
    open_form('DoctorSignUp')
    pass


  def doctor_login_click(self, **event_args):
    AppState.Dtypedu = self.doctor_login_username.text 
    AppState.Dtypedp = self.doctor_login_password.text
    if anvil.server.call('checkDAccount', AppState.Dtypedu, AppState.Dtypedp) :
      AppState.Dindex = anvil.server.call('getDIndex', AppState.Dtypedu, AppState.Dtypedp)

      open_form('DoctorUI')
    else:  
      print("no")
    pass

  def dlback_button_click(self, **event_args):
    open_form('Intro')
    pass







