from flask import Flask, render_template, url_for, request, flash, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/contact_form', methods=['GET', 'POST'])
def user_query():
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['email']
        message = request.form['message']

        form_data = [name, mail, message]

        insert_data_query = """
        INSERT INTO form_record VALUES (?, ?, ?)
        """

        conn = sqlite3.connect("form.db")
        cur = conn.cursor()
        cur.execute(insert_data_query, form_data)
        conn.commit()
        cur.close()
        conn.close()

        flash(f"Hi {name}, your message has been received successfully.", "success")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
