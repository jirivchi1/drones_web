from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from config import config
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_name=None):
    """Application factory pattern"""
    app = Flask(__name__,
                template_folder='views/templates',
                static_folder='views/static')

    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app.config.from_object(config[config_name])

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Import models (required for Flask-Migrate to detect them)
    from app.models import ContactMessage, Video, Testimonial

    # Register blueprints
    from app.controllers import main_controller
    app.register_blueprint(main_controller.bp)

    # Register admin blueprint
    from app.admin import admin_bp
    app.register_blueprint(admin_bp)

    # Register error handlers
    register_error_handlers(app)

    # Setup logging
    from app.utils import setup_logging
    setup_logging(app)

    # Create instance folder if it doesn't exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


def register_error_handlers(app):
    """Register custom error handlers"""
    from flask import render_template
    import logging

    logger = logging.getLogger(__name__)

    @app.errorhandler(404)
    def not_found_error(error):
        """Handle 404 errors"""
        logger.warning(f'404 error: {error}')
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        db.session.rollback()  # Rollback any failed database transactions
        logger.error(f'500 error: {error}', exc_info=True)
        return render_template('errors/500.html'), 500

    @app.errorhandler(403)
    def forbidden_error(error):
        """Handle 403 errors"""
        logger.warning(f'403 error: {error}')
        return render_template('errors/404.html'), 403  # Reuse 404 template

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        """Catch-all for any unhandled exceptions"""
        db.session.rollback()
        logger.error(f'Unexpected error: {error}', exc_info=True)
        return render_template('errors/500.html'), 500
