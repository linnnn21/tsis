import psycopg2
import csv

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="phonebook_db",        # name of your database
    user="postgres",              # PostgreSQL default user
    password="meouwqq21",
    host="localhost",             # server address
    port="5432"                   # default PostgreSQL port
)
cur = conn.cursor()

# Create the PhoneBook table if it doesn't exist
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()

# Insert records from a CSV file (e.g. data.csv)
def insert_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data inserted from CSV file.")

# Insert a single record from user input
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Entry added successfully.")

# Update existing record
def update_data():
    old_name = input("Enter the name of the contact to update: ")
    new_name = input("Enter new name (press Enter to skip): ")
    new_phone = input("Enter new phone number (press Enter to skip): ")

    if new_name:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, new_name or old_name))
    conn.commit()
    print("Entry updated.")

# Search and display records
def query_data():
    keyword = input("Enter name to search (or press Enter to show all): ")
    if keyword:
        cur.execute("SELECT * FROM PhoneBook WHERE name ILIKE %s", ('%' + keyword + '%',))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    results = cur.fetchall()
    for row in results:
        print(row)

# Delete record by name or phone number
def delete_data():
    value = input("Enter name or phone number to delete: ")
    cur.execute("DELETE FROM PhoneBook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    print("Entry deleted.")

# Main program menu
def menu():
    create_table()
    while True:
        print("""
========= PHONEBOOK MENU =========
1. Upload from CSV file
2. Insert entry manually
3. Update existing entry
4. Search entries
5. Delete entry
6. Exit
""")
        choice = input("Select an option (1–6): ")

        if choice == "1":
            insert_from_csv("data.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

    # Close cursor and connection
    cur.close()
    conn.close()
    print("Program exited.")

# Run the menu if this file is executed directly
if __name__ == "__main__":
    menu()
