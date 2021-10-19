from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from FlightDataImport import FlightData

class GUI():

    root = Tk()
    #USAMapImage = ImageTk.PhotoImage(file = './U.S.A Images/Untitled.png')
    #AirplaneIconImage = ImageTk.PhotoImage(file = './icons/airplane-icon-2.png')

    frame = Frame(root)
    frame.pack()
    canvas = Canvas(frame, bg = "black", width=1114, height=642)
    canvas.pack()
    
    background = PhotoImage(file = './U.S.A Images/Untitled.png')
    canvas.create_image(557,(321),image=background)
    plane = PhotoImage(file = './icons/airplane-icon-2.png')
    canvas.create_image(30,30,image=plane)

    #USAMap = Label(image = USAMapImage)
    #AirplaneIcon = Label(image = AirplaneIconImage)


    #FlightData = FlightData()
    #USAMap.pack()
    #root.geometry("1114x642")
    #root.title("Flight Tracking")
    #AirplaneIcon.place(x=100,y=100)

    root.mainloop()

    
    # Matthew Writes a Method
    # Given N and W, will give you X and Y pixels for the GUI




if __name__ == "__main__":
    
    Main = GUI()







