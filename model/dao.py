from tkinter import messagebox
from .db_connection import DB_connection

def show_messagebox(title, msg, type):
  if(type == 'warning'):
    messagebox.showwarning(title, msg)

  if(type == 'error'):
    messagebox.showerror(title, msg)

  if(type == 'info'):
    messagebox.showinfo(title, msg)

def create_table():
  connection = DB_connection()

  sql = f'''
  CREATE TABLE {connection.db_name}(
    product_id INTEGER,
    name VARCHAR(100),
    quantity INTEGER,
    sell_price INTEGER,
    buy_price INTEGER,
    PRIMARY KEY(product_id AUTOINCREMENT)
  )'''

  try:
    connection.cursor.execute(sql)
    connection.close()
    show_messagebox('Database', 'Ypu have create a database successfully', 'info')

  except:
    show_messagebox('Database', 'You already created a database', 'error')
    pass

def delete_table():
  connection = DB_connection()

  sql = f'DROP TABLE {connection.db_name}'

  try:
    connection.cursor.execute(sql)
    connection.close()
    show_messagebox('Delete database', 'Ypu have deleted a database successfully', 'info')

  except:
    show_messagebox('Delete database', 'You already deleted a database', 'error')
    pass

def add_product_to_db(product):
  connection = DB_connection()

  sql = f"""
  INSERT INTO {connection.db_name} (name, quantity, sell_price, buy_price)
  VALUES ('{product.name}', '{product.quantity}', '{product.sell_price}', '{product.buy_price}');
  """

  try:
    connection.cursor.execute(sql)
    connection.close()
    show_messagebox('Add product', 'You have added this product successfully', 'info')

  except:
    show_messagebox('Add product', 'You cannot add this product ', 'error')
    pass

def list_to_db():
  connection = DB_connection()

  sql = f'SELECT * FROM {connection.db_name}'

  try:
    connection.cursor.execute(sql)
    products_list = connection.cursor.fetchall()
    connection.close()
  
  except:
    show_messagebox('Add item', 'Create a table before create a new element', 'error')

  return products_list

def delete_from_db(id):
  connection = DB_connection()

  sql = f'DELETE FROM {connection.db_name} WHERE product_id = {id};'

  try:
    connection.cursor.execute(sql)
    connection.close()
  except:
    show_messagebox('Delete item', 'Cannot delete the item', 'error')
