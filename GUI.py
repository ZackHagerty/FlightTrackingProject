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
    
                                                # (latmin, longmin, longmax, latmax)
    flight_chart_array = FlightData.flightDataPull(24,-80,-79,30)

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



    # black only atc zones
    albuquerqueATC = Image.open('./atc_zones/albuquerque_zone_black.png')
    albuquerqueATCMap = ImageTk.PhotoImage(albuquerqueATC)
    canvas.create_image(150,100,image=albuquerqueATCMap)

    atlantaATC = Image.open('./atc_zones/atlanta_zone_black.png')
    atlantaATCMap = ImageTk.PhotoImage(atlantaATC)
    canvas.create_image(150,100, image = atlantaATCMap)
    
    bostonATC = Image.open('./atc_zones/boston_zone_black.png')
    bostonATCMap = ImageTk.PhotoImage(bostonATC)
    canvas.create_image(150,100, image = bostonATCMap)
    
    chicagoATC = Image.open('./atc_zones/chicago_zone_black.png')
    chicagoATCMap = ImageTk.PhotoImage(chicagoATC)
    canvas.create_image(150,100, image = chicagoATCMap)
    
    clevelandATC = Image.open('./atc_zones/cleveland_zone_black.png')
    clevelandATCMap = ImageTk.PhotoImage(clevelandATC)
    canvas.create_image(150,100, image = clevelandATCMap)
    
    denverATC = Image.open('./atc_zones/denver_zone_black.png')
    denverATCMap = ImageTk.PhotoImage(denverATC)
    canvas.create_image(150,100, image = denverATCMap)
    
    ft_worthATC = Image.open('./atc_zones/ft_worth_zone_black.png')
    ft_worthATCMap = ImageTk.PhotoImage(ft_worthATC)
    canvas.create_image(150,100, image = ft_worthATCMap)
    
    houstonATC = Image.open('./atc_zones/houston_zone_black.png')
    houstonATCMap = ImageTk.PhotoImage(houstonATC)
    canvas.create_image(150,100, image = houstonATCMap)
    
    indianapolisATC = Image.open('./atc_zones/indianapolis_zone_black.png')
    indianapolisATCMap = ImageTk.PhotoImage(indianapolisATC)
    canvas.create_image(150,100, image = indianapolisATCMap)
    
    jacksonvilleATC = Image.open('./atc_zones/jacksonville_zone_black.png')
    jacksonvilleATCMap = ImageTk.PhotoImage(jacksonvilleATC)
    canvas.create_image(150,100, image = jacksonvilleATCMap)
    
    kansas_cityATC = Image.open('./atc_zones/kansas_city_zone_black.png')
    kansas_cityATCMap = ImageTk.PhotoImage(kansas_cityATC)
    canvas.create_image(150,100, image = kansas_cityATCMap)
    
    los_angelesATC = Image.open('./atc_zones/los_angeles_zone_black.png')
    los_angelesATCMap = ImageTk.PhotoImage(los_angelesATC)
    canvas.create_image(150,100, image = los_angelesATCMap)

    memphisATC = Image.open('./atc_zones/memphis_zone_black.png')
    memphisATCMap = ImageTk.PhotoImage(memphisATC)
    canvas.create_image(150,100, image = memphisATCMap)

    miamiATC = Image.open('./atc_zones/miami_zone_black.png')
    miamiATCMap = ImageTk.PhotoImage(miamiATC)
    canvas.create_image(840,500, image = miamiATCMap)

    minnealpolisATC = Image.open('./atc_zones/minnealpolis_zone_black.png')
    minnealpolisATCMap = ImageTk.PhotoImage(minnealpolisATC)
    canvas.create_image(150,100, image = minnealpolisATCMap)

    new_yorkATC = Image.open('./atc_zones/new_york_zone_black.png')
    new_yorkATCMap = ImageTk.PhotoImage(new_yorkATC)
    canvas.create_image(150,100, image = new_yorkATCMap)

    oaklandATC = Image.open('./atc_zones/oakland_zone_black.png')
    oaklandATCMap = ImageTk.PhotoImage(oaklandATC)
    canvas.create_image(150,100, image = oaklandATCMap)

    salt_lakeATC = Image.open('./atc_zones/salt_lake_zone_black.png')
    salt_lakeATCMap = ImageTk.PhotoImage(salt_lakeATC)
    canvas.create_image(150,100, image = salt_lakeATCMap)

    seattleATC = Image.open('./atc_zones/seattle_zone_black.png')
    seattleATCMap = ImageTk.PhotoImage(seattleATC)
    canvas.create_image(150,100, image = seattleATCMap)

    washingtonATC = Image.open('./atc_zones/washington_zone_black.png')
    washingtonATCMap = ImageTk.PhotoImage(washingtonATC)
    canvas.create_image(150,100, image = washingtonATCMap)
    

    # put in all of the black ones in their correct places






    root.mainloop()

    



if __name__ == "__main__":
    

    Main = GUI()







