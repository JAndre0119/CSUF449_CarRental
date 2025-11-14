from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

DB_NAME = "cars.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

    # Email notification configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'Rafaelmercadoespinoza@gmail.com'
    app.config['MAIL_PASSWORD'] = '554420938'  # replace with real Gmail App Password

    db.init_app(app)
    mail.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    create_database(app)

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database created!")
