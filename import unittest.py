import unittest
import os
from unittest.mock import patch
from io import StringIO
from booking_system import new_booking, cancel_booking  # Adjust the module name accordingly

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

    def test_new_booking_successful(self):
        # Simulate user input
        user_input = "1\n10\n15\n1\n"

        # Redirect stdin to simulate user input
        with patch("builtins.input", side_effect=user_input.split("\n")):
            # Redirect stdout to capture print statements
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                new_booking("John Doe", "1234567890", 1, "john.doe@example.com", self.temp_file)

                # Verify that the output contains the expected success message
                self.assertIn("Booking successful", mock_stdout.getvalue())

    def test_cancel_booking_successful(self):
        # Simulate user input
        user_input = "1\n10\n15\n1\n"

        # Redirect stdin to simulate user input
        with patch("builtins.input", side_effect=user_input.split("\n")):
            # Redirect stdout to capture print statements
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                cancel_booking("John Doe", "1234567890", "john.doe@example.com", self.temp_file)

                # Verify that the output contains the expected success message
                self.assertIn("Cancellation successful", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
