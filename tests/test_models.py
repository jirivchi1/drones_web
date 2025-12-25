"""
Unit tests for database models
"""
import pytest
from app.models import ContactMessage, Video, Testimonial


class TestContactMessage:
    """Tests for ContactMessage model"""

    def test_create_contact_message(self, database):
        """Test creating a contact message"""
        message = ContactMessage(
            name='Test User',
            email='test@example.com',
            phone='987654321',
            message='Test message content',
            service_types='Bodas,Naturaleza'
        )
        database.session.add(message)
        database.session.commit()

        assert message.id is not None
        assert message.name == 'Test User'
        assert message.email == 'test@example.com'
        assert message.is_read is False

    def test_contact_message_to_dict(self, sample_contact_message):
        """Test converting contact message to dictionary"""
        data = sample_contact_message.to_dict()

        assert 'id' in data
        assert data['name'] == 'Juan Pérez'
        assert data['email'] == 'juan@ejemplo.com'
        assert isinstance(data['service_types'], list)
        assert 'Bodas' in data['service_types']

    def test_contact_message_default_values(self, database):
        """Test default values"""
        message = ContactMessage(
            name='Test',
            email='test@test.com',
            message='Test'
        )
        database.session.add(message)
        database.session.commit()

        assert message.is_read is False
        assert message.phone is None
        assert message.created_at is not None


class TestVideo:
    """Tests for Video model"""

    def test_create_video(self, database):
        """Test creating a video"""
        video = Video(
            title='Mi Video',
            description='Descripción del video',
            filename='video.mp4',
            category='Carrera',
            order=5
        )
        database.session.add(video)
        database.session.commit()

        assert video.id is not None
        assert video.title == 'Mi Video'
        assert video.category == 'Carrera'
        assert video.is_active is True

    def test_video_to_dict(self, sample_video):
        """Test converting video to dictionary"""
        data = sample_video.to_dict()

        assert 'id' in data
        assert data['title'] == 'Video de Prueba'
        assert data['category'] == 'Deportivo'
        assert data['order'] == 1

    def test_video_default_values(self, database):
        """Test default values"""
        video = Video(
            title='Test',
            filename='test.mp4',
            category='Test'
        )
        database.session.add(video)
        database.session.commit()

        assert video.order == 0
        assert video.is_active is True
        assert video.created_at is not None
        assert video.updated_at is not None


class TestTestimonial:
    """Tests for Testimonial model"""

    def test_create_testimonial(self, database):
        """Test creating a testimonial"""
        testimonial = Testimonial(
            author_name='María García',
            author_role='Cliente',
            content='Excelente servicio',
            order=1
        )
        database.session.add(testimonial)
        database.session.commit()

        assert testimonial.id is not None
        assert testimonial.author_name == 'María García'
        assert testimonial.is_active is True

    def test_testimonial_to_dict(self, database):
        """Test converting testimonial to dictionary"""
        testimonial = Testimonial(
            author_name='Carlos Ruiz',
            author_role='Director',
            author_image_url='https://example.com/image.jpg',
            content='Gran experiencia',
            order=2
        )
        database.session.add(testimonial)
        database.session.commit()

        data = testimonial.to_dict()

        assert 'id' in data
        assert data['author_name'] == 'Carlos Ruiz'
        assert data['author_role'] == 'Director'
        assert data['content'] == 'Gran experiencia'
