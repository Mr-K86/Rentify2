from flask import Flask, redirect, render_template, request, session, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret key'


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

        return redirect(url_for('login'))   # ✅ sirf POST ke baad

    return render_template("register.html")   # ✅ GET ke liye

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
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return "Invalid email or password."

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('login'))

#contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)