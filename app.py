"""
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch data from SQLite database
def get_data():
    conn = sqlite3.connect('modbus_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * FROM modbus_data''')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
    finally:
        conn.close()

# Route to display data on HTML page
@app.route('/')
def display_data():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
"""
"""

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to fetch data from SQLite database
def get_data():
    conn = sqlite3.connect('modbus_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * FROM modbus_data''')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
    finally:
        conn.close()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the button click event
@app.route('/show-data', methods=['POST'])
def show_data():
    data = get_data()
    return render_template('display.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

"""
"""
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch data from SQLite database
def get_data():
    conn = sqlite3.connect('modbus_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * FROM modbus_data''')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
    finally:
        conn.close()

# Route to display data on HTML page
@app.route('/')
def display_data():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
"""




"""
from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Function to check server connection status
def check_connection():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('modbus_data.db')
        conn.close()
        return True
    except Exception as e:
        return False

# Route to check server connection status
@app.route('/check-connection')
def check_connection_route():
    if check_connection():
        return jsonify({'status': 'connected'})
    else:
        return jsonify({'status': 'not connected'})

# Function to fetch data from SQLite database
def get_data():
    conn = sqlite3.connect('modbus_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * FROM modbus_data''')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
    finally:
        conn.close()

# Route to display data on HTML page
@app.route('/')
def display_data():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
"""




from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Function to check server connection status
def check_connection():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('modbus_data.db')
        conn.close()
        return True
    except Exception as e:
        return False

# Route to check server connection status
@app.route('/check-connection')
def check_connection_route():
    if check_connection():
        return jsonify({'status': 'connected'})
    else:
        return jsonify({'status': 'not connected'})

# Function to fetch latest data from SQLite database
# Function to fetch the latest set of data from SQLite database in ascending order by ID
def get_data():
    conn = sqlite3.connect('modbus_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * FROM (SELECT * FROM modbus_data ORDER BY id DESC LIMIT 15) ORDER BY id ASC''')
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
    finally:
        conn.close()


# Route to display latest data on HTML page
@app.route('/')
def display_data():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)















#http://127.0.0.1:5000/
