from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np

from FlightDataImport import FlightData

class GUI():

    def __init__(self):

        self.root = Tk()
        frame = Frame(self.root)
        frame.pack()
        self.canvas = Canvas(frame, bg = "black", width=1114, height=642)
        self.canvas.pack()
        self.initializingArrays()

        
    #Sets up the frame and background self.canvas
    def initializingArrays(self):
        #background image of US
        USAMapImage1 = PhotoImage(file = './U.S.A Images/Untitled.png')
        self.canvas.create_image(557,(321), image=USAMapImage1)
       
        #test image of plane
        self.plane2 = Image.open('./icons/airplane-icon-2-19.png') # 19x19 pixel image
        plane2Rot = self.plane2.rotate(45,Image.BICUBIC) # rotate 45deg, retain quality
        plane2done = ImageTk.PhotoImage(plane2Rot) # make it a photoimage (transparent bg)

        img_ref = []
        self.plane_ref = []
        
        flight_chart_array = FlightData.flightDataPull(20.038,-130.974,-65.748,50.214)

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

        self.createPlanes()


        
    def createPlanes(self):

        AAL_X_Array, AAL_Y_Array = FlightData.coordinateTranslate(self.AAL_Arraylat,self.AAL_Arraylong)
        AAY_X_Array, AAY_Y_Array = FlightData.coordinateTranslate(self.AAY_Arraylat,self.AAY_Arraylong)
        ACA_X_Array, ACA_Y_Array = FlightData.coordinateTranslate(self.ACA_Arraylat,self.ACA_Arraylong)
        AFR_X_Array, AFR_Y_Array = FlightData.coordinateTranslate(self.AFR_Arraylat,self.AFR_Arraylong)
        AMX_X_Array, AMX_Y_Array = FlightData.coordinateTranslate(self.AMX_Arraylat,self.AMX_Arraylong)
        ASA_X_Array, ASA_Y_Array = FlightData.coordinateTranslate(self.ASA_Arraylat,self.ASA_Arraylong)
        DAL_X_Array, DAL_Y_Array = FlightData.coordinateTranslate(self.DAL_Arraylat,self.DAL_Arraylong)
        FFT_X_Array, FFT_Y_Array = FlightData.coordinateTranslate(self.FFT_Arraylat,self.FFT_Arraylong)
        JBU_X_Array, JBU_Y_Array = FlightData.coordinateTranslate(self.JBU_Arraylat,self.JBU_Arraylong)
        NKS_X_Array, NKS_Y_Array = FlightData.coordinateTranslate(self.NKS_Arraylat,self.NKS_Arraylong)
        SWA_X_Array, SWA_Y_Array = FlightData.coordinateTranslate(self.SWA_Arraylat,self.SWA_Arraylong)
        UAL_X_Array, UAL_Y_Array = FlightData.coordinateTranslate(self.UAL_Arraylat,self.UAL_Arraylong)
        #print(long_Array)

        for i in range(len(AAL_X_Array)):
            plane3 = self.plane2.rotate(self.AAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(AAL_X_Array[i], AAL_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(AAY_X_Array)):
            plane3 = self.plane2.rotate(self.AAY_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(AAY_X_Array[i], AAY_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(ACA_X_Array)):
            plane3 = self.plane2.rotate(self.ACA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(ACA_X_Array[i], ACA_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(AFR_X_Array)):
            plane3 = self.plane2.rotate(self.AFR_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(AFR_X_Array[i], AFR_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(AMX_X_Array)):
            plane3 = self.plane2.rotate(self.AMX_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(AMX_X_Array[i], AMX_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(ASA_X_Array)):
            plane3 = self.plane2.rotate(self.ASA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(ASA_X_Array[i], ASA_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(DAL_X_Array)):
            plane3 = self.plane2.rotate(self.DAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(DAL_X_Array[i], DAL_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(FFT_X_Array)):
            plane3 = self.plane2.rotate(self.FFT_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(FFT_X_Array[i], FFT_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(JBU_X_Array)):
            plane3 = self.plane2.rotate(self.JBU_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(JBU_X_Array[i], JBU_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(NKS_X_Array)):
            plane3 = self.plane2.rotate(self.NKS_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(NKS_X_Array[i], NKS_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(SWA_X_Array)):
            plane3 = self.plane2.rotate(self.SWA_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(SWA_X_Array[i], SWA_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        for i in range(len(UAL_X_Array)):
            plane3 = self.plane2.rotate(self.UAL_Arraytrue[i], Image.BICUBIC)
            plane3done = ImageTk.PhotoImage(plane3)
            self.canvas.create_image(UAL_X_Array[i], UAL_Y_Array[i], image=plane3done)
            self.plane_ref.append(plane3done)

        self.root.mainloop()


        
if __name__ == "__main__":
    

    Main = GUI()
