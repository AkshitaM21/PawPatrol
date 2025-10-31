from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector
import os

app = Flask(__name__)

# Change working directory
os.chdir(r"C:\Users\PRAVEEN\OneDrive\Desktop\masti")

# ✅ Database Configuration (MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Mary892wait%4010@localhost/petcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ✅ Optional direct mysql.connector connection (for debugging or custom SQL)
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mary892wait@10",
        database="petcare"
    )
    mycursor = mydb.cursor()
    print("✅ Connected to MySQL (direct) successfully!")
except mysql.connector.Error as e:
    mydb = None
    mycursor = None
    print("❌ MySQL direct connection failed:", e)

# ✅ Ensure MySQL direct connection is closed on app teardown
@app.teardown_appcontext
def close_mysql_connection(exception=None):
    try:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
    except Exception:
        pass

# ✅ Appointment model (SQLAlchemy ORM)
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(50))
    pet_type = db.Column(db.String(50))
    pet_name = db.Column(db.String(100))
    pet_age = db.Column(db.String(20))
    pet_breed = db.Column(db.String(100))
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ✅ Create tables (if they don’t already exist)
with app.app_context():
    db.create_all()

BOOKING_SCRIPT = ""  # optional script injection

# ✅ Serve appointment page
@app.route('/appointment', methods=['GET'])
def appointment_page():
    appointments = Appointment.query.order_by(Appointment.id.desc()).all()
    return render_template('appointment.html', appointments=appointments, booking_script=BOOKING_SCRIPT)

# ✅ Root route redirects to appointment page
@app.route('/', methods=['GET'])
def root():
    return redirect(url_for('appointment_page'))

# ✅ Handle form submission (POST request)
@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    data = request.form
    new_app = Appointment(
        service=data.get('service'),
        pet_type=data.get('pet_type'),
        pet_name=data.get('pet_name'),
        pet_age=data.get('pet_age'),
        pet_breed=data.get('pet_breed'),
        date=data.get('date') or data.get('selected_date') or '',
        time=data.get('time') or data.get('selected_time') or '',
        full_name=data.get('full_name') or data.get('name'),
        email=data.get('email'),
        phone=data.get('phone'),
        notes=data.get('notes'),
    )
    db.session.add(new_app)
    db.session.commit()
    return redirect(url_for('appointment_page'))

# ✅ Run App
if __name__ == '__main__':
    app.run(debug=True)
