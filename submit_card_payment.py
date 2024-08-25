from flask import request
import sqlite3

def submit_card_payment():
    card_number = request.form.get('cr_no')
    card_expiry = request.form.get('exp')
    cvv = request.form.get('cvcpwd')

    try:
        # Connect to the database
        conn = sqlite3.connect('C:/Users/User/Desktop/bitsh/hospital_online_appointment/payment.db')
        cursor = conn.cursor()

        # Insert payment details into the card_payments table
        cursor.execute("INSERT INTO card_payments (card_number, card_expiry, cvv) VALUES (?, ?, ?)",
                       (card_number, card_expiry, cvv))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        return "Card payment submitted successfully."
    except Exception as e:
        return "An error occurred while submitting card payment."
