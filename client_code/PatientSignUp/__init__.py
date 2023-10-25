from ._anvil_designer import PatientSignUpTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class PatientSignUp(PatientSignUpTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def confirm_click(self, **event_args):
    AppState.Pusername=self.username_sign.text
    AppState.Ppassword=self.password_sign.text
    anvil.server.call('add_patient', AppState.Pusername, AppState.Ppassword)

    open_form('PatientLogin')
    pass



