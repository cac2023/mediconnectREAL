import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
class tab:
  def addDocTable(user, pas):
    app_tables.doctor.add_row(Username=user, Password=pas)
    pass
