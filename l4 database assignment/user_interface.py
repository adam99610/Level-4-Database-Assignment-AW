from booking_functions import new_booking, remove_old_booking, update_booking, show_bookings

def main():

    bookings = [
        {"CustDetails": "John Doe", "RoomNo": 1, "BookingDate": "2024-05-10", "Requests": "Near elevator"},
        {"CustDetails": "Jane Smith", "RoomNo": 2, "BookingDate": "2024-05-12", "Requests": "Quiet room"},
    ]

    while True:
        print("\nOptions:")
        print("1. Add new booking")
        print("2. update existing booking")
        print("3. remove a booking")
        print("4. show all bookings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Adding a new booking...")
            first_name = input("Enter Customer's first name: ")
            surname = input("Enter Customer's surname: ")
            postcode = input("Enter the Custokmer's postcode: ")
            phone_number = input("Ener the Customers phone number: ")
            room_id = input("Enter room number: ")
            booking_date = input("Enter a booking date (YYYY-MM-DD): ")
            requests = input("Enter any Special requests: ")

            customer_details = f"{first_name} {surname} {postcode}{phone_number}"

            new_booking(customer_details, room_id, booking_date, requests)
        
        elif choice == "2":
            print("Updating a booking...")
            booking_id = int(input("Enter booking ID to update: "))
            new_date = input("Enter a new booking date (YYY-MM-DD): ")
            update_booking(booking_id, new_date)

        elif choice == "3":
            print("Removing a booking: ")
            booking_id = int(input("Enter a booking ID to remove: "))
            remove_old_booking(booking_id)

        elif choice == "4":
            print("Showing all Bookings...")
            show_bookings()

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again. ")

        

if __name__ == "__main__":
    main()