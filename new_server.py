"""from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

# Create an instance of the Modbus server
server = ModbusServer(host="192.78.10.146", port=502, no_block=True)

try:
    # Start the server
    server.start()
    print("Server is running...")
    
    # Define the starting address and the number of registers
    starting_address = 0
    number_of_registers = 10
    
    # Initialize the data bank with zeros
    DataBank.set_words(starting_address, [0] * number_of_registers)
    
    while True:
        # Here you can specify the data to be sent in decimal
        # For example, updating the first register with the value 123
        DataBank.set_words(starting_address, [123])
        
        # The server will handle read/write requests from clients automatically
        # You can add your logic here for handling data updates
        
        # Sleep for a short time to avoid high CPU usage
        sleep(0.1)

except Exception as e:
    print("Error: " + str(e))
    server.stop()
"""


"""from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Create a Modbus data block with some sample data
block = ModbusSequentialDataBlock(0, [1, 2, 3, 4, 5])

# Create a Modbus slave context with the data block
context = ModbusServerContext(slaves={0: block}, single=True)

# Start the Modbus TCP server
StartTcpServer(context, address=("localhost", 5020))
"""


"""from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

# Create an instance of the Modbus server
server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

try:
    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and the number of registers
    starting_address = 1  # Make sure this matches the client's starting address
    number_of_registers = 10

    # Initialize the data bank with zeros
    DataBank.set_words(starting_address, [0] * number_of_registers)

    while True:
        # Update the first register with the value 123
        DataBank.set_words(starting_address, [123])

        # The server will handle read/write requests from clients automatically
        # You can add your logic here for handling data updates

        # Sleep for a short time to avoid high CPU usage
        sleep(0.1)

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""

"""from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

# Create an instance of the Modbus server
server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

try:
    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and the number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    number_of_registers = 10

    # Initialize the data bank with zeros
    #server.data_bank.set_words(starting_address, [1] * number_of_registers)
    server.data_bank.set_holding_registers(starting_address, [1 for _ in range(number_of_registers)])

    while True:
        # Update the first register with the value 123
        for i in range(1, 5):
            server.data_bank.set_holding_registers(i, [123])

        # The server will handle read/write requests from clients automatically
        # You can add your logic here for handling data updates

        # Sleep for a short time to avoid high CPU usage
        sleep(0.1)

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""




""" the code that is actually running
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep
import random

# Create an instance of the Modbus server
server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

try:
    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and the number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    number_of_registers = 20

    while True:
        # Generate random values and store them in the data bank
        random_values = [random.randint(0, 100) for _ in range(number_of_registers)]
        server.data_bank.set_holding_registers(starting_address, random_values)

        # The server will handle read/write requests from clients automatically
        # You can add your logic here for handling data updates

        # Sleep for a short time to avoid high CPU usage
        sleep(0.1)

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""
"""
 ###################################DECIMAL##################################
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep
import random

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)     ########## 192.168.1.146    MODBUS ip

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    num_registers = 20  # Define the number of registers to store data in


        # Generate random data for each register
    data_registers = [random.randint(0, 100) for _ in range(num_registers)]

        # Set the data in different registers
    for i, data in enumerate(data_registers):
        server.data_bank.set_holding_registers(starting_address + i, [data])
    while True:

        # The server will handle read/write requests from clients automatically
        # You can add your logic here for handling data updates

        # Sleep for a short time to avoid high CPU usage
        sleep(5)

except Exception as e:
    print('Error:', str(e))
    server.stop()

"""

"""
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep
import random

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    num_registers = 20  # Define the number of registers to store data in

    while True:
        # Generate random hexadecimal data for each register
        data_registers = [hex(random.randint(0, 255))[2:].zfill(2) for _ in range(num_registers)]

        # Convert hexadecimal strings to integers
        data_registers = [int(data, 16) for data in data_registers]

        # Set the data in different registers
        for i, data in enumerate(data_registers):
            server.data_bank.set_holding_registers(starting_address + i, [data])

        # Sleep for a short time to avoid high CPU usage
        sleep(5)

