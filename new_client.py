"""from pyModbusTCP.client import ModbusClient
import time

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 1
    number_of_registers = 10

    while True:
        # Read the value of the first register
        regs = client.read_holding_registers(starting_address, number_of_registers)
        
        if regs:
            print(f"Register value at address {starting_address}: {regs[0]}")
        else:
            print(f"Failed to read register at address {starting_address}")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        time.sleep(2)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
"""from pymodbus.client.sync import ModbusTcpClient

# Create a Modbus TCP client with the server's IP address and port
client = ModbusTcpClient("localhost", port=5020)

# Specify the starting address (e.g., register 1)
starting_address = 1

# Read data from the server (e.g., 3 registers)
response = client.read_holding_registers(starting_address, count=3, unit=0)

# Process the response data (e.g., print it)
if response.isError():
    print(f"Error reading data: {response}")
else:
    data = response.registers
    print(f"Received data: {data}")

# Close the connection
client.close()
"""


"""from pyModbusTCP.client import ModbusClient
import time

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    # Adjust the starting address to 0 if the server uses 0-based addressing
    starting_address = 0
    number_of_registers = 10

    while True:
        # Read the value of the first register
        regs = client.read_holding_registers(starting_address, number_of_registers)
        
        if regs:
            print(f"Register value at address {starting_address}: {regs}")
        else:
            print(f"Failed to read register at address {starting_address}")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        time.sleep(2)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""


