from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from . import db
from .models import Booking, Car, User
from datetime import datetime

bookings_bp = Blueprint("bookings", __name__)

# Show booking form
@bookings_bp.route("/book/<int:car_id>", methods=["GET", "POST"])
def book_car(car_id):
    car = Car.query.get_or_404(car_id)

    if request.method == "POST":
        # Get form data
        user_id = 1  # TODO: replace with logged-in user ID once auth is ready
        start_date = datetime.strptime(request.form["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(request.form["end_date"], "%Y-%m-%d").date()

        #if end_date < start_date:
        #    flash("End date must be after start date.", "error")
        #    return redirect(url_for("bookings.book_car", car_id=car_id))

        # Calculate total price
        days = (end_date - start_date).days + 1
        total_price = days * car.price_per_day

        # Save booking
        booking = Booking(
            user_id=user_id,
            car_id=car.id,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price
        )
        db.session.add(booking)
        db.session.commit()

        # Save checkout info to session so the checkout page can use it
        session['checkout'] = {
            'car_name': f"{car.make} {car.model}",
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d"),
            'total_price': total_price
        }

        flash(f"Booking confirmed for {car.make} {car.model}!", "success")
        return redirect(url_for("views.checkoutpage"))

    return render_template("book.html", car=car)

# Fallback route: catches bad POST requests to /book without a car_id
@bookings_bp.route("/book", methods=["POST"])
def book_car_fallback():
    flash("Booking error: Missing car ID. Please select a car again.", "error")
    return redirect(url_for("views.home"))
