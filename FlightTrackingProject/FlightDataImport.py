from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import json



#Latitude and Longitude trimming from OpenSky, to be changed later
longmin, latmin = -125.974, 30.038
longmax, latmax = -68.748, 52.214

#Pull Request from browser search of opensky using lat and long data
OpenSky_datapull = 'https://opensky-network.org/api/states/all?lamin=' + str(latmin) + '&lomin=' + str(longmin) + '&lamax=' + str(latmax) + '&lomax=' + str(longmax)
OpenSky_data = requests.get(OpenSky_datapull).json()
