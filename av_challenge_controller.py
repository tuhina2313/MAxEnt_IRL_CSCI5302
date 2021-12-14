"""av_challenge_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Camera , Keyboard, GPS, Supervisor
from vehicle import Car, Driver
import math
# from time import strptime
import csv

import random
import numpy as np

TIMESTEP = 64

def activate_devices():
    front_camera = tesla.getDevice("front_camera")
    rear_camera = tesla.getDevice("rear_camera")
    
    front_camera.enable(20)
    rear_camera.enable(30)
    lidar = tesla.getDevice("Sick LMS 291")
    lidar.enable(TIMESTEP)
    lidar.enablePointCloud()
    
def initialize_variables():
    avoidObstacleCounter = 0

def run_simulation():
    tesla = Driver()
    
    keyboard=Keyboard()
    keyboard.enable(TIMESTEP)
    
    curr_time = tesla.getTime()
    start_time = tesla.getTime()
    
    gps = tesla.getDevice("gps")
    gps.enable(TIMESTEP)
    
    episode =[]
    
    speed = 25
    
    curr_state = gps.getValues()
    curr_state.append(tesla.getSteeringAngle())
    curr_state.append(-1)
    
    while (tesla.step()) != -1:
        key = keyboard.getKey()
        tesla.setCruisingSpeed(speed)
        tesla.setGear(1)
        lidar = tesla.getDevice("Sick LMS 291")
        
        if key== 315:
            tesla.setCruisingSpeed(speed + 10)
            tesla.setSteeringAngle(0.0)
        elif key== 317:
            tesla.setBrakeIntensity(0.0)
        elif key== 314:
            tesla.setSteeringAngle(-0.3)
            # tesla.setCruisingSpeed(speed)
        elif key== 316:
            tesla.setSteeringAngle(0.3)
            # tesla.setCruisingSpeed(speed)
        else:
            tesla.setCruisingSpeed(0)
        
        if tesla.getTime() - curr_time > 2:
            state_tuple = []
            state_tuple.append(curr_state)
            curr_state = gps.getValues()
            for i in range(len(curr_state)):
                curr_state[i] = round(curr_state[i])
            curr_state.append(round(tesla.getSteeringAngle(),1))
            curr_state.append(key)
            state_tuple.append(curr_state)
            episode.append(state_tuple)
            curr_time = tesla.getTime()
        
        if tesla.getTime() - start_time > 15:
            with open('output2.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(episode)
            start_time = tesla.getTime()
    
        #controller termination
        if tesla.step() == -1:
            print("Terminating")
            with open("output2.csv", "wb") as f:
                file.truncate(0)
                writer = csv.writer(f)
                writer.writerows(state_tuple)
    
    robot_node.resetPhysics()
    print("Terminating")    
    return state_tuple     


if __name__ == "__main__":
    # activate_devices()
    # initialize_variables()
    
    gps_pos , gps_theta = run_simulation()
    print("END", len(gps_pos))

