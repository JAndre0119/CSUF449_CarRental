from website import create_app, db
from website.models import Car

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    cars = [
        Car(
            name="Tesla Model 3",
            make="Tesla",
            model="Model 3",
            year=2023,
            price_per_day=120,
            total_quantity=1,
            image_filename="tesla_model3.jpg"
        ),
        Car(
            name="Toyota Camry",
            make="Toyota",
            model="Camry",
            year=2022,
            price_per_day=60,
            total_quantity=1,
            image_filename="toyota_camry.jpg"
        ),
        Car(
            name="BMW X5",
            make="BMW",
            model="X5",
            year=2021,
            price_per_day=100,
            total_quantity=1,
            image_filename="bmw_x5.jpg"
        ),
    ]

    db.session.add_all(cars)
    db.session.commit()
    print("Cars with images seeded successfully!")
