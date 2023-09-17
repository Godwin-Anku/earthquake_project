import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):

        #main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1]) 
        self.maxsize(size[0], size[1])   

        #create widgets
        self.menu = Menu(self)

        #run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 0.5)
        self.create_widgets()

    def create_widgets(self):
        mag_label = ttk.Label(self, text = 'Magnitude')
        zero_mag_label = ttk.Label(self, text = 'Amplitude of zero magnitude earthquake')

        #create entry
        mag_entry = ttk.Entry(self)

        #create grid
        self.columnconfigure((0, 1), weight = 1)
        self.rowconfigure((0, 1),weight = 1)

        #place widgets
        mag_label.grid(row = 0, column = 0, sticky = 'w')
        zero_mag_label.grid(row = 1, column = 0, sticky = 'w')

        #entry layout
        mag_entry.grid(row = 0, column = 1, sticky = 'we')


App('Earthquake Analysis', (600,400))