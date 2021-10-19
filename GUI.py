from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from FlightDataImport import FlightData

class GUI():

    root = Tk()
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
    plane2 = Image.open('./icons/airplane-icon-2-19.png')
    plane2Rot = plane2.rotate(45,Image.BICUBIC)
    plane2done = ImageTk.PhotoImage(plane2Rot)

    # cant rotate this
    # plane = PhotoImage(file = './icons/airplane-icon-2-19.png')
    
    

    def makePlane(canvas,plane,x,y,heading):
        plane1 = plane.rotate(heading)
        plane1done = ImageTk.PhotoImage(plane1)
        canvas.create_image(30,30,image=plane1done)

    
    makePlane(canvas,plane2, 100, 321, 45)


    for i in range(6):
        print("Ran {0} times".format(i))
        #makePlane(canvas,plane2, 50*i, 50*i, 139)
        plane1 = plane2.rotate(33*i)
        plane1done = ImageTk.PhotoImage(plane1)
        canvas.create_image(30*i,30*i,image=plane1done)

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







