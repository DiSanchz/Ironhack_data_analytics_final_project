import os
import pandas as pd
import h3
import folium
import json
from folium import Map, Marker, GeoJson
import branca.colormap as cm
from geojson.feature import *
import numpy as np



### LOADING DATASETS & DEFINING RELEVANT LISTS

airbnbiii = pd.read_csv('data/airbnb_h3.csv')
airbnb = airbnbiii[airbnbiii['hex_id_8']!='8834413681fffff']

spotsi = pd.read_csv('data/spots_mid_h3.csv')
spots = spotsi[spotsi['hex_id_8']!='88f294a333fffff']
grid8 = pd.read_csv('data/tnf_grid_8.csv')
with open('data/dictador.json', 'r') as myfile:
    dictador=myfile.read()
    
dictador = json.loads(dictador)
listhex_airbnb = airbnb['hex_id_8']
listhex_allspots = spots['hex_id_8']
listhex_natural = spots[spots['Atracciones naturales'] == 1]['hex_id_8']
listhex_cultural = spots[spots['Cultural'] == 1]['hex_id_8']
listhex_golf = spots[spots['Golf'] == 1]['hex_id_8']
listhex_amuse = spots[spots['Parques y ocio'] == 1]['hex_id_8']
listhex_beach = spots[spots['Playas destacadas'] == 1]['hex_id_8']
listhex_trans = spots[spots['Transporte'] == 1]['hex_id_8']
listhex_shop = spots[spots['Zonas comerciales'] == 1]['hex_id_8']



########################################
########################################
########################################
# Star dishes
########################################
########################################
########################################


def hex_pinpoint(listhex1 = listhex_airbnb, listhex2 = listhex_allspots, n='3', setting='near'):
    '''Retorna la visualización de kamaz_list_cat tras recibir los parámetros que esta requiere'''
    return visualize_hexagons(kamaz_list_cat(listhex1, listhex2, setting, n))

###################################################################################################

def kamaz_cloro(listhex1 = listhex_airbnb, listhex2 = listhex_allspots, setting='near', n='9426', legend = True ):
    
    cloro = kamaz_list_cat_pandas(listhex1, listhex2, setting, n)

    m_hex = choropleth_map(df_aggreg = cloro,
                       hex_id_field = "hex_id",
                       geometry_field = "geometry",
                       value_field = "time",
                       layer_name = "Choropleth 8",
                       with_legend = legend)

    return m_hex

###################################################################################################

def kamaz_cloro_ktop(listhex1 = listhex_airbnb, listhex2 = listhex_allspots, n='9426',  setting='near', legend = True, k = '3' ):
    
    cloro = kamaz_list_cat_pandas_ktop(listhex1, listhex2, setting, n, k)

    m_hex = choropleth_map(df_aggreg = cloro,
                       hex_id_field = "hex_id",
                       geometry_field = "geometry",
                       value_field = "time",
                       layer_name = "Choropleth 8",
                       with_legend = legend)

    return m_hex









########################################
########################################
########################################
# Other homemade meals
########################################
########################################
########################################


def kamaz(hex1,hex2):
    '''
    Return distance between two hexagons measured with travel time
    hex1 -> airbnb hex code res8
    hex2 -> spot hex code res8
    '''
    
    return dictador[f"{hex1} - {hex2}"]['rows'][0]['elements'][0]['duration']['value'] #duración del viaje en segundos
    


