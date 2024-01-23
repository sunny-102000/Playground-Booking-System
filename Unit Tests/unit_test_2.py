import unittest
from unittest.mock import patch
from play_ground_booking import PlaygroundBookingSystem

class TestPlaygroundBookingSystem(unittest.TestCase):
    def setUp(self):
        self.booking_system = PlaygroundBookingSystem("bookings.xlsx")

    def tearDown(self):
        # Clean up the test file after each test
        import os
        if os.path.exists("bookings.xlsx"):
            os.remove("bookings.xlsx")

    @patch('builtins.input', side_effect=['John Doe', '1234567890', 'JD123', 'john.doe@example.com'])
    def test_create_user(self, mock_input):
        user = self.booking_system.create_user()
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.mobile_number, '1234567890')
        self.assertEqual(user.user_id, 'JD123')
        self.assertEqual(user.email, 'john.doe@example.com')

    @patch('builtins.input', side_effect=['Cricket', 'Stadium', 'CG01', '100'])
    def test_create_playground(self, mock_input):
        playground = self.booking_system.create_playground()
        self.assertEqual(playground.specific_ground, 'Cricket')
        self.assertEqual(playground.location, 'Stadium')
        self.assertEqual(playground.playground_id, 'CG01')  # Ensure playground ID is a string
        self.assertEqual(playground.price_ground, 100)

#    ## @patch('builtins.input', side_effect=['card'])
#     def test_make_payment(self, mock_input):
#         user = self.booking_system.create_user()
#         playground = self.booking_system.create_playground()
#         booking = self.booking_system.make_booking(user, playground)
#         payment = self.booking_system.make_payment(booking)
#         self.assertEqual(payment.payment_id, 1)  # Assuming it's the first payment created for the test
#         self.assertEqual(payment.price, playground.price_ground)
#         self.assertEqual(payment.payment_type, 'card')
#         self.assertIsNotNone(payment.payment_date)

    def test_save_changes(self):
        # Assuming there are some users, playgrounds, bookings, and payments already created
        # Add relevant assertions based on your implementation
        self.booking_system.save_changes()
        # Check if changes are reflected in the Excel file (you may need to read the file and assert)

if __name__ == '__main__':
    unittest.main()
