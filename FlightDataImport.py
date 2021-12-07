from tkinter import *
from os import sep
import pandas as pd
import requests

"""
Class that facilitates the Flight data pull from OneSky

Returns:
    flight_array: returns the flight array.
"""
class FlightData():

    """
    Initiation method that establishes the coordinates getting pulled

    """
    def __init__(self):
        # Latitude and Longitude trimming from OpenSky, to be changed later
        USlongmin, USlatmin = -130.974, 20.038 #Lat and Long for all US "bottom left"
        USlongmax, USlatmax = -65.748, 50.214  # "top right"

        longmin, latmin = USlongmin, USlatmin
        longmax, latmax = USlongmax, USlatmax
        self.flightDataPull(latmin, longmin, longmax, latmax)

    """
    Facilitates the data pull

    returns: flight data array

    Arguments:
    latmin- minimum latitude
    longmin - minimum longitude
    longmax - max longitude
    latmax - max latitude    
    """
    def flightDataPull(latmin, longmin, longmax, latmax):
        #Pull Request from browser search of opensky using lat and long data
        user_name = 'zack.hagerty'
        password = 'SE300'
        OpenSky_datapull = 'https://'+user_name+':'+password+'@opensky-network.org/api/states/all?lamin=' + str(latmin) + '&lomin=' + str(longmin) + '&lamax=' + str(latmax) + '&lomax=' + str(longmax)
        OpenSky_data = requests.get(OpenSky_datapull).json()



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

        flight_array = flight_df.to_numpy()

        return flight_array

        #flight_df.to_csv('icons.csv')

    """
    Easy translation of lat and long to x, y coordinats for use in GUI
    """
    def coordinateTranslate(N, W):
        x=[]
        y=[]
        for i in range(len(N)):
            # Based on photo from Zack:
            # max width 1114, max height 642
            x_add = (1114/(130-65)) * (W[i] + 130)
            y_add = -(642/30) * (N[i] - 50)
            x.append(x_add)
            y.append(y_add)

        return x,y
    