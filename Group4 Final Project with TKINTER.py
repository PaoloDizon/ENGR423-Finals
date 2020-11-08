# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:41:25 2020

@author: paolo
"""

import LocoDroneX
from tkinter import *


ldX = LocoDroneX.LocoDroneX()

ldX.connect('127.0.0.1:14540')


    
ldX.changeMode("MISSION")
startPos = ldX.getData(LocoDroneX.GET_POSITION)
distance = ldX.getTotalDisplacement(5)
waypoints = {'points': []}
ldX.takeoffAlt = 10



def square():
    
    print("you chose square")
    waypoints['points'].append([startPos['lat'],
                           startPos['lon'] + distance[1],
                           ldX.takeoffAlt])
    waypoints['points'].append([startPos['lat'] + distance[0],
                           startPos['lon'] + distance[1],
                           ldX.takeoffAlt])
    waypoints['points'].append([startPos['lat'] + distance[0],
                           startPos['lon'],
                           ldX.takeoffAlt])
    
    ldX.waypoints = waypoints['points'].copy()

    ldX.waypoints.insert(0, [startPos['lat'], startPos['lon'], startPos['alt']])
    ldX.createLoggers(LocoDroneX.LOG_DATA, 0.2)

    ldX.startMission(waypoints)
    ldX.disconnect()

def hourglass():
    print("you chose Hourglass")
    waypoints['points'].append([startPos['lat'], startPos['lon'], ldX.takeoffAlt])
    waypoints['points'].append([startPos['lat'], startPos['lon'] + distance[1], ldX.takeoffAlt])
    waypoints['points'].append([startPos['lat'] + distance[0], startPos['lon'], ldX.takeoffAlt])
    waypoints['points'].append([startPos['lat'] + distance[0], startPos['lon'] + distance[1], ldX.takeoffAlt])
    
    ldX.waypoints = waypoints['points'].copy()

    ldX.waypoints.insert(0, [startPos['lat'], startPos['lon'], startPos['alt']])
    ldX.createLoggers(LocoDroneX.LOG_DATA, 0.2)

    ldX.startMission(waypoints)
    ldX.disconnect()
    
def triangle():
    print("you chose Triangle")
    waypoints['points'].append([startPos['lat'], startPos['lon'], ldX.takeoffAlt])
    waypoints['points'].append([startPos['lat'], startPos['lon'] + distance[1], ldX.takeoffAlt])
    waypoints['points'].append([startPos['lat'] + distance[0], startPos['lon'], ldX.takeoffAlt])
    
    
    ldX.waypoints = waypoints['points'].copy()

    ldX.waypoints.insert(0, [startPos['lat'], startPos['lon'], startPos['alt']])
    ldX.createLoggers(LocoDroneX.LOG_DATA, 0.2)

    ldX.startMission(waypoints)
    ldX.disconnect()
    
    
    
window = Tk()

window.title("Welcome to the thunderdome")

window.geometry('350x200')


lbl = Label(window, text = "Pick a shape")

lbl.grid(column = 0, row = 0)

btn1 = Button(window, text = "Square", command = square)
btn1.grid(column=0, row = 2)

btn2 = Button(window, text = "Hourglass", command = hourglass)
btn2.grid(column = 0, row = 3)

btn2 = Button(window, text = "Triangle", command = triangle)
btn2.grid(column = 0, row = 4)


window.mainloop()    
    

    
