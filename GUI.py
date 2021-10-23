from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np

from FlightDataImport import FlightData

class GUI():

    root = Tk()
    
    #old image files or something
    #USAMapImage = ImageTk.PhotoImage(file = './U.S.A Images/Untitled.png')
    #AirplaneIconImage = ImageTk.PhotoImage(file = './icons/airplane-icon-2.png')


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
    

    # cant rotate this
    # plane = PhotoImage(file = './icons/airplane-icon-2-19.png')
    
    
    #possibility for making a plane and having it rotate
    # problem: it only makes 1 plane. Any time we place it, it moves and doesn't make a new one
    #def makePlane(canvas,plane,x,y,heading):
        #plane1 = plane.rotate(heading)
        #plane1done = ImageTk.PhotoImage(plane1)
        #canvas.create_image(x,y,image=plane1done)

    # see how this should make 2 new planes, but it does not
    # I commented this out since, as far as I could tell, it didn't do anything on the GUI, we can probably remove -D
    #makePlane(canvas,plane2, 100, 321, 45)
    #makePlane(canvas,plane2, 300, 321, 135)

    img_ref = []
    plane_ref = []
    #see how this only makes 1 plane, the one that should be plane 6
    #for i in range(6):
        #print("Ran {0} times".format(i)) #iterator
        #makePlane(canvas,plane2, 50*i, 50*i, 139)
        
        #these three lines is a duplicate of the makePlane method
        #plane3 = plane2.rotate(33*i, Image.BICUBIC)
        #plane3done = ImageTk.PhotoImage(plane3)
        #canvas.create_image(30*i,30*i,image=plane3done)
        #img_ref.append(plane3done)
    
    flight_chart_array = FlightData.flightDataPull(20.038,-130.974,-65.748,50.214)

    #true_Array = datafile['true_track'].tolist()
    #long_Array = datafile['long'].tolist()
    #lat_Array = datafile['lat'].tolist()
    true_ArrayFull = flight_chart_array[:,10]
    long_ArrayFull = flight_chart_array[:,5]
    lat_ArrayFull = flight_chart_array[:,6]

    true_Array = np.delete(true_ArrayFull, 0, 0)
    long_Array = np.delete(long_ArrayFull, 0, 0)
    lat_Array = np.delete(lat_ArrayFull, 0, 0)

    x_Array, y_Array = FlightData.coordinateTranslate(lat_Array,long_Array)
    #print(long_Array)

    for i in range(len(x_Array)):
        plane3 = plane2.rotate(true_Array[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(x_Array[i], y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # I don't think any of this is useful anymore since we are using
    # canvases and photoimages.
    # ------------------------------------
    #USAMap = Label(image = USAMapImage)
    #AirplaneIcon = Label(image = AirplaneIconImage)
    #FlightData = FlightData()
    #USAMap.pack()
    #root.geometry("1114x642")
    #root.title("Flight Tracking")
    #AirplaneIcon.place(x=100,y=100)

    root.mainloop()





if __name__ == "__main__":
    

    Main = GUI()







