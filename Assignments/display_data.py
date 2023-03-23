# importing libraries

from os import path #to import the path module from the os package that is used to check if the file passed as an argument exists or not using the path.exists() function.
from time import sleep #sleep is a function provided by the time module in Python,used to pause the execution of a program for a specified number of seconds.
import argparse


def read_sensor_data(duration, sensor_data):
    # to check whether file is passed in terminal
    if sensor_data is None:
        print("File Missing") #if sensor_value is not provided
        return
    elif not path.exists(sensor_data):
        print("File not found") #if the sensor_value path is wrong
        return
    else:
        # to check for duration
        d = int(duration) / 1000 if duration else 0.1 #1s=1000ms so divide the duration by 1000, if not provided set default value of 100ms/0.1s
        # reading the file
        with open(sensor_data, "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                print(int(line))  # printing the data
                sleep(d) #for delay of 100ms


#read_sensor_data(duration=100, sensor_data="sensor_values")
