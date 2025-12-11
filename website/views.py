from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from . import db
from .models import Car, Booking
from datetime import datetime

views = Blueprint('views', __name__)



@views.route('/')
def home():
    # Query cars to show availability summary
    cars = Car.query.order_by(Car.name).all()
    return render_template("home.html", cars=cars)
#the contact page connects to homepage and to the file contact.html
from flask_mail import Message
from . import mail

#what sends the informaton about the contact me page
#it sends it to my email and sends aconfirmation email to user.
@views.route('/contact', methods=['GET', 'POST'])

def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        message_content = request.form.get('message')

        msg = Message(
            subject=f"New Contact Form Submission from {name}",
            sender="Rafaelmercadoespinoza@gmail.com",

            recipients=[email]
        )

        msg.body = f"""
You received a new contact request:

Name: {name}
Email: {email}

Message:
{message_content}
"""

        mail.send(msg)

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('views.contact'))

    return render_template('contact.html')

@views.route('/book', methods=['GET', 'POST'])
def book():
    # car_type can be passed as query param to prefill the form
    car_type = request.args.get('car_type', '')

    # We want a list of car names for the form
    cars = Car.query.order_by(Car.name).all()

    # GET: render the form
    return render_template("book.html", car_type=car_type, cars=cars)


# New route for /book/<int:car_id>
@views.route('/book/<int:car_id>', methods=['GET', 'POST'])
def book_with_id(car_id):
    # Get the selected car by ID

    # Still load all cars for the dropdown
    cars = Car.query.order_by(Car.name).all()
    car =Car.query.filter_by(id=car_id).first()
    car_type = car.name

    if request.method == 'POST':
        # Collect form data
        start_date_str = request.form.get('start_date', '')
        end_date_str = request.form.get('end_date', '')

        # Validate
        if not (start_date_str and end_date_str):
            flash("Please select both start and end dates.", "error")
            return redirect(url_for("views.book"))

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash("Invalid date format.", "error")
            return redirect(url_for("views.book"))

        if end_date < start_date:
            flash("End date must be the same or after start date.", "error")
            return redirect(url_for("views.book"))

        # Count overlapping bookings for this specific car TODO
       # overlapping_count = Booking.query.filter(
         #   Booking.car_id == car.id,
         #   Booking.start_date <= end_date,
         #   Booking.end_date >= start_date
        #).count()

        #if overlapping_count >= car.total_quantity:
        #    flash(f"Sorry — {car.name} is not available for the selected dates.", "error")
        #    return redirect(url_for("views.ch"))
        days = (end_date - start_date).days + 1
        total_price = days * float(car.price_per_day)
        # Create booking
        new_booking = Booking(
            customer_name="Guest",
            email="hidden@hidden.com",
            car_type=car.name,
            car_id=car.id,
            start_date=start_date,
            end_date=end_date,
        )

        db.session.add(new_booking)
        db.session.commit()

        # Save booking info for checkout page
        session['checkout'] = {
            'car_type': car.name,
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d"),
            'total_price': total_price
        }

        flash("Booking successful! Proceed to checkout.", "success")
        return redirect(url_for('views.checkout'))

    # GET request renders the form with this car pre-selected
    return render_template("book.html", car_type=car.name, cars=cars,car_id = car.id)


# Checkout page route
# @views.route('/checkout')
# def checkout():
#     checkout_data = session.get('checkout')
#
#     # Block access if user did not come from a booking
#     if not checkout_data:
#         #pass in data here
#         flash("You must book a car before accessing checkout.", "error")
#         return redirect(url_for('views.book'))
#
#     return render_template(
#         "checkoutpage.html",
#         car_type=checkout_data['car_type'],
#         start_date=checkout_data['start_date'],
#         end_date=checkout_data['end_date']
#     )

@views.route('/checkout', methods=['GET', 'POST'])
def checkout():
    checkout_data = session.get("checkout")

    # Block access if user did not come from a booking
    #if 'checkout' not in session:
    #    flash("You must book a car before accessing checkout.", "error")
    #    return redirect(url_for('views.book'))

    # Handle payment submission (POST)
    if request.method == 'POST':
        flash("Payment successful! Your booking is confirmed.", "success")
        session.pop('checkout', None)  # Clear checkout session after payment
        return redirect(url_for('views.home'))

    return render_template(
        "checkoutpage.html",
        car_type=checkout_data['car_type'],
        start_date=checkout_data['start_date'],
        end_date=checkout_data['end_date'],
        total_price=checkout_data['total_price']
    )

@views.route('/browse')
def browse():
    cars = Car.query.order_by(Car.name).all()
    return render_template("browse.html", cars=cars)

@views.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        make = request.form.get('make', '').strip()
        model = request.form.get('model', '').strip()
        year = request.form.get('year', '').strip()
        price_per_day = request.form.get('price_per_day', '').strip()
        total_quantity = request.form.get('total_quantity', '').strip()
        image_filename = request.form.get('image_filename', '').strip()

        if not name:
            flash("Car name is required.", "error")
        else:
            new_car = Car(
                name=name,
                make=make,
                model=model,
                year=int(year) if year else None,
                price_per_day=float(price_per_day) if price_per_day else 0.0,
                total_quantity=int(total_quantity) if total_quantity else 1,
                image_filename=image_filename or "default.jpg"
            )
            db.session.add(new_car)
            db.session.commit()
            flash(f"Car '{name}' added successfully!", "success")
        return redirect(url_for('views.admin'))

    cars = Car.query.order_by(Car.name).all()
    return render_template("admin.html", cars=cars)

@views.route('/delete_car/<int:car_id>', methods=['POST'])
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    try:
        db.session.delete(car)
        db.session.commit()
        flash(f"Car '{car.name}' deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Error deleting car: " + str(e), "error")
    return redirect(url_for('views.admin'))

#@views.route('/checkout')
#def checkout():
 #   return render_template("checkoutpage.html")
