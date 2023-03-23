
# importing libraries

from os import path
from time import sleep
import argparse
def read_sensor_data(duration, sensor_data):
# to check whether file is passed in terminal
    if sensor_data is None:
        print("File Missing")
        return
    elif not path.exists(sensor_data):
        print("File not found")
        return
    else:
# to check for duration
        d = int(duration) / 1000 if duration else 0.1
 # reading the file
        with open(sensor_data, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                print(int(line)) #printing the data
                sleep(d)
read_sensor_data(duration=100, sensor_data="sensor_values")
