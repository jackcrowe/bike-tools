""" This script opens a simple GUI that allows a user to find the proper bike size for different sorts of bikes
    using the cyclist's measurements and preferences."""

from Tkinter import *
import ttk
import bikesizecalculator

# Calls the bikesizecalculator method. Used for the button press
def findbikes():
    search_types = []
    for bicycle_type in bicycle_types:
        if bicycle_types_selected[bicycle_type].get() == '1':
	    search_types.append(bicycle_type)
    querystring = bikesizecalculator.generate_craigslist_query(search_types, inseam.get() )
    query.set(querystring)
 
# create root window object    
root = Tk()
root.title("Bike Finder")

# The types of bicycles that can be searched for, and a dictionary to store whether
# each type of bike was selected
bicycle_types = ["Touring", "Commuter", "Track", "Road", "Mixte"]
number_of_types = len(bicycle_types)
bicycle_types_selected = dict(zip(bicycle_types, [0]* number_of_types))

# Creates a main window using ttk, with appropriate grid and padding
mainframe = ttk.Frame(root, padding="2 2 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# variable that stores the person's height in cm
inseam = IntVar()
query = StringVar()

# dynamically creates checkbox buttons for bike types
# manages the grid and creates 2 columns of checkboxes
current_column = 1
current_row = 1
item_number = 0
for bicycle_type in bicycle_types:
    # for each bike type, create a checkbox and move to the next row
    indicator = StringVar()
    bicycle_types_selected[bicycle_type] = indicator
    ttk.Checkbutton(mainframe, text=bicycle_type, variable=indicator).grid(
                    row=item_number/2, column=item_number%2, sticky=W)
    item_number += 1
                    
current_row = item_number/2 + 2

# Create a slider to select height in centimeters
slider = Scale(mainframe, label="Inseam in inches", from_=27, to=37, orient=HORIZONTAL, tickinterval=1, length=450, variable = inseam)
slider.grid(column=0, row=current_row, sticky=W, columnspan=2)
current_row += 1

# Button that is used to call the generation of the query
findbutton = ttk.Button(mainframe, text='Find Bikes!', command=findbikes)
findbutton.grid(column=0, row=current_row, sticky=E)
current_row += 1

# on the last row, display the query
query_entry = ttk.Entry(mainframe, textvariable=query)
query_entry.grid(column=0, row=current_row, sticky=W, columnspan=2)

# for each of the object created, do magic grid operation
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


    
root.mainloop()