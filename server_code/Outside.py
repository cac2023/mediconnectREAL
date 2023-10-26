import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_doctor(user, pas, name):
  app_tables.doctor.add_row(Username=user, Password=pas, Name=name)

@anvil.server.callable
def getDIndex(user, pas):
  index = None

  table_data = list(app_tables.doctor.search())

  condition = lambda row: row['Username'] == user and row['Password'] == pas

  
  for i, row in enumerate(table_data):
      if condition(row):
        return i
  return -1
        
    

  

@anvil.server.callable
def add_patient(user, pas, code, name):
  app_tables.patient.add_row(Username=user, Password=pas, UniqueCode=code, Name=name)

@anvil.server.callable
def checkDAccount(userx, pasx):
  doctor_table = app_tables.doctor
  matching_row = doctor_table.search(Username=userx, Password=pasx)
  for row in matching_row:
    return True
    
  return False

@anvil.server.callable
def getDiagnosis(userx):
  return app_tables.patient.get(Username=userx)['Diagnosis']


@anvil.server.callable
def checkPAccount(userx, pasx):
  patient_table = app_tables.patient
  matching_row = patient_table.search(Username=userx, Password=pasx)
  for row in matching_row:
    return True
    
  return False

