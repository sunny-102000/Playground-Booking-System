from play_ground_booking import PlaygroundBookingSystem

# Example Usage
booking_system = PlaygroundBookingSystem()

# Creating User
user1 = booking_system.create_user()
print("User created successfully.")
booking_system.display_users()

# Creating Playground
playground1 = booking_system.create_playground()
print("Playground created successfully.")
booking_system.display_playgrounds()

# Making Booking
booking1 = booking_system.make_booking(user1, playground1)
print("Booking made successfully.")
booking_system.display_bookings()

# Making Payment
payment1 = booking_system.make_payment(booking1)
print("Payment made successfully.")
booking_system.display_payments()

# Save Changes to Excel
booking_system.save_changes()
