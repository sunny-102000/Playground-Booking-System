import pandas as pd
import datetime

class User:
    def __init__(self, name, mobile_number, user_id, email):
        self.name = name
        self.mobile_number = str(mobile_number)
        self.user_id = str(user_id)
        self.email = str(email)

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Mobile: {self.mobile_number}, Email: {self.email}"

class PlayGround:
    def __init__(self, specific_ground, location, playground_id, price_ground):
        self.specific_ground = specific_ground
        self.location = location
        self.playground_id = str(playground_id)
        self.price_ground = int(price_ground)

    def __str__(self):
        return f"Playground ID: {self.playground_id}, Specific Ground: {self.specific_ground}, Location: {self.location}, Price: ${self.price_ground}"

class Booking:
    def __init__(self, user_id, playground_id):
        self.user_id = int(user_id)
        self.playground_id = int(playground_id)
        self.confirm_status = "Pending"  # Initial status is set to "Pending"

    def confirm_booking(self):
        # Logic to confirm the booking
        self.confirm_status = "Confirmed"
        return f"Booking confirmed for User ID {self.user_id} on Playground ID {self.playground_id}"

    def __str__(self):
        return f"User ID: {self.user_id}, Playground ID: {self.playground_id}, Confirmation Status: {self.confirm_status}"

class Payment:
    def __init__(self, payment_id, price, payment_type, payment_date):
        self.payment_id = int(payment_id)
        self.price = int(price)
        self.payment_type = str(payment_type)
        self.payment_date = str(payment_date)

    def __str__(self):
        return f"Payment ID: {self.payment_id}, Price: ${self.price}, Payment Type: {self.payment_type}, Payment Date: {self.payment_date}"

class PlaygroundBookingSystem:
    def __init__(self, excel_file="bookings.xlsx"):
        self.excel_file = excel_file
        self.users = {}
        self.playgrounds = {}
        self.bookings = []
        self.payments = []

        # Create Excel file with headers
        data = {'User ID': [], 'Name': [], 'Mobile Number': [], 'Email': [],
                'Playground ID': [], 'Specific Ground': [], 'Location': [], 'Price': [],
                'Confirmation Status': [],
                'Payment ID': [], 'Payment Type': [], 'Payment Date': []}

        self.df = pd.DataFrame(data)
        self.df.to_excel(self.excel_file, index=False)

    def create_user(self):
        name = input("Enter user name: ")
        mobile_number = input("Enter mobile number: ")
        user_id = input("Enter user ID: ")
        email = input("Enter email: ")

        user = User(name, mobile_number, user_id, email)
        self.users[user.user_id] = user
        return user

    def display_users(self):
        print("Users:")
        for user in self.users.values():
            print(user)

    def create_playground(self):
        specific_ground = input("Enter specific ground (e.g., cricket, badminton): ")
        location = input("Enter location: ")
        playground_id = input("Enter playground ID: ")
        price_ground = input("Enter price for the ground: ")

        playground = PlayGround(specific_ground, location, playground_id, price_ground)
        self.playgrounds[playground.playground_id] = playground
        return playground

    def display_playgrounds(self):
        print("Playgrounds:")
        for playground in self.playgrounds.values():
            print(playground)

    def make_booking(self, user, playground):
        booking = Booking(user.user_id, playground.playground_id)
        self.bookings.append(booking)
        return booking

    def display_bookings(self):
        print("Bookings:")
        for booking in self.bookings:
            print(booking)

    def make_payment(self, booking):
        payment_id = len(self.payments) + 1
        price = self.playgrounds[booking.playground_id].price_ground
        payment_type = input("Enter payment type (cash/card): ")
        payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        payment = Payment(payment_id, price, payment_type, payment_date)
        self.payments.append(payment)
        return payment

    def display_payments(self):
        print("Payments:")
        for payment in self.payments:
            print(payment)

    def save_changes(self):
        # Append data to Excel file
        data = {'User ID': [], 'Name': [], 'Mobile Number': [], 'Email': [],
                'Playground ID': [], 'Specific Ground': [], 'Location': [], 'Price': [],
                'Confirmation Status': [],
                'Payment ID': [], 'Payment Type': [], 'Payment Date': []}

        for user in self.users.values():
            data['User ID'].append(user.user_id)
            data['Name'].append(user.name)
            data['Mobile Number'].append(user.mobile_number)
            data['Email'].append(user.email)

        for playground in self.playgrounds.values():
            data['Playground ID'].append(playground.playground_id)
            data['Specific Ground'].append(playground.specific_ground)
            data['Location'].append(playground.location)
            data['Price'].append(playground.price_ground)

        for booking in self.bookings:
            data['Confirmation Status'].append(booking.confirm_status)

        for payment in self.payments:
            data['Payment ID'].append(payment.payment_id)
            data['Payment Type'].append(payment.payment_type)
            data['Payment Date'].append(payment.payment_date)

        df_new = pd.DataFrame(data)
        df_concatenated = pd.concat([self.df, df_new], axis=1)

        with pd.ExcelWriter(self.excel_file, engine='xlsxwriter') as writer:
            df_concatenated.to_excel(writer, index=False)

        print("Changes saved to the Excel file.")

