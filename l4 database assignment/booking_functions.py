import sqlite3 as db

# Function to add a booking
def new_booking(customer_id, room_id, booking_date, requests=None):
    connection = db.connect("bookings.db")
    cursor = connection.cursor()
    try:
        if requests is None:
            requests = ""
        # Extract customer details from the combined customer_id string
        first_name, surname, postcode, phone_number = customer_id.split()
        # Insert customer details into customerInfo table
        cursor.execute("""
        INSERT INTO customerInfo (FirstName, Surname, PostCode, phoneNumber)
        VALUES (?, ?, ?, ?)
        """, (first_name, surname, postcode, phone_number))
        # Get the ID of the newly inserted customer
        customer_id = cursor.lastrowid
        # Insert booking details into bookingInfo table
        cursor.execute("""
        INSERT INTO bookingInfo (CustDetails, RoomNo, BookingDate, Requests)
        VALUES (?, ?, ?, ?)
        """, (customer_id, room_id, booking_date, requests))
        connection.commit()
        print("Booking added successfully")
    except db.Error as e:
        print("Error occurred:", e)
    finally:
        connection.close()

# Function to remove the booking by the ID
def remove_old_booking(booking_id):
    connection = db.connect("bookings.db")
    cursor = connection.cursor()
    try:
        cursor.execute("""
        DELETE FROM bookingInfo
        WHERE ID = ?
        """, (booking_id,))
        connection.commit()  # Commit the changes
        print("Booking removed successfully.")
    except db.Error as e:
        print("Error occurred:", e)
    finally: 
        connection.close()

# Function to update the bookings
def update_booking(booking_id, new_date):
    connection = db.connect("bookings.db")
    cursor = connection.cursor()
    try:
        cursor.execute("""
        UPDATE bookingInfo
        SET BookingDate = ?
        WHERE ID = ?
        """, (new_date, booking_id))
        connection.commit()  # Commit the changes
        print("Booking Details Updated")
    except db.Error as e:
        print("Error occurred:", e)
    finally: 
        connection.close()
# Function to display all bookings with customer details
def show_bookings():
    connection = db.connect("bookings.db")
    cursor = connection.cursor()
    try:
        # Perform a JOIN operation between bookingInfo and customerInfo tables
        cursor.execute("""
        SELECT bookingInfo.ID, customerInfo.FirstName, customerInfo.Surname, customerInfo.PostCode, 
        customerInfo.phoneNumber, bookingInfo.RoomNo, bookingInfo.BookingDate, bookingInfo.Requests
        FROM bookingInfo
        JOIN customerInfo ON bookingInfo.CustDetails = customerInfo.ID
        """)
        bookings = cursor.fetchall()
        for booking in bookings:
            print("Booking ID:", booking[0])
            print("Customer Name:", f"{booking[1]} {booking[2]}")
            print("Customer Postcode:", booking[3])
            print("Customer Phone Number:", booking[4])
            print("Room Number:", booking[5])
            print("Booking Date:", booking[6])
            print("Special Requests:", booking[7])
            print("-----------------------------")
    except db.Error as e:
        print("Error occurred:", e)
    finally:
        connection.close()