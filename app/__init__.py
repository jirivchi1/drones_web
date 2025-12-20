from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__,
                template_folder='views/templates',
                static_folder='views/static')

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

    from app.controllers import main_controller
    app.register_blueprint(main_controller.bp)

    return app
