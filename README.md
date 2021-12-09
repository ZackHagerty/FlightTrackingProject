# FlightTrackingProject ERAU SE 300



## Description
This is Flight Tracking, a team project built in python over the course of ten weeks. Using data retrieved from the OneSky API, Flight Tracking displays and updates the locations of live flights across the continental United States. Flight Tracking is robust, with a focus on user interactivity and a heavy emphasis on a retro aesthetic. The user can utilize the U.I. to filter visible flights by company or Air Traffic Control (ATC) zone, allowing the user to fullly focus on one specific location or company.

To obtain info on specific flights, the user can hover over a live flight with their cursor to display the company's call sign and the plane's tail number.

This is a class project for **Embry-Riddle Aeronautical University***, class **SE 300*** (Software Engineering Practices)

The program was built by myself and my teammates, Devon Casey, Matthew Jolliffe, and Matthew Grabasch. 


## Languages and Packages

Python 3.9.7 https://www.python.org/downloads/release/python-397/

Flight Tracking relies heavily on Tkinter, a GUI package originally released in 1991 https://docs.python.org/3/library/tkinter.html

## Features 

### Default State:
![image](https://user-images.githubusercontent.com/70977089/145338021-3dba8151-576e-4d0e-9f14-9e41a4773531.png)

### Flight Tracking's Help Menu is Clippy!

![image](https://user-images.githubusercontent.com/70977089/145338176-ab4760a2-e09c-430b-a602-e5405615ba2c.png)

### ATC Zone and Company Filtering

![Animation](https://user-images.githubusercontent.com/70977089/145338661-731dfb33-1799-46cf-ba60-fca6f41d8616.gif)

## Guide

### To run:

1.) Create a virtual environment in python:
For more information, refer to https://docs.python.org/3/tutorial/venv.html

2.) Activate the virtual environment in console, and cd to the project directory.

3.) Run the command "pip install -r requirements.txt"

4.)Run the command "python GUI.py"

## UI

There are two filtering menus and a help menu. If you'd like to learn how to use the software, our good friend Clippy can help you out!

![Clippy](https://user-images.githubusercontent.com/70977089/145338919-b1632ed1-13bb-4576-826b-fb12cd537844.png)


## Known Issues:

1.) Tkinter, being as old as it is, struggles to plot the planes during data pulls. So, every twenty seconds, the UI freezes for roughly 1-5 seconds while the system refreshes.

2.) It's theorized that, after about eight hours, Flight Tracking might crash due to a memory error. Further soak testing is necessary to determine if this is actually an issue.
