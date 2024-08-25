import sqlite3
from datetime import datetime

@app.route('/submit-appointment', methods=['POST'])
def submit_appointment():
    # Extract form data ...
     appointment_date = request.form.get('appointment_date')
    appointment_date = datetime.strptime(appointment_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    # Establish a connection to the database
    conn = sqlite3.connect('hospital_appointment.db')
    cursor = conn.cursor()

    # Insert data into the database (example query, adjust based on your schema)
    insert_query = "INSERT INTO patients (full_name, mobile_number) VALUES (?, ?)"
    cursor.execute(insert_query, (full_name, mobile_number))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return "Appointmefrom flask import Flask, render_template, request
from submit_appointment import insert_appointment_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-appointment', methods=['POST'])
def submit_appointment():
    full_name = request.form.get('full_name')
    mobile_number = request.form.get('mobile_number')

    insert_appointment_data(full_name, mobile_number)

    return "Appointment submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)
