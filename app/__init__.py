# From flask we are importing the Flask class
from flask import Flask


def create_app():
    #  Creating a app variable and setting this to a instance of the Flask class
    # __name__ is a special variable in Python that is just the name of a module
    # Equal to __main__, so flask knows where to look for your templates, static files, etc
    app = Flask(__name__)

    from app.main.routes import main
    from app.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
