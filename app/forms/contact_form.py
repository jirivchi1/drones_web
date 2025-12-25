from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, Optional
from wtforms.widgets import CheckboxInput, ListWidget


class MultiCheckboxField(SelectMultipleField):
    """Custom field for multiple checkboxes"""
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class ContactForm(FlaskForm):
    """Contact form with validation and CSRF protection"""

    # Personal information
    name = StringField(
        'Tu nombre',
        validators=[
            DataRequired(message='El nombre es obligatorio'),
            Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres')
        ],
        render_kw={'placeholder': 'Tu nombre'}
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(message='El email es obligatorio'),
            Email(message='Por favor ingresa un email válido')
        ],
        render_kw={'placeholder': 'tu@email.com'}
    )

    phone = StringField(
        'Teléfono',
        validators=[
            Optional(),
            Length(max=20, message='El teléfono no puede exceder 20 caracteres')
        ],
        render_kw={'placeholder': '+34 600 000 000'}
    )

    # Message
    message = TextAreaField(
        'Describe tu proyecto o evento',
        validators=[
            DataRequired(message='El mensaje es obligatorio'),
            Length(min=10, max=1000, message='El mensaje debe tener entre 10 y 1000 caracteres')
        ],
        render_kw={
            'rows': 4,
            'placeholder': 'Cuéntanos sobre tu evento, qué tipo de grabación necesitas, fecha aproximada...'
        }
    )

    # Service types
    service_types = MultiCheckboxField(
        'Tipo de servicio que buscas',
        choices=[
            ('Eventos Deportivos', 'Eventos Deportivos'),
            ('Bodas', 'Bodas'),
            ('Inmobiliaria', 'Inmobiliaria'),
            ('Naturaleza', 'Naturaleza'),
            ('Publicidad', 'Publicidad'),
            ('Cinematográfico', 'Cinematográfico'),
            ('Otro', 'Otro')
        ],
        validators=[Optional()]
    )

    def validate(self, extra_validators=None):
        """Custom validation"""
        if not super().validate(extra_validators):
            return False

        # Add any custom validation logic here
        return True
