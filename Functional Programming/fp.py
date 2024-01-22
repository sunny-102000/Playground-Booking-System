import pandas as pd
import datetime

# Point 1: Only final data structures
# Functional programming style using dictionaries for data structures
# No classes, simple data structures
def create_user():
    # Point 2: (Mostly) side-effect-free functions
    # Input parameters, output result, no modification of external state
    name = input("Enter user name: ")
    mobile_number = input("Enter mobile number: ")
    user_id = input("Enter user ID: ")
    email = input("Enter email: ")
    return {'name': name, 'mobile_number': mobile_number, 'user_id': user_id, 'email': email}

def save_changes(users, playgrounds, bookings, payments):
    # Point 2: (Mostly) side-effect-free functions
    # Saving changes to external storage (e.g., database, file)
    # For simplicity, we'll just print the data here.
    print("Changes saved.")

# Functional Programming

users = []
playgrounds = []
bookings = []
payments = []

while True:

    if choice == '1':
        # Point 3: The use of higher-order functions
        # Functions (create_user) are passed around as first-class citizens
        users.append(create_user())
    elif choice == '2':
        # Point 4: Functions as parameters and return values
        # Function display_users takes users as a parameter
        display_users(users)
    elif choice == '3':
        # Point 3: The use of higher-order functions
        # Functions (create_playground) are passed around as first-class citizens
        playgrounds.append(create_playground())
    elif choice == '4':
        # Point 4: Functions as parameters and return values
        # Function display_playgrounds takes playgrounds as a parameter
        display_playgrounds(playgrounds)
    elif choice == '5':
