# Appointment-Management-Application

Overview
This is a web-based Appointment Management System where students can book appointments with staff members. The staff can manage their availability and confirm or reject appointments. The project is built using Django for the backend and HTML, CSS, TailwindCSS, and JavaScript for the frontend.

Features
User Authentication: Separate login for students and staff members.
Appointment Booking: Students can book appointments with available staff members.
Staff Availability: Staff can manage their availability slots (date and time).
Dashboard: Separate dashboards for students and staff to manage appointments.
Students: Book and view appointments.
Staff: Manage availability and confirm or reject appointments.
CRUD Operations: Create, view, update, and delete appointments.
Responsive Design: Optimized for both desktop and mobile devices.
Technologies Used
Backend: Django (Python)
Frontend: HTML, TailwindCSS, JavaScript
Database: SQLite (Django's default)
Installation
Clone the repository:

    git clone https://github.com/DEV-Nik06/appointment_system.git
    cd appointment_system

Create a virtual environment and activate it:

    python -m venv env
    source venv/bin/activate  # On Windows use: .venv\Scripts\activate

Install the dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate
Create a superuser (optional, for admin access):

    python manage.py createsuperuser
Run the development server:

    python manage.py runserver
    Open your browser and navigate to http://127.0.0.1:8000.

Usage

Students:

    Register or log in.
    Book an appointment with a staff member.
    View your booked appointments from the dashboard.

Staff:

    Log in.
    Manage availability by setting available time slots.
    Confirm or reject student appointments.

Folder Structure

    ├── appointments/       # Main Django app with models, views, templates
    ├── static/             # Static files (CSS, images)
    ├── templates/          # HTML templates
    ├── db.sqlite3          # SQLite database
    ├── manage.py           # Django management script
    ├── requirements.txt    # Dependencies
    └── README.md           # Project documentation

Contributing

    If you want to contribute to this project:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Push to your branch (git push origin feature-branch).
    Open a Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
