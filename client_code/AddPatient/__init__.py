from ._anvil_designer import AddPatientTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class AddPatient(AddPatientTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Entercode_click(self, **event_args):
    f = self.enterCode.text
    if anvil.server.call('checkPatientCode', f) :
      anvil.server.call('addPatientCode', AppState.Dindex, f)
      open_form('DoctorUI')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DoctorUI')
    pass
