from tkinter import *
import tkinter as tk
from tkinter.constants import DISABLED,NORMAL
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np

from FlightDataImport import FlightData


class GUI():

    def __init__(self, root):
        self.on = False
        #Sets up the frame and background self.canvas
        self.root = root
        frame = Frame(root)
        frame.pack()
        self.canvas = Canvas(frame, bg = "black", width=1114, height=642)
        self.canvas.pack()
        
        
        #background image of US
        self.USAMapImage1 = PhotoImage(file = './U.S.A Images/Untitled.png')
        self.canvas.create_image(557,(321),image=self.USAMapImage1)

        self.menusSetup(root)

        self.settingUpPlanes()
        
        self.arrayStuff(root)
        

    def menusSetup(self, root):
        #creating a menu bar

        clippy = Image.open('./icons/Clippy.png')
        clippyText = Image.open('./icons/Speech.png')
        self.clipper = ImageTk.PhotoImage(clippy)
        self.Speech = ImageTk.PhotoImage(clippyText)
        butt = Button(root, image=self.clipper, bg = '#aadaff', activebackground= '#aadaff', command= self.my_command, borderwidth= 0)
        butt.place(x = 1010, y = 525)
        
        menubar=Menu(root)

        #Airline Dropdown Menu
        self.AALCheckVar = IntVar(value=1)
        self.AAYCheckVar = IntVar()
        self.ACACheckVar = IntVar()
        self.AFRCheckVar = IntVar()
        self.AMXCheckVar = IntVar()
        self.ASACheckVar = IntVar()
        self.DALCheckVar = IntVar(value=1)
        self.FFTCheckVar = IntVar()
        self.JBUCheckVar = IntVar()
        self.NKSCheckVar = IntVar()
        self.SWACheckVar = IntVar()
        self.UALCheckVar = IntVar()

        airlineMenu=Menu(menubar, tearoff=0)
        airlineMenu.add_checkbutton(label="American Airlines", variable= self.AALCheckVar, command = lambda: self.hideAAL())
        airlineMenu.add_checkbutton(label="Allegiant Airlines", variable = self.AAYCheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="Air Canada", variable = self.ACACheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="Air France", variable = self.AFRCheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="AeroMexico", variable = self.AMXCheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="Alaska Air", variable = self.ASACheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="Delta Airlines", variable= self.DALCheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="Frontier Airlines", variable = self.FFTCheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="Jet Blue Airlines", variable = self.JBUCheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="Spirit Airlines", variable = self.NKSCheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="South West Airlines", variable = self.SWACheckVar, command = lambda : print("Something command from airline menu"))
        airlineMenu.add_checkbutton(label="United Airlines", variable = self.UALCheckVar, command = lambda : print("Something command from airline menu"))
        menubar.add_cascade(label="Airline",menu=airlineMenu)


        #ATC Zone Dropdown Menu
        self.ZBWCheckVar = IntVar(value=1)
        self.ZNYCheckVar = IntVar(value=1)
        self.ZOBCheckVar = IntVar(value=1)
        self.ZDCCheckVar = IntVar(value=1)
        self.ZIDCheckVar = IntVar(value=1)
        self.ZTLCheckVar = IntVar(value=1)
        self.ZJXCheckVar = IntVar(value=1)
        self.ZMACheckVar = IntVar(value=1)
        self.ZHUCheckVar = IntVar(value=1)
        self.ZMECheckVar = IntVar(value=1)
        self.ZKCCheckVar = IntVar(value=1)
        self.ZAUCheckVar = IntVar(value=1)
        self.ZMPCheckVar = IntVar(value=1)
        self.ZFWCheckVar = IntVar(value=1)
        self.ZABCheckVar = IntVar(value=1)
        self.ZDVCheckVar = IntVar(value=1)
        self.ZLCCheckVar = IntVar(value=1)
        self.ZLACheckVar = IntVar(value=1)
        self.ZOACheckVar = IntVar(value=1)
        self.ZSECheckVar = IntVar(value=1)

        atcZoneMenu=Menu(menubar, tearoff=0)
        atcZoneMenu.add_checkbutton(label="ZBW", variable= self.ZBWCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZNY", variable= self.ZNYCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZOB", variable= self.ZOBCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZDC", variable= self.ZDCCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZID", variable= self.ZIDCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZTL", variable= self.ZTLCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZJX", variable= self.ZJXCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZMA", variable= self.ZMACheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZHU", variable= self.ZHUCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZME", variable= self.ZMECheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZKC", variable= self.ZKCCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZAU", variable= self.ZAUCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZMP", variable= self.ZMPCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZFW", variable= self.ZFWCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZAB", variable= self.ZABCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZDV", variable= self.ZDVCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZLC", variable= self.ZLCCheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZLA", variable= self.ZLACheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZOA", variable= self.ZOACheckVar, command = lambda : print("Something command from atcZone menu"))
        atcZoneMenu.add_checkbutton(label="ZSE", variable= self.ZSECheckVar, command = lambda : print("Something command from atcZone menu"))
        menubar.add_cascade(label="ATC Zones", menu=atcZoneMenu)


        root.config(menu=menubar)
        

        
    def my_command(self):
        if(self.on == False):
            self.canvas.create_image(1010, 450, image = self.Speech, tags = ('speech'))
            self.on = True
        else:
            self.canvas.delete('speech')
            self.on = False

    def hideAAL(self):
        if self.AALCheckVar.get() == 1:
            self.canvas.itemconfigure('AALplane', state = 'normal')
            print("Kill me now")
        else:
            print(self.AALCheckVar.get())
            self.canvas.itemconfigure('AALplane', state = 'hidden')



    def settingUpPlanes(self):
        #test image of plane
        self.plane2 = Image.open('./icons/airplane-icon-2-19.png') # 19x19 pixel image
        plane2Rot = self.plane2.rotate(45,Image.BICUBIC) # rotate 45deg, retain quality

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
        self.canvas.create_image(995, 151, image=self.atc_BW, tags = 'zbw')

        #ZNY
        atc_zny = Image.open('./atc_zones/sized_ATC/zny-84.png')
        self.atc_NY = ImageTk.PhotoImage(atc_zny)
        self.canvas.create_image(929, 207, image=self.atc_NY, tags = 'zny')

        #ZOB
        atc_zob = Image.open('./atc_zones/sized_ATC/zob-154.png')
        self.atc_OB = ImageTk.PhotoImage(atc_zob)
        self.canvas.create_image(845, 193, image=self.atc_OB, tags = 'zob')

        #ZDC
        atc_zdc = Image.open('./atc_zones/sized_ATC/zdc-148.png')
        self.atc_DC = ImageTk.PhotoImage(atc_zdc)
        self.canvas.create_image(915, 309, image=self.atc_DC, tags = 'zdc')

        #ZID
        atc_zid = Image.open('./atc_zones/sized_ATC/zid-137.png')
        self.atc_ID = ImageTk.PhotoImage(atc_zid)
        self.canvas.create_image(780, 260, image=self.atc_ID, tags = 'zid')

        #ZTL
        atc_ztl = Image.open('./atc_zones/sized_ATC/ztl-150.png')
        self.atc_TL = ImageTk.PhotoImage(atc_ztl)
        self.canvas.create_image(786, 355, image=self.atc_TL, tags = 'ztl')

        #ZJX
        atc_zjx = Image.open('./atc_zones/sized_ATC/zjx-203.png')
        self.atc_JX = ImageTk.PhotoImage(atc_zjx)
        self.canvas.create_image(817, 425, image=self.atc_JX, tags = 'zjx')

        #ZMA
        atc_zma = Image.open('./atc_zones/sized_ATC/zma-165.png')
        self.atc_MA = ImageTk.PhotoImage(atc_zma)
        self.canvas.create_image(834, 520, image=self.atc_MA, tags = 'zma')

        #ZHU
        atc_zhu = Image.open('./atc_zones/sized_ATC/zhu-289.png')
        self.atc_HU = ImageTk.PhotoImage(atc_zhu)
        self.canvas.create_image(610, 497, image=self.atc_HU, tags = 'zhu')

        #ZME
        atc_zme = Image.open('./atc_zones/sized_ATC/zme-183.png')
        self.atc_ME = ImageTk.PhotoImage(atc_zme)
        self.canvas.create_image(674, 348, image=self.atc_ME, tags = 'zme')

        #ZKC
        atc_zkc = Image.open('./atc_zones/sized_ATC/zkc-253.png')
        self.atc_KC = ImageTk.PhotoImage(atc_zkc)
        self.canvas.create_image(591, 270, image=self.atc_KC, tags = 'zkc')

        #ZAU
        atc_zau = Image.open('./atc_zones/sized_ATC/zau-156.png')
        self.atc_AU = ImageTk.PhotoImage(atc_zau)
        self.canvas.create_image(698, 180, image=self.atc_AU, tags = 'zau')

        #ZMP
        atc_zmp = Image.open('./atc_zones/sized_ATC/zmp-363.png')
        self.atc_MP = ImageTk.PhotoImage(atc_zmp)
        self.canvas.create_image(637, 135, image=self.atc_MP, tags = 'zmp')

        #ZFW
        atc_zfw = Image.open('./atc_zones/sized_ATC/zfw-215.png')
        self.atc_FW = ImageTk.PhotoImage(atc_zfw)
        self.canvas.create_image(549, 375, image=self.atc_FW, tags = 'zfw')
        
        #ZAB
        atc_zab = Image.open('./atc_zones/sized_ATC/zab-245.png')
        self.atc_AB = ImageTk.PhotoImage(atc_zab)
        self.canvas.create_image(391, 379, image=self.atc_AB, tags = 'zab')

        #ZDV
        atc_zdv = Image.open('./atc_zones/sized_ATC/zdv-230.png')
        self.atc_DV = ImageTk.PhotoImage(atc_zdv)
        self.canvas.create_image(421, 218, image=self.atc_DV, tags = 'zdv')

        #ZLC
        atc_zlc = Image.open('./atc_zones/sized_ATC/zlc-283.png')
        self.atc_LC = ImageTk.PhotoImage(atc_zlc)
        self.canvas.create_image(317, 157, image=self.atc_LC, tags = 'zlc')

        #ZLA
        atc_zla = Image.open('./atc_zones/sized_ATC/zla-204.png')
        self.atc_LA = ImageTk.PhotoImage(atc_zla)
        self.canvas.create_image(214, 355, image=self.atc_LA, tags = 'zla')

        #ZOA
        atc_zoa = Image.open('./atc_zones/sized_ATC/zoa-172.png')
        self.atc_OA = ImageTk.PhotoImage(atc_zoa)
        self.canvas.create_image(136, 276, image=self.atc_OA, tags = 'zoa')

        #ZSE
        atc_zse = Image.open('./atc_zones/sized_ATC/zse-230.png')
        self.atc_SE = ImageTk.PhotoImage(atc_zse)
        self.canvas.create_image(146, 126, image=self.atc_SE, tags = 'zse')

    # =====================   END ATC Zones   ===============================

    def arrayStuff(self, root):
        print("I hate this")
        self.plane_ref = []
        
        # Read the flight data
        flight_chart_array = FlightData.flightDataPull(20.038,-130.974,-65.748,50.214)

        # These arrays are for placing the planes and their directions
        self.AAL_callSign = []
        self.AAL_Arraylong = []
        self.AAL_Arraylat = []
        self.AAL_Arraytrue = []

        self.AAY_callSign = []
        self.AAY_Arraylong = []
        self.AAY_Arraylat = []
        self.AAY_Arraytrue = []

        self.ACA_callSign = []
        self.ACA_Arraylong = []
        self.ACA_Arraylat = []
        self.ACA_Arraytrue = []

        self.AFR_callSign = []
        self.AFR_Arraylong = []
        self.AFR_Arraylat = []
        self.AFR_Arraytrue = []

        self.AMX_callSign = []
        self.AMX_Arraylong = []
        self.AMX_Arraylat = []
        self.AMX_Arraytrue = []

        self.ASA_callSign = []
        self.ASA_Arraylong = []
        self.ASA_Arraylat = []
        self.ASA_Arraytrue = []

        self.DAL_callSign = []
        self.DAL_Arraylong = []
        self.DAL_Arraylat = []
        self.DAL_Arraytrue = []

        self.FFT_callSign = []
        self.FFT_Arraylong = []
        self.FFT_Arraylat = []
        self.FFT_Arraytrue = []

        self.JBU_callSign = []
        self.JBU_Arraylong = []
        self.JBU_Arraylat = []
        self.JBU_Arraytrue = []

        self.NKS_callSign = []
        self.NKS_Arraylong = []
        self.NKS_Arraylat = []
        self.NKS_Arraytrue = []

        self.SWA_callSign = []
        self.SWA_Arraylong = []
        self.SWA_Arraylat = []
        self.SWA_Arraytrue = []

        self.UAL_callSign = []
        self.UAL_Arraylong = []
        self.UAL_Arraylat = []
        self.UAL_Arraytrue = []

        #Sort by company code, add it to each array
        for i in range(len(flight_chart_array)):
            
            if flight_chart_array[i,1].startswith('AAL'):
                self.AAL_callSign.append(flight_chart_array[i, 1])
                self.AAL_Arraylong.append(flight_chart_array[i,5])
                self.AAL_Arraylat.append(flight_chart_array[i,6])
                self.AAL_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('AAY'):
                self.AAY_callSign.append(flight_chart_array[i, 1])
                self.AAY_Arraylong.append(flight_chart_array[i,5])
                self.AAY_Arraylat.append(flight_chart_array[i,6])
                self.AAY_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('ACA'):
                self.ACA_callSign.append(flight_chart_array[i, 1])
                self.ACA_Arraylong.append(flight_chart_array[i,5])
                self.ACA_Arraylat.append(flight_chart_array[i,6])
                self.ACA_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('AFR'):
                self.AFR_callSign.append(flight_chart_array[i, 1])
                self.AFR_Arraylong.append(flight_chart_array[i,5])
                self.AFR_Arraylat.append(flight_chart_array[i,6])
                self.AFR_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('AMX'):
                self.AMX_callSign.append(flight_chart_array[i, 1])
                self.AMX_Arraylong.append(flight_chart_array[i,5])
                self.AMX_Arraylat.append(flight_chart_array[i,6])
                self.AMX_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('ASA'):
                self.ASA_callSign.append(flight_chart_array[i, 1])
                self.ASA_Arraylong.append(flight_chart_array[i,5])
                self.ASA_Arraylat.append(flight_chart_array[i,6])
                self.ASA_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('DAL'):
                self.DAL_callSign.append(flight_chart_array[i, 1])
                self.DAL_Arraylong.append(flight_chart_array[i,5])
                self.DAL_Arraylat.append(flight_chart_array[i,6])
                self.DAL_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('FFT'):
                self.FFT_callSign.append(flight_chart_array[i, 1])
                self.FFT_Arraylong.append(flight_chart_array[i,5])
                self.FFT_Arraylat.append(flight_chart_array[i,6])
                self.FFT_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('JBU'):
                self.JBU_callSign.append(flight_chart_array[i, 1])
                self.JBU_Arraylong.append(flight_chart_array[i,5])
                self.JBU_Arraylat.append(flight_chart_array[i,6])
                self.JBU_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('NKS'):
                self.NKS_callSign.append(flight_chart_array[i, 1])
                self.NKS_Arraylong.append(flight_chart_array[i,5])
                self.NKS_Arraylat.append(flight_chart_array[i,6])
                self.NKS_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('SWA'):
                self.SWA_callSign.append(flight_chart_array[i, 1])
                self.SWA_Arraylong.append(flight_chart_array[i,5])
                self.SWA_Arraylat.append(flight_chart_array[i,6])
                self.SWA_Arraytrue.append(flight_chart_array[i,10])

            if flight_chart_array[i,1].startswith('UAL'):
                self.UAL_callSign.append(flight_chart_array[i, 1])
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

        self.plotPlanes(root)

    # =====================   PLANE PLACEMENT   ===============================    
    
    # place each plane in x,y and with rotation with each color per airline
    
    def plotPlanes(self, root):
        # American
        self.canvas.delete("plane")
        self.planeImages = {}
        self.planeImages["AAL"] = []
        for i in range(len(self.AAL_X_Array)):
            plane3 = self.plane_sky_blue.rotate(-self.AAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            AAL = self.canvas.create_image(self.AAL_X_Array[i], self.AAL_Y_Array[i], image=plane3done, tags =('AALplane'))
            ToolTip.CreateToolTip(self.canvas, AAL , text = 'AAL, ' + self.AAL_callSign[i])
            self.plane_ref.append(plane3done)

        # Allegiant
        for i in range(len(self.AAY_X_Array)):
            plane3 = self.plane_orange.rotate(-self.AAY_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            AAY = self.canvas.create_image(self.AAY_X_Array[i], self.AAY_Y_Array[i], image=plane3done, tags =('AAYplane'))
            ToolTip.CreateToolTip(self.canvas, AAY, text = 'AAY, ' + self.AAY_callSign[i])
            self.plane_ref.append(plane3done)

        # Air Canada
        for i in range(len(self.ACA_X_Array)):
            plane3 = self.plane_red.rotate(-self.ACA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            ACA = self.canvas.create_image(self.ACA_X_Array[i], self.ACA_Y_Array[i], image=plane3done, tags =('ACAplane'))
            ToolTip.CreateToolTip(self.canvas, ACA, text = 'ACA, ' + self.ACA_callSign[i])
            self.plane_ref.append(plane3done)

        # Air France
        for i in range(len(self.AFR_X_Array)):
            plane3 = self.plane_light_blue.rotate(-self.AFR_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            AFR = self.canvas.create_image(self.AFR_X_Array[i], self.AFR_Y_Array[i], image=plane3done, tags =('AFRplane'))
            ToolTip.CreateToolTip(self.canvas, AFR, text = 'AFR, ' + self.AFR_callSign[i])
            self.plane_ref.append(plane3done)

        # AeroMexico
        for i in range(len(self.AMX_X_Array)):
            plane3 = self.plane_green.rotate(-self.AMX_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            AMX = self.canvas.create_image(self.AMX_X_Array[i], self.AMX_Y_Array[i], image=plane3done, tags =('AMXplane'))
            ToolTip.CreateToolTip(self.canvas, AMX, text = 'AMX, ' + self.AMX_callSign[i])
            self.plane_ref.append(plane3done)

        # Air Alaska
        for i in range(len(self.ASA_X_Array)):
            plane3 = self.plane_light_gray.rotate(-self.ASA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            ASA = self.canvas.create_image(self.ASA_X_Array[i], self.ASA_Y_Array[i], image=plane3done, tags =('ASAplane'))
            ToolTip.CreateToolTip(self.canvas, ASA, text = 'ASA, ' + self.ASA_callSign[i])
            self.plane_ref.append(plane3done)

        # Delta
        for i in range(len(self.DAL_X_Array)):
            plane3 = self.plane_burgundy.rotate(-self.DAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            DAL = self.canvas.create_image(self.DAL_X_Array[i], self.DAL_Y_Array[i], image=plane3done, tags =('DALplane'))
            ToolTip.CreateToolTip(self.canvas, DAL, text = 'DAL, ' + self.DAL_callSign[i])
            self.plane_ref.append(plane3done)

        # Frontier
        for i in range(len(self.FFT_X_Array)):
            plane3 = self.plane_dark_green.rotate(-self.FFT_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            FFT = self.canvas.create_image(self.FFT_X_Array[i], self.FFT_Y_Array[i], image=plane3done, tags =('FFTplane'))
            ToolTip.CreateToolTip(self.canvas, FFT, text = 'FFT, ' + self.FFT_callSign[i])
            self.plane_ref.append(plane3done)

        # Jetblue
        for i in range(len(self.JBU_X_Array)):
            plane3 = self.plane_cyan.rotate(-self.JBU_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            JBU = self.canvas.create_image(self.JBU_X_Array[i], self.JBU_Y_Array[i], image=plane3done, tags =('JBUplane'))
            ToolTip.CreateToolTip(self.canvas, JBU, text = 'JBU, ' + self.JBU_callSign[i])
            self.plane_ref.append(plane3done)

        # Spirit
        for i in range(len(self.NKS_X_Array)):
            plane3 = self.plane_yellow.rotate(-self.NKS_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            NKS = self.canvas.create_image(self.NKS_X_Array[i], self.NKS_Y_Array[i], image=plane3done, tags =('NKSplane'))
            ToolTip.CreateToolTip(self.canvas, NKS, text = 'NKS, ' + self.NKS_callSign[i])
            self.plane_ref.append(plane3done)

        # Southwest
        for i in range(len(self.SWA_X_Array)):
            plane3 = self.plane_darker_blue.rotate(-self.SWA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            SWA = self.canvas.create_image(self.SWA_X_Array[i], self.SWA_Y_Array[i], image=plane3done, tags =('SWAplane'))
            ToolTip.CreateToolTip(self.canvas, SWA, text = 'SWA, ' + self.SWA_callSign[i])
            self.plane_ref.append(plane3done)

        # United
        for i in range(len(self.UAL_X_Array)):
            plane3 = self.plane_gold.rotate(-self.UAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            UAL = self.canvas.create_image(self.UAL_X_Array[i], self.UAL_Y_Array[i], image=plane3done, tags =('UALplane'))
            ToolTip.CreateToolTip(self.canvas, UAL, text = 'UAL, ' + self.UAL_callSign[i])
            self.plane_ref.append(plane3done)


        # this gotta be the last line or it all doesn't work
        root.after(20000, self.arrayStuff, root)
        
class ToolTip(object):

    def __init__(self, canvas, widget):
        self.canvas = canvas
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.canvas.bbox(ALL)
        x = self.canvas.winfo_pointerx() + 10
        y = self.canvas.winfo_pointery() + 10
        self.tipwindow = tw = Toplevel(self.canvas)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

    def CreateToolTip(canvas, widget, text):
        toolTip = ToolTip(canvas, widget)
        def enter(event):
            toolTip.showtip(text)
        def leave(event):
            toolTip.hidetip()
        canvas.tag_bind(widget, '<Enter>', enter)
        canvas.tag_bind(widget, '<Leave>', leave)


if __name__ == "__main__":
    
    root = Tk()
    Main = GUI(root)
    root.mainloop()
