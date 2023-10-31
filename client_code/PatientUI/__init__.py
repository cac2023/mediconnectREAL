from ._anvil_designer import PatientUITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState
import datetime

class PatientUI(PatientUITemplate):
  question = ''
  Answer = 'No Answer Yet!'
  names = AppState.PatientName
  medd = AppState.currentMed
  dif = AppState.currentDiag
  index = anvil.server.call('getPatientIndexFromName', names)
  #diagnosis = anvil.server.call('getDiagnosis', AppState.Pusername)
  def __init__(self, **properties):
    self.init_components(**properties)
    x = anvil.server.call('getQuestion', self.index)
    if x is not None:
      self.question=x
    y = anvil.server.call('getAnswer', self.index)
    if y is not None:
      self.Answer=x      
    # Any code you write here will run before the form opens.
    print(AppState.b)
    if True:
      n = Notification("Take " + self.medd)
      n.show()    

  def button_2_click(self, **event_args):
    anvil.server.call('setQuestion', index, self.text_box_1.text )
    anvil.server.call('setAnswer', index, None )
    open_form('PatientUI')
    pass

