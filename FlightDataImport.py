#from tkinter import *
#from tkinter import ttk
#from PIL import ImageTk, Image
from os import sep
import pandas as pd
import requests
import json
import csv

class FlightData():

    def __init__(self):
        # Latitude and Longitude trimming from OpenSky, to be changed later
        longmin, latmin = -130.974, 20.038
        longmax, latmax = -65.748, 50.214
        self.flightDataPull(latmin, longmin, longmax, latmax)

    def flightDataPull(self, latmin, longmin, longmax, latmax):
        #Pull Request from browser search of opensky using lat and long data
        OpenSky_datapull = 'https://opensky-network.org/api/states/all?lamin=' + str(latmin) + '&lomin=' + str(longmin) + '&lamax=' + str(latmax) + '&lomax=' + str(longmax)
        OpenSky_data = requests.get(OpenSky_datapull).json()



        columns = ['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground (T/F)','velocity','true_track','vertical_rate','sensors',
        'geo_altitude','squawk','spi','position_source']
        flight_df=pd.DataFrame(OpenSky_data['states'],columns=columns)
        flight_df=flight_df.fillna('No Data')


        flight_df.to_csv('icons.csv')