def submit_bank_payment():
    bank_name = request.form.get('bank_name')
    beneficiary_name = request.form.get('beneficiary_name')
    swift_code = request.form.get('swift_code')

    try:
        conn = sqlite3.connect('path_to_your_database/payment.db')
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO bank_payments (bank_name, beneficiary_name, swift_code)
            VALUES (?, ?, ?)
        """

        cursor.execute(insert_query, (bank_name, beneficiary_name, swift_code))
        conn.commit()  # Commit changes
        conn.close()   # Close the connection

        return "Bank payment submitted successfully."
    except Exception as e:
        return f"An error occurred while submitting bank payment: {e}"