def kamaz_list_cat(listhex1 = listhex_airbnb, listhex2 = listhex_allspots, setting='near', n='3'):
    '''
    returns the airbnb hexes wich are on average closer/further of a given list of hexagons
    listhex1 = airbnb hexes list (presumably all airbnb hex_id_8)
    listhex2 = list of objective hexes (presumably all or a subset of spots hex_id_8)
    n = number of highlighted elements to show
    setting = near/far -> if near, return hexes which minimizes total distance, if far, return hexes which maximize it
    '''
    comparedict = {}
    

    for lx1 in listhex1:
        storage = []
        #print(lx1)
        for lx2 in listhex2:
            #print(lx2)
            storage.append(kamaz(lx1,lx2))
            
        comparedict[f'{lx1}'] = sum(storage)
        
    all_values= list(comparedict.values())
    all_values.sort()
    
    desired_list_near = []
    desired_list_far = []
    desired_near = all_values[:int(n)]
    desired_far = all_values[(int(n)+1)*(-1):-1]

    if setting == 'near':

        for i in desired_near:
            desired_list_near.append(list(comparedict.keys())[list(comparedict.values()).index(i)])
        return desired_list_near
        
    elif setting == 'far':

        for i in desired_far:
            desired_list_far.append(list(comparedict.keys())[list(comparedict.values()).index(i)])
            
        return desired_list_far

############################ - Pandas Version
    
def kamaz_list_cat_pandas(listhex1, listhex2, setting='near',  n='1426'):
    '''
    returns the airbnb hexes wich are on average closer/further of a given list of hexagons
    listhex1 = airbnb hexes list (presumably all airbnb hex_id_8)
    listhex2 = list of objective hexes (presumably all or a subset of spots hex_id_8)
    n = number of highlighted elements to show
    setting = near/far -> if near, return hexes which minimizes total distance, if far, return hexes which maximize it
    '''
    comparedict = {}
    
    for lx1 in listhex1:
        storage = []
        #print(lx1)
        for lx2 in listhex2:
            #print(lx2)
            storage.append(kamaz(lx1,lx2))
            
        comparedict[f'{lx1}'] = sum(storage)
        
    all_values= list(comparedict.values())
    all_values.sort()
    
    desired_list = []
    desired_near = all_values[:int(n)]
    desired_far = all_values[(int(n)+1)*(-1):-1]

    if setting == 'near':
    
        
        for i in desired_near:
            desired_list.append(list(comparedict.keys())[list(comparedict.values()).index(i)])
        
        
    elif setting == 'far':
    
        
        for i in desired_far:
            desired_list.append(list(comparedict.keys())[list(comparedict.values()).index(i)])
    
    
    framesit = pd.DataFrame(desired_list, columns=['hex_id'])
    framesit['geometry'] = framesit['hex_id'].apply(lambda x: {"type": "Polygon",
                                                   "coordinates":
                                                   [h3.h3_to_geo_boundary(
                                                       h=x, geo_json=True)]})

    if setting == 'near':                                                   
        framesit['time'] = desired_near
    elif setting == 'far':
        framesit['time'] = desired_far
    
    return framesit


############################ - #N top elements Pandas Version


def kamaz_list_cat_pandas_ktop(listhex1, listhex2, setting='near', n='3', k='2'):
    '''
    returns the airbnb hexes wich are on average closer/further of a given list of hexagons
    listhex1 = airbnb hexes list (presumably all airbnb hex_id_8)
    listhex2 = list of objective hexes (presumably all or a subset of spots hex_id_8)
    n = number of highlighted elements to show (must be integer)
    setting = near/far -> if near, return hexes which minimizes total distance, if far, return hexes which maximize it
    k = number of closest elements to consider (must be integer)
    '''
    comparedict = {}
    
    for lx1 in listhex1:
        storage = []
        #print(lx1)
        for lx2 in listhex2:
            #print(lx2)
            storage.append(kamaz(lx1,lx2))
            
        storage.sort()
        
        if setting == 'near':
            comparedict[f'{lx1}'] = sum(storage[:int(k)])
            
        elif setting == 'far':
            comparedict[f'{lx1}'] = sum(storage[:(int(k))])
        
    all_values= list(comparedict.values())
    all_values.sort()
    
    desired_list = []
    desired_near = all_values[:int(n)]
    desired_far = all_values[(int(n)+1)*(-1):-1]

    if setting == 'near':
    
        
        for i in desired_near:
            desired_list.append(list(comparedict.keys())[list(comparedict.values()).index(i)])
        
        
    elif setting == 'far':
    
        
        for i in desired_far:
            desired_list.append(list(comparedict.keys())[list(comparedict.values()).index(i)])
    
    
    framesit = pd.DataFrame(desired_list, columns=['hex_id'])
    framesit['geometry'] = framesit['hex_id'].apply(lambda x: {"type": "Polygon",
                                                   "coordinates":
                                                   [h3.h3_to_geo_boundary(
                                                       h=x, geo_json=True)]})

    if setting == 'near':                                                   
        framesit['time'] = desired_near
    elif setting == 'far':
        framesit['time'] = desired_far
    
    return framesit

