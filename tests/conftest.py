"""
Pytest configuration and fixtures
"""
import pytest
from app import create_app, db
from app.models import ContactMessage, Video, Testimonial


@pytest.fixture(scope='session')
def app():
    """Create application for testing"""
    app = create_app('testing')
    return app


@pytest.fixture(scope='function')
def client(app):
    """Create test client"""
    return app.test_client()


@pytest.fixture(scope='function')
def database(app):
    """Create database for testing"""
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def sample_contact_message(database):
    """Create a sample contact message for testing"""
    message = ContactMessage(
        name='Juan Pérez',
        email='juan@ejemplo.com',
        phone='123456789',
        message='Mensaje de prueba',
        service_types='Bodas,Inmobiliaria'
    )
    database.session.add(message)
    database.session.commit()
    return message


@pytest.fixture(scope='function')
def sample_video(database):
    """Create a sample video for testing"""
    video = Video(
        title='Video de Prueba',
        description='Descripción de prueba',
        filename='test.mp4',
        category='Deportivo',
        order=1
    )
    database.session.add(video)
    database.session.commit()
    return video
