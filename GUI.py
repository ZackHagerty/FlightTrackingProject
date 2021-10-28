from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np

from FlightDataImport import FlightData

class GUI():

    root = Tk()

    #Sets up the frame and background canvas
    frame = Frame(root)
    frame.pack()
    canvas = Canvas(frame, bg = "black", width=1114, height=642)
    canvas.pack()
    
    #background image of US
    USAMapImage1 = PhotoImage(file = './U.S.A Images/Untitled.png')
    canvas.create_image(557,(321),image=USAMapImage1)

    #test image of plane
    plane2 = Image.open('./icons/airplane-icon-2-19.png') # 19x19 pixel image
    plane2Rot = plane2.rotate(45,Image.BICUBIC) # rotate 45deg, retain quality
    plane2done = ImageTk.PhotoImage(plane2Rot) # make it a photoimage (transparent bg)

    img_ref = []
    plane_ref = []
    
    flight_chart_array = FlightData.flightDataPull(20.038,-87.928,-79.80946,50.214)

    true_Array = flight_chart_array[:,10]
    long_Array = flight_chart_array[:,5]
    lat_Array = flight_chart_array[:,6]

    true_Array = np.delete(true_Array, 0, 0)
    long_Array = np.delete(long_Array, 0, 0)
    lat_Array = np.delete(lat_Array, 0, 0)

    x_Array, y_Array = FlightData.coordinateTranslate(lat_Array,long_Array)
    #print(long_Array)

    for i in range(len(x_Array)):
        plane3 = plane2.rotate(true_Array[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(x_Array[i], y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    root.mainloop()



if __name__ == "__main__":
    

    Main = GUI()
