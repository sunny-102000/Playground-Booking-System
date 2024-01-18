import unittest
from unittest.mock import patch
from io import StringIO
from booking_system import new_booking, cancel_booking

class TestBookingSystem(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = "test_OBS.xls"

    def tearDown(self):
        # Clean up the temporary file
        try:
            os.remove(self.temp_file)
        except OSError:
            pass

    @patch('builtins.input', side_effect=["1", "10", "15", "1", "John Doe", "1234567890", "john.doe@example.com"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_successful_booking(self, mock_stdout, mock_input):
        new_booking("John Doe", "1234567890", 1, "john.doe@example.com", self.temp_file)

        # Verify that the output contains the expected success message
        self.assertIn("Booking successful", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
