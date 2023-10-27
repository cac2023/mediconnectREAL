import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_doctor(user, pas, name):
  app_tables.doctor.add_row(Username=user, Password=pas, Name=name, PatientCodes=[])

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
def getPIndex(user, pas):
  index = None

  table_data = list(app_tables.patient.search())

  condition = lambda row: row['Username'] == user and row['Password'] == pas

  
  for i, row in enumerate(table_data):
      if condition(row):
        return i
  return -1    

@anvil.server.callable
def getDoctorName(indexs):
  table_data = app_tables.doctor.search()
  return table_data[indexs]['Name']

@anvil.server.callable
def checkPatientCode(code):
  patient_table = app_tables.patient
  matching_row = patient_table.search(UniqueCode=code)
  for row in matching_row:
    return True
  return False

@anvil.server.callable
def addPatientCode(index, code):
  table_data = app_tables.doctor.search()      
  row = table_data[index]
  d = row['PatientCodes']
  d.append(code)
  row['PatientCodes'] = d 


@anvil.server.callable
def checkDoctorCodes(index, code) :
   table_data = app_tables.doctor.search()      
   row = table_data[index]
   if code in row['PatientCodes'] :
     return True
   return False

@anvil.server.callable
def getPatientIndexFromCode(code) :
  index = None

  table_data = list(app_tables.patient.search())

  condition = lambda row: row['UniqueCode'] == code

  
  for i, row in enumerate(table_data):
      if condition(row):
        return i
  return -1
  
@anvil.server.callable
def getThePatientsName(code) :
  return getPatientName(getPatientIndexFromCode(code))

@anvil.server.callable
def editDiag(code, text) :
  index = getPatientIndexFromCode(code)
  table_data = app_tables.patient.search()      
  row = table_data[index]
  row['Diagnosis'] = text

@anvil.server.callable
def editMed(code, text) :
  index = getPatientIndexFromCode(code)
  table_data = app_tables.patient.search()      
  row = table_data[index]
  row['Medications'] = text

@anvil.server.callable
def getPatientName(indexs):
  table_data = app_tables.patient.search()
  return table_data[indexs]['Name']

@anvil.server.callable
def getCodeFromIndex(index) :
   table_data = app_tables.patient.search()      
   row = table_data[index]
   return row['UniqueCode']

@anvil.server.callable
def getdiFromIndex(index) :
   table_data = app_tables.patient.search()      
   row = table_data[index]
   return row['Diagnosis']

@anvil.server.callable
def getmFromIndex(index) :
   table_data = app_tables.patient.search()      
   row = table_data[index]
   return row['Medications']

@anvil.server.callable
def add_patient(user, pas, code, name):
  app_tables.patient.add_row(Username=user, Password=pas, UniqueCode=code, Name=name, Diagnosis='')

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

