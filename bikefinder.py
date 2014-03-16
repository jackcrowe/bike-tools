""" This script opens a simple GUI that allows a user to find the proper bike size for different sorts of bikes
    using the cyclist's measurements and preferences."""

from Tkinter import *
import ttk
import bikesizecalculator

# create root window object    
root = Tk()
root.title("Bike Finder")

# The types of bicycles that can be searched for, and a dictionary to store whether
# each type of bike was selected
bicycle_types = ["Touring", "Commuter", "Track", "Road", "Mixte"]
number_of_types = len(bicycle_types)
bicycle_types_selected = dict(zip(bicycle_types, [0]* number_of_types))

# Creates a main window using ttk, with appropriate grid and padding
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# variable that stores the person's height in cm
person_height = IntVar()

# dynamically creates checkbox buttons for bike types
current_column = 2
current_row = 2
for bicycle_type in bicycle_types:
    # for each bike type, create a checkbox and move to the next row
    indicator = StringVar()
    bicycle_types_selected[bicycle_type] = indicator
    ttk.Checkbutton(mainframe, text=bicycle_type, variable=indicator).grid(
                    column=current_column, row=current_row, sticky=W)
    print bicycle_type
    print bicycle_types_selected[bicycle_type]
    current_row += 1

# Create a slider to select height in centimeters
slider = Scale(mainframe, label="Slider", from_=20, to=100, orient=HORIZONTAL, tickinterval=5, length=600, variable = person_height)
slider.grid(column=current_column, row=current_row, sticky=E)
current_row += 1

# for each of the object created, do magic grid operation
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

findbutton = ttk.Button(mainframe, text='Find Bikes!', command=bikesizecalculator.generate_craigslist_query(bicycle_types, person_height))
findbutton.grid(column=3, row=current_row, sticky=E)
    
root.mainloop()