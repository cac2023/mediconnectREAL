import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_doctor(user, pas):
  app_tables.doctor.add_row(Username=user, Password=pas)

@anvil.server.callable
def add_patient(user, pas):
  app_tables.patient.add_row(Username=user, Password=pas)

@anvil.server.callable
def checkDAccount(userx, pasx):
  doctor_table = app_tables.doctor
  matching_row = doctor_table.search(Username=userx, Password=pasx)
  for row in matching_row:
    return True
    
  return False

@anvil.server.callable
def checkPAccount(userx, pasx):
  patient_table = app_tables.patient
  matching_row = patient_table.search(Username=userx, Password=pasx)
  for row in matching_row:
    return True
    
  return False

