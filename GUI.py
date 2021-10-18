from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from FlightDataImport import FlightData

class GUI():

    root = Tk()
    USAMapImage = ImageTk.PhotoImage(file = './U.S.A Images/Untitled.png')
    USAMap = Label(image = USAMapImage)

    FlightData = FlightData()
    USAMap.pack()
    root.geometry("1114x642")
    root.title("Flight Tracking")
    root.mainloop()

    
    # Matthew Writes a Method
    # Given N and W, will give you X and Y pixels for the GUI


    def coordinateTranslate(N, W):
        
        # Based on photo from Zack:
        x = (130-65)/1114 * (W + 130)
        y = -(642/30) * (N - 50)

        return x,y

if __name__ == "__main__":
    
    Main = GUI()







