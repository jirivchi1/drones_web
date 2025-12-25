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


@bp.route('/admin/mensajes')
def admin_messages():
    """View all contact messages (admin panel)"""
    # Get filter parameters
    search_query = request.args.get('search', '').strip()
    filter_status = request.args.get('status', 'all')

    # Base query
    query = ContactMessage.query

    # Apply filters
    if search_query:
        search_pattern = f'%{search_query}%'
        query = query.filter(
            db.or_(
                ContactMessage.name.ilike(search_pattern),
                ContactMessage.email.ilike(search_pattern),
                ContactMessage.message.ilike(search_pattern)
            )
        )

    if filter_status == 'read':
        query = query.filter_by(is_read=True)
    elif filter_status == 'unread':
        query = query.filter_by(is_read=False)

    # Get messages ordered by date
    messages = query.order_by(ContactMessage.created_at.desc()).all()

    # Get statistics
    total_messages = ContactMessage.query.count()
    unread_count = ContactMessage.query.filter_by(is_read=False).count()

    return render_template('admin_messages.html',
                         messages=messages,
                         total_messages=total_messages,
                         unread_count=unread_count,
                         search_query=search_query,
                         filter_status=filter_status)


@bp.route('/admin/mensajes/<int:message_id>/mark-read', methods=['POST'])
def mark_message_read(message_id):
    """Mark a message as read/unread"""
    try:
        message = ContactMessage.query.get_or_404(message_id)
        message.is_read = not message.is_read
        db.session.commit()

        status = 'leído' if message.is_read else 'no leído'
        logger.info(f'Message {message_id} marked as {status}')

        flash(f'Mensaje marcado como {status}', 'success')
        return redirect(url_for('main.admin_messages'))
    except Exception as e:
        db.session.rollback()
        logger.error(f'Error marking message as read: {str(e)}')
        flash('Error al actualizar el mensaje', 'error')
        return redirect(url_for('main.admin_messages'))


@bp.route('/admin/mensajes/<int:message_id>/delete', methods=['POST'])
def delete_message(message_id):
    """Delete a contact message"""
    try:
        message = ContactMessage.query.get_or_404(message_id)
        db.session.delete(message)
        db.session.commit()

        logger.info(f'Message {message_id} deleted')
        flash('Mensaje eliminado correctamente', 'success')
        return redirect(url_for('main.admin_messages'))
    except Exception as e:
        db.session.rollback()
        logger.error(f'Error deleting message: {str(e)}')
        flash('Error al eliminar el mensaje', 'error')
        return redirect(url_for('main.admin_messages'))


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
