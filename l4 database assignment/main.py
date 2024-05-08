import sqlite3 as db

def main():
    connection = db.connect("bookings.db")
    cursor = connection.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS customerInfo
    """)
    cursor.execute("""
    DROP TABLE IF EXISTS roomInfo
    """)
    cursor.execute("""
    DROP TABLE IF EXISTS bookingInfo
    """)
    cursor.execute("""
    DROP TABLE IF EXISTS facilityInfo
    """)
    cursor.execute("""
    DROP TABLE IF EXISTS roomFacilities
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS facilityInfo(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roomInfo (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        capacity INTEGER NOT NULL
        
    );
    """)

    cursor.execute("""
    CREATE TABLE roomFacilities (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        roomID INTEGER,
        facilityID INTEGER,
        
        FOREIGN KEY (roomID) REFERENCES roomInfo(ID),
        FOREIGN KEY (facilityID) REFERENCES facilityInfo(ID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customerInfo(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        Surname TEXT,
        PostCode TEXT,
        phoneNumber NUMERIC
    );

    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookingInfo (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustDetails TEXT,
        RoomNo INTEGER,
        BookingDate NUMERIC,
        Requests TEXT,
        FOREIGN KEY ("CustDetails") REFERENCES customerInfo("ID"),
        FOREIGN KEY ("RoomNo") REFERENCES roomInfo("ID")
    );
    """)

    cursor.execute("""
    INSERT INTO facilityInfo (name) VALUES
    ('Screens'),
    ('Tables'),
    ('Chairs'),
    ('Kettle'),
    ('Mini Fridge'),
    ('Air Conditioning'),
    ('OnSuite Bathroom'),
    ('Single Beds'),
    ('Double Beds'),
    ('Queen Size Bed'),
    ('King Size Bed');
    """)

    cursor.execute("""
    INSERT INTO customerInfo (FirstName,Surname,PostCode,phoneNumber)
    VALUES('Bob', 'Jones', 'M7 0BZ', 447757493683),
    ('James', 'Garner', 'M9 9QF', 447951923584)
    """)

    cursor.execute("""
    INSERT INTO roomInfo (capacity) VALUES
    (4),
    (6);
    """)
    connection.commit()
    connection.close()
    
if __name__ == "__main__":
    main()

    # Close the database connection
    
