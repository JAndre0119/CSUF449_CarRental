from . import db
from datetime import datetime

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)        # e.g., "Sedan", "SUV", "Luxury"
    make = db.Column(db.String(80), nullable=True)
    model = db.Column(db.String(80), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    price_per_day = db.Column(db.Float, nullable=True, default=0.0)
    total_quantity = db.Column(db.Integer, nullable=False, default=1)
    image_filename = db.Column(db.String(200), nullable=True)
    bookings = db.relationship('Booking', backref='car', lazy=True)

    def __repr__(self):
        return f"<Car {self.name} qty={self.total_quantity}>"

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    car_type = db.Column(db.String(80), nullable=False)  # keeps human-readable type
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(30), default='Confirmed')

    def __repr__(self):
        return f"<Booking {self.customer_name} {self.car_type} {self.start_date}→{self.end_date}>"
