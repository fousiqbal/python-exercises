
"""
This code reads sensor data from a file and prints it to the console with a specified time delay of 100ms between each reading. It takes two optional arguments:
    --duration: the time delay (in seconds) between readings, defaults to 0.1 seconds if not provided
    --sensor-data: the path to the file containing the sensor data
Usage: python script.py --duration 1 --sensor-data path/to/file.txt
Returns:
    None if file is missing or not found, otherwise prints the sensor data to console with a delay between each reading.
"""

# importing libraries
import unittest
from unittest.mock import patch
import io
import sys
import os
from os import path
import time
from time import sleep
import argparse
from display_data import read_sensor_data


# testcase class
class TestReadSensorData(unittest.TestCase):
    def setUp(self):
        self.duration = 100
        self.sensor_data = "sensor_values"

    # Test case 1: File missing
    def test_file_missing(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            read_sensor_data(self.duration, None)
            self.assertEqual(fake_out.getvalue().strip(), "File Missing")

    # Test case 2: File not found
    def test_file_not_found(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            read_sensor_data(self.duration, "wrong_file_name")
            self.assertEqual(fake_out.getvalue().strip(), "File not found")

    # Test case 3: Non-integer duration input
    def test_non_integer_duration_input(self):
        with patch("sys.stdout", new=io.StringIO()) as stdout:
            read_sensor_data(duration=100, sensor_data="sensor_values")
        self.assertGreater(len(stdout.getvalue()), 0)

    # Test case 4: No duration input
    def test_no_duration_input(self):
        with patch("sys.stdout", new=io.StringIO()) as stdout:
            read_sensor_data(duration=None, sensor_data="sensor_values")
        self.assertGreater(len(stdout.getvalue()), 0)

    # Test case 5: Reading sensor data from file
    def test_read_file(self):
        with patch("time.sleep") as mock_sleep:
            # create a file with sensor values
              location = "/home/fousiai/python_training/python-exercises/Assignments/sensor_data.py"
              sensor_file = open(self.sensor_data, 'w')
              sensor_file.write("1\n2\n3")
              sensor_file.close()
        with open(self.sensor_data, 'r') as f:
            # redirect stdout to check printed values
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                read_sensor_data(self.duration, self.sensor_data)
                self.assertEqual(fake_out.getvalue().strip(), "1\n2\n3")



if __name__ == "__main__":
    unittest.main()
    

