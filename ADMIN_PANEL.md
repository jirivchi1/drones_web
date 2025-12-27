# 📹 Panel de Administración de Videos - UpFrames

## 🚀 Acceso al Panel

1. **URL del panel admin:** `http://localhost:5000/admin/videos`

2. **Credenciales de acceso:**
   - **Usuario:** `admin`
   - **Contraseña:** Configurada en la variable `ADMIN_PASSWORD` (por defecto: `admin123`)

3. **Cómo cambiar la contraseña:**
   - Edita el archivo `.env` y añade:
     ```
     ADMIN_PASSWORD=tu_contraseña_segura
     ```
   - O modifica `config.py` directamente

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

## 📞 Soporte

Si tienes problemas o preguntas, revisa:
1. Los logs de Flask en la consola
2. El archivo `logs/app.log`
3. La documentación de Flask en https://flask.palletsprojects.com/
