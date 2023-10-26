from ._anvil_designer import DoctorUITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class DoctorUI(DoctorUITemplate):
  
  
  index = anvil.server.call('getDIndex', AppState.Dtypedu, AppState.Dtypedp)
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.index)

    # Any code you write here will run before the form opens.
