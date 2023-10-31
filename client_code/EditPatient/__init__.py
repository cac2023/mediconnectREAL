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

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    if self.med.text != '' :
      anvil.server.call('editMed', AppState.currentCode, self.med.text)
    if self.dia.text != '' :
      anvil.server.call('editDiag', AppState.currentCode, self.dia.text)
    if self.timings.text != '' :
      multiplier = 0
      if self.drop_down_1.selected_value == self.second:
        multiplier = 1
      if self.drop_down_1.selected_value == self.minute:
        multiplier = 60
      if self.drop_down_1.selected_value == self.hour:
        multiplier = 3600
      if self.drop_down_1.selected_value == self.day:
        multiplier = 86400
      if self.drop_down_1.selected_value == self.week:
        multiplier = 604800
      if self.drop_down_1.selected_value == self.month:
        multiplier = 2629744
      if self.drop_down_1.selected_value == self.year:
        multiplier = 31556926
      value = int(self.timings.text) * multiplier
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
