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
        
        # Prompt user to select facilities
        selected_facilities = input("Enter the facilities (separated by commas) for this room: ").split(',')
        for facility in selected_facilities:
            # Get the facility ID for the selected facility name
            cursor.execute("SELECT ID FROM facilityInfo WHERE name = ?", (facility.strip(),))
            facility_id = cursor.fetchone()[0]
            # Insert room and facility ID into roomFacilities table
            cursor.execute("""
            INSERT INTO roomFacilities (roomID, facilityID)
            VALUES (?, ?)
            """, (room_id, facility_id))
        
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
        
# Function to display all bookings with customer details and facilities
def show_bookings():
    connection = db.connect("bookings.db")
    cursor = connection.cursor()
    try:
        # Perform a JOIN operation between bookingInfo, customerInfo, roomInfo, and roomFacilities tables
        cursor.execute("""
        SELECT bookingInfo.ID, customerInfo.FirstName, customerInfo.Surname, customerInfo.PostCode, 
        customerInfo.phoneNumber, bookingInfo.RoomNo, roomInfo.refnumber, roomInfo.capacity, roomInfo.price,
        bookingInfo.BookingDate, bookingInfo.Requests, GROUP_CONCAT(facilityInfo.name)
        FROM bookingInfo
        JOIN customerInfo ON bookingInfo.CustDetails = customerInfo.ID
        JOIN roomInfo ON bookingInfo.RoomNo = roomInfo.ID
        LEFT JOIN roomFacilities ON roomFacilities.roomID = roomInfo.ID
        LEFT JOIN facilityInfo ON roomFacilities.facilityID = facilityInfo.ID
        GROUP BY bookingInfo.ID
        """)
        bookings = cursor.fetchall()
        for booking in bookings:
            print("Booking ID:", booking[0])
            print("Customer Name:", f"{booking[1]} {booking[2]}")
            print("Customer Postcode:", booking[3])
            print("Customer Phone Number:", booking[4])
            print("Room Number:", booking[5])
            print("Room Reference Number:", booking[6])
            print("Room Capacity:", booking[7])
            print("Room Price:", booking[8])
            print("Booking Date:", booking[9])
            print("Special Requests:", booking[10])
            print("Facilities:", booking[11])
            print("-----------------------------")
    except db.Error as e:
        print("Error occurred:", e)
    finally:
        connection.close()

if __name__ == "__main__":
    # Test the show_bookings function
    show_bookings()