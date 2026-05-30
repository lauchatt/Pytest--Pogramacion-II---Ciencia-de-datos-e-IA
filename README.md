# Ejercicios Python - Nivel Bajo-Medio

Colección de ejercicios prácticos para practicar tipos de datos, estructuras
enlazadas, algoritmos de ordenamiento/búsqueda, operaciones funcionales y
procesamiento de texto.

## Estructura

```
ejercicios-python/
├── README.md
├── requirements.txt
├── data/
│   └── ejemplo.csv
├── 01_tipos_datos/         # int, float, str, bool, list, tuple, dict, set
├── 02_listas_ordenamiento/ # Bubble, Selection, Insertion, Merge Sort
├── 03_listas_enlazadas/    # Simple, doble, circular
├── 04_insercion/           # Inicio, final, n-posición, ordenado
├── 05_map_filter_zip/      # Map, filter, zip sobre CSV real
├── 06_busqueda/            # Lineal, binaria (iterativa y recursiva)
└── 07_texto_tokenizacion/  # Limpieza, puntuación, stopwords, tokenización
```

## Requisitos

- Python 3.10+
- pytest

## Instalación

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
# venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

## Ejecutar Tests

```bash
# Todos los ejercicios
pytest -v

# Ejercicio específico
pytest 01_tipos_datos/test_01_tipos_datos.py -v

# Con traza corta
pytest -v --tb=short

# Solo el nombre de test que coincida
pytest -v -k "test_busqueda_binaria"
```

## Resolución de ejercicios

Cada `ejercicio.py` contiene funciones con docstrings que describen lo que
debe hacer cada una. Completá las implementaciones y ejecutá los tests para
verificar. Los tests están en `test_ejercicio.py` dentro de cada módulo.
