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

### Galería de Videos
- Carrusel con 1 video a la vez (pantalla completa)
- Navegación con flechas izquierda/derecha
- Indicadores de posición (dots)
- Overlay informativo al hacer hover
- Bordes difuminados para integración suave

## Próximas Características

- [ ] Formulario de contacto
- [ ] Página de servicios
- [ ] Integración con backend para gestión de videos
- [ ] Sistema de administración
- [ ] Optimización SEO

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
