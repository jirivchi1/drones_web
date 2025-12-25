# Tests

Este directorio contiene los tests para la aplicación UpFrames.

## Estructura

```
tests/
├── __init__.py
├── conftest.py          # Configuración de pytest y fixtures
├── test_models.py       # Tests unitarios para modelos
├── test_routes.py       # Tests de integración para rutas
└── README.md           # Este archivo
```

## Ejecutar los Tests

### Todos los tests

```bash
pytest
```

### Con reporte de cobertura

```bash
pytest --cov=app --cov-report=html
```

### Solo tests unitarios

```bash
pytest tests/test_models.py
```

### Solo tests de integración

```bash
pytest tests/test_routes.py
```

### Ver reporte HTML de cobertura

```bash
pytest --cov=app --cov-report=html
# Luego abre: htmlcov/index.html
```

### Modo verbose

```bash
pytest -v
```

### Ver print statements

```bash
pytest -s
```

## Fixtures Disponibles

- `app`: Aplicación Flask configurada para testing
- `client`: Cliente de testing de Flask
- `database`: Base de datos de prueba
- `sample_contact_message`: Mensaje de contacto de ejemplo
- `sample_video`: Video de ejemplo

## Ejemplo de Uso

```python
def test_example(client, database):
    """Test de ejemplo"""
    response = client.get('/')
    assert response.status_code == 200
```
