# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:41:25 2020

@author: paolo
"""

import LocoDroneX

ldX = LocoDroneX.LocoDroneX()

ldX.connect('127.0.0.1:14540')

try:
    ldX.changeMode("MISSION")
    startPos = ldX.getData(LocoDroneX.GET_POSITION)
    distance = ldX.getTotalDisplacement(5)
    waypoints = {'points': []}
    ldX.takeoffAlt = 10
    
    choice = input("Type in 'A' for square pattern. Type in 'B for hourglass pattern, Type C for triangle pattern: ")
    if choice == "A":
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
    
    if choice == "B":
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
        
    if choice == "C":
        print("you chose Triangle")
        waypoints['points'].append([startPos['lat'], startPos['lon'], ldX.takeoffAlt])
        waypoints['points'].append([startPos['lat'], startPos['lon'] + distance[1], ldX.takeoffAlt])
        waypoints['points'].append([startPos['lat'] + distance[0], startPos['lon'], ldX.takeoffAlt])
        
        
        ldX.waypoints = waypoints['points'].copy()
    
        ldX.waypoints.insert(0, [startPos['lat'], startPos['lon'], startPos['alt']])
        ldX.createLoggers(LocoDroneX.LOG_DATA, 0.2)
    
        ldX.startMission(waypoints)
        ldX.disconnect()
        
    else:
        ldX.disconnect()
        print("invalid choice")
except Exception as e:
    ldX.disconect()
    print(e)
    
