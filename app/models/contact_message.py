from app import db
from datetime import datetime


class ContactMessage(db.Model):
    """Model for storing contact form submissions"""
    __tablename__ = 'contact_messages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    message = db.Column(db.Text, nullable=False)
    service_types = db.Column(db.String(255), nullable=True)  # Stored as comma-separated string
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<ContactMessage {self.id}: {self.name} - {self.email}>'

    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'message': self.message,
            'service_types': self.service_types.split(',') if self.service_types else [],
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat()
        }
