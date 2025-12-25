# Configuración de Envío de Emails

Esta guía te ayudará a configurar el envío de emails para notificaciones del formulario de contacto.

## Opción 1: Gmail (Recomendado para desarrollo y pequeños proyectos)

### Paso 1: Habilitar la verificación en dos pasos

1. Ve a tu cuenta de Google: https://myaccount.google.com/
2. Navega a **Seguridad**
3. Habilita la **Verificación en dos pasos**

### Paso 2: Generar una contraseña de aplicación

1. Una vez habilitada la verificación en dos pasos, ve a: https://myaccount.google.com/apppasswords
2. Selecciona **App**: "Correo"
3. Selecciona **Dispositivo**: "Otro (nombre personalizado)"
4. Escribe: "UpFrames Website"
5. Haz clic en **Generar**
6. **Copia la contraseña de 16 caracteres** que aparece

### Paso 3: Configurar las variables de entorno

Edita el archivo `.env` en la raíz del proyecto:

```env
# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=tu-email@gmail.com
MAIL_PASSWORD=xxxx xxxx xxxx xxxx    # La contraseña de aplicación generada
MAIL_DEFAULT_SENDER=tu-email@gmail.com
ADMIN_EMAIL=tu-email@gmail.com       # Email donde recibirás las notificaciones
```

### Paso 4: Reinicia la aplicación

```bash
# Detén la aplicación si está corriendo
# Vuelve a ejecutar:
flask run
```

## Opción 2: Servidor SMTP Personalizado

Si tienes tu propio servidor SMTP o usas otro proveedor (como SendGrid, Mailgun, etc.):

```env
MAIL_SERVER=smtp.tu-servidor.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=tu-usuario
MAIL_PASSWORD=tu-contraseña
MAIL_DEFAULT_SENDER=noreply@tudominio.com
ADMIN_EMAIL=admin@tudominio.com
```

## Opción 3: SendGrid (Recomendado para producción)

### Paso 1: Crear cuenta en SendGrid

1. Ve a https://sendgrid.com/
2. Crea una cuenta gratuita (100 emails/día gratis)

### Paso 2: Generar API Key

1. Ve a **Settings > API Keys**
2. Crea una nueva API Key con permisos de "Mail Send"
3. Copia la API Key

### Paso 3: Configurar variables de entorno

```env
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=apikey
MAIL_PASSWORD=SG.xxxxxxxxxxxxxx    # Tu API Key de SendGrid
MAIL_DEFAULT_SENDER=noreply@tudominio.com
ADMIN_EMAIL=admin@tudominio.com
```

## Verificar que funciona

1. Reinicia tu aplicación Flask
2. Ve a http://localhost:5000/contacto
3. Envía un mensaje de prueba
4. Revisa:
   - Los logs en `logs/app.log` para confirmar que el email se envió
   - Tu bandeja de entrada del email configurado en `ADMIN_EMAIL`

## Solución de problemas

### Error: "SMTPAuthenticationError"
- Verifica que tu contraseña de aplicación esté correcta
- Asegúrate de que la verificación en dos pasos esté habilitada
- Prueba generar una nueva contraseña de aplicación

### Error: "Connection refused"
- Verifica que el puerto sea correcto (587 para TLS)
- Comprueba que `MAIL_USE_TLS=true`
- Asegúrate de tener conexión a internet

### Los emails no llegan
- Revisa la carpeta de spam
- Verifica que `ADMIN_EMAIL` esté configurado correctamente
- Comprueba los logs en `logs/app.log` para ver errores

### Error: "SMTPServerDisconnected"
- Puede ser que Gmail bloquee el acceso. Intenta:
  1. Visitar: https://accounts.google.com/DisplayUnlockCaptcha
  2. Permitir aplicaciones menos seguras (no recomendado)
  3. Usar SendGrid en su lugar

## Modo de desarrollo sin email

Si no quieres configurar email en desarrollo, el sistema seguirá funcionando:

- Los mensajes se guardarán en la base de datos
- Verás un warning en los logs indicando que el email no se envió
- Podrás ver los mensajes en http://localhost:5000/admin/mensajes

## Recomendaciones para producción

1. **Usa un servicio profesional** como SendGrid, Mailgun, o Amazon SES
2. **Configura SPF, DKIM y DMARC** para tu dominio
3. **Usa variables de entorno** seguras (no las pongas en el código)
4. **Monitorea los emails enviados** para detectar problemas
5. **Implementa rate limiting** para prevenir spam
6. **Usa plantillas HTML** para emails más profesionales

## Plantilla de Email Actual

El sistema envía un email con el siguiente formato:

- **Asunto**: "Nuevo mensaje de contacto - [Nombre del Cliente]"
- **Contenido**:
  - Nombre del cliente
  - Email del cliente
  - Teléfono (si se proporcionó)
  - Servicios solicitados (si se seleccionaron)
  - Mensaje completo

El email se envía desde `MAIL_DEFAULT_SENDER` a `ADMIN_EMAIL`.
