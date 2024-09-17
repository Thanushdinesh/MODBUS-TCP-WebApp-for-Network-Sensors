import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('modbus_data.db')
cursor = conn.cursor()

try:
    # Execute a DELETE query to empty the table before storing new data
    cursor.execute('''DELETE FROM modbus_data''')
    conn.commit()
    print("Database emptied successfully.")


except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the SQLite database
    conn.close()
