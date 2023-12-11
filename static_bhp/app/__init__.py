from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurations, extensions, and other setup can go here

    from .views import physical_properties
    app.register_blueprint(physical_properties)

    return app
