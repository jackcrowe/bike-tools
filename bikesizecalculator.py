"""
bikesizecalculator:: a module for calculating the bike size appropriate for a person.
"""

from math import *

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
def calculate_bike_size(bike_type, inseam):
    category = get_geometry_categorization(bike_type)
    if category == road_geometry:
        return get_road_size(inseam)
    else:
        return get_mountain_size(inseam)
      
""" generates a craigslist query given an array of bike types and a person's height"""
def generate_craigslist_query(bike_types, inseam):
    if len(bike_types) == 0:
        return ''
    query = ''
    for bike_type in bike_types:
        bike_size = int(calculate_bike_size(bike_type, inseam))
        query += '"'+bike_type+' '+str(bike_size)+'"|'
    location = 'http://chicago.craigslist.org/'
    category = 'bik'
    search_type = 'T'
    search_url = '%ssearch/%s?query=%s&srchType=%s' % (
            location, category, query, search_type)
    return search_url

""" looks up the category of geometry for a bike type """
def get_geometry_categorization(bike_type):
    return bike_type_categories[bike_type]
    
""" returns the appropriate road bike size for a person of the given height """
def get_road_size(inseam):
    return floor(1.72*float(inseam) - 0.68)
    
""" returns the appropriate mountain bike size for a person of the given height """
def get_mountain_size(inseam):
    return inseam-10
 