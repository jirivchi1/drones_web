from app import db
from datetime import datetime


class Testimonial(db.Model):
    """Model for customer testimonials"""
    __tablename__ = 'testimonials'

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(100), nullable=False)
    author_role = db.Column(db.String(100), nullable=False)
    author_image_url = db.Column(db.String(500), nullable=True)
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, default=0, nullable=False)  # Display order
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Testimonial {self.id}: {self.author_name} - {self.author_role}>'

    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'author_name': self.author_name,
            'author_role': self.author_role,
            'author_image_url': self.author_image_url,
            'content': self.content,
            'order': self.order,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
