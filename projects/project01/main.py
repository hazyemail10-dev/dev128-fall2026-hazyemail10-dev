# Starting file for Project 1
# Irwin Li, 11/8/2026, DEV128

import sqlite3

# Connect to the persistent personnel database
registry_connection = sqlite3.connect("users.db")
registry_cursor = registry_connection.cursor()


# Create the personnel table without removing existing records
registry_cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        street_address TEXT,
        city TEXT,
        state TEXT,
        zipcode TEXT
    )
""")


# Initial fictional personnel records
initial_personnel = [
    ("Gregor", "Eisenhorn", "gregor@inquisition.example",
     "202-555-0101", "101 Imperial Avenue", "Seattle", "WA", "98101"),

    ("Gideon", "Ravenor", "gideon@inquisition.example",
     "202-555-0102", "202 Throne Street", "Bellevue", "WA", "98004"),

    ("Midas", "Betancore", "midas@inquisition.example",
     "202-555-0103", "303 Aquila Road", "Tacoma", "WA", "98402"),

    ("Alizebeth", "Bequin", "alizebeth@inquisition.example",
     "202-555-0104", "404 Ordo Avenue", "Redmond", "WA", "98052"),

    ("Godwyn", "Fischig", "godwyn@inquisition.example",
     "202-555-0105", "505 Sector Boulevard", "Everett", "WA", "98201")
]


# Check whether the registry already contains personnel
registry_cursor.execute("SELECT COUNT(*) FROM user")
existing_personnel_count = registry_cursor.fetchone()[0]


# Insert the initial records only when the database is empty
if existing_personnel_count == 0:
    registry_cursor.executemany("""
        INSERT INTO user (
            first_name,
            last_name,
            email,
            phone,
            street_address,
            city,
            state,
            zipcode
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, initial_personnel)

    registry_connection.commit()
    print("Initial personnel records successfully registered!")

else:
    print("Existing personnel registry detected. Records preserved.")


# Report 1: Display all personnel names
def display_personnel_directory():
    print("\n" + "=" * 55)
    print("IMPERIAL INQUISITION | PERSONNEL DIRECTORY")
    print("=" * 55)

    registry_cursor.execute("""
        SELECT first_name, last_name
        FROM user
        ORDER BY last_name, first_name
    """)

    personnel_records = registry_cursor.fetchall()

    for registry_number, (first_name, last_name) in enumerate(
        personnel_records, start=1
    ):
        print(f"{registry_number:02d}. {first_name} {last_name}")

    print("-" * 55)
    print(f"Total registered personnel: {len(personnel_records)}")


# Report 2: Display personnel contact information
def display_contact_directory():
    print("\n" + "=" * 65)
    print("IMPERIAL INQUISITION | CONTACT DIRECTORY")
    print("=" * 65)

    registry_cursor.execute("""
        SELECT first_name, last_name, email, phone
        FROM user
        ORDER BY last_name, first_name
    """)

    contact_records = registry_cursor.fetchall()

    for first_name, last_name, email, phone in contact_records:
        print(f"\nPersonnel: {first_name} {last_name}")
        print(f"Email:     {email}")
        print(f"Phone:     {phone}")
        print("-" * 65)

    print(f"Total contacts: {len(contact_records)}")

# Register a new member of the Imperial Inquisition
def register_new_personnel():
    print("\n" + "=" * 55)
    print("IMPERIAL INQUISITION | PERSONNEL REGISTRATION")
    print("=" * 55)

    # Collect the eight required personnel details
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    email = input("Email address: ").strip()
    phone = input("Phone number: ").strip()
    street_address = input("Street address: ").strip()
    city = input("City: ").strip()
    state = input("State: ").strip()
    zipcode = input("Zipcode: ").strip()

    # Group the information into one database record
    new_personnel_record = (
        first_name,
        last_name,
        email,
        phone,
        street_address,
        city,
        state,
        zipcode
    )

    # Insert the new record using parameterized SQL
    registry_cursor.execute("""
        INSERT INTO user (
            first_name,
            last_name,
            email,
            phone,
            street_address,
            city,
            state,
            zipcode
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, new_personnel_record)

    # Save the new record permanently
    registry_connection.commit()

    print("\n" + "-" * 55)
    print(f"Personnel registered successfully: {first_name} {last_name}")
    print("Registry database updated.")
    print("-" * 55)

# Display the available registry operations
def display_registry_menu():
    print("\n" + "=" * 55)
    print("       IMPERIAL INQUISITION PERSONNEL REGISTRY")
    print("=" * 55)
    print("1. View Personnel Directory")
    print("2. View Contact Directory")
    print("3. Register New Personnel")
    print("4. Exit Registry")
    print("=" * 55)


# Run the registry interface until the user chooses to exit
def run_registry_interface():
    while True:
        display_registry_menu()

        menu_selection = input("Select an option (1-4): ").strip()

        if menu_selection == "1":
            display_personnel_directory()

        elif menu_selection == "2":
            display_contact_directory()

        elif menu_selection == "3":
            register_new_personnel()

        elif menu_selection == "4":
            print("\nRegistry session terminated. The Emperor protects.")
            break

        else:
            print("\nInvalid selection. Please choose an option from 1 to 4.")


# Start the interactive application
run_registry_interface()

# Close the database connection after exiting
registry_connection.close()