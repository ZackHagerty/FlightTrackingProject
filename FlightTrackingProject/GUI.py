from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
USAMapImage = ImageTk.PhotoImage(file = './U.S.A Images/Untitled.png')
USAMap = Label(image = USAMapImage)

USAMap.pack()
root.geometry("1114x642")
root.title("Flight Tracking")
root.mainloop()


# Open images in GUI






