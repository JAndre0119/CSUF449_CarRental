# EasyCar Rentals – Flask Web Application

🚗 A simple car rental web app built with **Flask**, **SQLite**, and **SQLAlchemy**.  
Allows users to browse cars, view details, and book rentals.  

---

## Features

- Home page showcasing available cars dynamically from the database.  
- Book a car with selectable rental days and quantity.  
- Responsive design using **Bootstrap 5**.  
- Backend database integration using **SQLite** + **SQLAlchemy**.  
- Modular Flask structure with Blueprints.  

---

## Tech Stack

- Python 3.x  
- Flask  
- Flask-SQLAlchemy  
- SQLite (database)  
- Jinja2 (templating)  
- Bootstrap 5 (frontend)  

---

## Project Structure

CSUF449_CarRental/
│
├── website/ # Flask app package
│ ├── init.py # App factory + database setup
│ ├── models.py # Database models (Car, Booking)
│ ├── views.py # Flask routes
│ ├── templates/ # HTML templates
│ │ ├── base.html # Base template for all pages
│ │ ├── home.html # Home page
│ │ └── book.html # Booking page
│ └── static/ # CSS / images / JS
│ └── style.css
│
├── seed.py # Script to populate initial cars
├── main.py # Run the Flask app
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## Installation

1. Clone the repository:
- bash
- git clone https://github.com/JAndre0119/CSUF449_CarRental.git
- cd CSUF449_CarRental

2. Create a virtual environment:
- bash
- python -m venv venv

3. Activate the virtual environment:
- Windows (cmd):
- cmd
- venv\Scripts\activate

- Windows (PowerShell):
- powershell
- venv\Scripts\Activate.ps1

- Mac/Linux:
- bash
- source venv/bin/activate

4. Install dependencies:
- bash
- pip install -r requirements.txt

5. Database Setup
- Create the database and tables:
- python
- from website import create_app, db
- app = create_app()
- app.app_context().push()
- db.create_all()

6. Seed the database with initial cars:
- bash
- python seed.py

7. View the database using:
- SQLite CLI: sqlite3 database.db
- DB Browser for SQLite: https://sqlitebrowser.org

8. Running the App
- bash
- python main.py
- Open http://127.0.0.1:5000 in your browser.

9. Usage
- Home Page: View all available cars with images, make, model, year, and price.
- Book Now: Click “Rent Now” to go to the booking page.
- Booking Page: Select car, number of rental days, and quantity. Submit to reserve.

10. Adding Images for Cars
- Add a column image_url in the Car model.
- Store URLs for each car’s image in the database.
- Update home.html to use:
- html
- <img src="{{ car.image_url }}" alt="{{ car.name }}">

11. Dependencies
- Flask==2.3.4
- Flask-SQLAlchemy==3.0.5
- Jinja2==3.1.3

12. Notes
- Make sure your virtual environment is active whenever installing packages or running the app.
- Use a database GUI or Python shell to inspect/update cars and bookings.
- You can extend the app by adding:
- User accounts
- Payment integration
- Admin dashboard
