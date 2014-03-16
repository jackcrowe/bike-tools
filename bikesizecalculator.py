"""
bikesizecalculator:: a module for calculating the bike size appropriate for a person.
"""

# Uses the craigslist python library from github
# https://github.com/jackcrowe/bike-tools.git
from craigslist import *

# globals to store categorization of bike types
mountain_geometry = "MTN"
road_geometry = "ROAD"
stepthrough_geometry = "STEP"

# dictionary for bike type to geometry categorization
bike_type_categories = {
     'Touring' : road_geometry,
     'Commuter' : road_geometry,
     'Track' : road_geometry,
     'Road' : road_geometry,
     'Mixte' : stepthrough_geometry,
     'Hardtail' : mountain_geometry,
     'XC' : mountain_geometry }

""" calculates the correct bike size for the given bike type and person's height"""
def calculate_bike_size(bike_type, person_height):
    try:
        category = get_geometry_categorization(bike_type)
        if category == road_geometry:
            return 22
        return 0
    except ValueError:
        pass
      
""" generates a craigslist given an array of bike types and a person's height"""
def generate_craigslist_query(bike_types, person_height):
    search('http://portland.craigslist.org/', 'bia', 'Schwinn', 'T', 'sss')
    return

""" looks up the category of geometry for a bike type """
def get_geometry_categorization(bike_type):
    return bike_type_categories[bike_type]