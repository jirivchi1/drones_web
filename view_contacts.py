"""
Script para ver mensajes de contacto guardados en la base de datos
Ejecutar: python view_contacts.py
"""
import os
os.environ['FLASK_ENV'] = 'development'

from app import create_app, db
from app.models import ContactMessage
from datetime import datetime

app = create_app('development')

with app.app_context():
    # Obtener todos los mensajes
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()

    if not messages:
        print("\n❌ No hay mensajes de contacto guardados todavía.\n")
        print("Prueba enviando un formulario en: http://127.0.0.1:5000/contacto")
    else:
        print(f"\n📧 Total de mensajes: {len(messages)}\n")
        print("=" * 80)

        for msg in messages:
            # Formatear la fecha
            fecha = msg.created_at.strftime('%d/%m/%Y %H:%M:%S')

            # Estado de lectura
            estado = "✅ Leído" if msg.is_read else "📬 No leído"

            print(f"\nID: {msg.id} | {estado} | Fecha: {fecha}")
            print("-" * 80)
            print(f"👤 Nombre:     {msg.name}")
            print(f"📧 Email:      {msg.email}")
            print(f"📱 Teléfono:   {msg.phone or 'No proporcionado'}")
            print(f"🎯 Servicios:  {msg.service_types or 'No especificado'}")
            print(f"💬 Mensaje:")
            print(f"   {msg.message}")
            print("=" * 80)

        # Estadísticas
        no_leidos = ContactMessage.query.filter_by(is_read=False).count()
        print(f"\n📊 Estadísticas:")
        print(f"   Total: {len(messages)}")
        print(f"   No leídos: {no_leidos}")
        print(f"   Leídos: {len(messages) - no_leidos}\n")
