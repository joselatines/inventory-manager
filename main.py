import tkinter as tk
from client_manager.gui_app import MyFrame, nav_bar

# create the window
# root === window

root = tk.Tk()
root.title('App')
root.resizable(0,0)

nav_bar(root)

# create the frame
""" frame = tk.Frame(root)
frame.pack()
frame.config(width=500, height=500) """

app = MyFrame(root)

# starts the window
root.mainloop()

