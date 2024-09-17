import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('modbus_data.db')
cursor = conn.cursor()

# Create the modbus_data table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS modbus_data (
                    id INTEGER PRIMARY KEY,
                    register_number TEXT,
                    register_value INTEGER
                )''')

# Insert initial data if the table is empty
cursor.execute('''SELECT COUNT(*) FROM modbus_data''')
if cursor.fetchone()[0] == 0:
    initial_data = [
        ('Register1', 0),
        ('Register2', 0),
        ('Register3', 0),
        # Add more initial rows if needed
    ]
    cursor.executemany('''INSERT INTO modbus_data (register_number, register_value) VALUES (?, ?)''', initial_data)
    conn.commit()

try:
    # Display the fetched data
    cursor.execute('''SELECT * FROM modbus_data LIMIT 15''')
    data = cursor.fetchall()

    print("ID | Register Number | Register Value")
    print("---------------------------------")
    for row in data:
        print(f"{row[0]:<2} | {row[1]:<15} | {row[2]:<8}")

    # Assuming you have updated values here, let's simulate updating the register values
    updated_values = [(1, 100), (2, 200), (3, 300)]  # Example updated values

    for updated_row in updated_values:
        # Assuming 'updated_row' is a tuple with (id, register_value)
        # You should replace this part with actual logic to update the values in your database
        cursor.execute('''UPDATE modbus_data SET register_value = ? WHERE id = ?''', (updated_row[1], updated_row[0]))
        conn.commit()

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the SQLite database
    conn.close()



















"""import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('modbus_data.db')
cursor = conn.cursor()

try:

    # Execute a SELECT query to fetch all data from the table
    cursor.execute('''SELECT * FROM modbus_data''')
    data = cursor.fetchall()

    # Display the fetched data
    print("ID | Register Number | Register Value")
    print("---------------------------------")
    for row in data:
        print(f"{row[0]:<2} | {row[1]:<15} | {row[2]:<8}")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the SQLite database
    conn.close()


"""






"""# Execute a DELETE query to empty the table before storing new data
    cursor.execute('''DELETE FROM modbus_data''')
    conn.commit()
    print("Database emptied successfully.")"""





"""
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="192.78.10.113",
    user="user_123",
    password="user_123",
    database="modbus_database"
)
cursor = conn.cursor()

try:
    # Execute a SELECT query to fetch all data from the table
    cursor.execute('''SELECT * FROM modbus_data''')
    data = cursor.fetchall()

    # Display the fetched data
    print("ID | Register Number | Hex Value")
    print("---------------------------------")
    for row in data:
        print(f"{row[0]:<2} | {row[1]:<15} | {row[2]:<8}")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the MySQL database
    conn.close()
"""

"""

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('modbus_data.db')
cursor = conn.cursor()

try:
    # Execute a DELETE query to empty the table before storing new data
    cursor.execute('''DELETE FROM modbus_data''')
    conn.commit()
    print("Database emptied successfully.")

    # Define the values (alphabets) you want to send
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Set the data in different registers
    for i, char in enumerate(alphabets):
        hex_value = hex(ord(char) - ord('A') + 1)  # Convert character to hexadecimal value 1-26
        cursor.execute('''INSERT INTO modbus_data (register_number, hex_value)
                          VALUES (?, ?)''', (i + 1, hex_value))
        conn.commit()

    print("Data stored successfully.")

    # Fetch and display the updated data from the database
    cursor.execute('''SELECT * FROM modbus_data''')
    updated_data = cursor.fetchall()

    # Display the fetched updated data
    print("Updated Data:")
    print("ID | Register Number | Hex Value")
    print("---------------------------------")
    for row in updated_data:
        print(f"{row[0]:<2} | {row[1]:<15} | {row[2]:<8}")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the SQLite database
    conn.close()
"""
