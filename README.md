# UpFrames - Videografía Aérea Profesional

Aplicación web para mostrar videos profesionales de eventos capturados con drones.

## Características

- ✅ Hero interactivo con palabras dinámicas rotando
- ✅ Carrusel de videos con navegación fluida
- ✅ Diseño minimalista y limpio
- ✅ Responsive (móvil, tablet, desktop)
- ✅ Arquitectura MVC con Flask

## Estructura del Proyecto

```
dron_website/
├── app/
│   ├── controllers/      # Controladores (lógica de negocio)
│   ├── models/           # Modelos (datos)
│   ├── views/
│   │   ├── templates/    # Plantillas HTML
│   │   └── static/       # Archivos estáticos (CSS, JS, imágenes, videos)
│   └── __init__.py       # Inicialización de la app
├── requirements.txt      # Dependencias Python
├── run.py                # Punto de entrada
└── .env                  # Variables de entorno
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/jirivchi1/drones_web.git
cd drones_web
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar en Local

```bash
python run.py
```

La aplicación estará disponible en: **http://127.0.0.1:5000**

## Tecnologías

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Arquitectura:** MVC (Model-View-Controller)
- **Diseño:** Minimalista, inspirado en diseños modernos

## Funcionalidades Implementadas

### Hero Section
- Texto dinámico con palabras rotando cada 2.5 segundos
- Animaciones suaves con efectos bounce
- Botones de llamada a la acción
- Iconos de redes sociales (WhatsApp, Instagram, Facebook, YouTube)

### Galería de Videos
- Carrusel con 1 video a la vez (pantalla completa)
- Navegación con flechas izquierda/derecha
- Indicadores de posición (dots)
- Overlay informativo al hacer hover
- Bordes difuminados para integración suave
- **Carga dinámica desde base de datos**
- Filtrado por categorías con botones animados

### Testimonios
- Scroll infinito con múltiples columnas
- Diseño responsive (1/2/3 columnas según dispositivo)
- **Carga dinámica desde base de datos**

### Formulario de Contacto
- Diseño minimalista con animaciones
- Validación de campos con Flask-WTF
- Protección CSRF
- Almacenamiento en base de datos SQLite
- Notificaciones por email (Gmail/SMTP)

### Panel de Administración
- Vista de todos los mensajes de contacto
- **Búsqueda** por nombre, email o contenido
- **Filtrado** por estado (leído/no leído)
- **Marcar como leído/no leído**
- **Eliminar mensajes**
- Estadísticas (total, leídos, no leídos)
- Interfaz moderna con gradientes

### Base de Datos y Modelos
- SQLAlchemy ORM con SQLite
- Modelos: ContactMessage, Video, Testimonial
- Migraciones con Flask-Migrate
- Script para poblar datos iniciales

### Sistema de Email
- Flask-Mail configurado
- Soporte para Gmail, SendGrid, SMTP personalizado
- Notificaciones automáticas al admin
- Manejo robusto de errores

### Sistema de Logging
- Logs rotativos (10MB máx, 10 backups)
- Niveles: INFO (app.log), ERROR (error.log)
- Logging en todas las operaciones críticas

### Testing
- Suite de tests con pytest
- 17 tests (unitarios e integración)
- 85% de cobertura de código
- Tests de modelos, rutas, formularios

### Seguridad
- CSRF protection en todos los formularios
- Validación de inputs
- Manejo seguro de errores
- Páginas de error personalizadas (404, 500)

## Configuración Inicial

### 1. Base de Datos

```bash
# Inicializar migraciones
flask db init

# Crear migración
flask db migrate -m "Initial migration"

# Aplicar migración
flask db upgrade

# Poblar base de datos con datos iniciales
python populate_db.py
```

### 2. Configurar Email (Opcional)

Para recibir notificaciones por email, sigue la guía en:
```
docs/EMAIL_SETUP.md
```

Prueba tu configuración:
```bash
python test_email.py
```

### 3. Tests

```bash
# Ejecutar todos los tests
pytest

# Con reporte de cobertura
pytest --cov=app --cov-report=html

# Ver reporte HTML
# Abre: htmlcov/index.html
```

## Rutas Disponibles

- `/` - Página principal
- `/contacto` - Formulario de contacto
- `/admin/mensajes` - Panel de administración (mensajes)

## Próximas Características

- [ ] Autenticación para panel de admin
- [ ] Subida de videos desde el panel de admin
- [ ] Gestión de testimonios desde el panel
- [ ] Sistema de categorías dinámico
- [ ] Optimización SEO
- [ ] Analytics y métricas

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto es privado y pertenece a UpFrames.

---

**Desarrollado con ❤️ para UpFrames**
