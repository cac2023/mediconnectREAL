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
  index = AppState.ii
  textt = AppState.yes
  y = AppState.aas
  x=AppState.qqs
  if x is not None:
    question=x
  if y is not None:
    Answer=y      
  #diagnosis = anvil.server.call('getDiagnosis', AppState.Pusername)
  def __init__(self, **properties):
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if AppState.b:
      alert("Take the medication: " + self.medd, dismissable=True, timeout=None)
      #n = Notification("Take " + self.medd)
      #n.show()    

  def button_2_click(self, **event_args):
    anvil.server.call('setQuestion', self.index, self.text_box_1.text )
    anvil.server.call('setAnswer', self.index, None )
    AppState.qqs=anvil.server.call('getQuestion', self.index)
    AppState.aas=anvil.server.call('getAnswer', self.index)
    self.text_box_1.text = anvil.server.call('getQuestion', self.index)
    self.label_6.text= 'No Answer Yet!'
    pass

