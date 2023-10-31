from ._anvil_designer import EditPatientTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState

class EditPatient(EditPatientTemplate):

  named = AppState.currentName
  second = 'second'
  minute = 'minute'
  hour = 'hour'
  day = 'day'
  week = 'week'
  month = 'month'
  year = 'year'
  qd = AppState.qq
  question = 'No Question Yet'
  if qd is not None:
    question = qd


  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    if self.qd is not None:
      anvil.server.call('setAnswer', anvil.server.call('getPatientIndexFromCode', AppState.currentCode), self.answerd.text )
    if self.med.text != '' :
      anvil.server.call('editMed', AppState.currentCode, self.med.text)
    if self.dia.text != '' :
      anvil.server.call('editDiag', AppState.currentCode, self.dia.text)
    if self.timings.text != '' :
      multiplier = 0
      typess=''
      numm=''
      if self.drop_down_1.selected_value == self.second:
        multiplier = 1
        typess = self.second
      if self.drop_down_1.selected_value == self.minute:
        multiplier = 60
        typess = self.minute
        
      if self.drop_down_1.selected_value == self.hour:
        multiplier = 3600
        typess = self.hour
      if self.drop_down_1.selected_value == self.day:
        multiplier = 86400
        typess = self.day
      if self.drop_down_1.selected_value == self.week:
        multiplier = 604800
        typess = self.week
      if self.drop_down_1.selected_value == self.month:
        multiplier = 2629744
        typess = self.month
      if self.drop_down_1.selected_value == self.year:
        multiplier = 31556926
        typess = self.year
      value = int(self.timings.text) * multiplier
      numm = self.timings.text
      indexx=anvil.server.call('getPatientIndexFromCode', AppState.currentCode)
      app_tables.patient.search()[indexx]['DisplayNum'] = numm
      app_tables.patient.search()[indexx]['DisplayType'] = typess

      
      anvil.server.call('setSchedule', AppState.currentCode, value )
      anvil.server.call('setLastEmail', AppState.currentCode)

    
    open_form('DoctorUI')

    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DisplayAPatient')
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
