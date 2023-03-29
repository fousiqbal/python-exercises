
"""
This code reads sensor data from a file and prints it to the console with a specified time delay of 100ms between each reading. It takes two optional arguments:
    --duration: the time delay (in seconds) between readings, defaults to 0.1 seconds if not provided
    --sensor-data: the path to the file containing the sensor data
Usage: python script.py --duration 1 --sensor-data path/to/file.txt
Returns:
    None if file is missing or not found, otherwise prints the sensor data to console with a delay between each reading.
"""


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
                                                     #int function is used to convert a string input to an integer which is required for mathematical calculations in the read_sensor_data function.
        # reading the file
        with open(sensor_data, "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                print(int(line))  # printing the data
                sleep(d) #for delay of 100ms

if __name__ == "__main__":
     read_sensor_data(duration=100, sensor_data="sensor_values")
