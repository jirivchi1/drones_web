from flask import current_app, render_template
from flask_mail import Message
from app import mail
import logging

logger = logging.getLogger(__name__)


def send_contact_email(contact_data):
    """
    Send email notification when a contact form is submitted

    Args:
        contact_data (dict): Dictionary containing contact form data
            - name: Contact's name
            - email: Contact's email
            - phone: Contact's phone (optional)
            - message: Contact's message
            - service_types: List of requested services

    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        # Get admin email from config
        admin_email = current_app.config.get('ADMIN_EMAIL', 'admin@upframes.com')

        # Prepare email subject
        subject = f'Nuevo mensaje de contacto - {contact_data["name"]}'

        # Prepare email body
        service_types_str = ', '.join(contact_data.get('service_types', [])) if contact_data.get('service_types') else 'No especificado'

        body = f"""
¡Nuevo mensaje de contacto recibido!

DATOS DEL CLIENTE:
------------------
Nombre: {contact_data['name']}
Email: {contact_data['email']}
Teléfono: {contact_data.get('phone', 'No proporcionado')}

SERVICIOS SOLICITADOS:
----------------------
{service_types_str}

MENSAJE:
--------
{contact_data['message']}

---
Este email fue enviado automáticamente desde el formulario de contacto de UpFrames.
"""

        # Create message
        msg = Message(
            subject=subject,
            recipients=[admin_email],
            body=body,
            sender=current_app.config.get('MAIL_DEFAULT_SENDER')
        )

        # Send email
        mail.send(msg)

        logger.info(f'Contact email sent successfully for {contact_data["email"]}')
        return True

    except Exception as e:
        logger.error(f'Error sending contact email: {str(e)}')
        # Don't raise exception - we still want to save to database even if email fails
        return False
