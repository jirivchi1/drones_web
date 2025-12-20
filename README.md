# Videos con Drones

Aplicaci\u00f3n web para mostrar videos profesionales de eventos capturados con drones.

## Estructura del Proyecto (MVC)

```
dron_website/
\u251c\u2500\u2500 app/
\u2502   \u251c\u2500\u2500 controllers/      # Controladores (l\u00f3gica de negocio)
\u2502   \u251c\u2500\u2500 models/           # Modelos (datos)
\u2502   \u251c\u2500\u2500 views/
\u2502   \u2502   \u251c\u2500\u2500 templates/    # Plantillas HTML
\u2502   \u2502   \u2514\u2500\u2500 static/       # Archivos est\u00e1ticos (CSS, JS, im\u00e1genes)
\u2502   \u2514\u2500\u2500 __init__.py       # Inicializaci\u00f3n de la app
\u251c\u2500\u2500 requirements.txt       # Dependencias
\u251c\u2500\u2500 run.py                 # Punto de entrada
\u2514\u2500\u2500 .env                   # Variables de entorno
```

## Instalaci\u00f3n

1. Crear entorno virtual:
```bash
python -m venv venv
```

2. Activar entorno virtual:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar en Local

```bash
python run.py
```

La aplicaci\u00f3n estar\u00e1 disponible en: http://127.0.0.1:5000

## Pr\u00f3ximos Pasos

- [ ] A\u00f1adir galer\u00eda de videos
- [ ] Integrar logo existente
- [ ] Mejorar dise\u00f1o responsive
