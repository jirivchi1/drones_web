# 🎛️ Panel de Administración Completo - UpFrames

## 🚀 Acceso al Panel

1. **URLs del panel admin:**
   - **Gestión de Videos:** `http://localhost:5000/admin/videos`
   - **Gestión de Mensajes:** `http://localhost:5000/admin/mensajes`

2. **Credenciales de acceso:**
   - **Usuario:** `admin`
   - **Contraseña:** Configurada en la variable `ADMIN_PASSWORD` (por defecto: `admin123`)

3. **Cómo cambiar la contraseña:**
   - Edita el archivo `.env` y añade:
     ```
     ADMIN_PASSWORD=tu_contraseña_segura
     ```
   - O modifica `config.py` directamente

**Importante:** Ambos paneles (videos y mensajes) usan la misma autenticación

## 🎬 Funcionalidades del Panel

### 1. Ver Lista de Videos
- Muestra todos los videos subidos
- Cada video muestra:
  - Título
  - Categoría/Botón
  - Nombre del archivo
  - Orden de aparición

### 2. Subir Nuevo Video

**Pasos:**
1. Click en "➕ Subir Nuevo Video"
2. Rellena el formulario:
   - **Título:** Nombre descriptivo del video (ej: "Deportivo - Audi A4")
   - **Categoría/Botón:** Texto que aparecerá en el botón (ej: "Deportivo")
   - **Descripción:** (Opcional) Texto adicional que aparece bajo el título
   - **Archivo de Video:** Selecciona tu video (.mp4, .mov, .avi, .webm)
3. Click en "⬆️ Subir Video"

**Notas importantes:**
- Tamaño máximo: 500 MB
- Formatos soportados: MP4, MOV, AVI, WEBM
- El archivo se guardará en `app/views/static/videos/`
- Puedes arrastrar y soltar el archivo en la zona de carga

### 3. Editar Video

**Pasos:**
1. En la lista de videos, click en "✏️ Editar"
2. Modifica los campos que desees:
   - Título
   - Categoría/Botón
   - Descripción
   - Archivo de video (opcional - solo si quieres reemplazarlo)
3. Click en "💾 Guardar Cambios"

### 4. Eliminar Video

**Pasos:**
1. En la lista de videos, click en "🗑️ Eliminar"
2. Confirma la eliminación
3. El archivo se eliminará del servidor y de la base de datos

### 5. Cambiar Orden de Videos

**Pasos:**
- Usa los botones "↑" (subir) y "↓" (bajar) para cambiar el orden
- El orden determina en qué posición aparece el video en el carrusel
- El primer video (orden 0) será el que se muestre por defecto

## 🔄 Cómo se Muestran los Videos en la Web

1. **Botón de Categoría:**
   - El texto del campo "Categoría" se usa como nombre del botón
   - Cada video genera un botón automáticamente
   - Ejemplo: Si pones "Deportivo" → aparecerá un botón "Deportivo"

2. **Carrusel de Videos:**
   - Los videos se muestran en el orden que configuraste
   - Al hacer click en un botón, se muestra el video correspondiente
   - Los usuarios pueden hacer click en el video para reproducirlo

3. **Sincronización Automática:**
   - Los cambios se reflejan inmediatamente en la web
   - No necesitas reiniciar el servidor
   - Solo recarga la página de inicio para ver los cambios

## 🎯 Ejemplo de Uso

### Caso: Añadir un nuevo video de "Bodas"

1. Ve a `/admin/videos`
2. Click en "Subir Nuevo Video"
3. Rellena:
   - **Título:** "Bodas - María & Carlos"
   - **Categoría:** "Bodas"
   - **Descripción:** "Videografía aérea profesional de bodas inolvidables"
   - **Archivo:** Selecciona `boda_maria_carlos.mp4`
4. Click en "Subir Video"
5. El video aparecerá con un botón "Bodas" en la sección de trabajos

## 🛡️ Seguridad

⚠️ **IMPORTANTE PARA PRODUCCIÓN:**

1. **Cambia la contraseña por defecto** antes de subir a producción
2. **Usa HTTPS** en producción para proteger las credenciales
3. **Considera implementar** un sistema de login más robusto (Flask-Login)
4. **Limita el acceso** al panel admin solo a IPs autorizadas (opcional)

## 📝 Notas Adicionales

- **Capacidad de almacenamiento:** Asegúrate de tener suficiente espacio en disco
- **Formato recomendado:** MP4 con codec H.264 para máxima compatibilidad
- **Compresión:** Usa herramientas como Handbrake para optimizar el tamaño sin perder calidad
- **Nombres de archivo:** Se sanitizan automáticamente para evitar conflictos
- **Duplicados:** Si subes un archivo con el mismo nombre, se añade un número al final

## 🔧 Troubleshooting

