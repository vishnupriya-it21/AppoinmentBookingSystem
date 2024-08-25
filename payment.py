from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from submit_bank_payment import submit_bank_payment  # Import the function
from submit_card_payment import submit_card_payment  # Import the function



app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('payment.db', check_same_thread=False)
cursor = conn.cursor()

# Create necessary tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS card_payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_number NUMBER,
        card_expiry NUMBER,
        cvv NUMBER
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bank_payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bank_name TEXT ,
        beneficiary_name TEXT ,
        swift_code TEXT 
    );
''')

conn.commit()

@app.route('/')
def payment_page():
    return render_template('payment.html')

@app.route('/submit_bank_payment', methods=['GET','POST'])
def submit_bank_payment():
    bank_name = request.form.get('bk_nm')
    beneficiary_name = request.form.get('ben_nm')
    swift_code = request.form.get('scode')

    # TODO: Store payment details in the database or perform payment processing
    conn = sqlite3.connect('C:/Users/User/Desktop/bitsh/hospital_online_appointment/payment.db')
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO bank_payments (bank_name, beneficiary_name ,swift_code)
    VALUES (?, ?, ?)
    """

    cursor.execute(insert_query, (bank_name, beneficiary_name ,swift_code))
    conn.commit()
    conn.close()

    return "Bank payment submitted successfully."

@app.route('/submit_card_payment', methods=['GET','POST'])
def submit_card_payment():
    card_number = request.form.get('cr_no')
    card_expiry = request.form.get('exp')
    cvv = request.form.get('cvcpwd')

    # TODO: Store payment details in the database or perform payment processing
    conn = sqlite3.connect('C:/Users/User/Desktop/bitsh/hospital_online_appointment/payment.db')
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO card_payments (card_number, card_expiry ,cvv)
    VALUES (?, ?, ?)
    """

    cursor.execute(insert_query, (card_number, card_expiry ,cvv))
    conn.commit()
    conn.close()

    return "Card payment submitted successfully."

def store_data():
    card_number = request.args.get('card_number')
    card_expiry = request.args.get('card_expiry')
    cvv = request.args.get('cvcpwd')

    print("Received card_number:", card_number)
    print("Received card_expiry:", card_expiry)
    print("Received cvv:", cvv)

    try:
        # Insert payment details into the card_payments table
        cursor.execute("INSERT INTO card_payments (card_number, card_expiry, cvv) VALUES (?, ?, ?)",
                       (card_number, card_expiry, cvv))
        
        # Commit changes and close the connection
        conn.commit()
        return "Card payment submitted successfully."
    except Exception as e:
        return f"An error occurred while submitting card payment: {e}"

if __name__ == '__main__':
    app.run(debug=True)