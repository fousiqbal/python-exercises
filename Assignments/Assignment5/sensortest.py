import unittest
import io
import sys
from unittest.mock import patch
from test.support import captured_stdout
from os import path
from time import sleep
import argparse
from unittest.mock import MagicMock

from display_data import read_sensor_data


class TestReadSensorData(unittest.TestCase):

    # Test case 1: Missing file argument
    def test_missing_file_argument(self):
        expected_output = "File Missing\n"
        with captured_stdout() as stdout:
            read_sensor_data(duration=100, sensor_data=None)
        self.assertEqual(stdout.getvalue(), expected_output)

    # Test case 2: File not found
    def test_file_not_found(self):
        expected_output = "File not found\n"
        with captured_stdout() as stdout:
            read_sensor_data(duration=100, sensor_data="fake_file")
        self.assertEqual(stdout.getvalue(), expected_output)

    # Test case 3: Reading sensor data from file
    @patch('builtins.open', new_callable=MagicMock)
    @patch('time.sleep', new_callable=MagicMock)
    def test_read_sensor_data(self, mock_sleep, mock_file):
        mock_file.return_value.__enter__.return_value.readline.side_effect = ['1\n', '2\n', '3\n', '']
        expected_output = "1\n2\n3\n"
        with captured_stdout() as stdout:
            read_sensor_data(duration=100, sensor_data="sensor_values")
        self.assertEqual(stdout.getvalue(), expected_output)
        self.assertEqual(mock_sleep.call_count, 3)

    # Test case 4: Non-integer duration input
    def test_non_integer_duration_input(self):
        with captured_stdout() as stdout:
            read_sensor_data(duration="abc", sensor_data="sensor_values")
        self.assertGreater(len(stdout.getvalue()), 0)

    # Test case 5: No duration input
    def test_no_duration_input(self):
        with captured_stdout() as stdout:
            read_sensor_data(duration=None, sensor_data="sensor_values")
        self.assertGreater(len(stdout.getvalue()), 0)

if __name__ == '__main__':
    unittest.main()

