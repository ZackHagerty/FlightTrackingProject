from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from os import sep
import pandas as pd
import numpy as np
import requests
import json
import csv
from FlightDataImport import FlightData
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
    'geo_altitude','squawk','spi','position_source','unknown']
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
flight_arrayFull = flight_df.to_numpy()
#flight_array = np.delete(flight_arrayFull, obj=0, axis=0)
#print(flight_arrayFull[:,1])

for i in range(len(flight_arrayFull)):
    
    if flight_arrayFull[i,1].startswith('AAL'):
        print('AAL')

    if flight_arrayFull[i,1].startswith('AAY'):
        print('1')

    if flight_arrayFull[i,1].startswith('ACA'):
        print('2')

    if flight_arrayFull[i,1].startswith('AFR'):
        print('3')

    if flight_arrayFull[i,1].startswith('AMX'):
        print('4')

    if flight_arrayFull[i,1].startswith('ASA'):
        print('5')

    if flight_arrayFull[i,1].startswith('DAL'):
        print('6')

    if flight_arrayFull[i,1].startswith('FFT'):
        print('7')

    if flight_arrayFull[i,1].startswith('JBU'):
        print('8')

    if flight_arrayFull[i,1].startswith('NKS'):
        print('9')

    if flight_arrayFull[i,1].startswith('SWA'):
        print('10')

    if flight_arrayFull[i,1].startswith('UAL'):
        print('11')

    if flight_arrayFull[i,1].startswith('UPS'):
        print('12')

    if flight_arrayFull[i,1].startswith('FDX'):
        print('13')