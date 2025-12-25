import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime


def setup_logging(app):
    """
    Configure logging for the application

    Creates separate log files for:
    - app.log: All logs (INFO and above)
    - error.log: Only ERROR and CRITICAL logs
    """
    if not app.debug and not app.testing:
        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(os.path.dirname(app.instance_path), 'logs')
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # File handler for general logs
        file_handler = RotatingFileHandler(
            os.path.join(logs_dir, 'app.log'),
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        # File handler for errors only
        error_handler = RotatingFileHandler(
            os.path.join(logs_dir, 'error.log'),
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        error_handler.setFormatter(logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s [%(pathname)s:%(lineno)d]: %(message)s'
        ))
        error_handler.setLevel(logging.ERROR)
        app.logger.addHandler(error_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('UpFrames application startup')

    else:
        # Development mode - log to console
        if not app.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(
                '[%(asctime)s] %(levelname)s: %(message)s'
            ))
            app.logger.addHandler(console_handler)
            app.logger.setLevel(logging.DEBUG)
            app.logger.debug('UpFrames running in development mode')