except Exception as e:
    print('Error:', str(e))
    server.stop()

"""



"""
################################################# hex charecter################################

from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep
import random
import string

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    num_registers = 20  # Define the number of registers to store data in

    while True:
        # Generate random strings for each register
        data_registers = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(num_registers)]

        # Encode strings into bytes
        data_registers = [data.encode() for data in data_registers]

        # Set the data in different registers
        for i, data in enumerate(data_registers):
            server.data_bank.set_holding_registers(starting_address + i * 2, [int(byte) for byte in data])  # Convert bytes to list of integers

        # Sleep for a short time to avoid high CPU usage
        sleep(5)

except Exception as e:
    print('Error:', str(e))
    server.stop()

"""

"""
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep
import random
import string

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    num_registers = 20  # Define the number of registers to store data in

    # Define the alphabet characters
    alphabet = string.ascii_uppercase  # This will give you 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        # Generate random strings for each register containing only alphabetic characters
        data_registers = [''.join(random.choices(alphabet, k=10)) for _ in range(num_registers)]

        # Encode strings into bytes
        data_registers = [data.encode() for data in data_registers]

        # Set the data in different registers
        for i, data in enumerate(data_registers):
            server.data_bank.set_holding_registers(starting_address + i * 2, [int(byte) for byte in data])  # Convert bytes to list of integers

        # Sleep for a short time to avoid high CPU usage
        sleep(5)

except Exception as e:
    print('Error:', str(e))
    server.stop()
""" 
"""

from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    num_registers = 5  # Define the number of registers to store data in

    # Define the values (alphabets) you want to send
    alphabets = "ABCDEFGHIJk"

    while True:
        # Set the data in different registers
        for i, char in enumerate(alphabets):
            ascii_value = ord(char)  # Get the ASCII value of the character
            server.data_bank.set_holding_registers(starting_address + i * 2, [ascii_value])  # Set ASCII value in register

        # Sleep for a short time to avoid high CPU usage
        sleep(5)

except Exception as e:
    print('Error:', str(e))
    server.stop()

"""

from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)   ################192.168.1.146

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    num_registers = 15  # Define the number of registers to store data in

    # Define the values (alphabets) you want to send
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        # Set the data in different registers
        for i, char in enumerate(alphabets):
            register_value = ord(char) - ord('A') + 1  # Convert character to value 1-26
            server.data_bank.set_holding_registers(starting_address + i, [register_value])  # Set value in register

        # Sleep for a short time to avoid high CPU usage
        sleep(20)

except Exception as e:
    print('Error:', str(e))
    server.stop()

"""
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address and number of registers
    starting_address = 0  # Make sure this matches the client's starting address
    num_registers = 20  # Define the number of registers to store data in

    # Define the values (alphabets) you want to send
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        # Set the data in different registers
        for i, char in enumerate(alphabets):
            register_value = ord(char) - ord('A') + 1  # Convert character to value 1-26
            server.data_bank.set_holding_registers(starting_address + i, [register_value])  # Set value in register

        # Sleep for a short time to avoid high CPU usage
        sleep(5)

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""

















