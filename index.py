from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

import sqlite3

def create_database():
    conn = sqlite3.connect('C:/Users/User/Desktop/bitsh/hospital_online_appointment/hospital_appointment.db')
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        mobile_number NUMBER,
        email TEXT,
        appointment_date NUMBER,
        area TEXT,
        city TEXT,
        state TEXT,
        postal_code NUMBER
    )
    """

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

# Call the create_database function before running the app
create_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-appointment', methods=['POST'])
def submit_appointment():
    # Extract form data from the request
    full_name = request.form.get('full_name')
    mobile_number = request.form.get('mobile_number')
    email = request.form.get('email')
    appointment_date = request.form.get('appointment_date')
    area = request.form.get('area')
    city = request.form.get('city')
    state = request.form.get('state')
    postal_code = request.form.get('postal_code')

    # TODO: Use SQLite3 to store the data in the database
    conn = sqlite3.connect('C:/Users/User/Desktop/bitsh/hospital_online_appointment/hospital_appointment.db')
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO appointments (full_name, mobile_number, email, appointment_date, area, city, state, postal_code)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(insert_query, (full_name, mobile_number, email, appointment_date, area, city, state, postal_code))
    conn.commit()
    conn.close()

    return redirect(url_for('payment'))

@app.route('/payment')
def payment():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True)
