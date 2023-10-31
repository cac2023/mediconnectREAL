from ._anvil_designer import PatientUITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState
import datetime

class PatientUI(PatientUITemplate):
  names = AppState.PatientName
  medd = AppState.currentMed
  dif = AppState.currentDiag
  #diagnosis = anvil.server.call('getDiagnosis', AppState.Pusername)
  def __init__(self, **properties):
   
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    print(AppState.b)
    if True:
      n = Notification("Take " + self.medd)
      n.show()    

