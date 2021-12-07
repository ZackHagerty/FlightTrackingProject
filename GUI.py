"""
GUI.py created by Zack Hagerty, Devon Casey, 



"""

import random
from tkinter import *
import tkinter as tk
from tkinter.constants import DISABLED,NORMAL
from tkinter import ALL, EventType
from PIL import ImageTk, Image

from FlightDataImport import FlightData

"""
GUI Class. This class facilitates all operations,
including plane location updating/plotting, data pull
calls.
"""
class GUI():

    """
    GUI class's initialization method. Serves to set
    up the GUI upon call.

    Arguments: 
    root - the Tkinter instance.
    """
    def __init__(self, root):
        self.on = False
        #Sets up the frame and background self.canvas
        self.root = root
        frame = Frame(root)
        frame.pack()
        self.canvas = Canvas(frame, bg = "black", width=1114, height=642)
        self.canvas.pack()
        root.wm_title("Flight Tracking")
        
        #background image of US
        self.USAMapImage1 = PhotoImage(file = './U.S.A Images/Untitled.png')
        self.Mask = Image.open('./icons/MASK.png')
        self.canvas.create_image(557,(321),image=self.USAMapImage1)
        root.config(cursor = "heart")
        self.menuVariables()

        self.menusSetup(root)

        self.settingUpPlanes()
        
        self.arrayStuff(root)

    """
    Creates the variables to be used in the menu
    that filters the companies and ATC Zones    
    """
    def menuVariables(self):

        val = 1
        #Airline Dropdown Menu
        self.AALCheckVar = IntVar(value=val)
        self.AAYCheckVar = IntVar(value=val)
        self.ACACheckVar = IntVar(value=val)
        self.AFRCheckVar = IntVar(value=val)
        self.AMXCheckVar = IntVar(value=val)
        self.ASACheckVar = IntVar(value=val)
        self.DALCheckVar = IntVar(value=val)
        self.FFTCheckVar = IntVar(value=val)
        self.JBUCheckVar = IntVar(value=val)
        self.NKSCheckVar = IntVar(value=val)
        self.SWACheckVar = IntVar(value=val)
        self.UALCheckVar = IntVar(value=val)

        #ATC Zone Dropdown Menu
        self.ZBWCheckVar = IntVar(value=0)
        self.ZNYCheckVar = IntVar(value=0)
        self.ZOBCheckVar = IntVar(value=0)
        self.ZDCCheckVar = IntVar(value=0)
        self.ZIDCheckVar = IntVar(value=0)
        self.ZTLCheckVar = IntVar(value=0)
        self.ZJXCheckVar = IntVar(value=val)
        self.ZMACheckVar = IntVar(value=0)
        self.ZHUCheckVar = IntVar(value=0)
        self.ZMECheckVar = IntVar(value=0)
        self.ZKCCheckVar = IntVar(value=0)
        self.ZAUCheckVar = IntVar(value=0)
        self.ZMPCheckVar = IntVar(value=0)
        self.ZFWCheckVar = IntVar(value=0)
        self.ZABCheckVar = IntVar(value=0)
        self.ZDVCheckVar = IntVar(value=0)
        self.ZLCCheckVar = IntVar(value=0)
        self.ZLACheckVar = IntVar(value=val)
        self.ZOACheckVar = IntVar(value=0)
        self.ZSECheckVar = IntVar(value=0)    

    """
    This method will facilitate the operation
    of the menu at the top of the GUI, 
    allowing user to filter ATC zones and
    companies
    Arguments:
    -root
    """
    def menusSetup(self, root):
        #creating a menu bar

        clippy = Image.open('./icons/Clippy.png')
        clippyText = Image.open('./icons/Speech.png')
        self.clipper = ImageTk.PhotoImage(clippy)
        self.Speech = ImageTk.PhotoImage(clippyText)
        butt = Button(root, image=self.clipper, bg = '#aadaff', activebackground= '#aadaff', command= self.my_command, borderwidth= 0)
        butt.place(x = 1010, y = 533)
        
        menubar=Menu(root)

        airlineMenu=Menu(menubar, tearoff=0)
        airlineMenu.add_checkbutton(label="American Airlines", variable= self.AALCheckVar, command = lambda : self.hidePlane('AALplane', self.AALCheckVar.get()))
        airlineMenu.add_checkbutton(label="Allegiant Airlines", variable = self.AAYCheckVar, command = lambda : self.hidePlane('AAYplane', self.AAYCheckVar.get()))
        airlineMenu.add_checkbutton(label="Air Canada", variable = self.ACACheckVar, command = lambda : self.hidePlane('ACAplane', self.ACACheckVar.get()))
        airlineMenu.add_checkbutton(label="Air France", variable = self.AFRCheckVar, command = lambda : self.hidePlane('AFRplane', self.AFRCheckVar.get()))
        airlineMenu.add_checkbutton(label="AeroMexico", variable = self.AMXCheckVar, command = lambda : self.hidePlane('AMXplane', self.AMXCheckVar.get()))
        airlineMenu.add_checkbutton(label="Alaska Air", variable = self.ASACheckVar, command = lambda : self.hidePlane('ASAplane', self.ASACheckVar.get()))
        airlineMenu.add_checkbutton(label="Delta Airlines", variable= self.DALCheckVar, command = lambda : self.hidePlane('DALplane', self.DALCheckVar.get()))
        airlineMenu.add_checkbutton(label="Frontier Airlines", variable = self.FFTCheckVar, command = lambda : self.hidePlane('FFTplane', self.FFTCheckVar.get()))
        airlineMenu.add_checkbutton(label="Jet Blue Airlines", variable = self.JBUCheckVar, command = lambda : self.hidePlane('JBUplane', self.JBUCheckVar.get()))
        airlineMenu.add_checkbutton(label="Spirit Airlines", variable = self.NKSCheckVar, command = lambda : self.hidePlane('NKSplane', self.NKSCheckVar.get()))
        airlineMenu.add_checkbutton(label="South West Airlines", variable = self.SWACheckVar, command = lambda : self.hidePlane('SWAplane', self.SWACheckVar.get()))
        airlineMenu.add_checkbutton(label="United Airlines", variable = self.UALCheckVar, command = lambda : self.hidePlane('UALplane', self.UALCheckVar.get()))
        menubar.add_cascade(label="Airline",menu=airlineMenu)


        atcZoneMenu=Menu(menubar, tearoff=0)
        atcZoneMenu.add_checkbutton(label="ZBW", variable= self.ZBWCheckVar, command = lambda : self.hideZone('mask_ZBW', self.ZBWCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZNY", variable= self.ZNYCheckVar, command = lambda : self.hideZone('mask_ZNY', self.ZNYCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZOB", variable= self.ZOBCheckVar, command = lambda : self.hideZone('mask_ZOB', self.ZOBCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZDC", variable= self.ZDCCheckVar, command = lambda : self.hideZone('mask_ZDC', self.ZDCCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZID", variable= self.ZIDCheckVar, command = lambda : self.hideZone('mask_ZID', self.ZIDCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZTL", variable= self.ZTLCheckVar, command = lambda : self.hideZone('mask_ZTL', self.ZTLCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZJX", variable= self.ZJXCheckVar, command = lambda : self.hideZone('mask_ZJX', self.ZJXCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZMA", variable= self.ZMACheckVar, command = lambda : self.hideZone('mask_ZMA', self.ZMACheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZHU", variable= self.ZHUCheckVar, command = lambda : self.hideZone('mask_ZHU', self.ZHUCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZME", variable= self.ZMECheckVar, command = lambda : self.hideZone('mask_ZME', self.ZMECheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZKC", variable= self.ZKCCheckVar, command = lambda : self.hideZone('mask_ZKC', self.ZKCCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZAU", variable= self.ZAUCheckVar, command = lambda : self.hideZone('mask_ZAU', self.ZAUCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZMP", variable= self.ZMPCheckVar, command = lambda : self.hideZone('mask_ZMP', self.ZMPCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZFW", variable= self.ZFWCheckVar, command = lambda : self.hideZone('mask_ZFW', self.ZFWCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZAB", variable= self.ZABCheckVar, command = lambda : self.hideZone('mask_ZAB', self.ZABCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZDV", variable= self.ZDVCheckVar, command = lambda : self.hideZone('mask_ZDV', self.ZDVCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZLC", variable= self.ZLCCheckVar, command = lambda : self.hideZone('mask_ZLC', self.ZLCCheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZLA", variable= self.ZLACheckVar, command = lambda : self.hideZone('mask_ZLA', self.ZLACheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZOA", variable= self.ZOACheckVar, command = lambda : self.hideZone('mask_ZOA', self.ZOACheckVar.get()))
        atcZoneMenu.add_checkbutton(label="ZSE", variable= self.ZSECheckVar, command = lambda : self.hideZone('mask_ZSE', self.ZSECheckVar.get()))
        menubar.add_cascade(label="ATC Zones", menu=atcZoneMenu)

        root.config(menu=menubar)
    
    """
    This function controls clippy
    """
    def my_command(self):
        if(self.on == False):
            self.canvas.create_image(1010, 450, image = self.Speech, tags = ('speech'))
            self.on = True
        else:
            self.canvas.delete('speech')
            self.on = False

    """
    Company plane toggle

    Arguments:
    plane - Company being filtered out
    checkVar - Whether or not that plane is already toggles. 0 = off, 1 = on
    """
    def hidePlane(self, plane, checkVar):
        if checkVar == 1:
            self.canvas.itemconfigure(plane, state = 'normal')
        else:
            self.canvas.itemconfigure(plane, state = 'hidden')


        """
        ATC Zone toggle method

        Arguments:
        mask - the image being passed
        checkVar - checks to see if the plane is already on. 0 = no, 1 = yes.
        """
    def hideZone(self, mask, checkVar):
        if checkVar == 0:
            self.canvas.itemconfigure(mask, state = 'normal')
        else:
            self.canvas.itemconfigure(mask, state = 'hidden')

    """
    Loads all images used in the GUI
    """
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
        self.canvas.create_image(995, 151, image=self.atc_BW, tags = 'ZBW')

        #ZNY
        atc_zny = Image.open('./atc_zones/sized_ATC/zny-84.png')
        self.atc_NY = ImageTk.PhotoImage(atc_zny)
        self.canvas.create_image(929, 207, image=self.atc_NY, tags = 'ZNY')

        #ZOB
        atc_zob = Image.open('./atc_zones/sized_ATC/zob-154.png')
        self.atc_OB = ImageTk.PhotoImage(atc_zob)
        self.canvas.create_image(845, 193, image=self.atc_OB, tags = 'ZOB')

        #ZDC
        atc_zdc = Image.open('./atc_zones/sized_ATC/zdc-148.png')
        self.atc_DC = ImageTk.PhotoImage(atc_zdc)
        self.canvas.create_image(915, 309, image=self.atc_DC, tags = 'ZDC')

        #ZID
        atc_zid = Image.open('./atc_zones/sized_ATC/zid-137.png')
        self.atc_ID = ImageTk.PhotoImage(atc_zid)
        self.canvas.create_image(780, 260, image=self.atc_ID, tags = 'ZID')

        #ZTL
        atc_ztl = Image.open('./atc_zones/sized_ATC/ztl-150.png')
        self.atc_TL = ImageTk.PhotoImage(atc_ztl)
        self.canvas.create_image(786, 355, image=self.atc_TL, tags = 'ZTL')

        #ZJX
        atc_zjx = Image.open('./atc_zones/sized_ATC/zjx-203.png')
        self.atc_JX = ImageTk.PhotoImage(atc_zjx)
        self.canvas.create_image(817, 425, image=self.atc_JX, tags = 'ZJX')

        #ZMA
        atc_zma = Image.open('./atc_zones/sized_ATC/zma-165.png')
        self.atc_MA = ImageTk.PhotoImage(atc_zma)
        self.canvas.create_image(834, 520, image=self.atc_MA, tags = 'ZMA')

        #ZHU
        atc_zhu = Image.open('./atc_zones/sized_ATC/zhu-289.png')
        self.atc_HU = ImageTk.PhotoImage(atc_zhu)
        self.canvas.create_image(610, 497, image=self.atc_HU, tags = 'ZHU')

        #ZME
        atc_zme = Image.open('./atc_zones/sized_ATC/zme-183.png')
        self.atc_ME = ImageTk.PhotoImage(atc_zme)
        self.canvas.create_image(674, 348, image=self.atc_ME, tags = 'ZME')

        #ZKC
        atc_zkc = Image.open('./atc_zones/sized_ATC/zkc-253.png')
        self.atc_KC = ImageTk.PhotoImage(atc_zkc)
        self.canvas.create_image(591, 270, image=self.atc_KC, tags = 'ZKC')

        #ZAU
        atc_zau = Image.open('./atc_zones/sized_ATC/zau-156.png')
        self.atc_AU = ImageTk.PhotoImage(atc_zau)
        self.canvas.create_image(698, 180, image=self.atc_AU, tags = 'ZAU')

        #ZMP
        atc_zmp = Image.open('./atc_zones/sized_ATC/zmp-363.png')
        self.atc_MP = ImageTk.PhotoImage(atc_zmp)
        self.canvas.create_image(637, 135, image=self.atc_MP, tags = 'ZMP')

        #ZFW
        atc_zfw = Image.open('./atc_zones/sized_ATC/zfw-215.png')
        self.atc_FW = ImageTk.PhotoImage(atc_zfw)
        self.canvas.create_image(549, 375, image=self.atc_FW, tags = 'ZFW')
        
        #ZAB
        atc_zab = Image.open('./atc_zones/sized_ATC/zab-245.png')
        self.atc_AB = ImageTk.PhotoImage(atc_zab)
        self.canvas.create_image(391, 379, image=self.atc_AB, tags = 'ZAB')

        #ZDV
        atc_zdv = Image.open('./atc_zones/sized_ATC/zdv-230.png')
        self.atc_DV = ImageTk.PhotoImage(atc_zdv)
        self.canvas.create_image(421, 218, image=self.atc_DV, tags = 'ZDV')

        #ZLC
        atc_zlc = Image.open('./atc_zones/sized_ATC/zlc-283.png')
        self.atc_LC = ImageTk.PhotoImage(atc_zlc)
        self.canvas.create_image(317, 157, image=self.atc_LC, tags = 'ZLC')

        #ZLA
        atc_zla = Image.open('./atc_zones/sized_ATC/zla-204.png')
        self.atc_LA = ImageTk.PhotoImage(atc_zla)
        self.canvas.create_image(214, 355, image=self.atc_LA, tags = 'ZLA')

        #ZOA
        atc_zoa = Image.open('./atc_zones/sized_ATC/zoa-172.png')
        self.atc_OA = ImageTk.PhotoImage(atc_zoa)
        self.canvas.create_image(136, 276, image=self.atc_OA, tags = 'ZOA')

        #ZSE
        atc_zse = Image.open('./atc_zones/sized_ATC/zse-230.png')
        self.atc_SE = ImageTk.PhotoImage(atc_zse)
        self.canvas.create_image(146, 126, image=self.atc_SE, tags = 'ZSE')

        duck = Image.open('./icons/duck.png')
        self.duck = ImageTk.PhotoImage(duck)
        

        

    # =====================   END ATC Zones   ===============================

        """
        Calls data pull, creates arrays to hold data, and populates arrays

        Arguments:
        -root
        """
    def arrayStuff(self, root):
        smask = ImageTk.PhotoImage(self.Mask)
        self.canvas.create_image(10,10, image = smask, tags =('window'))

  
        self.plane_ref = []

        self.duckProbability = random.randint(0, 20)

        # Read the flight data
        flight_chart_array = FlightData.flightDataPull(20.038,-130.974,-65.748,50.214)

        # These arrays are for placing the planes and their directions
        self.AAL_callSign, self.AAL_Arraylong, self.AAL_Arraylat, self.AAL_Arraytrue = [], [], [], []
        self.AAY_callSign, self.AAY_Arraylong, self.AAY_Arraylat, self.AAY_Arraytrue = [], [], [], []
        self.ACA_callSign, self.ACA_Arraylong, self.ACA_Arraylat, self.ACA_Arraytrue = [], [], [], []
        self.AFR_callSign, self.AFR_Arraylong, self.AFR_Arraylat, self.AFR_Arraytrue = [], [], [], []
        self.AMX_callSign, self.AMX_Arraylong, self.AMX_Arraylat, self.AMX_Arraytrue = [], [], [], []
        self.ASA_callSign, self.ASA_Arraylong, self.ASA_Arraylat, self.ASA_Arraytrue = [], [], [], []
        self.DAL_callSign, self.DAL_Arraylong, self.DAL_Arraylat, self.DAL_Arraytrue = [], [], [], []
        self.FFT_callSign, self.FFT_Arraylong, self.FFT_Arraylat, self.FFT_Arraytrue = [], [], [], []
        self.JBU_callSign, self.JBU_Arraylong, self.JBU_Arraylat, self.JBU_Arraytrue = [], [], [], []
        self.NKS_callSign, self.NKS_Arraylong, self.NKS_Arraylat, self.NKS_Arraytrue = [], [], [], []
        self.SWA_callSign, self.SWA_Arraylong, self.SWA_Arraylat, self.SWA_Arraytrue = [], [], [], []
        self.UAL_callSign, self.UAL_Arraylong, self.UAL_Arraylat, self.UAL_Arraytrue = [], [], [], []


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

        self.refreshGUI(root)

    """
    Recreates planes and masks every refresh cycle.
    Arguments:
    root
    """
    def refreshGUI(self, root):
        # American
        self.canvas.delete("plane")
        self.planeImages = {}
        self.planeImages["AAL"] = []

        if(self.duckProbability == 3):
            self.canvas.create_image(50, 500, image = self.duck, tags = ('plane'))

        for i in range(len(self.AAL_X_Array)):
            
            if self.AALCheckVar.get() == 1:
                plane3 = self.plane_sky_blue.rotate(-self.AAL_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AAL = self.canvas.create_image(self.AAL_X_Array[i], self.AAL_Y_Array[i], image=plane3done, tags =('AALplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, AAL , text = 'AAL, ' + self.AAL_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_sky_blue.rotate(-self.AAL_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AAL = self.canvas.create_image(self.AAL_X_Array[i], self.AAL_Y_Array[i], image=plane3done, tags =('AALplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, AAL , text = 'AAL, ' + self.AAL_callSign[i])
                self.plane_ref.append(plane3done)

        # Allegiant
        for i in range(len(self.AAY_X_Array)):
            if self.AAYCheckVar.get() == 1:
                plane3 = self.plane_orange.rotate(-self.AAY_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AAY = self.canvas.create_image(self.AAY_X_Array[i], self.AAY_Y_Array[i], image=plane3done, tags =('AAYplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, AAY, text = 'AAY, ' + self.AAY_callSign[i])
                self.plane_ref.append(plane3done)
            else:
                plane3 = self.plane_orange.rotate(-self.AAY_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AAY = self.canvas.create_image(self.AAY_X_Array[i], self.AAY_Y_Array[i], image=plane3done, tags =('AAYplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, AAY, text = 'AAY, ' + self.AAY_callSign[i])
                self.plane_ref.append(plane3done)

        # Air Canada
        for i in range(len(self.ACA_X_Array)):
            
            if self.ACACheckVar.get() == 1:
                plane3 = self.plane_red.rotate(-self.ACA_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                ACA = self.canvas.create_image(self.ACA_X_Array[i], self.ACA_Y_Array[i], image=plane3done, tags =('ACAplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, ACA, text = 'ACA, ' + self.ACA_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_red.rotate(-self.ACA_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                ACA = self.canvas.create_image(self.ACA_X_Array[i], self.ACA_Y_Array[i], image=plane3done, tags =('ACAplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, ACA, text = 'ACA, ' + self.ACA_callSign[i])
                self.plane_ref.append(plane3done)

        # Air France
        for i in range(len(self.AFR_X_Array)):

            if self.AFRCheckVar.get() == 1:
                plane3 = self.plane_light_blue.rotate(-self.AFR_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AFR = self.canvas.create_image(self.AFR_X_Array[i], self.AFR_Y_Array[i], image=plane3done, tags =('AFRplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, AFR, text = 'AFR, ' + self.AFR_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_light_blue.rotate(-self.AFR_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AFR = self.canvas.create_image(self.AFR_X_Array[i], self.AFR_Y_Array[i], image=plane3done, tags =('AFRplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, AFR, text = 'AFR, ' + self.AFR_callSign[i])
                self.plane_ref.append(plane3done)

        # AeroMexico
        for i in range(len(self.AMX_X_Array)):

            if self.AMXCheckVar.get() == 1:
                plane3 = self.plane_green.rotate(-self.AMX_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AMX = self.canvas.create_image(self.AMX_X_Array[i], self.AMX_Y_Array[i], image=plane3done, tags =('AMXplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, AMX, text = 'AMX, ' + self.AMX_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_green.rotate(-self.AMX_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                AMX = self.canvas.create_image(self.AMX_X_Array[i], self.AMX_Y_Array[i], image=plane3done, tags =('AMXplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, AMX, text = 'AMX, ' + self.AMX_callSign[i])
                self.plane_ref.append(plane3done)

        # Air Alaska
        for i in range(len(self.ASA_X_Array)):

            if self.ASACheckVar.get() == 1:
                plane3 = self.plane_light_gray.rotate(-self.ASA_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                ASA = self.canvas.create_image(self.ASA_X_Array[i], self.ASA_Y_Array[i], image=plane3done, tags =('ASAplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, ASA, text = 'ASA, ' + self.ASA_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_light_gray.rotate(-self.ASA_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                ASA = self.canvas.create_image(self.ASA_X_Array[i], self.ASA_Y_Array[i], image=plane3done, tags =('ASAplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, ASA, text = 'ASA, ' + self.ASA_callSign[i])
                self.plane_ref.append(plane3done)

        # Delta
        for i in range(len(self.DAL_X_Array)):

            if self.DALCheckVar.get() == 1:
                plane3 = self.plane_burgundy.rotate(-self.DAL_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                DAL = self.canvas.create_image(self.DAL_X_Array[i], self.DAL_Y_Array[i], image=plane3done, tags =('DALplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, DAL, text = 'DAL, ' + self.DAL_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_burgundy.rotate(-self.DAL_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                DAL = self.canvas.create_image(self.DAL_X_Array[i], self.DAL_Y_Array[i], image=plane3done, tags =('DALplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, DAL, text = 'DAL, ' + self.DAL_callSign[i])
                self.plane_ref.append(plane3done)

        # Frontier
        for i in range(len(self.FFT_X_Array)):

            if self.FFTCheckVar.get() == 1:
                plane3 = self.plane_dark_green.rotate(-self.FFT_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                FFT = self.canvas.create_image(self.FFT_X_Array[i], self.FFT_Y_Array[i], image=plane3done, tags =('FFTplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, FFT, text = 'FFT, ' + self.FFT_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_dark_green.rotate(-self.FFT_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                FFT = self.canvas.create_image(self.FFT_X_Array[i], self.FFT_Y_Array[i], image=plane3done, tags =('FFTplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, FFT, text = 'FFT, ' + self.FFT_callSign[i])
                self.plane_ref.append(plane3done)

        # Jetblue
        for i in range(len(self.JBU_X_Array)):

            if self.JBUCheckVar.get() == 1:
                plane3 = self.plane_cyan.rotate(-self.JBU_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                JBU = self.canvas.create_image(self.JBU_X_Array[i], self.JBU_Y_Array[i], image=plane3done, tags =('JBUplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, JBU, text = 'JBU, ' + self.JBU_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_cyan.rotate(-self.JBU_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                JBU = self.canvas.create_image(self.JBU_X_Array[i], self.JBU_Y_Array[i], image=plane3done, tags =('JBUplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, JBU, text = 'JBU, ' + self.JBU_callSign[i])
                self.plane_ref.append(plane3done)

        # Spirit
        for i in range(len(self.NKS_X_Array)):

            if self.NKSCheckVar.get() == 1:
                plane3 = self.plane_yellow.rotate(-self.NKS_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                NKS = self.canvas.create_image(self.NKS_X_Array[i], self.NKS_Y_Array[i], image=plane3done, tags =('NKSplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, NKS, text = 'NKS, ' + self.NKS_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_yellow.rotate(-self.NKS_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                NKS = self.canvas.create_image(self.NKS_X_Array[i], self.NKS_Y_Array[i], image=plane3done, tags =('NKSplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, NKS, text = 'NKS, ' + self.NKS_callSign[i])
                self.plane_ref.append(plane3done)

        # Southwest
        for i in range(len(self.SWA_X_Array)):

            if self.SWACheckVar.get() == 1:
                plane3 = self.plane_darker_blue.rotate(-self.SWA_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                SWA = self.canvas.create_image(self.SWA_X_Array[i], self.SWA_Y_Array[i], image=plane3done, tags =('SWAplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, SWA, text = 'SWA, ' + self.SWA_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_darker_blue.rotate(-self.SWA_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                SWA = self.canvas.create_image(self.SWA_X_Array[i], self.SWA_Y_Array[i], image=plane3done, tags =('SWAplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, SWA, text = 'SWA, ' + self.SWA_callSign[i])
                self.plane_ref.append(plane3done)

        # United
        for i in range(len(self.UAL_X_Array)):

            if self.UALCheckVar.get() == 1:
                plane3 = self.plane_gold.rotate(-self.UAL_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                UAL = self.canvas.create_image(self.UAL_X_Array[i], self.UAL_Y_Array[i], image=plane3done, tags =('UALplane', 'plane'), state = 'normal')
                ToolTip.CreateToolTip(self.canvas, UAL, text = 'UAL, ' + self.UAL_callSign[i])
                self.plane_ref.append(plane3done)

            else:
                plane3 = self.plane_gold.rotate(-self.UAL_Arraytrue[i], Image.BICUBIC)
                plane3done = ImageTk.PhotoImage(plane3)
                UAL = self.canvas.create_image(self.UAL_X_Array[i], self.UAL_Y_Array[i], image=plane3done, tags =('UALplane', 'plane'), state = 'hidden')
                ToolTip.CreateToolTip(self.canvas, UAL, text = 'UAL, ' + self.UAL_callSign[i])
                self.plane_ref.append(plane3done)
                
        """
        The following code creates the masks, as well as their borders. Refreshed ever cycle to make sure 
        that zones that are currently filtered out, stay filtered out.
        """
        nop_zbw = Image.open('./atc_zones/cropped/zbw-cropped.png')
        self.nop_bw = ImageTk.PhotoImage(nop_zbw)
        self.canvas.create_image( 995, 151, image=self.nop_bw, tags = ('mask_ZBW','plane'))
        atc_zbw2 = Image.open('./atc_zones/sized_ATC/ZBW-170.png')
        self.atc_BW2 = ImageTk.PhotoImage(atc_zbw2)
        self.canvas.create_image(995, 151, image=self.atc_BW2, tags = ('mask_ZBW', 'plane'))

        if self.ZBWCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZBW', state = 'hidden')

        nop_zny = Image.open('./atc_zones/cropped/zny-cropped.png')
        self.nop_ny = ImageTk.PhotoImage(nop_zny)
        self.canvas.create_image( 929, 207, image=self.nop_ny, tags = ('mask_ZNY','plane'))
        atc_zny2 = Image.open('./atc_zones/sized_ATC/zny-84.png')
        self.atc_NY2 = ImageTk.PhotoImage(atc_zny2)
        self.canvas.create_image(929, 207, image=self.atc_NY2, tags = ('mask_ZNY', 'plane'))

        if self.ZNYCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZNY', state = 'hidden')

        nop_zob = Image.open('./atc_zones/cropped/zob-cropped.png')
        self.nop_ob = ImageTk.PhotoImage(nop_zob)
        self.canvas.create_image( 845, 193, image=self.nop_ob, tags = ('mask_ZOB','plane'))
        atc_zob2 = Image.open('./atc_zones/sized_ATC/zob-154.png')
        self.atc_OB2 = ImageTk.PhotoImage(atc_zob2)
        self.canvas.create_image(845, 193, image=self.atc_OB2, tags = ('mask_ZOB','plane'))
        
        if self.ZOBCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZOB', state = 'hidden')

        nop_zdc = Image.open('./atc_zones/cropped/zdc-cropped.png')
        self.nop_dc = ImageTk.PhotoImage(nop_zdc)
        self.canvas.create_image( 915, 309, image=self.nop_dc, tags = ('mask_ZDC', 'plane'))
        atc_zdc2 = Image.open('./atc_zones/sized_ATC/zdc-148.png')
        self.atc_DC2 = ImageTk.PhotoImage(atc_zdc2)
        self.canvas.create_image(915, 309, image=self.atc_DC2, tags = ('mask_ZDC','plane'))
        
        if self.ZDCCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZDC', state = 'hidden')

        nop_zid = Image.open('./atc_zones/cropped/zid-cropped.png')
        self.nop_id = ImageTk.PhotoImage(nop_zid)
        self.canvas.create_image( 780, 260, image=self.nop_id, tags = ('mask_ZID', 'plane'))
        atc_zid2 = Image.open('./atc_zones/sized_ATC/zid-137.png')
        self.atc_ID2 = ImageTk.PhotoImage(atc_zid2)
        self.canvas.create_image(780, 260, image=self.atc_ID2, tags = ('mask_ZID' ,'plane'))
        
        if self.ZIDCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZID', state = 'hidden')

        nop_ztl = Image.open('./atc_zones/cropped/ztl-cropped.png')
        self.nop_tl = ImageTk.PhotoImage(nop_ztl)
        self.canvas.create_image( 786, 355, image=self.nop_tl, tags = ('mask_ZTL', 'plane'))
        atc_ztl2 = Image.open('./atc_zones/sized_ATC/ztl-150.png')
        self.atc_TL2 = ImageTk.PhotoImage(atc_ztl2)
        self.canvas.create_image(786, 355, image=self.atc_TL2, tags = ('mask_ZTL','plane'))

        if self.ZTLCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZTL', state = 'hidden')

        nop_zjx = Image.open('./atc_zones/cropped/zjx-cropped.png')
        self.nop_jx = ImageTk.PhotoImage(nop_zjx)
        self.canvas.create_image( 817, 425, image=self.nop_jx, tags = ('mask_ZJX', 'plane'))
        atc_zjx2 = Image.open('./atc_zones/sized_ATC/zjx-203.png')
        self.atc_JX2 = ImageTk.PhotoImage(atc_zjx2)
        self.canvas.create_image(817, 425, image=self.atc_JX2, tags = ('mask_ZJX', 'plane'))
        
        if self.ZJXCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZJX', state = 'hidden')

        nop_zma = Image.open('./atc_zones/cropped/zma-cropped.png')
        self.nop_ma = ImageTk.PhotoImage(nop_zma)
        self.canvas.create_image( 834, 520, image=self.nop_ma, tags = ('mask_ZMA', 'plane'))
        atc_zma2 = Image.open('./atc_zones/sized_ATC/zma-165.png')
        self.atc_MA2 = ImageTk.PhotoImage(atc_zma2)
        self.canvas.create_image(834, 520, image=self.atc_MA2, tags = ('mask_ZMA', 'plane'))
        
        if self.ZMACheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZMA', state = 'hidden')

        nop_zhu = Image.open('./atc_zones/cropped/zhu-cropped.png')
        self.nop_hu = ImageTk.PhotoImage(nop_zhu)
        self.canvas.create_image( 610, 497, image=self.nop_hu, tags = ('mask_ZHU', 'plane'))
        atc_zhu2 = Image.open('./atc_zones/sized_ATC/zhu-289.png')
        self.atc_HU2 = ImageTk.PhotoImage(atc_zhu2)
        self.canvas.create_image(610, 497, image=self.atc_HU2, tags = ('mask_ZHU', 'plane'))
        
        if self.ZHUCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZHU', state = 'hidden')

        nop_zme = Image.open('./atc_zones/cropped/zme-cropped.png')
        self.nop_me = ImageTk.PhotoImage(nop_zme)
        self.canvas.create_image( 674, 348, image=self.nop_me, tags = ('mask_ZME', 'plane'))
        atc_zme2 = Image.open('./atc_zones/sized_ATC/zme-183.png')
        self.atc_ME2 = ImageTk.PhotoImage(atc_zme2)
        self.canvas.create_image(674, 348, image=self.atc_ME2, tags = ('mask_ZME', 'plane'))
        
        if self.ZMECheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZME', state = 'hidden')

        nop_zkc = Image.open('./atc_zones/cropped/zkc-cropped.png')
        self.nop_kc = ImageTk.PhotoImage(nop_zkc)
        self.canvas.create_image( 591, 270, image=self.nop_kc, tags = ('mask_ZKC', 'plane'))
        atc_zkc2 = Image.open('./atc_zones/sized_ATC/zkc-253.png')
        self.atc_KC2 = ImageTk.PhotoImage(atc_zkc2)
        self.canvas.create_image(591, 270, image=self.atc_KC2, tags = ('mask_ZKC','plane'))
        
        if self.ZKCCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZKC', state = 'hidden')

        nop_zau = Image.open('./atc_zones/cropped/zau-cropped.png')
        self.nop_au = ImageTk.PhotoImage(nop_zau)
        self.canvas.create_image( 698, 180, image=self.nop_au, tags = ('mask_ZAU', 'plane'))
        atc_zau2 = Image.open('./atc_zones/sized_ATC/zau-156.png')
        self.atc_AU2 = ImageTk.PhotoImage(atc_zau2)
        self.canvas.create_image(698, 180, image=self.atc_AU2, tags = ('mask_ZAU', 'plane'))

        if self.ZAUCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZAU', state = 'hidden')

        nop_zmp = Image.open('./atc_zones/cropped/zmp-cropped.png')
        self.nop_mp = ImageTk.PhotoImage(nop_zmp)
        self.canvas.create_image( 637, 135, image=self.nop_mp, tags = ('mask_ZMP', 'plane'))
        atc_zmp2 = Image.open('./atc_zones/sized_ATC/zmp-363.png')
        self.atc_MP2 = ImageTk.PhotoImage(atc_zmp2)
        self.canvas.create_image(637, 135, image=self.atc_MP2, tags = ('mask_ZMP', 'plane'))
        
        if self.ZMPCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZMP', state = 'hidden')

        nop_zfw = Image.open('./atc_zones/cropped/zfw-cropped.png')
        self.nop_fw = ImageTk.PhotoImage(nop_zfw)
        self.canvas.create_image( 549, 375, image=self.nop_fw, tags = ('mask_ZFW', 'plane'))
        atc_zfw2 = Image.open('./atc_zones/sized_ATC/zfw-215.png')
        self.atc_FW2 = ImageTk.PhotoImage(atc_zfw2)
        self.canvas.create_image(549, 375, image=self.atc_FW2, tags = ('mask_ZFW', 'plane'))

        if self.ZFWCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZFW', state = 'hidden')

        nop_zab = Image.open('./atc_zones/cropped/zab-cropped.png')
        self.nop_ab = ImageTk.PhotoImage(nop_zab)
        self.canvas.create_image( 391, 379, image=self.nop_ab, tags = ('mask_ZAB', 'plane'))
        atc_zab2 = Image.open('./atc_zones/sized_ATC/zab-245.png')
        self.atc_AB2 = ImageTk.PhotoImage(atc_zab2)
        self.canvas.create_image(391, 379, image=self.atc_AB2, tags = ('mask_ZAB', 'plane'))
        
        if self.ZABCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZAB', state = 'hidden')

        nop_zdv = Image.open('./atc_zones/cropped/zdv-cropped.png')
        self.nop_dv = ImageTk.PhotoImage(nop_zdv)
        self.canvas.create_image( 421 , 218, image=self.nop_dv, tags = ('mask_ZDV', 'plane'))
        atc_zdv2 = Image.open('./atc_zones/sized_ATC/zdv-230.png')
        self.atc_DV2 = ImageTk.PhotoImage(atc_zdv2)
        self.canvas.create_image(421, 218, image=self.atc_DV2, tags = ('mask_ZDV', 'plane'))
        
        if self.ZDVCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZDV', state = 'hidden')

        nop_zlc = Image.open('./atc_zones/cropped/zlc-cropped.png')
        self.nop_lc = ImageTk.PhotoImage(nop_zlc)
        self.canvas.create_image( 317, 157, image=self.nop_lc, tags = ('mask_ZLC', 'plane'))
        atc_zlc2 = Image.open('./atc_zones/sized_ATC/zlc-283.png')
        self.atc_LC2 = ImageTk.PhotoImage(atc_zlc2)
        self.canvas.create_image(317, 157, image=self.atc_LC2, tags = ('mask_ZLC', 'plane'))
        
        if self.ZLCCheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZLC', state = 'hidden')

        nop_zla = Image.open('./atc_zones/cropped/zla-cropped.png')
        self.nop_la = ImageTk.PhotoImage(nop_zla)
        self.canvas.create_image(214 , 355, image=self.nop_la, tags = ('mask_ZLA', 'plane'))
        atc_zla2 = Image.open('./atc_zones/sized_ATC/zla-204.png')
        self.atc_LA2 = ImageTk.PhotoImage(atc_zla2)
        self.canvas.create_image(214, 355, image=self.atc_LA2, tags = ('mask_ZLA','plane'))

        if self.ZLACheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZLA', state = 'hidden')

        nop_zoa = Image.open('./atc_zones/cropped/zoa-cropped.png')
        self.nop_OA = ImageTk.PhotoImage(nop_zoa)
        self.canvas.create_image(136,276, image=self.nop_OA, tags = ('mask_ZOA', 'plane'))
        atc_zoa2 = Image.open('./atc_zones/sized_ATC/zoa-172.png')
        self.atc_OA2 = ImageTk.PhotoImage(atc_zoa2)
        self.canvas.create_image(136, 276, image=self.atc_OA2, tags = ('mask_ZOA', 'plane'))
        
        if self.ZOACheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZOA', state = 'hidden')

        nop_zse = Image.open('./atc_zones/cropped/zse-cropped.png')
        self.nop_SE = ImageTk.PhotoImage(nop_zse)
        self.canvas.create_image(146,126, image=self.nop_SE, tags = ('mask_ZSE', 'plane'))
        atc_zse2 = Image.open('./atc_zones/sized_ATC/zse-230.png')
        self.atc_SE2 = ImageTk.PhotoImage(atc_zse2)
        self.canvas.create_image(146, 126, image=self.atc_SE2, tags = ('mask_ZSE', 'plane'))
        
        if self.ZSECheckVar.get() == 1:
            self.canvas.itemconfigure('mask_ZSE', state = 'hidden')

        self.canvas.delete('window')
        self.smask = ImageTk.PhotoImage(self.Mask)

        # this gotta be the last line or it all doesn't work
        root.after(19800, self.caller, root)
        root.after(20000, self.arrayStuff, root)

    """
    Method that breaks user's connection to plane. If this isn't present,
    tool tips will stick around after GUI updates
    """ 
    def caller(self, root):
        self.canvas.create_image(10,10, image = self.smask, tags =('window'))


"""
This class controls the plane data info that pops up when
the mouse hovers over a plane.
"""    
class ToolTip(object):

    """
    Initialization method for ToolTip class. Receives data
    from object call and makes class instances of those variables
    Arguments:
    canvas - the canvas object within the tkinter instance.
    widget - the plane currently underneath the mouse.
    """
    def __init__(self, canvas, widget):
        self.canvas = canvas
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    
        """
        Method that shows the tip when mouse hovering over plane
        Arguments:
        text - message being generated when mouse is over plane
        """
    def showtip(self, text):
    
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.canvas.bbox(ALL)
        x = self.canvas.winfo_pointerx() + 10
        y = self.canvas.winfo_pointery() + 10
        self.tipwindow = tw = Toplevel(self.canvas)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        self.label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        self.label.pack(ipadx=1)

    """
    Hides the tool tip when mouse leaves the plane
    """
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

    """
    Method that facilitates the creation and destruction of tooltips,
    and binds those functions to user actions
    """
    def CreateToolTip(canvas, widget, text):
        toolTip = ToolTip(canvas, widget)
        def enter(event):
            toolTip.showtip(text)
        def leave(event):
            toolTip.hidetip()
        canvas.tag_bind(widget, '<Enter>', enter)
        canvas.tag_bind(widget, '<Leave>', leave)



"""
Class's main method. Creates an instance of 
Tkinter, then passes it to the GUI class.
"""
if __name__ == "__main__":
    
    root = Tk()
    Main = GUI(root)
    root.mainloop()
