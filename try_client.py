
from pyModbusTCP.client import ModbusClient
from time import sleep
import sqlite3

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.105", port=502)

# Create a connection to the SQLite database
conn = sqlite3.connect('modbus_data.db')
cursor = conn.cursor()

# Create a table to store the data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS modbus_data (
                    id INTEGER PRIMARY KEY,
                    register_number INTEGER,
                    hex_value TEXT
                 )''')
conn.commit()

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 15  # Number of registers to read data from

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)

        if regs:
            # Print the hexadecimal values of each register
            for i, reg in enumerate(regs):
                hex_value = hex(reg)
                print(f"Data stored at register {i + 1}: {hex_value}")

                # Save the data to the SQLite database
                cursor.execute('''INSERT INTO modbus_data (register_number, hex_value)
                                  VALUES (?, ?)''', (i + 1, hex_value))
                conn.commit()
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(20)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the SQLite database
    conn.close()

    # Close the connection to the server
    client.close()


"""

from pyModbusTCP.client import ModbusClient
from time import sleep
import mysql.connector

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.113", port=502)

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="192.78.10.113",
    user="user_123",
    password="user_123",
    database="modbus_database"
)
cursor = conn.cursor()

# Create a table to store the data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS modbus_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    register_number INT,
                    hex_value VARCHAR(255)
                 )''')
conn.commit()

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 5  # Number of registers to read data from

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)

        if regs:
            # Print the hexadecimal values of each register
            for i, reg in enumerate(regs):
                hex_value = hex(reg)
                print(f"Data stored at register {i + 1}: {hex_value}")

                # Save the data to the MySQL database
                cursor.execute('''INSERT INTO modbus_data (register_number, hex_value)
                                  VALUES (%s, %s)''', (i + 1, hex_value))
                conn.commit()
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(15)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the MySQL database
    conn.close()

    # Close the connection to the server
    client.close()




from pyModbusTCP.client import ModbusClient
from time import sleep
import mysql.connector

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.113", port=502)

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="192.78.10.113",
    user="user_123",
    password="user_123",
    database="modbus_database"
)
cursor = conn.cursor()

# Create a table to store the data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS modbus_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    register_number INT,
                    hex_value VARCHAR(255)
                 )''')
conn.commit()

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 5  # Number of registers to read data from

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)

        if regs:
            # Print the hexadecimal values of each register
            for i, reg in enumerate(regs):
                hex_value = hex(reg)
                print(f"Data stored at register {i + 1}: {hex_value}")

                # Save the data to the MySQL database
                cursor.execute('''INSERT INTO modbus_data (register_number, hex_value)
                                  VALUES (%s, %s)''', (i + 1, hex_value))
                conn.commit()
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(15)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection to the MySQL database
    conn.close()

    # Close the connection to the server
    client.close()

"""
