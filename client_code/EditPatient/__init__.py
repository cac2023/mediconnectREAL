from ._anvil_designer import EditPatientTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class EditPatient(EditPatientTemplate):
  named = AppState.currentName

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    if self.med.text != '' :
      anvil.server.call('editMed', AppState.currentCode, self.med.text)
    if self.dia.text != '' :
      anvil.server.call('editDiag', AppState.currentCode, self.dia.text)
    open_form('DoctorUI')

    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DisplayAPatient')
    pass
