from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
image = ImageTk.PhotoImage(file = './U.S.A Images/USAElevationMap.jpg')
label = Label(image = image)
label.pack()
root.resizable(True, True)
root.mainloop()


# Open images in GUI






