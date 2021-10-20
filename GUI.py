from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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
    def makePlane(canvas,plane,x,y,heading):
        plane1 = plane.rotate(heading)
        plane1done = ImageTk.PhotoImage(plane1)
        canvas.create_image(x,y,image=plane1done)

    # see how this should make 2 new planes, but it does not
    # I commented this out since, as far as I could tell, it didn't do anything -D
    #makePlane(canvas,plane2, 100, 321, 45)
    #makePlane(canvas,plane2, 300, 321, 135)

    #see how this only makes 1 plane, the one that should be plane 6
    for i in range(6):
        print("Ran {0} times".format(i)) #iterator
        #makePlane(canvas,plane2, 50*i, 50*i, 139)
        
        #these three lines is a duplicate of the makePlane method
        plane3 = plane2.rotate(33*i)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(30*i,30*i,image=plane3done)

    #This currently is causing everything to fail, I'm working on it -D
    for i in range(len(FlightData.flight_Long_Array)):
        coord_X, coord_Y = FlightData.coordinateTranslate(FlightData.flight_Lat_Array,FlightData.flight_Long_Array)
        makePlane(canvas,plane2,coord_X,coord_Y,FlightData.flight_True_Array)



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







