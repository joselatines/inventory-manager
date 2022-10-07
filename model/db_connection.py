import sqlite3

class DB_connection:
  def __init__(self):
    self.db_name = 'products'
    self.database = 'C:\Projects\Personal-projects\python\inventory-manager\database\products.db'
    self.connection = sqlite3.connect(self.database)
    self.cursor = self.connection.cursor()

  def close(self):
    self.connection.commit()
    self.connection.close()