### El panel no carga
- Verifica que el servidor Flask esté corriendo
- Comprueba que la ruta sea correcta: `/admin/videos`

### No puedo subir videos grandes
- Aumenta `MAX_CONTENT_LENGTH` en `config.py`
- Verifica límites de tu servidor web (Nginx, Apache)

### El video no se muestra en la web
- Verifica que el archivo se guardó en `static/videos/`
- Comprueba que el formato sea compatible (MP4 recomendado)
- Limpia caché del navegador

### Olvidé la contraseña de admin
- Edita `.env` o `config.py` para establecer una nueva
- Reinicia el servidor Flask

---

# 📧 Gestión de Mensajes de Contacto

## 📋 Acceso al Panel de Mensajes

**URL:** `http://localhost:5000/admin/mensajes`

Este panel te permite gestionar todos los mensajes recibidos a través del formulario de contacto.

## 🎯 Funcionalidades

### 1. Ver Lista de Mensajes

- Muestra todos los mensajes ordenados por fecha (más recientes primero)
- Cada mensaje muestra:
  - ✉️ **Nombre** y **email** del remitente
  - 📅 **Fecha y hora** de recepción
  - 💬 **Mensaje** completo
  - 📱 **Teléfono** (si lo proporcionó)
  - 🎯 **Servicios de interés** seleccionados
  - ● **Estado** (Nuevo/Leído)

### 2. Filtrar Mensajes

**Opciones de filtro:**
- **📋 Todos:** Muestra todos los mensajes
- **🔵 No leídos:** Solo mensajes nuevos sin leer
- **✅ Leídos:** Solo mensajes ya revisados

### 3. Marcar como Leído/No Leído

**Individual:**
1. En cada mensaje, click en "✓ Marcar como leído"
2. Para desmarcar: "📖 Marcar como no leído"

**Masivo:**
- Botón "✓ Marcar todos como leídos" en la parte superior
- Marca todos los mensajes del filtro actual

### 4. Responder Mensajes

**Pasos:**
1. Click en "📨 Responder por email" en cualquier mensaje
2. Se abre tu cliente de email predeterminado
3. El email del remitente se rellena automáticamente
4. Escribe tu respuesta y envía

### 5. Eliminar Mensajes

**Individual:**
1. Click en "🗑️ Eliminar" en el mensaje
2. Confirma la eliminación
3. El mensaje se borra permanentemente

**Masivo (solo leídos):**
1. Click en "🗑️ Eliminar leídos" en la parte superior
2. Confirma la acción
3. Se eliminan todos los mensajes marcados como leídos

## 💡 Contador de Mensajes Nuevos

- En el título aparece un **badge rojo** con el número de mensajes no leídos
- Ejemplo: "📧 Mensajes de Contacto **[5 nuevos]**"
- Se actualiza automáticamente al marcar mensajes

## 🎨 Indicadores Visuales

### Mensajes No Leídos
- Fondo azul claro
- Barra azul en el lateral izquierdo
- Badge "● Nuevo"

### Mensajes Leídos
- Fondo blanco
- Badge "✓ Leído" en verde

## 🔄 Flujo de Trabajo Recomendado

1. **Revisión diaria:**
   - Entra a `/admin/mensajes`
   - Filtra por "🔵 No leídos"
   - Revisa cada mensaje

2. **Procesamiento:**
   - Lee el mensaje completo
   - Responde si es necesario usando "📨 Responder por email"
   - Marca como leído

3. **Limpieza periódica:**
   - Una vez respondidos, los mensajes se pueden eliminar
   - Usa "🗑️ Eliminar leídos" para limpiar en bloque

## 📊 Información Capturada

Cada mensaje contiene:

1. **Datos del remitente:**
   - Nombre completo
   - Email de contacto
   - Teléfono (opcional)

2. **Mensaje:**
   - Texto libre del cliente
   - Consultas, solicitudes, etc.

3. **Servicios de interés:**
   - Bodas
   - Eventos
   - Inmobiliaria
   - Comercial
   - Naturaleza
   - Deportivo

4. **Metadatos:**
   - Fecha y hora de envío
   - Estado (leído/no leído)

## 🔗 Navegación entre Paneles

Desde el panel de mensajes:
- Click en "🎥 Gestionar Videos" para ir al panel de videos

Desde el panel de videos:
- Cambia la URL a `/admin/mensajes`

## 🛡️ Seguridad

- **Misma autenticación** que el panel de videos
- **CRUD completo:** Create (a través del formulario público), Read, Update (estado), Delete
- **Sin exposición de datos sensibles:** Los mensajes solo son accesibles con credenciales de admin

---

## 📞 Soporte

Si tienes problemas o preguntas, revisa:
1. Los logs de Flask en la consola
2. El archivo `logs/app.log`
3. La documentación de Flask en https://flask.palletsprojects.com/
