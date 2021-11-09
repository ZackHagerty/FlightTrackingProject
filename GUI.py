from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np

from FlightDataImport import FlightData

class GUI():

    def __init__(self):
        self.root = Tk()

        #Sets up the frame and background self.canvas
        self.frame = Frame(self.root)
        self.frame.pack()
        self.canvas = Canvas(self.frame, bg = "black", width=1114, height=642)
        self.canvas.pack()
        
        #background image of US
        self.USAMapImage1 = PhotoImage(file = './U.S.A Images/Untitled.png')
        self.canvas.create_image(557,(321),image=self.USAMapImage1)
        self.menusSetup()

        self.settingUpPlanes()
        self.arrayStuff()
        self.plotPlanes()

    def menusSetup(self):
        #creating a menu bar
        menubar=Menu(self.root)

        #Airline Dropdown Menu
        airlineMenu=Menu(menubar, tearoff=0)
        airlineMenu.add_command(label="Something", command = lambda : print("Something command from airline menu"))
        menubar.add_cascade(label="Airline",menu=airlineMenu)


        #ATC Zone Dropdown Menu
        atcZoneMenu=Menu(menubar, tearoff=0)
        atcZoneMenu.add_command(label="Something", command = lambda : print("Something command from atcZone menu"))
        menubar.add_cascade(label="ATC Zones", menu=atcZoneMenu)


        self.root.config(menu=menubar)
        # def menuClick(self, menuRectangle, optionButtonOne, optionButtonTwo, optionButtonThree, optionButtonFour, optionButtonFive):
        #     self.itemconfigure(menuRectangle, state = 'hidden')  
        #     self.itemconfigure(optionButtonOne, state = 'hidden')  
        #     self.itemconfigure(optionButtonTwo, state = 'hidden') 
        #     self.itemconfigure(optionButtonThree, state = 'hidden') 
        #     self.itemconfigure(optionButtonFour, state = 'hidden')
        #     self.itemconfigure(optionButtonFive, state = 'hidden')

        # optionButtonOne = tkinter.Button(command = menuClick())
        # optionButtonTwo = tkinter.Button(command = menuClick())
        # optionButtonThree = tkinter.Button(command = menuClick())
        # optionButtonFour = tkinter.Button(command = menuClick())
        # optionButtonFive = tkinter.Button(command = menuClick())
        # optionButtonOne.place(x = 100, y = 100)
        # optionButtonTwo.place(x = 100, y = 100)
        # optionButtonThree.place(x = 100, y = 100)
        # optionButtonFour.place(x = 100, y = 100)
        # optionButtonFive.place(x = 100, y = 100)
        # optionButtonOne.pack()
        # optionButtonTwo.pack()
        # optionButtonThree.pack()
        # optionButtonFour.pack()
        # optionButtonFive.pack()
            
        # #User option Button
        # def optionsMenu(self, menuRectangle, optionButtonOne, optionButtonTwo, optionButtonThree, optionButtonFour, optionButtonFive):
        #    self.itemconfigure(menuRectangle, state = 'normal')
        #    self.itemconfigure(optionButtonOne, state = 'normal') 
        #    self.itemconfigure(optionButtonTwo, state = 'normal') 
        #    self.itemconfigure(optionButtonThree, state = 'normal') 
        #    self.itemconfigure(optionButtonFour, state = 'normal')
        #    self.itemconfigure(optionButtonFive, state = 'normal')   
        
        # optionButtonOne = tkinter.Button(command = menuClick())
        # optionButtonTwo = tkinter.Button(command = menuClick())
        # optionButtonThree = tkinter.Button(command = menuClick())
        # optionButtonFour = tkinter.Button(command = menuClick())
        # optionButtonFive = tkinter.Button(command = menuClick())

        # self.gearImage = PhotoImage(file = './icons/gear_icon.png')
        # gearButton = tk.Button(self.root, image = self.gearImage, width = 40, height = 40, bg = '#aadaff', bd = 0, command = self.menuShow())
        # gearButton.place(x = 2, y = 600)

        # self.helpImage = PhotoImage(file = './icons/question_pic.png')
        # helpButton = tk.Button(self.root, image = self.helpImage, width = 40, height = 40, bg = '#aadaff', bd = 0)
        # helpButton.place(x = 42, y = 600)
    # def menuShow(self):
    #     menuRectangle = self.canvas.create_rectangle(100,100,500,500, fill = 'gray')
    def settingUpPlanes(self):
        #test image of plane
        self.plane2 = Image.open('./icons/airplane-icon-2-19.png') # 19x19 pixel image
        plane2Rot = self.plane2.rotate(45,Image.BICUBIC) # rotate 45deg, retain quality
        plane2done = ImageTk.PhotoImage(plane2Rot) # make it a photoimage (transparent bg)

        # COLORFUL PLANES!! =D
        self.plane_burgundy = Image.open('./Airline-colors-19px/bergundy-19.png')
        self.plane_cyan = Image.open('./Airline-colors-19px/cyan-19.png')
        self.plane_dark_blue = Image.open('./Airline-colors-19px/dark-blue-19.png')
        self.plane_dark_green = Image.open('./Airline-colors-19px/dark-green-19.png')
        self.plane_darker_blue = Image.open('./Airline-colors-19px/darker-blue-19.png')
        self.plane_gold = Image.open('./Airline-colors-19px/gold-19.png')
        self.plane_green = Image.open('./Airline-colors-19px/green-19.png')
        self.plane_light_blue = Image.open('./Airline-colors-19px/light-blue-19.png')
        self.plane_light_gray = Image.open('./Airline-colors-19px/light-gray-19.png')
        self.plane_orange = Image.open('./Airline-colors-19px/orange-19.png')
        self.plane_red = Image.open('./Airline-colors-19px/red-19.png')
        self.plane_sky_blue = Image.open('./Airline-colors-19px/sky-blue-19.png')
        self.plane_violet = Image.open('./Airline-colors-19px/violet-19.png')
        self.plane_yellow = Image.open('./Airline-colors-19px/yellow-19.png')

        # =======================   ATC Zones   ===============================
        #ZBW
        atc_zbw = Image.open('./atc_zones/sized_ATC/ZBW-170.png')
        self.atc_BW = ImageTk.PhotoImage(atc_zbw)
        self.canvas.create_image(995, 151, image=self.atc_BW)

        #ZNY
        atc_zny = Image.open('./atc_zones/sized_ATC/zny-84.png')
        self.atc_NY = ImageTk.PhotoImage(atc_zny)
        self.canvas.create_image(929, 207, image=self.atc_NY)

        #ZOB
        atc_zob = Image.open('./atc_zones/sized_ATC/zob-154.png')
        self.atc_OB = ImageTk.PhotoImage(atc_zob)
        self.canvas.create_image(845, 193, image=self.atc_OB)

        #ZDC
        atc_zdc = Image.open('./atc_zones/sized_ATC/zdc-148.png')
        self.atc_DC = ImageTk.PhotoImage(atc_zdc)
        self.canvas.create_image(915, 309, image=self.atc_DC)

        #ZID
        atc_zid = Image.open('./atc_zones/sized_ATC/zid-137.png')
        self.atc_ID = ImageTk.PhotoImage(atc_zid)
        self.canvas.create_image(780, 260, image=self.atc_ID)

        #ZTL
        atc_ztl = Image.open('./atc_zones/sized_ATC/ztl-150.png')
        self.atc_TL = ImageTk.PhotoImage(atc_ztl)
        self.canvas.create_image(786, 355, image=self.atc_TL)

        #ZJX
        atc_zjx = Image.open('./atc_zones/sized_ATC/zjx-203.png')
        self.atc_JX = ImageTk.PhotoImage(atc_zjx)
        self.canvas.create_image(817, 425, image=self.atc_JX)

        #ZMA
        atc_zma = Image.open('./atc_zones/sized_ATC/zma-165.png')
        self.atc_MA = ImageTk.PhotoImage(atc_zma)
        self.canvas.create_image(834, 520, image=self.atc_MA)

        #ZHU
        atc_zhu = Image.open('./atc_zones/sized_ATC/zhu-289.png')
        self.atc_HU = ImageTk.PhotoImage(atc_zhu)
        self.canvas.create_image(610, 497, image=self.atc_HU)

        #ZME
        atc_zme = Image.open('./atc_zones/sized_ATC/zme-183.png')
        self.atc_ME = ImageTk.PhotoImage(atc_zme)
        self.canvas.create_image(674, 348, image=self.atc_ME)

        #ZKC
        atc_zkc = Image.open('./atc_zones/sized_ATC/zkc-253.png')
        self.atc_KC = ImageTk.PhotoImage(atc_zkc)
        self.canvas.create_image(591, 270, image=self.atc_KC)

        #ZAU
        atc_zau = Image.open('./atc_zones/sized_ATC/zau-156.png')
        self.atc_AU = ImageTk.PhotoImage(atc_zau)
        self.canvas.create_image(698, 180, image=self.atc_AU)

        #ZMP
        atc_zmp = Image.open('./atc_zones/sized_ATC/zmp-363.png')
        self.atc_MP = ImageTk.PhotoImage(atc_zmp)
        self.canvas.create_image(637, 135, image=self.atc_MP)

        #ZFW
        atc_zfw = Image.open('./atc_zones/sized_ATC/zfw-215.png')
        self.atc_FW = ImageTk.PhotoImage(atc_zfw)
        self.canvas.create_image(549, 375, image=self.atc_FW)
        
        #ZAB
        atc_zab = Image.open('./atc_zones/sized_ATC/zab-245.png')
        self.atc_AB = ImageTk.PhotoImage(atc_zab)
        self.canvas.create_image(391, 379, image=self.atc_AB)

        #ZDV
        atc_zdv = Image.open('./atc_zones/sized_ATC/zdv-230.png')
        self.atc_DV = ImageTk.PhotoImage(atc_zdv)
        self.canvas.create_image(421, 218, image=self.atc_DV)

        #ZLC
        atc_zlc = Image.open('./atc_zones/sized_ATC/zlc-283.png')
        self.atc_LC = ImageTk.PhotoImage(atc_zlc)
        self.canvas.create_image(317, 157, image=self.atc_LC)

        #ZLA
        atc_zla = Image.open('./atc_zones/sized_ATC/zla-204.png')
        self.atc_LA = ImageTk.PhotoImage(atc_zla)
        self.canvas.create_image(214, 355, image=self.atc_LA)

        #ZOA
        atc_zoa = Image.open('./atc_zones/sized_ATC/zoa-172.png')
        self.atc_OA = ImageTk.PhotoImage(atc_zoa)
        self.canvas.create_image(136, 276, image=self.atc_OA)

        #ZSE
        atc_zse = Image.open('./atc_zones/sized_ATC/zse-230.png')
        self.atc_SE = ImageTk.PhotoImage(atc_zse)
        self.canvas.create_image(146, 126, image=self.atc_SE)

    # =====================   END ATC Zones   ===============================

    def arrayStuff(self):

        img_ref = []
        self.plane_ref = []
        
        # Read the flight data
        flight_chart_array = FlightData.flightDataPull(20.038,-130.974,-65.748,50.214)

        # These arrays are for placing the planes and their directions
        self.AAL_Arraylong = []
        self.AAL_Arraylat = []
        self.AAL_Arraytrue = []

        self.AAY_Arraylong = []
        self.AAY_Arraylat = []
        self.AAY_Arraytrue = []

        self.ACA_Arraylong = []
        self.ACA_Arraylat = []
        self.ACA_Arraytrue = []

        self.AFR_Arraylong = []
        self.AFR_Arraylat = []
        self.AFR_Arraytrue = []

        self.AMX_Arraylong = []
        self.AMX_Arraylat = []
        self.AMX_Arraytrue = []

        self.ASA_Arraylong = []
        self.ASA_Arraylat = []
        self.ASA_Arraytrue = []

        self.DAL_Arraylong = []
        self.DAL_Arraylat = []
        self.DAL_Arraytrue = []

        self.FFT_Arraylong = []
        self.FFT_Arraylat = []
        self.FFT_Arraytrue = []

        self.JBU_Arraylong = []
        self.JBU_Arraylat = []
        self.JBU_Arraytrue = []

        self.NKS_Arraylong = []
        self.NKS_Arraylat = []
        self.NKS_Arraytrue = []

        self.SWA_Arraylong = []
        self.SWA_Arraylat = []
        self.SWA_Arraytrue = []

        self.UAL_Arraylong = []
        self.UAL_Arraylat = []
        self.UAL_Arraytrue = []

        #Sort by company code, add it to each array
        for i in range(len(flight_chart_array)):
            
            if flight_chart_array[i,1].startswith('AAL'):
                self.AAL_Arraylong.append(flight_chart_array[i,5])
                self.AAL_Arraylat.append(flight_chart_array[i,6])
                self.AAL_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('AAY'):
                self.AAY_Arraylong.append(flight_chart_array[i,5])
                self.AAY_Arraylat.append(flight_chart_array[i,6])
                self.AAY_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('ACA'):
                self.ACA_Arraylong.append(flight_chart_array[i,5])
                self.ACA_Arraylat.append(flight_chart_array[i,6])
                self.ACA_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('AFR'):
                self.AFR_Arraylong.append(flight_chart_array[i,5])
                self.AFR_Arraylat.append(flight_chart_array[i,6])
                self.AFR_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('AMX'):
                self.AMX_Arraylong.append(flight_chart_array[i,5])
                self.AMX_Arraylat.append(flight_chart_array[i,6])
                self.AMX_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('ASA'):
                self.ASA_Arraylong.append(flight_chart_array[i,5])
                self.ASA_Arraylat.append(flight_chart_array[i,6])
                self.ASA_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('DAL'):
                self.DAL_Arraylong.append(flight_chart_array[i,5])
                self.DAL_Arraylat.append(flight_chart_array[i,6])
                self.DAL_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('FFT'):
                self.FFT_Arraylong.append(flight_chart_array[i,5])
                self.FFT_Arraylat.append(flight_chart_array[i,6])
                self.FFT_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('JBU'):
                self.JBU_Arraylong.append(flight_chart_array[i,5])
                self.JBU_Arraylat.append(flight_chart_array[i,6])
                self.JBU_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('NKS'):
                self.NKS_Arraylong.append(flight_chart_array[i,5])
                self.NKS_Arraylat.append(flight_chart_array[i,6])
                self.NKS_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('SWA'):
                self.SWA_Arraylong.append(flight_chart_array[i,5])
                self.SWA_Arraylat.append(flight_chart_array[i,6])
                self.SWA_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('UAL'):
                self.UAL_Arraylong.append(flight_chart_array[i,5])
                self.UAL_Arraylat.append(flight_chart_array[i,6])
                self.UAL_Arraytrue.append(flight_chart_array[i,10])

        # Translate lat/long to x/y for the GUI
        self.AAL_X_Array, self.AAL_Y_Array = FlightData.coordinateTranslate(self.AAL_Arraylat,self.AAL_Arraylong)
        self.AAY_X_Array, self.AAY_Y_Array = FlightData.coordinateTranslate(self.AAY_Arraylat,self.AAY_Arraylong)
        self.ACA_X_Array, self.ACA_Y_Array = FlightData.coordinateTranslate(self.ACA_Arraylat,self.ACA_Arraylong)
        self.AFR_X_Array, self.AFR_Y_Array = FlightData.coordinateTranslate(self.AFR_Arraylat,self.AFR_Arraylong)
        self.AMX_X_Array, self.AMX_Y_Array = FlightData.coordinateTranslate(self.AMX_Arraylat,self.AMX_Arraylong)
        self.ASA_X_Array, self.ASA_Y_Array = FlightData.coordinateTranslate(self.ASA_Arraylat,self.ASA_Arraylong)
        self.DAL_X_Array, self.DAL_Y_Array = FlightData.coordinateTranslate(self.DAL_Arraylat,self.DAL_Arraylong)
        self.FFT_X_Array, self.FFT_Y_Array = FlightData.coordinateTranslate(self.FFT_Arraylat,self.FFT_Arraylong)
        self.JBU_X_Array, self.JBU_Y_Array = FlightData.coordinateTranslate(self.JBU_Arraylat,self.JBU_Arraylong)
        self.NKS_X_Array, self.NKS_Y_Array = FlightData.coordinateTranslate(self.NKS_Arraylat,self.NKS_Arraylong)
        self.SWA_X_Array, self.SWA_Y_Array = FlightData.coordinateTranslate(self.SWA_Arraylat,self.SWA_Arraylong)
        self.UAL_X_Array, self.UAL_Y_Array = FlightData.coordinateTranslate(self.UAL_Arraylat,self.UAL_Arraylong)
        #print(long_Array)

    # =====================   PLANE PLACEMENT   ===============================    
    
    # place each plane in x,y and with rotation with each color per airline
    
    def plotPlanes(self):
        # American
        for i in range(len(self.AAL_X_Array)):
            plane3 = self.plane_sky_blue.rotate(self.AAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.AAL_X_Array[i], self.AAL_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Allegiant
        for i in range(len(self.AAY_X_Array)):
            plane3 = self.plane_orange.rotate(self.AAY_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.AAY_X_Array[i], self.AAY_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Air Canada
        for i in range(len(self.ACA_X_Array)):
            plane3 = self.plane_red.rotate(self.ACA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.ACA_X_Array[i], self.ACA_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Air France
        for i in range(len(self.AFR_X_Array)):
            plane3 = self.plane_light_blue.rotate(self.AFR_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.AFR_X_Array[i], self.AFR_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # AeroMexico
        for i in range(len(self.AMX_X_Array)):
            plane3 = self.plane_green.rotate(self.AMX_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.AMX_X_Array[i], self.AMX_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Air Alaska
        for i in range(len(self.ASA_X_Array)):
            plane3 = self.plane_light_gray.rotate(self.ASA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.ASA_X_Array[i], self.ASA_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Delta
        for i in range(len(self.DAL_X_Array)):
            plane3 = self.plane_burgundy.rotate(self.DAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.DAL_X_Array[i], self.DAL_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Frontier
        for i in range(len(self.FFT_X_Array)):
            plane3 = self.plane_dark_green.rotate(self.FFT_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.FFT_X_Array[i], self.FFT_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Jetblue
        for i in range(len(self.JBU_X_Array)):
            plane3 = self.plane_cyan.rotate(self.JBU_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.JBU_X_Array[i], self.JBU_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Spirit
        for i in range(len(self.NKS_X_Array)):
            plane3 = self.plane_yellow.rotate(self.NKS_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.NKS_X_Array[i], self.NKS_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # Southwest
        for i in range(len(self.SWA_X_Array)):
            plane3 = self.plane_darker_blue.rotate(self.SWA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.SWA_X_Array[i], self.SWA_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        # United
        for i in range(len(self.UAL_X_Array)):
            plane3 = self.plane_gold.rotate(self.UAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(self.UAL_X_Array[i], self.UAL_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)


        # this gotta be the last line or it all doesn't work
        self.root.mainloop()



if __name__ == "__main__":
    

    Main = GUI()