########################################
########################################
########################################
#H3 adapted funcs below
########################################
########################################
########################################

def visualize_hexagons(hexagons, color="red", folium_map=None):
    """
    hexagons is a list of hexcluster. Each hexcluster is a list of hexagons. 
    eg. [[hex1, hex2], [hex3, hex4]]
    """
    polylines = []
    lat = []
    lng = []
    for hex in hexagons:
        polygons = h3.h3_set_to_multi_polygon([hex], geo_json=False)
        # flatten polygons into loops.
        outlines = [loop for polygon in polygons for loop in polygon]
        polyline = [outline + [outline[0]] for outline in outlines][0]
        lat.extend(map(lambda v:v[0],polyline))
        lng.extend(map(lambda v:v[1],polyline))
        polylines.append(polyline)
    
    if folium_map is None:
        m = folium.Map(location=[sum(lat)/len(lat), sum(lng)/len(lng)], zoom_start=10, tiles='cartodbpositron')
    else:
        m = folium_map
    for polyline in polylines:
        my_PolyLine=folium.PolyLine(locations=polyline,weight=3,color=color) # weight = grosor de la frontera del hex
        m.add_child(my_PolyLine)
    return m


def choropleth_map(df_aggreg, hex_id_field, geometry_field, value_field,
                   layer_name, initial_map = None, kind = "linear",
                   border_color = 'black', fill_opacity = 0.7,
                   with_legend = False):

    """Plots a choropleth map with folium"""

    if initial_map is None:
        initial_map = base_empty_map()

    # the custom colormap depends on the map kind
    if kind == "linear":
        min_value = df_aggreg[value_field].min()
        max_value = df_aggreg[value_field].max()
        m = round((min_value + max_value) / 2, 0)
        custom_cm = cm.LinearColormap(['green', 'yellow', 'red'],
                                      vmin = min_value,
                                      vmax = max_value)
    elif kind == "outlier":
        # for outliers, values would be -1,0,1
        custom_cm = cm.LinearColormap(['blue', 'white', 'red'],
                                      vmin=-1, vmax=1)
    elif kind == "filled_nulls":
        min_value = df_aggreg[df_aggreg[value_field] > 0][value_field].min()
        max_value = df_aggreg[df_aggreg[value_field] > 0][value_field].max()
        m = round((min_value + max_value) / 2, 0)
        custom_cm = cm.LinearColormap(['silver', 'green', 'yellow', 'green'],
                                      index = [0, min_value, m, max_value],
                                      vmin = min_value,
                                      vmax = max_value)

    # create geojson data from dataframe
    geojson_data = hexagons_dataframe_to_geojson(df_aggreg, hex_id_field,
                                                 geometry_field, value_field)

    # plot on map
    GeoJson(
        geojson_data,
        style_function=lambda feature: {
            'fillColor': custom_cm(feature['properties']['value']),
            'color': border_color,
            'weight': 1,
            'fillOpacity': fill_opacity
        },
        name = layer_name
    ).add_to(initial_map)

    # add legend (not recommended if multiple layers)
    if with_legend is True:
        custom_cm.add_to(initial_map)

    return initial_map

def base_empty_map():
    """Prepares a folium map centered in a central GPS point of Tenerife"""
    m = Map(location = [28.273007, -16.640793],
            zoom_start = 9.5,
            tiles = "cartodbpositron",
            attr = '''© <a href="http://www.openstreetmap.org/copyright">
                      OpenStreetMap</a>contributors ©
                      <a href="http://cartodb.com/attributions#basemaps">
                      CartoDB</a>'''
            )
    return m

