import unittest
from unittest.mock import patch
import io
import sys
import os
# import sensor_data
from os import path

import time 

import argparse

#from sensor_data import sensor_values
def read_sensor_data(duration, sensor_data):
    if sensor_data is None:
        print("File Missing")
        return
    elif not path.exists(sensor_data):
        print("File not found")
        return
    else:
        d = int(duration) / 1000 if duration else 0.1
        with open(sensor_data, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                print(int(line)) #printing the data
                time.sleep(d)

class TestReadSensorData(unittest.TestCase):
    def setUp(self):
        self.duration = 100
        self.sensor_data = "sensor_values"

    def test_file_missing(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            read_sensor_data(self.duration, None)
            self.assertEqual(fake_out.getvalue().strip(), "File Missing")

    def test_file_not_found(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            read_sensor_data(self.duration, "wrong_file_name")
            self.assertEqual(fake_out.getvalue().strip(), "File not found")

    def test_read_file(self):
        with patch('time.sleep') as mock_sleep:
            # create a file with sensor values
            sensor_file = open(self.sensor_data, 'w')
            sensor_file.write("1\n2\n3\n")
            sensor_file.close()

            with open(self.sensor_data, 'r') as f:
                # redirect stdout to check printed values
                with patch('sys.stdout', new=io.StringIO()) as fake_out:
                    read_sensor_data(self.duration, self.sensor_data)
                    self.assertEqual(fake_out.getvalue().strip(), "1\n2\n3")

                # check sleep function is called with the correct argument
                mock_sleep.assert_called_with(0.1)
                
            # delete the file after testing
            os.remove(self.sensor_data)
if __name__ == '__main__':
    unittest.main()

