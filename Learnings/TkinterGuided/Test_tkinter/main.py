from tkinter import *
from tkinter import ttk

root = Tk()
#root.geometry("1024x800")
root.title("CRoL")


menuframe = ttk.Frame(root,
                      borderwidth=2,
                      relief= 'sunken',
                      padding="15 15 3 3")

menuframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe = ttk.Frame(root, padding="15 15 3 3")
mainframe.grid(column=1, row=0, sticky=(N,W,E,S))

menu_title = ttk.Label(menuframe, text="Menu", font=("Arial", 25), padding="10 10 10 10").grid(column=1, row= 0)

#Menu buttons to the left
ttk.Button(menuframe, text="Home", width= 25).grid(column=1, row=1)
ttk.Button(menuframe, text="Character Screen", width= 25).grid(column=1, row=2)
ttk.Button(menuframe, text="Inventory", width= 25).grid(column=1, row=3)

screen_title = StringVar()
screen_title.set("Home")

screen_label=ttk.Label(mainframe, textvariable=screen_title, font= ("Arial", 25))
screen_label.grid(column=4, row=1, padx= 3, pady=3)

root.mainloop()