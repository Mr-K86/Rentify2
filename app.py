from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword@123",
    database="rentify2"
)

cursor =db.cursor()

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Register page (GET + POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        Full_Name = request.form['Full_Name']
        Email = request.form['Email']
        Password = request.form['Password']
        query = "INSERT INTO register (Full_Name, Email, Password) VALUES (%s, %s, %s)"
        values = (Full_Name, Email, Password)
        cursor.execute(query, values)
        db.commit()
        return "Registration successful!"
    return render_template("register.html")

#items page
@app.route('/items')
def items():
    return render_template('items.html')

#login page
@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['Email']
        password = request.form['Password']
        query = "SELECT * FROM register WHERE Email = %s AND Password = %s"
        values = (email, password)
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            return "Login successful!"
        else:
            return "Invalid email or password."
    return render_template('login.html')

#contact  us page
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)