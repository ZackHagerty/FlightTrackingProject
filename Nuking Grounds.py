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

USlongmin, USlatmin = -130.974, 20.038 #Lat and Long for all US "bottom left"
USlongmax, USlatmax = -65.748, 50.214  # "top right"

FLlongmin, FLlatmin = -87.928, 24.228337
FLlongmax, FLlatmax = -79.80946, 31.125


longmin, latmin = USlongmin, USlatmin
longmax, latmax = USlongmax, USlatmax

def flightDataPull(latmin, longmin, longmax, latmax):
        #Pull Request from browser search of opensky using lat and long data
        user_name = 'zack.hagerty'
        password = 'SE300'
        OpenSky_datapull = 'https://'+user_name+':'+password+'@opensky-network.org/api/states/all?lamin=' + str(latmin) + '&lomin=' + str(longmin) + '&lamax=' + str(latmax) + '&lomax=' + str(longmax)
        OpenSky_data = requests.get(OpenSky_datapull).json()