import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch data from SQLite database
def fetch_data():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('modbus_data.db')
        cursor = conn.cursor()

        # Execute a SELECT query to fetch the first 15 rows from the table
        cursor.execute('''SELECT * FROM modbus_data LIMIT 15''')
        data = cursor.fetchall()

        # Close the connection to the SQLite database
        conn.close()

        # Clear previous data in treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert fetched data into treeview
        for row in data:
            tree.insert("", "end", values=row)

    except Exception as e:
        print(f"Error: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Modbus Data Viewer")

# Create a frame to hold the treeview and scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create Treeview widget
tree = ttk.Treeview(frame, columns=("ID", "Register Number", "Register Value"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Register Number", text="Register Number")
tree.heading("Register Value", text="Register Value")

# Create a scrollbar for the treeview
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the treeview
tree.configure(yscrollcommand=scrollbar.set)
tree.pack(fill="both", expand=True)  # Pack the treeview within the frame

# Fetch data button
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

















"""
import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch data from SQLite database
def fetch_data():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('modbus_data.db')
        cursor = conn.cursor()

        # Execute a SELECT query to fetch the first 15 rows from the table
        cursor.execute('''SELECT * FROM modbus_data LIMIT 15''')
        data = cursor.fetchall()

        # Close the connection to the SQLite database
        conn.close()

        # Clear previous data in treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert fetched data into treeview
        for row in data:
            tree.insert("", "end", values=row)

    except Exception as e:
        print(f"Error: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Modbus Data Viewer")

# Create a frame to hold the treeview and scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create Treeview widget
tree = ttk.Treeview(frame, columns=("ID", "Register Number", "Register Value"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Register Number", text="Register Number")
tree.heading("Register Value", text="Register Value")

# Create a scrollbar for the treeview
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the treeview
tree.configure(yscrollcommand=scrollbar.set)
tree.pack(fill="both", expand=True)  # Pack the treeview within the frame

# Fetch data button
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()


"""







"""import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch data from SQLite database
def fetch_data():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('modbus_data.db')
        cursor = conn.cursor()

        # Execute a SELECT query to fetch all data from the table
        cursor.execute('''SELECT * FROM modbus_data''')
        data = cursor.fetchall()

        # Close the connection to the SQLite database
        conn.close()

        # Clear previous data in treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert fetched data into treeview
        for row in data:
            tree.insert("", "end", values=row)

    except Exception as e:
        print(f"Error: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Modbus Data Viewer")

# Create Treeview widget
tree = ttk.Treeview(root, columns=("ID", "Register Number", "Register Value"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Register Number", text="Register Number")
tree.heading("Register Value", text="Register Value")
tree.pack(fill="both", expand=True)

# Fetch data button
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
"""



"""
import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch data from SQLite database
def fetch_data():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('modbus_data.db')
        cursor = conn.cursor()

        # Execute a SELECT query to fetch all data from the table
        cursor.execute('''SELECT * FROM modbus_data''')
        data = cursor.fetchall()

        # Close the connection to the SQLite database
        conn.close()

        # Clear previous data in treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert fetched data into treeview
        for row in data:
            tree.insert("", "end", values=row)

    except Exception as e:
        print(f"Error: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Modbus Data Viewer")

# Create a frame to hold the treeview and scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create Treeview widget
tree = ttk.Treeview(frame, columns=("ID", "Register Number", "Register Value"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Register Number", text="Register Number")
tree.heading("Register Value", text="Register Value")

# Create a scrollbar for the treeview
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the treeview
tree.configure(yscrollcommand=scrollbar.set)
tree.pack(fill="both", expand=True)  # Pack the treeview within the frame

# Fetch data button
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

"""



