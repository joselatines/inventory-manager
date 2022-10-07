import tkinter as tk

from classes.Product import Product
from model.dao import add_product_to_db, show_messagebox

def display_charge_product_window():
  root = tk.Tk()

  frame = tk.Frame(root)
  frame.pack()
  frame.config(width=500, height=500)

  # label and entry
  name_label= tk.Label(frame, text="Product name")
  name_label.grid(row=1, column=0)
  name_entry = tk.Entry(frame)
  name_entry.grid(row=1, column=1)

  # label and entry
  quantity_label= tk.Label(frame, text="How many products you have")
  quantity_label.grid(row=2, column=0)
  quantity_entry = tk.Entry(frame) 
  quantity_entry.grid(row=2, column=1)

  # label and entry
  sell_price_label= tk.Label(frame, text="Price for clients")
  sell_price_label.grid(row=3, column=0)
  sell_price_entry = tk.Entry(frame) 
  sell_price_entry.grid(row=3, column=1)

  # label and entry
  buy_price_label= tk.Label(frame, text="Price from distributors")
  buy_price_label.grid(row=4, column=0)
  buy_price_entry = tk.Entry(frame)
  buy_price_entry.grid(row=4, column=1)

  def save_product():
    try:
      name = name_entry.get()
      quantity = int(quantity_entry.get())
      sell_price = int(sell_price_entry.get())
      buy_price = int(buy_price_entry.get())

      product = Product(name, quantity,sell_price, buy_price)
    
      add_product_to_db(product)
      show_messagebox('Add product', 'Added successfully', 'info')
      root.destroy()

    except:
      show_messagebox('Add product', 'Please insert valid values', 'error')

  # save btn
  save_btn = tk.Button(frame,text='Save 🔼', command=save_product)
  save_btn.config(width=20)
  save_btn.grid(row=5, column=0) 

  # cancel btn
  cancel_btn = tk.Button(frame,text='Cancel', command=root.destroy)
  cancel_btn.config(width=20)
  cancel_btn.grid(row=5, column=1) 

  root.mainloop() 


