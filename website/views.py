from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Car, Booking
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # Query cars to show availability summary
    cars = Car.query.order_by(Car.name).all()
    return render_template("home.html", cars=cars)

@views.route('/book', methods=['GET', 'POST'])
def book():
    # car_type can be passed as query param to prefill the form
    car_type = request.args.get('car_type', '')

    # We want a list of car names for the form
    cars = Car.query.order_by(Car.name).all()

    if request.method == 'POST':
        # Collect form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        car_type = request.form.get('car_type', '')
        start_date_str = request.form.get('start_date', '')
        end_date_str = request.form.get('end_date', '')

        # Validate
        if not (name and email and car_type and start_date_str and end_date_str):
            flash("Please fill out all fields.", "error")
            return redirect(url_for('views.book', car_type=car_type))

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash("Invalid date format.", "error")
            return redirect(url_for('views.book', car_type=car_type))

        if end_date < start_date:
            flash("End date must be the same or after start date.", "error")
            return redirect(url_for('views.book', car_type=car_type))

        # Find matching car types (one or more rows can share same name)
        car = Car.query.filter_by(name=car_type).first()
        if not car:
            flash("Selected car type does not exist.", "error")
            return redirect(url_for('views.book'))

        # Count overlapping bookings for that car type (overlap if start <= existing.end and end >= existing.start)
        overlapping_count = Booking.query.filter(
            Booking.car_type == car_type,
            Booking.start_date <= end_date,
            Booking.end_date >= start_date
        ).count()

        if overlapping_count >= car.total_quantity:
            flash(f"Sorry — {car_type} is not available for the selected dates.", "error")
            return redirect(url_for('views.book', car_type=car_type))

        # Everything ok → create booking
        new_booking = Booking(
            customer_name=name,
            email=email,
            car_type=car_type,
            car_id=car.id,
            start_date=start_date,
            end_date=end_date
        )
        db.session.add(new_booking)
        db.session.commit()
        flash("Booking successful! Check your email for confirmation (not implemented).", "success")
        return redirect(url_for('views.home'))

    # GET: render the form
    return render_template("book.html", car_type=car_type, cars=cars)
