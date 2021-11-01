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
    ZBW = PhotoImage(file = './icons/ZBW.png')
    canvas.create_image(970,185,image=ZBW)

    #test image of plane
    plane2 = Image.open('./icons/airplane-icon-2-19.png') # 19x19 pixel image
    plane2Rot = plane2.rotate(45,Image.BICUBIC) # rotate 45deg, retain quality
    plane2done = ImageTk.PhotoImage(plane2Rot) # make it a photoimage (transparent bg)

    img_ref = []
    plane_ref = []
    
    flight_chart_array = FlightData.flightDataPull(20.038,-130.974,-65.748,50.214)

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

    for i in range(len(AAL_X_Array)):
        plane3 = plane2.rotate(AAL_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AAL_X_Array[i], AAL_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(AAY_X_Array)):
        plane3 = plane2.rotate(AAY_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AAY_X_Array[i], AAY_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(ACA_X_Array)):
        plane3 = plane2.rotate(ACA_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(ACA_X_Array[i], ACA_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(AFR_X_Array)):
        plane3 = plane2.rotate(AFR_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AFR_X_Array[i], AFR_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(AMX_X_Array)):
        plane3 = plane2.rotate(AMX_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(AMX_X_Array[i], AMX_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(ASA_X_Array)):
        plane3 = plane2.rotate(ASA_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(ASA_X_Array[i], ASA_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(DAL_X_Array)):
        plane3 = plane2.rotate(DAL_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(DAL_X_Array[i], DAL_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(FFT_X_Array)):
        plane3 = plane2.rotate(FFT_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(FFT_X_Array[i], FFT_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(JBU_X_Array)):
        plane3 = plane2.rotate(JBU_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(JBU_X_Array[i], JBU_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(NKS_X_Array)):
        plane3 = plane2.rotate(NKS_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(NKS_X_Array[i], NKS_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(SWA_X_Array)):
        plane3 = plane2.rotate(SWA_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(SWA_X_Array[i], SWA_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    for i in range(len(UAL_X_Array)):
        plane3 = plane2.rotate(UAL_Arraytrue[i], Image.BICUBIC)
        plane3done = ImageTk.PhotoImage(plane3)
        canvas.create_image(UAL_X_Array[i], UAL_Y_Array[i], image=plane3done)
        plane_ref.append(plane3done)

    root.mainloop()



if __name__ == "__main__":
    

    Main = GUI()
