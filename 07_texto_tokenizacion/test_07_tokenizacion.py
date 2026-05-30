import pytest
from texto_tokenizacion import (
    limpiar_texto,
    eliminar_puntuacion,
    eliminar_stopwords,
    tokenizar,
    normalizar_texto,
    pipeline_tokenizacion,
    descripcion_pipeline,
)


def test_limpiar_texto():
    texto = "  Hola  Mundo\nEsto es\tuna prueba  "
    resultado = limpiar_texto(texto)
    assert resultado == "hola mundo esto es una prueba"
    assert resultado.islower()


def test_eliminar_puntuacion():
    texto = "¡Hola, mundo! ¿Cómo estás?"
    resultado = eliminar_puntuacion(texto)
    assert "¡" not in resultado
    assert "," not in resultado
    assert "¿" not in resultado
    assert resultado == "Hola mundo Cómo estás"


def test_eliminar_stopwords():
    tokens = ["este", "es", "un", "ejemplo", "de", "texto"]
    resultado = eliminar_stopwords(tokens)
    assert resultado == ["ejemplo", "texto"]


def test_tokenizar():
    texto = "hola mundo python"
    resultado = tokenizar(texto)
    assert resultado == ["hola", "mundo", "python"]


def test_normalizar_texto():
    texto = "  ¡Hola,  Mundo!  \n"
    resultado = normalizar_texto(texto)
    assert resultado == "hola mundo"


def test_pipeline_tokenizacion_completo():
    texto = "Este es un ejemplo de texto para tokenización."
    resultado = pipeline_tokenizacion(texto, eliminar_stop=True)
    assert "este" not in resultado
    assert "es" not in resultado
    assert "un" not in resultado
    assert "de" not in resultado
    assert "ejemplo" in resultado
    assert "texto" in resultado
    assert "tokenización" in resultado


def test_pipeline_tokenizacion_sin_stopwords():
    texto = "Hola mundo python"
    resultado = pipeline_tokenizacion(texto, eliminar_stop=False)
    assert resultado == ["hola", "mundo", "python"]


def test_texto_vacio():
    assert pipeline_tokenizacion("") == []
    assert normalizar_texto("") == ""
    assert tokenizar("") == []
    assert limpiar_texto("   ") == ""


def test_descripcion_pipeline():
    desc = descripcion_pipeline()
    assert "Paso 1" in desc
    assert "Paso 2" in desc
    assert "Paso 3" in desc
    assert "Paso 4" in desc
