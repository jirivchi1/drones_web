from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, jsonify
from app import db
from app.models import ContactMessage, Video, Testimonial
from app.forms import ContactForm
from app.services import send_contact_email
import logging

bp = Blueprint('main', __name__)
logger = logging.getLogger(__name__)


@bp.route('/')
def index():
    """Home page"""
    # Get all active videos ordered by order field
    videos = Video.query.filter_by(is_active=True).order_by(Video.order).all()

    # Get all active testimonials ordered by order field
    testimonials = Testimonial.query.filter_by(is_active=True).order_by(Testimonial.order).all()

    # Get unique categories from videos for category buttons
    categories = db.session.query(Video.category).filter_by(is_active=True).distinct().all()
    categories = [cat[0] for cat in categories]

    return render_template('index.html',
                         videos=videos,
                         testimonials=testimonials,
                         categories=categories)


@bp.route('/contacto', methods=['GET', 'POST'])
def contact():
    """Contact page with form"""
    form = ContactForm()

    if form.validate_on_submit():
        try:
            # Get form data
            name = form.name.data
            email = form.email.data
            phone = form.phone.data
            message = form.message.data
            service_types = form.service_types.data

            # Save to database
            contact_message = ContactMessage(
                name=name,
                email=email,
                phone=phone,
                message=message,
                service_types=','.join(service_types) if service_types else None
            )

            db.session.add(contact_message)
            db.session.commit()

            logger.info(f'Contact message saved: {contact_message.id} - {email}')

            # Send email notification
            email_data = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
                'service_types': service_types
            }

            email_sent = send_contact_email(email_data)

            if email_sent:
                logger.info(f'Email sent successfully for contact {contact_message.id}')
            else:
                logger.warning(f'Email failed to send for contact {contact_message.id}')

            # Flash success message
            flash('¡Gracias por tu mensaje! Te contactaremos pronto.', 'success')

            # Redirect to avoid form resubmission
            return redirect(url_for('main.contact'))

        except Exception as e:
            db.session.rollback()
            logger.error(f'Error processing contact form: {str(e)}')
            flash('Hubo un error al enviar tu mensaje. Por favor intenta nuevamente.', 'error')

    elif request.method == 'POST':
        # Form validation failed
        flash('Por favor corrige los errores en el formulario.', 'error')

    return render_template('contact.html', form=form)
