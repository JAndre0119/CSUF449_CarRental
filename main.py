from website import create_app  
import logging
from logging.handlers import RotatingFileHandler

app = create_app()

if __name__ == '__main__':
    #runs our app and starts the web

    app.run()

