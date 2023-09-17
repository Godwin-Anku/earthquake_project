import tkinter as tk
from tkinter import ttk
import numpy as np

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
        self.mainframe = Mainframe(self)
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

        #create solve button
        self.solve_button = ttk.Button(self, text = 'Solve', command = self.calculate_woodand_mag)

        #create entry
        self.mag_entry = ttk.Entry(self)

        #create grid
        self.columnconfigure((0, 1), weight = 1)
        self.rowconfigure((0, 1),weight = 1)

        #place widgets
        mag_label.grid(row = 0, column = 0, sticky = 'w')
        zero_mag_label.grid(row = 1, column = 0, sticky = 'w')

        #entry layout
        self.mag_entry.grid(row = 0, column = 1, sticky = 'we')

        #solve button
        self.solve_button.grid(row = 1, column = 1, sticky = 'we')

    def calculate_woodand_mag(self):
        try:
            magnitude = float(self.mag_entry.get())
            zero_mag_amplitude = 1.0
            woodand_mag_amplitude = np.power(10, magnitude * zero_mag_amplitude)
            self.master.mainframe.woodand_mag_label.config(text = f'Maximum Wood-Anderson amplitude: {woodand_mag_amplitude}')
        except ValueError:
            self.master.mainframe.woodand_mag_label.config(text = 'Please enter a valid number')

class Mainframe(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, rely = 0.5, relwidth = 1, relheight = 0.5)

        #create widgets
        self.woodand_mag_label = ttk.Label(self, text = 'Maximum Wood-Anderson amplitude recorded on a Wood-Anderson seismograph')
        self.woodand_mag_label.pack(expand = True, fill = 'both')

App('Earthquake Analysis', (600,400))
