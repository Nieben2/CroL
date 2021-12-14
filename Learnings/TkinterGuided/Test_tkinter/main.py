import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

import threading
import time
from Energy import energy
from Skills import skills

energy_obj = energy()
skills = skills()


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("CroL")
        self.iconbitmap("icon.ico")
        self.geometry("1600x800")
        #self.grid_columnconfigure(10, weight=10)
        mainframe = tk.Frame(self, bg="gray", borderwidth=0)
        mainframe.grid(row=1, column=1, sticky="NESW")
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Status bar frame definition
        statusBar = tk.Frame(self, borderwidth= 5, relief="ridge")
        statusBar.grid(columnspan=2, row=0, pady=5, padx=5, sticky="ew")
        statusBar.grid_rowconfigure(0, weight=1)
        statusBar.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)

        #Status label - Not used. Only for help in placing the statusbar
        #statuslabel = tk.Label(statusBar, text="Statusbar", font=self.title_font)
        #statuslabel.grid(column=1, row=0, pady=5, padx=5, sticky="nw")
        #statuslabel.place(relx=.5, rely=.5, anchor="center")

        #Progress bar - Not sure if i want a progress bar in the status field
        #progressbar = ttk.Progressbar(statusBar,
        #                         orient="horizontal",
        #                         mode='determinate',
        #                         length= 500)
        #progressbar.grid(column=10, row= 1, sticky="e")
        #label_exp = tk.Label(statusBar,
        #                     text="Progress",).grid(column=10, row=0)


        #Menu frame definition
        menuframe = tk.Frame(mainframe, borderwidth= 5, relief="ridge")
        menuframe.grid(column=0, row=0, pady=0, padx=0, sticky="nws")
        #mainframe.grid_rowconfigure(0, weight=1)
        #mainframe.grid_columnconfigure(0, weight=1)
        label = tk.Label(menuframe, text="Menu", font=self.title_font)
        label.grid(column=0, row=0, pady=0, padx=5)

        # Menu buttons

        button_home = tk.Button(menuframe,
                                     text="Home",
                                     command=lambda: self.show_frame("Homescreen")). \
            grid(column=0, row=1, pady=5, padx=5, sticky="ew")

        button_character = tk.Button(menuframe,
                                     text="Character Screen",
                                     command=lambda: self.show_frame("Character_screen")). \
            grid(column=0, row=2, pady=5, padx=5, sticky="ew")

        button_skills = tk.Button(menuframe,
                                  text="Skills",
                                  command=lambda: self.show_frame("Skillscreen")). \
            grid(column=0, row=3, pady=5, padx=5, sticky="ew")

        button_gather = tk.Button(menuframe,
                                     text="Gather Materials",
                                     command=lambda: self.show_frame("Gather")). \
            grid(column=0, row=4, pady=5, padx=5, sticky="ew")

        button_test = tk.Button(menuframe,
                                     text="test",
                                     command=lambda: self.show_frame("Inventory")). \
            grid(column=0, row=5, pady=5, padx=5, sticky="ew")

        # the container is where we'll stack a bunch of frames

        container = tk.Frame(mainframe)
        container.grid(column=1, row=0, pady=0, padx=0, sticky="nesw")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Homescreen, Character_screen, Skillscreen, Gather):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nesw")




        self.show_frame("Homescreen")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class Homescreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth= 5, relief="ridge")
        self.controller = controller
        label = tk.Label(self, text="This place feels like home", font=controller.title_font)
        #label_lspace = tk.Label(self, text="                                        ")
        #label_rspace = tk.Label(self, text="                                        ")
        #label_lspace.grid(column= 0, row=3, pady=10)
        #label_rspace.grid(column=5, row=3, pady=10)
        label.grid(column=1, row=1, pady=5, sticky="ew")
        #self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        tk.Button(self, text="Work",
                  command= lambda : self.work_button()). \
            grid(column=0, row=4, pady=5, padx=5, sticky="ew")

        tk.Button(self, text="Rest",
                  command=lambda: self.rest_button()). \
            grid(column=0, row=5, pady=5, padx=5, sticky="ew")



    def work_button(self):
        energy_obj.energy_loss(20,0.8)

        tk.Label(self, text=energy_obj.energy).grid(column=1, row=4, pady=5, padx=5, sticky="ew")

    def rest_button(self):
        energy_obj.energy_gain(30)

        tk.Label(self, text=energy_obj.energy).grid(column=1, row=4, pady=5, padx=5, sticky="ew")


class Character_screen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth= 2, relief="ridge")
        self.controller = controller
        label = tk.Label(self, text="Attributes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class Skillscreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth= 2, relief="ridge")
        self.controller = controller
        label = tk.Label(self, text="Skills", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class Gather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth=5, relief="ridge")
        self.controller = controller
        self.gather_progress = tk.IntVar()
        self.gather_result = tk.StringVar()
        label = tk.Label(self, text="You venture forth into the wilds", font=controller.title_font)
        label.grid(column=5, row=1, pady=5, sticky="ew")
        #self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(5, weight=1)
        tk.Label(self, textvariable=self.gather_result).grid(column=2, row=4)


        tk.Button(self, text="Gather",
                  command= lambda : self.threading()). \
            grid(column=0, row=4, pady=5, padx=5, sticky="ew")

    def progressbar(self):
        self.gather_pb = ttk.Progressbar(self,
                        orient="horizontal",
                        mode='determinate',
                        length= 250,
                        variable=self.gather_progress).grid(column=1, row=4)




    def threading(self):
        def btn_gather_click():
            self.progressbar()
            self.gather_progress.set(0)
            for i in range(100):
                self.update_idletasks()
                self.gather_progress.set(i+1)
                self.after(10)
                if self.gather_progress.get() >= 100:
                    self.gather_result.set(skills.gathering(30))
                    self.threading()

        t = threading.Thread(None, btn_gather_click, ())
        t.start()




if __name__ == "__main__":
    app = Window()
    app.mainloop()