"""   	the code that is running correctly
from pyModbusTCP.client import ModbusClient
import time

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    number_of_registers = 20

    while True:
        # Read the values of the registers
        regs = client.read_holding_registers(starting_address, number_of_registers)
        
        if regs:
            # Print the values of the registers
            for i, val in enumerate(regs):
                print(f"Register value at address {i}: {val}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        time.sleep(2)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
"""
from pyModbusTCP.client import ModbusClient
import time

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers =5

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)
        
        if regs:
            # Print the values of all registers
            for i, val in enumerate(regs):
                print(f"Register value at address {starting_address + i}: {val}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        time.sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
#########################################DATABASE STORING VALUES########################################

"""from pyModbusTCP.client import ModbusClient
import time
import mysql.connector

# Create a MySQL connection
mysql_config = {
    'host': '192.78.10.146',    # MySQL host
    'user': 'thanush',    # MySQL username
    'password': 'thanush',    # MySQL password
    'database': 'modbus_data'    # MySQL database name
}

# Connect to MySQL
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS modbus_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    register_address INT,
                    value INT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )''')
conn.commit()

# Create an instance of the Modbus client
client = ModbusClient(host="192.168.1.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 20

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)
        
        if regs:
            # Print the values of all registers
            for i, val in enumerate(regs):
                print(f"Register value at address {starting_address + i}: {val}")

                # Insert data into MySQL database
                cursor.execute('''INSERT INTO modbus_data (register_address, value) VALUES (%s, %s)''', (starting_address + i, val))
                conn.commit()
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        time.sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close MySQL connection
    conn.close()
    # Close the connection to the Modbus server
    client.close()
"""

"""
from pyModbusTCP.client import ModbusClient
import time

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 5  # Update this to match the number of registers sent by the server

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)

        if regs:
            # Convert the received data to strings
            data_strings = [bytes(regs[i:i+2]).decode() for i in range(0, len(regs), 2)]
            #for i in range(1, len(regs), 2)]
            
            # Print the values of all registers
            for i, val in enumerate(data_strings):
                print(f"Data at register address {starting_address + i * 2}: {val}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        time.sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()


"""

"""
from pyModbusTCP.client import ModbusClient
import time

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 5

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)
        
        if regs:
            # Print the values of all registers
            print("Register values:")
            for i, val in enumerate(regs):
                print(f"Register address {starting_address + i}: {val}")

            # Convert register values to alphabets
            alphabets = "".join(chr(reg) for reg in regs)
            print(f"Received alphabets: {alphabets}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        time.sleep(2)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
"""
from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 5  # Number of registers from which to read data

    while True:
        for i in range(num_registers):
            # Read the value of each register individually
            reg = client.read_holding_registers(starting_address + i, 1)
            
            if reg:
                # Convert the ASCII value to character
                alphabet = chr(reg[0])
                print(f"Register {i}: {alphabet}")
            else:
                print(f"Failed to read register {i}")

        # Sleep for a short time to avoid flooding the server with requests
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()



"""

"""

from pyModbusTCP.client import ModbusClient
from time import sleep

try:
    # Create an instance of the Modbus client
    client = ModbusClient(host='192.78.10.146', port=502)

    # Connect to the Modbus server
    client.open()
    print("Connected to the server")

    # Define the starting address and calculate the total number of registers
    starting_address = 0
    num_registers_to_read = 0

    # Keep reading registers until a null character is found
    while True:
        # Read a block of 20 registers
        data = client.read_holding_registers(starting_address + num_registers_to_read, 20)

        # If data is not received or all null characters are received, break the loop
        if data is None or all(x == 0 for x in data):
            break

        # Count non-null characters received
        num_non_null = sum(1 for x in data if x != 0)

        # Accumulate the count of non-null characters
        num_registers_to_read += num_non_null

    # Read the accumulated data from the registers
    data = client.read_holding_registers(starting_address, num_registers_to_read)

    if data is None:
        print('Error reading registers')
    else:
        # Convert the received data to characters
        received_data = ''.join([chr(x) for x in data])

        # Split the received data into individual words
        words = received_data.split('\x00')

        # Display each word on a separate line
        for word in words:
            print(word)

    # Close the connection to the server
    client.close()

    # Wait for 5 seconds before re-displaying the words
    sleep(5)

except Exception as e:
    print('Error:', str(e))
"""
"""
from pyModbusTCP.client import ModbusClient

# Define the words list
words = ['thanush', 'advika', 'arko']

try:
    # Create an instance of the Modbus client
    client = ModbusClient(host='192.78.10.146', port=502)

    # Connect to the Modbus server
    client.open()
    print("Connected to the server")

    # Define the starting address for the holding registers
    starting_address = 0

    # Number of characters per word (adjust if words have varying lengths)
    num_characters_per_word = 6

    # Determine the total number of registers used based on word lengths
    num_registers = len(words) * num_characters_per_word

    # Read values from each register and print in desired format
    for register_index in range(num_registers):
        data = client.read_holding_registers(starting_address + register_index, 1)

        if data is None:
            print(f'Error reading register {register_index}')
        else:
            # Extract the character from the received data
            char = chr(data[0]) if data[0] != 0 else ' '  # Handle null characters gracefully

            # Calculate the word index based on register index
            word_index = int(register_index / num_characters_per_word)

            # Print the desired output format
            print(f"Value at register {register_index}; Word {word_index+1}: {char}")

    # Close the connection to the server
    client.close()

except Exception as e:
    print('Error:', str(e))
"""
"""
from pyModbusTCP.client import ModbusClient

# Define the words list (optional, for reference)
words = ['thanush', 'advika', 'arko']

try:
    # Create an instance of the Modbus client
    client = ModbusClient(host='192.78.10.146', port=502)

    # Connect to the Modbus server
    client.open()
    print("Connected to the server")

    # Define the starting address for the holding registers
    starting_address = 0

    # Number of characters per word (adjust if words have varying lengths)
    num_characters_per_word = 6

    # Determine the total number of registers used based on word lengths
    num_registers = len(words) * num_characters_per_word

    # Read and display each word
    for word_index in range(len(words)):
        # Calculate the starting register address for the current word
        start_register_address = starting_address + word_index * num_characters_per_word

        # Read all characters for the current word in one go
        data = client.read_holding_registers(start_register_address, num_characters_per_word)

        if data is None:
            print(f'Error reading registers for word {word_index+1}')
        else:
            # Convert data to characters and ignore null characters
            word = ''.join([chr(x) for x in data if x != 0])
            print(f"Value at register {start_register_address}; Word {word_index+1}: {word}")

    # Close the connection to the server
    client.close()

except Exception as e:
    print('Error:', str(e))
"""
"""
from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 5  # Number of registers from which to read data

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)

        if regs:
            # Decode the ASCII values into alphabets
            alphabets = ''.join(chr(reg) for reg in regs)
            print("Alphabets received from registers:", alphabets)
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
"""
from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

try:
    # Connect to the server
    client.open()
    print("Connected to the server")

    # Define the starting address and the number of registers to read
    starting_address = 0
    num_registers = 20  # Number of registers to read data from

    while True:
        # Read the values of all registers
        regs = client.read_holding_registers(starting_address, num_registers)

        if regs:
            # Print the values of each register
            for i, reg in enumerate(regs):
                print(f"Register {i}: {reg}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
################################   NUMERAL VALUES     ######################################3
"""
from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

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
            # Print the values of each register
            for i, reg in enumerate(regs):
                print(f"Data stored at register {i + 1}: {reg}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""

################################## Alpabets ####################################
"""
from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

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
            # Print the alphabets corresponding to each register value
            for i, reg in enumerate(regs):
                alphabet = chr(reg + ord('A') - 1) if 1 <= reg <= 26 else 'N/A'
                print(f"Data stored at register {i + 1}: {alphabet}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
#################################     HEX       ####################################
"""
from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

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
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(15)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""
###################################################OCTAL########################################################################3
"""

from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

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
            # Print the octal values of each register
            for i, reg in enumerate(regs):
                oct_value = oct(reg)
                print(f"Data stored at register {i + 1}: {oct_value}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""

################################################# BINARY####################################################

from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.105", port=502)

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
            # Print the binary values of each register
            for i, reg in enumerate(regs):
                bin_value = bin(reg)
                print(f"Data stored at register {i + 1}: {bin_value}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()

"""
from pyModbusTCP.client import ModbusClient
from time import sleep

# Create an instance of the Modbus client
client = ModbusClient(host="192.78.10.146", port=502)

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
            # Print the binary values of each register
            for i, reg in enumerate(regs):
                bin_value = "{0:b}".format(reg)  # Convert to binary without the '0b' prefix
                print(f"Data stored at register {i + 1}: {bin_value}")
        else:
            print("Failed to read registers")

        # Sleep for a short time to avoid flooding the server with requests
        print("---------------------------------------------------------------")
        sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the connection
    client.close()
"""

