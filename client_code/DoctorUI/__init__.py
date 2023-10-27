from ._anvil_designer import DoctorUITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class DoctorUI(DoctorUITemplate):
  Namess = AppState.DoctorName
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('AddPatients')
    pass

  def button_2_click(self, **event_args):
    open_form('DisplayAPatient')
    pass


