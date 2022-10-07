import tkinter as tk
from tkinter import ttk

from client_manager.main import display_charge_product_window
from model.dao import create_table, delete_from_db, delete_table, list_to_db

colors = {'primary': '#3a86ff', 'danger': '#ef233c'}

# we are making the same as if we code this
""" root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
frame.config(width=500, height=500) """

class MyFrame(tk.Frame):
  def __init__(self, root = None, width = 450, height=320):
    super().__init__(root, width=width, height=height)
    self._root = root
    self.pack()
    self.config()

    self.table()
    self.action_btns()

  def table(self):
    products_list = list_to_db()

    columns = ('Product', 'Quantity','Sell Price', 'Buy price')
    self.table = ttk.Treeview(self, columns = columns)
    self.table.grid(row=1, column=0, columnspan=4) 

    self.table.heading('#0', text='ID')
    self.table.heading('#1', text='Product')
    self.table.heading('#2', text='Quantity')
    self.table.heading('#3', text='Sell price')
    self.table.heading('#4', text='Buy price')

    for product in products_list:
      self.table.insert('', 0, text = product[0],values=(product[1], product[2],product[3], product[4]))

  def action_btns(self):

    # charge products btn
    self.charge_btn = tk.Button(self,text='Charge 🔼', command=display_charge_product_window)
    self.charge_btn.config(width=20, bg=colors['primary'])
    self.charge_btn.grid(row=2, column=0) 

    # delete products btn
    self.discharge_btn = tk.Button(self,text='Delete 🔽')
    self.discharge_btn.config(width=20, bg=colors['danger'], command= self.delete_item)
    self.discharge_btn.grid(row=2, column=1) 


  def delete_item(self):
    try:
      self.id_product = self.table.item(self.table.selection())['text']
      delete_from_db(self.id_product)
      self.table()
    except:
      pass

def nav_bar(root, width = 300, height = 300):
  # create the bar
  bar_menu = tk.Menu()
  root.config(menu = bar_menu, width = width, height = height)
  
  # one "menu" in the menu bar 
  initial_menu = tk.Menu(bar_menu, tearoff=0)
  bar_menu.add_cascade(label='Inicio', menu=initial_menu)

  # initial_menu item
  initial_menu.add_command(label = 'Create data base', command=create_table)
  initial_menu.add_command(label = 'Delete data base', command=delete_table)
  initial_menu.add_command(label = 'Exit', command = root.destroy)

  bar_menu.add_cascade(label='Configuration')
  bar_menu.add_cascade(label='Help')

