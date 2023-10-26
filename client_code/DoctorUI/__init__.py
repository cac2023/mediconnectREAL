from ._anvil_designer import DoctorUITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class DoctorUI(DoctorUITemplate):
  def get_index(user, pas):
        return anvil.server.call('getDIndex', user, pas)
  
  index = get_index() AppState.Dtypedu, AppState.Dtypedp)
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.index)

    # Any code you write here will run before the form opens.

