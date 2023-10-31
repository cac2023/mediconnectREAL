from ._anvil_designer import PatientLoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Variables import AppState
import datetime


class PatientLogin(PatientLoginTemplate):
  
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def doctor_signup_click(self, **event_args):
    open_form('PatientSignUp')
    pass

  ##self.rich_text_1.visible = False
  
  def doctor_login_click(self, **event_args):

    AppState.Ptypedu = self.patient_login_username.text
    AppState.Ptypedp = self.patient_login_password.text
      
    if anvil.server.call('checkPAccount', AppState.Ptypedu, AppState.Ptypedp) :
      AppState.Pindex = anvil.server.call('getPIndex', AppState.Ptypedu, AppState.Ptypedp)
      AppState.PatientName = anvil.server.call('getPatientName', AppState.Pindex)
      AppState.patientsCode= anvil.server.call('getCodeFromIndex', AppState.Pindex)
      if anvil.server.call('getdiFromIndex', AppState.Pindex) == '' :
        open_form('NewPatient')
      else :
        AppState.currentDiag = anvil.server.call('getdiFromIndex', AppState.Pindex)
        AppState.currentMed = anvil.server.call('getmFromIndex', AppState.Pindex)
        index = AppState.Pindex
        table_data = app_tables.patient.search()      
        row = table_data[index]
        current_datetime = datetime.datetime.now()
 
        if current_datetime.replace(tzinfo=None) >= row['LastNoti'].replace(tzinfo=None) + datetime.timedelta(seconds=row['Schedule']):
          AppState.b = True
          row['LastNoti'] = current_datetime
        open_form('PatientUI')
    else:  
      ##self.rich_text_1.visible = True
      print("no")
    
      
    pass

  def plback_button_click(self, **event_args):
    open_form('Intro')
    pass


  







