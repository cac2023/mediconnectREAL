from ._anvil_designer import PatientUITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState


class PatientUI(PatientUITemplate):
  names = AppState.PatientName
  #diagnosis = anvil.server.call('getDiagnosis', AppState.Pusername)
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
