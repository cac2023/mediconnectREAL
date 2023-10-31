from ._anvil_designer import DisplayAPatientTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class DisplayAPatient(DisplayAPatientTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



  def Enters_click(self, **event_args):
    f = self.text_box_1.text
    if anvil.server.call('checkDoctorCodes', AppState.Dindex, f ) :
      AppState.currentCode=f
      AppState.aa=anvil.server.call('getAnswer', anvil.server.call('getPatientIndexFromCode', AppState.currentCode))

      AppState.qq=anvil.server.call('getQuestion', anvil.server.call('getPatientIndexFromCode', AppState.currentCode))
      AppState.currentName = anvil.server.call('getThePatientsName', AppState.currentCode)
      open_form('EditPatient')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DoctorUI')
    pass





