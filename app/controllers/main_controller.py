from flask import Blueprint, render_template, request, flash, redirect, url_for

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        service_types = request.form.getlist('service_type')

        # Aquí puedes agregar la lógica para enviar email o guardar en base de datos
        # Por ahora solo imprimimos en consola
        print(f"Nuevo mensaje de contacto:")
        print(f"Nombre: {name}")
        print(f"Email: {email}")
        print(f"Teléfono: {phone}")
        print(f"Mensaje: {message}")
        print(f"Servicios: {', '.join(service_types)}")

        flash('¡Gracias por tu mensaje! Te contactaremos pronto.', 'success')
        return redirect(url_for('main.contact'))

    return render_template('contact.html')
