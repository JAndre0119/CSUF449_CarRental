from . import db
from datetime import datetime
import os
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    make = db.Column(db.String(80), nullable=True)
    model = db.Column(db.String(80), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    price_per_day = db.Column(db.Float, nullable=True, default=0.0)
    total_quantity = db.Column(db.Integer, nullable=False, default=1)
    image_filename = db.Column(db.String(200), nullable=True)

    bookings = db.relationship('Booking', backref='car', lazy=True)

    # ⚠️ NEW — Safe image getter with fallback
    @property
    def image_url(self):
        # If no filename → use placeholder
        if not self.image_filename:
            return "/static/images/placeholder.jpg"

        # Path to actual file
        img_path = os.path.join(
            current_app.root_path, "static", "images", self.image_filename
        )

        # If file missing → use placeholder
        if not os.path.exists(img_path):
            return "/static/images/placeholder.jpg"

        # Otherwise return the file
        return f"/static/images/{self.image_filename}"

    def __repr__(self):
        return f"<Car {self.name} qty={self.total_quantity}>"


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    car_type = db.Column(db.String(80), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(30), default='Confirmed')

    def __repr__(self):
        return f"<Booking {self.customer_name} {self.car_type} {self.start_date}→{self.end_date}>"

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"
