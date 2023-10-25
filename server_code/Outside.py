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


