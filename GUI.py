from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np

from FlightDataImport import FlightData

class GUI():

    root = Tk()

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

    # COLORFUL PLANES!! =D
    plane_burgundy = Image.open('./Airline-colors-19px/bergundy-19.png')
    plane_cyan = Image.open('./Airline-colors-19px/cyan-19.png')
    plane_dark_blue = Image.open('./Airline-colors-19px/dark-blue-19.png')
    plane_dark_green = Image.open('./Airline-colors-19px/dark-green-19.png')
    plane_darker_blue = Image.open('./Airline-colors-19px/darker-blue-19.png')
    plane_gold = Image.open('./Airline-colors-19px/gold-19.png')
    plane_green = Image.open('./Airline-colors-19px/green-19.png')
    plane_light_blue = Image.open('./Airline-colors-19px/light-blue-19.png')
    plane_light_gray = Image.open('./Airline-colors-19px/light-gray-19.png')
    plane_orange = Image.open('./Airline-colors-19px/orange-19.png')
    plane_red = Image.open('./Airline-colors-19px/red-19.png')
    plane_sky_blue = Image.open('./Airline-colors-19px/sky-blue-19.png')
    plane_violet = Image.open('./Airline-colors-19px/violet-19.png')
    plane_yellow = Image.open('./Airline-colors-19px/yellow-19.png')

    # =======================   ATC Zones   ===============================
    #ZBW
    atc_zbw = Image.open('./atc_zones/sized_ATC/ZBW-170.png')
    atc_BW = ImageTk.PhotoImage(atc_zbw)
    canvas.create_image(995, 151, image=atc_BW)

    #ZNY
    atc_zny = Image.open('./atc_zones/sized_ATC/zny-84.png')
    atc_NY = ImageTk.PhotoImage(atc_zny)
    canvas.create_image(929, 207, image=atc_NY)

    #ZOB
    atc_zob = Image.open('./atc_zones/sized_ATC/zob-154.png')
    atc_OB = ImageTk.PhotoImage(atc_zob)
    canvas.create_image(845, 193, image=atc_OB)

    #ZDC
    atc_zdc = Image.open('./atc_zones/sized_ATC/zdc-148.png')
    atc_DC = ImageTk.PhotoImage(atc_zdc)
    canvas.create_image(915, 309, image=atc_DC)

    #ZID
    atc_zid = Image.open('./atc_zones/sized_ATC/zid-137.png')
    atc_ID = ImageTk.PhotoImage(atc_zid)
    canvas.create_image(780, 260, image=atc_ID)

    #ZTL
    atc_ztl = Image.open('./atc_zones/sized_ATC/ztl-150.png')
    atc_TL = ImageTk.PhotoImage(atc_ztl)
    canvas.create_image(786, 355, image=atc_TL)

    #ZJX
    atc_zjx = Image.open('./atc_zones/sized_ATC/zjx-203.png')
    atc_JX = ImageTk.PhotoImage(atc_zjx)
    canvas.create_image(817, 425, image=atc_JX)

    #ZMA
    atc_zma = Image.open('./atc_zones/sized_ATC/zma-165.png')
    atc_MA = ImageTk.PhotoImage(atc_zma)
    canvas.create_image(834, 520, image=atc_MA)

    #ZHU
    atc_zhu = Image.open('./atc_zones/sized_ATC/zhu-289.png')
    atc_HU = ImageTk.PhotoImage(atc_zhu)
    canvas.create_image(610, 497, image=atc_HU)

    #ZME
    atc_zme = Image.open('./atc_zones/sized_ATC/zme-183.png')
    atc_ME = ImageTk.PhotoImage(atc_zme)
    canvas.create_image(674, 348, image=atc_ME)

    #ZKC
    atc_zkc = Image.open('./atc_zones/sized_ATC/zkc-253.png')
    atc_KC = ImageTk.PhotoImage(atc_zkc)
    canvas.create_image(591, 270, image=atc_KC)

    #ZAU
    atc_zau = Image.open('./atc_zones/sized_ATC/zau-156.png')
    atc_AU = ImageTk.PhotoImage(atc_zau)
    canvas.create_image(698, 180, image=atc_AU)

    #ZMP
    atc_zmp = Image.open('./atc_zones/sized_ATC/zmp-363.png')
    atc_MP = ImageTk.PhotoImage(atc_zmp)
    canvas.create_image(637, 135, image=atc_MP)

    #ZFW
    atc_zfw = Image.open('./atc_zones/sized_ATC/zfw-215.png')
    atc_FW = ImageTk.PhotoImage(atc_zfw)
    canvas.create_image(549, 375, image=atc_FW)
    
    #ZAB
    atc_zab = Image.open('./atc_zones/sized_ATC/zab-245.png')
    atc_AB = ImageTk.PhotoImage(atc_zab)
    canvas.create_image(391, 379, image=atc_AB)

    #ZDV
    atc_zdv = Image.open('./atc_zones/sized_ATC/zdv-230.png')
    atc_DV = ImageTk.PhotoImage(atc_zdv)
    canvas.create_image(421, 218, image=atc_DV)

    #ZLC
    atc_zlc = Image.open('./atc_zones/sized_ATC/zlc-283.png')
    atc_LC = ImageTk.PhotoImage(atc_zlc)
    canvas.create_image(317, 157, image=atc_LC)

    #ZLA
    atc_zla = Image.open('./atc_zones/sized_ATC/zla-204.png')
    atc_LA = ImageTk.PhotoImage(atc_zla)
    canvas.create_image(214, 355, image=atc_LA)

    #ZOA
    atc_zoa = Image.open('./atc_zones/sized_ATC/zoa-172.png')
    atc_OA = ImageTk.PhotoImage(atc_zoa)
    canvas.create_image(136, 276, image=atc_OA)

    #ZSE
    atc_zse = Image.open('./atc_zones/sized_ATC/zse-230.png')
    atc_SE = ImageTk.PhotoImage(atc_zse)
    canvas.create_image(146, 126, image=atc_SE)

    # =====================   END ATC Zones   ===============================

    img_ref = []
    plane_ref = []
    
    # Read the flight data
    flight_chart_array = FlightData.flightDataPull(20.038,-130.974,-65.748,50.214)

    # These arrays are for placing the planes and their directions
    AAL_Arraylong = []
    AAL_Arraylat = []
    AAL_Arraytrue = []

    AAY_Arraylong = []
    AAY_Arraylat = []
    AAY_Arraytrue = []

    ACA_Arraylong = []
    ACA_Arraylat = []
    ACA_Arraytrue = []

    AFR_Arraylong = []
    AFR_Arraylat = []
    AFR_Arraytrue = []

    AMX_Arraylong = []
    AMX_Arraylat = []
    AMX_Arraytrue = []

    ASA_Arraylong = []
    ASA_Arraylat = []
    ASA_Arraytrue = []

    DAL_Arraylong = []
    DAL_Arraylat = []
    DAL_Arraytrue = []

    FFT_Arraylong = []
    FFT_Arraylat = []
    FFT_Arraytrue = []

    JBU_Arraylong = []
    JBU_Arraylat = []
    JBU_Arraytrue = []

    NKS_Arraylong = []
    NKS_Arraylat = []
    NKS_Arraytrue = []

    SWA_Arraylong = []
    SWA_Arraylat = []
    SWA_Arraytrue = []

    UAL_Arraylong = []
    UAL_Arraylat = []
    UAL_Arraytrue = []

    #Sort by company code, add it to each array
    for i in range(len(flight_chart_array)):
        
        if flight_chart_array[i,1].startswith('AAL'):
            AAL_Arraylong.append(flight_chart_array[i,5])
            AAL_Arraylat.append(flight_chart_array[i,6])
            AAL_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('AAY'):
            AAY_Arraylong.append(flight_chart_array[i,5])
            AAY_Arraylat.append(flight_chart_array[i,6])
            AAY_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('ACA'):
            ACA_Arraylong.append(flight_chart_array[i,5])
            ACA_Arraylat.append(flight_chart_array[i,6])
            ACA_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('AFR'):
            AFR_Arraylong.append(flight_chart_array[i,5])
            AFR_Arraylat.append(flight_chart_array[i,6])
            AFR_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('AMX'):
            AMX_Arraylong.append(flight_chart_array[i,5])
            AMX_Arraylat.append(flight_chart_array[i,6])
            AMX_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('ASA'):
            ASA_Arraylong.append(flight_chart_array[i,5])
            ASA_Arraylat.append(flight_chart_array[i,6])
            ASA_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('DAL'):
            DAL_Arraylong.append(flight_chart_array[i,5])
            DAL_Arraylat.append(flight_chart_array[i,6])
            DAL_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('FFT'):
            FFT_Arraylong.append(flight_chart_array[i,5])
            FFT_Arraylat.append(flight_chart_array[i,6])
            FFT_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('JBU'):
            JBU_Arraylong.append(flight_chart_array[i,5])
            JBU_Arraylat.append(flight_chart_array[i,6])
            JBU_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('NKS'):
            NKS_Arraylong.append(flight_chart_array[i,5])
            NKS_Arraylat.append(flight_chart_array[i,6])
            NKS_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('SWA'):
            SWA_Arraylong.append(flight_chart_array[i,5])
            SWA_Arraylat.append(flight_chart_array[i,6])
            SWA_Arraytrue.append(flight_chart_array[i,10])

        if flight_chart_array[i,1].startswith('UAL'):
            UAL_Arraylong.append(flight_chart_array[i,5])
            UAL_Arraylat.append(flight_chart_array[i,6])
            UAL_Arraytrue.append(flight_chart_array[i,10])

    # Translate lat/long to x/y for the GUI
    AAL_X_Array, AAL_Y_Array = FlightData.coordinateTranslate(AAL_Arraylat,AAL_Arraylong)
    AAY_X_Array, AAY_Y_Array = FlightData.coordinateTranslate(AAY_Arraylat,AAY_Arraylong)
    ACA_X_Array, ACA_Y_Array = FlightData.coordinateTranslate(ACA_Arraylat,ACA_Arraylong)
    AFR_X_Array, AFR_Y_Array = FlightData.coordinateTranslate(AFR_Arraylat,AFR_Arraylong)
    AMX_X_Array, AMX_Y_Array = FlightData.coordinateTranslate(AMX_Arraylat,AMX_Arraylong)
    ASA_X_Array, ASA_Y_Array = FlightData.coordinateTranslate(ASA_Arraylat,ASA_Arraylong)
    DAL_X_Array, DAL_Y_Array = FlightData.coordinateTranslate(DAL_Arraylat,DAL_Arraylong)
    FFT_X_Array, FFT_Y_Array = FlightData.coordinateTranslate(FFT_Arraylat,FFT_Arraylong)
    JBU_X_Array, JBU_Y_Array = FlightData.coordinateTranslate(JBU_Arraylat,JBU_Arraylong)
    NKS_X_Array, NKS_Y_Array = FlightData.coordinateTranslate(NKS_Arraylat,NKS_Arraylong)
    SWA_X_Array, SWA_Y_Array = FlightData.coordinateTranslate(SWA_Arraylat,SWA_Arraylong)
    UAL_X_Array, UAL_Y_Array = FlightData.coordinateTranslate(UAL_Arraylat,UAL_Arraylong)
    #print(long_Array)

    # =====================   PLANE PLACEMENT   ===============================    
    
    # place each plane in x,y and with rotation with each color per airline
    
    # American
    for i in range(len(AAL_X_Array)):
        plane3 = plane_sky_blue.rotate(AAL_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AAL_X_Array[i], AAL_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Allegiant
    for i in range(len(AAY_X_Array)):
        plane3 = plane_orange.rotate(AAY_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AAY_X_Array[i], AAY_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Air Canada
    for i in range(len(ACA_X_Array)):
        plane3 = plane_red.rotate(ACA_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(ACA_X_Array[i], ACA_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Air France
    for i in range(len(AFR_X_Array)):
        plane3 = plane_light_blue.rotate(AFR_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AFR_X_Array[i], AFR_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # AeroMexico
    for i in range(len(AMX_X_Array)):
        plane3 = plane_green.rotate(AMX_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AMX_X_Array[i], AMX_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Air Alaska
    for i in range(len(ASA_X_Array)):
        plane3 = plane_light_gray.rotate(ASA_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(ASA_X_Array[i], ASA_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Delta
    for i in range(len(DAL_X_Array)):
        plane3 = plane_burgundy.rotate(DAL_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(DAL_X_Array[i], DAL_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Frontier
    for i in range(len(FFT_X_Array)):
        plane3 = plane_dark_green.rotate(FFT_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(FFT_X_Array[i], FFT_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Jetblue
    for i in range(len(JBU_X_Array)):
        plane3 = plane_cyan.rotate(JBU_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(JBU_X_Array[i], JBU_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Spirit
    for i in range(len(NKS_X_Array)):
        plane3 = plane_yellow.rotate(NKS_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(NKS_X_Array[i], NKS_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # Southwest
    for i in range(len(SWA_X_Array)):
        plane3 = plane_darker_blue.rotate(SWA_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(SWA_X_Array[i], SWA_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    # United
    for i in range(len(UAL_X_Array)):
        plane3 = plane_gold.rotate(UAL_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(UAL_X_Array[i], UAL_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)


    # this gotta be the last line or it all doesn't work
    root.mainloop()



if __name__ == "__main__":
    

    Main = GUI()
