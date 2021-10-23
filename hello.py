from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from os import sep
import pandas as pd
import requests
import json
import csv
# prints the words 'hello world'
print("Hello World")
USlongmin, USlatmin = -130.974, 20.038 #Lat and Long for all US "bottom left"
USlongmax, USlatmax = -65.748, 50.214  # "top right"

FLlongmin, FLlatmin = -87.928, 24.228337
FLlongmax, FLlatmax = -79.80946, 31.125


longmin, latmin = USlongmin, USlatmin
longmax, latmax = USlongmax, USlatmax

OpenSky_datapull = 'https://opensky-network.org/api/states/all?lamin=' + str(latmin) + '&lomin=' + str(longmin) + '&lamax=' + str(latmax) + '&lomax=' + str(longmax)
OpenSky_data = requests.get(OpenSky_datapull).json()
#https://opensky-network.org/api/states/all?lamin=20.038&lomin=-130.974&lamax=50.214&lomax=-65.748

try:
    columns = ['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground (T/F)','velocity','true_track','vertical_rate','sensors',
    'geo_altitude','squawk','spi','position_source','test']
    flight_df=pd.DataFrame(OpenSky_data['states'],columns=columns)
    flight_df=flight_df.fillna('No Data')
except ValueError:
    columns = ['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground (T/F)','velocity','true_track','vertical_rate','sensors',
    'geo_altitude','squawk','spi','position_source']
    flight_df=pd.DataFrame(OpenSky_data['states'],columns=columns)
    flight_df=flight_df.fillna('No Data')



#columns = ['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground (T/F)','velocity','true_track','vertical_rate','sensors',
#'geo_altitude','squawk','spi','position_source']
#flight_df=pd.DataFrame(OpenSky_data['states'],columns=columns)
#flight_df=flight_df.fillna('No Data')


flight_df.to_csv('test.csv')
flight_array = flight_df.to_numpy
print(flight_array)