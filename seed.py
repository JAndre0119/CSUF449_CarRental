from website import create_app, db
from website.models import Car

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    cars = [
        # Sedans
        Car(name="Toyota Camry", make="Toyota", model="Camry", year=2022, price_per_day=60, total_quantity=3, image_filename="placeholder.jpg"),
        Car(name="Honda Accord", make="Honda", model="Accord", year=2023, price_per_day=65, total_quantity=3, image_filename="placeholder.jpg"),
        Car(name="Nissan Altima", make="Nissan", model="Altima", year=2021, price_per_day=55, total_quantity=2, image_filename="placeholder.jpg"),
        Car(name="Hyundai Sonata", make="Hyundai", model="Sonata", year=2022, price_per_day=58, total_quantity=2, image_filename="placeholder.jpg"),

        # Compact Cars
        Car(name="Toyota Corolla", make="Toyota", model="Corolla", year=2022, price_per_day=45, total_quantity=3, image_filename="placeholder.jpg"),
        Car(name="Honda Civic", make="Honda", model="Civic", year=2023, price_per_day=50, total_quantity=3, image_filename="placeholder.jpg"),
        Car(name="Mazda 3", make="Mazda", model="3", year=2021, price_per_day=48, total_quantity=2, image_filename="placeholder.jpg"),

        # SUVs
        Car(name="Toyota RAV4", make="Toyota", model="RAV4", year=2023, price_per_day=80, total_quantity=3, image_filename="placeholder.jpg"),
        Car(name="Honda CR-V", make="Honda", model="CR-V", year=2022, price_per_day=78, total_quantity=3, image_filename="placeholder.jpg"),
        Car(name="Ford Escape", make="Ford", model="Escape", year=2021, price_per_day=70, total_quantity=2, image_filename="placeholder.jpg"),
        Car(name="BMW X5", make="BMW", model="X5", year=2021, price_per_day=110, total_quantity=1, image_filename="placeholder.jpg"),
        Car(name="Audi Q5", make="Audi", model="Q5", year=2022, price_per_day=115, total_quantity=1, image_filename="placeholder.jpg"),

        # Luxury Sedans
        Car(name="Mercedes C-Class", make="Mercedes", model="C300", year=2023, price_per_day=140, total_quantity=1, image_filename="placeholder.jpg"),
        Car(name="BMW 5 Series", make="BMW", model="530i", year=2022, price_per_day=150, total_quantity=1, image_filename="placeholder.jpg"),
        Car(name="Audi A4", make="Audi", model="A4", year=2021, price_per_day=130, total_quantity=1, image_filename="placeholder.jpg"),

        # Electric Cars
        Car(name="Tesla Model 3", make="Tesla", model="Model 3", year=2023, price_per_day=120, total_quantity=2, image_filename="placeholder.jpg"),
        Car(name="Tesla Model Y", make="Tesla", model="Model Y", year=2022, price_per_day=130, total_quantity=2, image_filename="placeholder.jpg"),
        Car(name="Chevy Bolt", make="Chevrolet", model="Bolt", year=2021, price_per_day=65, total_quantity=2, image_filename="placeholder.jpg"),

        # Trucks
        Car(name="Ford F-150", make="Ford", model="F-150", year=2022, price_per_day=95, total_quantity=2, image_filename="placeholder.jpg"),
        Car(name="Ram 1500", make="Ram", model="1500", year=2021, price_per_day=90, total_quantity=2, image_filename="placeholder.jpg"),
        Car(name="Toyota Tacoma", make="Toyota", model="Tacoma", year=2023, price_per_day=85, total_quantity=2, image_filename="placeholder.jpg"),

        # Vans
        Car(name="Honda Odyssey", make="Honda", model="Odyssey", year=2022, price_per_day=88, total_quantity=2, image_filename="placeholder.jpg"),
        Car(name="Toyota Sienna", make="Toyota", model="Sienna", year=2021, price_per_day=92, total_quantity=1, image_filename="placeholder.jpg"),

        # Sports Cars
        Car(name="Ford Mustang", make="Ford", model="Mustang", year=2023, price_per_day=150, total_quantity=1, image_filename="placeholder.jpg"),
        Car(name="Chevrolet Camaro", make="Chevrolet", model="Camaro", year=2022, price_per_day=160, total_quantity=1, image_filename="placeholder.jpg"),
        Car(name="Dodge Challenger", make="Dodge", model="Challenger", year=2021, price_per_day=155, total_quantity=1, image_filename="placeholder.jpg"),

        # Luxury SUVs
        Car(name="Range Rover Evoque", make="Land Rover", model="Evoque", year=2023, price_per_day=180, total_quantity=1, image_filename="placeholder.jpg"),
        Car(name="Porsche Macan", make="Porsche", model="Macan", year=2022, price_per_day=200, total_quantity=1, image_filename="placeholder.jpg"),

        # Economy Cars
        Car(name="Kia Forte", make="Kia", model="Forte", year=2022, price_per_day=40, total_quantity=3, image_filename="placeholder.jpg"),
        Car(name="Hyundai Elantra", make="Hyundai", model="Elantra", year=2021, price_per_day=42, total_quantity=3, image_filename="placeholder.jpg"),
    ]

    db.session.add_all(cars)
    db.session.commit()

    print("Seeded 30 cars with placeholder.jpg!")
