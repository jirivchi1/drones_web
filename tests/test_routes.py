"""
Integration tests for application routes
"""
import pytest
from app.models import ContactMessage


class TestHomeRoute:
    """Tests for home page"""

    def test_home_page_loads(self, client, database):
        """Test that home page loads successfully"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'UpFrames' in response.data or b'Videos con Drones' in response.data


class TestContactRoute:
    """Tests for contact page and form"""

    def test_contact_page_loads(self, client, database):
        """Test that contact page loads"""
        response = client.get('/contacto')
        assert response.status_code == 200

    def test_contact_form_submission_valid(self, client, database):
        """Test valid form submission"""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '123456789',
            'message': 'This is a test message for the contact form',
            'service_types': ['Bodas', 'Naturaleza']
        }

        response = client.post('/contacto', data=form_data, follow_redirects=True)

        # Check redirect happened
        assert response.status_code == 200

        # Check message was saved
        message = ContactMessage.query.filter_by(email='test@example.com').first()
        assert message is not None
        assert message.name == 'Test User'
        assert message.message == 'This is a test message for the contact form'

    def test_contact_form_validation_missing_name(self, client, database):
        """Test form validation - missing name"""
        form_data = {
            'email': 'test@example.com',
            'message': 'Test message without name'
        }

        response = client.post('/contacto', data=form_data)

        # Should show error, not redirect
        assert response.status_code == 200
        assert b'El nombre es obligatorio' in response.data or b'field is required' in response.data

    def test_contact_form_validation_invalid_email(self, client, database):
        """Test form validation - invalid email"""
        form_data = {
            'name': 'Test User',
            'email': 'invalid-email',
            'message': 'Test message with invalid email'
        }

        response = client.post('/contacto', data=form_data)

        # Should show error
        assert response.status_code == 200

    def test_contact_form_validation_short_message(self, client, database):
        """Test form validation - message too short"""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Short'  # Less than 10 characters
        }

        response = client.post('/contacto', data=form_data)

        # Should show error
        assert response.status_code == 200


class TestAdminRoute:
    """Tests for admin messages page"""

    def test_admin_messages_page_loads(self, client, database):
        """Test that admin messages page loads"""
        response = client.get('/admin/mensajes')
        assert response.status_code == 200

    def test_admin_messages_shows_messages(self, client, sample_contact_message):
        """Test that admin page shows saved messages"""
        response = client.get('/admin/mensajes')
        assert response.status_code == 200
        assert b'Juan' in response.data or b'juan@ejemplo.com' in response.data


class TestErrorPages:
    """Tests for error pages"""

    def test_404_error_page(self, client, database):
        """Test 404 error page"""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404
        assert b'404' in response.data or b'no encontrada' in response.data
