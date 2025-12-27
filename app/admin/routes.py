from flask import render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from app.admin import admin_bp
from app.models import Video, ContactMessage
from app import db
from functools import wraps
import os

# Autenticación básica (puedes mejorarla después)
def check_admin_auth():
    """Verifica si el usuario tiene acceso admin"""
    # Por ahora, autenticación básica con contraseña
    # TODO: Implementar sistema de login más robusto
    auth = request.authorization
    if not auth or auth.password != current_app.config.get('ADMIN_PASSWORD', 'admin123'):
        return False
    return True

def requires_admin(f):
    """Decorador para proteger rutas admin"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_admin_auth():
            return render_template('admin/login.html'), 401, {
                'WWW-Authenticate': 'Basic realm="Admin Area"'
            }
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/videos')
@requires_admin
def videos_list():
    """Lista todos los videos en el panel admin"""
    videos = Video.query.order_by(Video.order).all()
    return render_template('admin/videos.html', videos=videos)


@admin_bp.route('/videos/new', methods=['GET', 'POST'])
@requires_admin
def video_new():
    """Crear un nuevo video"""
    if request.method == 'POST':
        # Validar datos
        title = request.form.get('title')
        category = request.form.get('category')
        description = request.form.get('description', '')

        if not title or not category:
            flash('El título y la categoría son obligatorios', 'error')
            return redirect(url_for('admin.video_new'))

        # Manejar el archivo de video
        if 'video_file' not in request.files:
            flash('No se seleccionó ningún archivo de video', 'error')
            return redirect(url_for('admin.video_new'))

        file = request.files['video_file']

        if file.filename == '':
            flash('No se seleccionó ningún archivo de video', 'error')
            return redirect(url_for('admin.video_new'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # Asegurar nombre único
            base_name, ext = os.path.splitext(filename)
            counter = 1
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

            while os.path.exists(upload_path):
                filename = f"{base_name}_{counter}{ext}"
                upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                counter += 1

            # Guardar archivo
            file.save(upload_path)

            # Crear entrada en base de datos
            max_order = db.session.query(db.func.max(Video.order)).scalar() or -1

            video = Video(
                title=title,
                category=category,
                description=description,
                filename=filename,
                order=max_order + 1
            )

            db.session.add(video)
            db.session.commit()

            flash(f'Video "{title}" subido exitosamente', 'success')
            return redirect(url_for('admin.videos_list'))
        else:
            flash('Tipo de archivo no permitido. Solo se permiten archivos .mp4, .mov, .avi', 'error')
            return redirect(url_for('admin.video_new'))

    return render_template('admin/video_form.html', video=None)


@admin_bp.route('/videos/<int:video_id>/edit', methods=['GET', 'POST'])
@requires_admin
def video_edit(video_id):
    """Editar un video existente"""
    video = Video.query.get_or_404(video_id)

    if request.method == 'POST':
        video.title = request.form.get('title')
        video.category = request.form.get('category')
        video.description = request.form.get('description', '')

        # Si se sube un nuevo archivo, reemplazar el anterior
        if 'video_file' in request.files:
            file = request.files['video_file']
            if file and file.filename != '' and allowed_file(file.filename):
                # Eliminar archivo anterior
                old_path = os.path.join(current_app.config['UPLOAD_FOLDER'], video.filename)
                if os.path.exists(old_path):
                    os.remove(old_path)

                # Guardar nuevo archivo
                filename = secure_filename(file.filename)
                base_name, ext = os.path.splitext(filename)
                counter = 1
                upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

                while os.path.exists(upload_path):
                    filename = f"{base_name}_{counter}{ext}"
                    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                    counter += 1

                file.save(upload_path)
                video.filename = filename

        db.session.commit()
        flash(f'Video "{video.title}" actualizado exitosamente', 'success')
        return redirect(url_for('admin.videos_list'))

    return render_template('admin/video_form.html', video=video)


@admin_bp.route('/videos/<int:video_id>/delete', methods=['POST'])
@requires_admin
def video_delete(video_id):
    """Eliminar un video"""
    video = Video.query.get_or_404(video_id)

    # Eliminar archivo físico
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], video.filename)
    if os.path.exists(file_path):
        os.remove(file_path)

    # Eliminar de base de datos
    db.session.delete(video)
    db.session.commit()

    flash(f'Video "{video.title}" eliminado exitosamente', 'success')
    return redirect(url_for('admin.videos_list'))


@admin_bp.route('/videos/<int:video_id>/move/<direction>', methods=['POST'])
@requires_admin
def video_move(video_id, direction):
    """Cambiar el orden de un video (arriba/abajo)"""
    video = Video.query.get_or_404(video_id)

    if direction == 'up' and video.order > 0:
        # Encontrar el video con order anterior
        other_video = Video.query.filter_by(order=video.order - 1).first()
        if other_video:
            video.order, other_video.order = other_video.order, video.order
            db.session.commit()

    elif direction == 'down':
        # Encontrar el video con order siguiente
        other_video = Video.query.filter_by(order=video.order + 1).first()
        if other_video:
            video.order, other_video.order = other_video.order, video.order
            db.session.commit()

    return redirect(url_for('admin.videos_list'))


def allowed_file(filename):
    """Verifica si el archivo tiene una extensión permitida"""
    ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'webm'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ============================================================================
# RUTAS PARA GESTIÓN DE MENSAJES DE CONTACTO
# ============================================================================

@admin_bp.route('/mensajes')
@requires_admin
def messages_list():
    """Lista todos los mensajes de contacto"""
    # Obtener parámetros de filtro
    filter_status = request.args.get('status', 'all')

    # Construir query base
    query = ContactMessage.query

    # Aplicar filtros
    if filter_status == 'unread':
        query = query.filter_by(read=False)
    elif filter_status == 'read':
        query = query.filter_by(read=True)

    # Ordenar por fecha (más recientes primero)
    messages = query.order_by(ContactMessage.created_at.desc()).all()

    # Contar mensajes no leídos
    unread_count = ContactMessage.query.filter_by(read=False).count()

    return render_template('admin/messages.html',
                         messages=messages,
                         filter_status=filter_status,
                         unread_count=unread_count)


@admin_bp.route('/mensajes/<int:message_id>/toggle-read', methods=['POST'])
@requires_admin
def message_toggle_read(message_id):
    """Cambiar estado leído/no leído de un mensaje"""
    message = ContactMessage.query.get_or_404(message_id)

    message.read = not message.read
    db.session.commit()

    status = 'leído' if message.read else 'no leído'
    flash(f'Mensaje marcado como {status}', 'success')

    return redirect(url_for('admin.messages_list'))


@admin_bp.route('/mensajes/<int:message_id>/delete', methods=['POST'])
@requires_admin
def message_delete(message_id):
    """Eliminar un mensaje de contacto"""
    message = ContactMessage.query.get_or_404(message_id)

    db.session.delete(message)
    db.session.commit()

    flash(f'Mensaje de "{message.name}" eliminado exitosamente', 'success')

    return redirect(url_for('admin.messages_list'))


@admin_bp.route('/mensajes/mark-all-read', methods=['POST'])
@requires_admin
def messages_mark_all_read():
    """Marcar todos los mensajes como leídos"""
    ContactMessage.query.update({ContactMessage.read: True})
    db.session.commit()

    flash('Todos los mensajes marcados como leídos', 'success')

    return redirect(url_for('admin.messages_list'))


@admin_bp.route('/mensajes/delete-all-read', methods=['POST'])
@requires_admin
def messages_delete_all_read():
    """Eliminar todos los mensajes leídos"""
    deleted_count = ContactMessage.query.filter_by(read=True).delete()
    db.session.commit()

    flash(f'{deleted_count} mensajes leídos eliminados exitosamente', 'success')

    return redirect(url_for('admin.messages_list'))
