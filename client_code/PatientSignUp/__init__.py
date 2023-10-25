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

  def usernmae_sign_pressed_enter(self, **event_args):
    AppState.Pusername=self.usernmae_sign.text
    pass

  def password_sign_pressed_enter(self, **event_args):
    AppState.Ppassword=self.password_sign.text
    pass

  def confirm_click(self, **event_args):
     open_form('PatientLogin')
     pass



