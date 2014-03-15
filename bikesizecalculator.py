"""
bikesizecalculator:: a module for calculating the bike size appropriate for a person.

Copyright (c) 2014 Duane R. Crowe. All Rights Reserved.
"""


from craigslist import *

def calculate_bike_size(bike_type, person_height):
    try:
          
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
      
def generate_craigslist_query(bike_types, person_height):
        search(' http://portland.craigslist.org/', 'bia', 'Schwinn', 'T', 'sss')
        