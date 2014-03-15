# This script opens a simple GUI that allows a user to find the proper bike size for different sorts of bikes
# using the cyclist's measurements and preferences.
from Tkinter import *
import ttk
import bikesizecalculator

    
root = Tk()
root.title("Feet to Meters")

bicycle_types = ["Touring", "Commuter", "Track", "Road", "Mixte"]

number_of_types = len(bicycle_types)
bicycle_types_selected = dict(zip(bicycle_types, [0]* number_of_types))

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

person_height = IntVar()



current_column = 2
current_row = 2
for bicycle_type in bicycle_types:
    indicator = StringVar()
    bicycle_types_selected[bicycle_type] = indicator
    ttk.Checkbutton(mainframe, text=bicycle_type, variable=indicator).grid(
                    column=current_column, row=current_row, sticky=W)
    print bicycle_type
    print bicycle_types_selected[bicycle_type]
    current_row += 1

slider = Scale(mainframe, label="Slider", from_=20, to=100, orient=HORIZONTAL, tickinterval=5, length=600, variable = person_height)
slider.grid(column=current_column, row=current_row, sticky=E)
current_row += 1


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', bikesizecalculator.generate_craigslist_query(bicycle_types, person_height) )

root.mainloop()