"""

from pyModbusTCP.server import DataBank, ModbusServer

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address for the holding registers
    starting_address = 0  # Make sure this matches the client's starting address

    # Specify the words to be stored in the holding registers
    data_registers_1 = ['Hello', 'World', 'Python', 'Modbus']  # Words for registers 0-3
    data_registers_2 = ['OpenAI', 'ChatGPT', 'Programming', 'Example']  # Words for registers 4-7

    # Flatten and convert the words into ASCII values
    data_registers_1_ascii = [ord(char) for word in data_registers_1 for char in word]
    data_registers_2_ascii = [ord(char) for word in data_registers_2 for char in word]

    # Set the data into specific registers
    server.data_bank.set_holding_registers(starting_address, data_registers_1_ascii)
    server.data_bank.set_holding_registers(starting_address + len(data_registers_1_ascii), data_registers_2_ascii)

    # The server will handle read/write requests from clients automatically
    # You can add your logic here for handling data updates

    # Keep the server running indefinitely
    while True:
        pass

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""

"""
from pyModbusTCP.server import DataBank, ModbusServer

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address for the holding registers
    starting_address = 0  # Make sure this matches the client's starting address

    # Define the words to be stored in the holding registers
    words = ['thanush', 'advika', 'arka', 'akhil']

    # Set the data into specific registers
    for i, word in enumerate(words):
        # Encode the word as ASCII values
        word_ascii = [ord(char) for char in word]
        # Set the data into the corresponding registers
        if i == 0:  # Store 'thanush' in register 1
            server.data_bank.set_holding_registers(starting_address + 1, word_ascii)
        else:
            server.data_bank.set_holding_registers(starting_address + i, word_ascii)

    # The server will handle read/write requests from clients automatically
    # You can add your logic here for handling data updates

    # Keep the server running indefinitely
    while True:
        pass

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""

"""

from pyModbusTCP.server import DataBank, ModbusServer

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address for the holding registers
    starting_address = 0

    # Define the words to be stored in the holding registers
    words = ['thanush', 'advika', 'arka', 'akhil']

    # Calculate the total number of registers needed
    num_registers = sum(len(word) for word in words)

    # Set the data into specific registers
    current_register = starting_address
    for word in words:
        # Encode the word as ASCII values
        word_ascii = [ord(char) for char in word]
        # Set the data into the corresponding registers
        server.data_bank.set_holding_registers(current_register, word_ascii)
        # Move to the next set of registers for the next word
        current_register += len(word)

    # Keep the server running indefinitely
    while True:
        pass

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""

"""
from pyModbusTCP.server import DataBank, ModbusServer

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address for the holding registers
    starting_address = 0

    # Define the words to be stored in the holding registers
    words = ['thanush', 'advika', 'arko']

    # Set the data into specific registers
    for i, word in enumerate(words):
        # Encode the word as ASCII values
        word_ascii = [ord(char) for char in word]
        # Set the data into the corresponding registers
        server.data_bank.set_holding_registers(starting_address + i * len(word), word_ascii)

    # Keep the server running indefinitely
    while True:
        pass

except Exception as e:
    print('Error:', str(e))
    server.stop()
"""
"""
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

def start_server(words):  # Function to start the server with words as argument
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address for the holding registers
    starting_address = 0

    # Set individual characters into specific registers
    for i, word in enumerate(words):
        register_address = starting_address + i * len(word)
        for char_index, char in enumerate(word):
            # Encode characters as ASCII values
            word_ascii = ord(char)
            # Set data into the corresponding register (one character per register)
            server.data_bank.set_holding_registers(register_address + char_index, [word_ascii])

    # Keep the server running indefinitely
    while True:
        pass

# Exception handling block is indented at the same level as the function body
#except Exception as e:
 #   print('Error:', str(e))
    server.stop()


# Define the words list outside the function
words = ['thanush', 'advika', 'arko']

# Start the server with the words list
start_server(words)
"""

"""
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

try:
    # Create an instance of the Modbus server
    server = ModbusServer(host='192.78.10.146', port=502, no_block=True)

    # Start the server
    server.start()
    print('Server is running...')

    # Define the starting address for the holding registers
    starting_address = 0  # Make sure this matches the client's starting address

    # Specify the alphabets to be stored in the holding registers
    data_registers_1 = ['A', 'B', 'C', 'D']  # Alphabets for registers 0-3
    data_registers_2 = ['E', 'F', 'G', 'H']  # Alphabets for registers 4-7

    # Set the data into specific registers
    server.data_bank.set_holding_registers(starting_address, [ord(char) for char in data_registers_1])
    server.data_bank.set_holding_registers(starting_address + len(data_registers_1), [ord(char) for char in data_registers_2])

    # The server will handle read/write requests from clients automatically
    # You can add your logic here for handling data updates

    # Sleep for a short time to avoid high CPU usage
    sleep(5)

except Exception as e:
    print('Error:', str(e))
    server.stop()

"""