def hexagons_dataframe_to_geojson(df_hex, hex_id_field,
                                  geometry_field, value_field,
                                  file_output = None):

    """Produce the GeoJSON representation containing all geometries in a dataframe
     based on a column in geojson format (geometry_field)"""

    list_features = []

    for i, row in df_hex.iterrows():
        feature = Feature(geometry = row[geometry_field],
                          id = row[hex_id_field],
                          properties = {"value": row[value_field]})
        list_features.append(feature)

    feat_collection = FeatureCollection(list_features)

    geojson_result = json.dumps(feat_collection)

    # optionally write to file
    if file_output is not None:
        with open(file_output, "w") as f:
            json.dump(feat_collection, f)

    return geojson_result


########################################
########################################
########################################
# Mc menus
########################################
########################################
########################################


def combo2(listhexa = listhex_beach, listhexb = listhex_natural, ka = '2', kb = '2'):
    
    cloro_one = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexa, setting='near', n='9426', k= ka)
    cloro_two = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexb, setting='near', n='9426', k= kb)
    
    lets_c1 = cloro_one.merge(cloro_two, on = 'hex_id', suffixes = ['','_2'])
    
    lets_c1['combo'] = lets_c1['time']*0.5 + lets_c1['time_2']*0.5
    
    m_hex = choropleth_map(df_aggreg = lets_c1,
                       hex_id_field = "hex_id",
                       geometry_field = "geometry",
                       value_field = "combo",
                       layer_name = "Choropleth 8",
                       with_legend = False)

    return m_hex


def combo3(listhexa = listhex_beach, listhexb = listhex_natural, listhexc = listhex_cultural, ka = '2', kb = '2', kc = '2'):
    
    cloro_one = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexa, setting='near', n='9426', k = ka)
    cloro_two = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexb, setting='near', n='9426', k = kb)
    cloro_three = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexc, setting='near', n='9426', k = kc)
    
    lets_c1 = cloro_one.merge(cloro_two, on = 'hex_id', suffixes = ['','_2'])
    lets_c2 = lets_c1.merge(cloro_three, on = 'hex_id', suffixes = ['','_3'])
    
    lets_c2['combo'] = lets_c2['time']*0.3333 + lets_c2['time_2']*0.3333 + lets_c2['time_3']*0.3334
    
    m_hex = choropleth_map(df_aggreg = lets_c2,
                       hex_id_field = "hex_id",
                       geometry_field = "geometry",
                       value_field = "combo",
                       layer_name = "Choropleth 8",
                       with_legend = False)

    return m_hex


def combo4(listhexa = listhex_beach, listhexb = listhex_natural, listhexc = listhex_cultural, listhexd = listhex_shop,
           ka = '2', kb = '2', kc = '2', kd = '2'):
    
    cloro_one = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexa, setting='near', n='9426', k = ka)
    cloro_two = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexb, setting='near', n='9426', k = kb)
    cloro_three = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexc, setting='near', n='9426', k = kc)
    cloro_four = kamaz_list_cat_pandas_ktop(listhex1 = listhex_airbnb, listhex2 = listhexd, setting='near', n='9426', k = kd)
    
    lets_c1 = cloro_one.merge(cloro_two, on = 'hex_id', suffixes = ['','_2'])
    lets_c2 = lets_c1.merge(cloro_three, on = 'hex_id', suffixes = ['','_3'])
    lets_c3 = lets_c2.merge(cloro_four, on = 'hex_id', suffixes = ['','_4'])
    
    lets_c3['combo'] = lets_c3['time']*0.25 + lets_c3['time_2']*0.25 + lets_c3['time_3']*0.25 + lets_c3['time_4']*0.25
    
    m_hex = choropleth_map(df_aggreg = lets_c3,
                       hex_id_field = "hex_id",
                       geometry_field = "geometry",
                       value_field = "combo",
                       layer_name = "Choropleth 8",
                       with_legend = False)

    return m_hex