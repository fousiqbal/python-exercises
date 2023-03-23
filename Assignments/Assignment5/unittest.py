import unittest
from unittest.mock import patch
from io import StringIO
from os import remove

class TestSensorDataReading(unittest.TestCase):
    def setUp(self):
        # create a file with sensor data for testing
        with open("test_sensor_values", "w") as f:
            f.write("10\n20\n30\n40\n50\n")


    def test_missing_file(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            read_sensor_data(duration=100, sensor_data=None)
            self.assertEqual(fake_out.getvalue().strip(), "File Missing")

    def test_file_not_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            read_sensor_data(duration=100, sensor_data="non_existing_file")
            self.assertEqual(fake_out.getvalue().strip(), "File not found")

    def test_reading_data(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            read_sensor_data(duration=100, sensor_data="test_sensor_values")
            self.assertEqual(fake_out.getvalue().strip(), "10\n20\n30\n40\n50")

    def test_duration(self):
        with patch('sys.stdout', new=StringIO()) as fake_out, patch('time.sleep') as mock_sleep:
            read_sensor_data(duration=500, sensor_data="test_sensor_values")
            mock_sleep.assert_called_with(0.5) # check if sleep function is called with correct argument

if __name__ == '__main__':
    unittest.main()

