# 🐾 Paw Patrol - Pet Care & Appointment Booking System

## 📘 Project Overview

**Paw Patrol** is a web-based pet care platform designed for easy and efficient veterinary appointment booking.
It allows pet owners to schedule consultations, grooming, vaccinations, and other services online with an intuitive and visually rich interface.

---

## 💡 Features

* **Interactive Appointment Booking** — Multi-step form for booking with date, time, service, and pet details.
* **Responsive Design** — Built with Tailwind CSS for mobile and desktop compatibility.
* **Dynamic UI Elements** — Feather icons, time-slot animations, and confirmation flows.
* **Backend Integration** — Flask (`app.py`) handles appointment data submission.
* **Quick Access Navigation** — Fixed navbar with service links and “Book Appointment” button.

---

## 🛠️ Technology Stack

| Layer      | Tools & Frameworks                                     |
| ---------- | ------------------------------------------------------ |
| Frontend   | HTML5, Tailwind CSS, Vanilla JavaScript, Feather Icons |
| Backend    | Python (Flask)                                         |
| Database   | SQLite                                                 |
| Deployment | Localhost / Flask Development Server                   |

---

## 🧱 System Architecture

A simple **client-server architecture**:

* **Frontend (HTML + JS)** — Renders forms, collects user data.
* **Flask Backend (`app.py`)** — Receives form data and stores it in SQLite.
* **Database** — Stores user appointments, services, and pet details.

---

## 🗄️ Database Model

**appointments**

| Column     | Type         | Description           |
| ---------- | ------------ | --------------------- |
| id         | INTEGER (PK) | Unique appointment ID |
| name       | TEXT         | Owner’s name          |
| pet_name   | TEXT         | Pet’s name            |
| service    | TEXT         | Selected service      |
| date       | DATE         | Appointment date      |
| time       | TEXT         | Selected time slot    |
| contact    | TEXT         | Owner’s phone/email   |
| created_at | TIMESTAMP    | Booking creation date |

---

## ⚙️ Setup & Run Instructions

### Step 1 — Setup & Run Server

```bash
pip install flask
python app.py
```

This will start the Flask server and initialize the database automatically.

### Step 2 — Open UI

Visit:
[http://localhost:5000/](http://localhost:5000/)
to access the **homepage** and navigate to **Book Appointment**.

### Step 3 — Make a Booking

Fill in:

* Name
* Pet Name
* Service
* Date & Time
* Contact Details
  and submit the form.
  The booking details will be saved in the database.

---

## 🧪 API Sample

**POST /appointment**

**Sample JSON Input:**

```json
{
  "name": "Akshita",
  "pet_name": "Bruno",
  "service": "Grooming",
  "date": "2025-10-31",
  "time": "10:30 AM",
  "contact": "+91 9876543210"
}
```

**Sample JSON Output:**

```json
{
  "id": 1,
  "name": "Akshita",
  "pet_name": "Bruno",
  "service": "Grooming",
  "date": "2025-10-31",
  "time": "10:30 AM",
  "status": "Booked"
}
```

---

## 🎨 Design Highlights

* Tailwind-powered responsive design.
* Smooth transitions and step indicators.
* Calendar-style date and time pickers.
* Feather icons for a clean modern UI.

---

## 📚 Files Included

```
├── app.py                # Flask backend
├── index.html            # Home page
├── appointment.html      # Appointment booking UI
├── static/               # CSS/JS assets (if any)
└── README.md             # Documentation
```

---

## 🧩 Future Enhancements

* Email/SMS appointment confirmations
* Admin dashboard for managing bookings
* Multi-vet scheduling and availability tracking
* Secure authentication for users and staff

---

**Developed by:** Akshita M
**Institution:** SRM KTR
**Course:** CSE - AIML
**Year:** 2025
