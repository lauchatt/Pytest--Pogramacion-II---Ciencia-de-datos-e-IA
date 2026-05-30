"""
Ejercicio 7: Manipulación y Limpieza de Texto
Limpieza, normalización y tokenización paso a paso.
"""
import re
from typing import List


def limpiar_texto(texto: str) -> str:
    """
    Paso 1: Limpieza básica.
    - Convierte a minúsculas
    - Elimina saltos de línea y tabs
    - Normaliza espacios múltiples
    """
    texto = texto.lower()  # ← add this
    texto = texto.replace("\n", " ").replace("\t", " ")
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def eliminar_puntuacion(texto: str) -> str:
    """
    Paso 2: Elimina signos de puntuación.
    - Mantiene guiones dentro de palabras
    - Usa regex para eliminar todo lo que no sea palabra/espacio/guion
    """
    texto = re.sub(r"[^\w\s-]", "", texto)  
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def eliminar_stopwords(tokens: List[str], idioma: str = "es") -> List[str]:
    """
    Paso 3: Elimina stopwords del texto.
    Incluye conjunto básico en español (e inglés por compatibilidad).
    """
    stopwords = {
        "de", "la", "que", "el", "en", "y", "a", "los", "del", "se",
        "las", "por", "un", "para", "con", "no", "una", "su", "al",
        "lo", "como", "más", "pero", "sus", "le", "ya", "o", "este",
        "si", "porque", "entre", "cuando", "muy", "sin", "sobre",
        "también", "me", "hasta", "hay", "donde", "quien", "todo", "nada",
        "cada", "seguir", "menos", "mucho", "ahora", "siempre", "ser",
        "es", "son", "era", "fue", "ha", "han", "había", "he", "has",
        "haber", "está", "están", "estaba", "estado", "tener", "tiene",
        "tenía", "hacer", "hace", "hacía", "poder", "puede", "podía",
        "poner", "pone", "debe", "deber", "dice", "dijo", "sido",
        "eso", "esa", "ese", "estos", "estas", "esto",
        "él", "ella", "ellos", "nos", "os", "les", "te", "le",
        "mis", "tus", "sus", "mi", "tu", "yo", "tú",
        "nosotros", "vosotros", "ellas",
        "i", "a", "an", "the", "and", "or", "but", "in", "on", "at",
        "to", "for", "of", "with", "by", "from", "up", "about", "into",
        "over", "after", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will",
        "would", "could", "should", "may", "might", "shall", "can",
    }
    return [token for token in tokens if token not in stopwords]


def tokenizar(texto: str) -> List[str]:
    """
    Paso 4: Tokenización.
    Divide el texto en tokens (palabras) usando espacios como separador.
    """
    return texto.split()


def normalizar_texto(texto: str) -> str:
    """Aplica limpieza + eliminación de puntuación. Texto listo para
    tokenizar."""
    texto = limpiar_texto(texto)
    texto = eliminar_puntuacion(texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def pipeline_tokenizacion(texto: str, eliminar_stop: bool = True) -> List[str]:
    """
    Pipeline completa de tokenización:
    1. Limpiar texto (minúsculas, espacios)
    2. Eliminar puntuación
    3. Tokenizar (split por espacios)
    4. Eliminar stopwords (opcional)
    """
    texto = normalizar_texto(texto)
    tokens = tokenizar(texto)
    if eliminar_stop:
        tokens = eliminar_stopwords(tokens)
    return tokens


def descripcion_pipeline() -> str:
    """Retorna descripción del paso a paso de tokenización."""
    return """=== PIPELINE DE TOKENIZACIÓN ===

    Paso 1 - Limpieza básica:
    - Convertir a minúsculas (unificación)
    - Eliminar saltos de línea y tabs
    - Normalizar espacios múltiples

    Paso 2 - Eliminar puntuación:
    - Remover signos de puntuación (. , ! ? : ; " ' ¿ ¡ etc.)
    - Mantener guiones dentro de palabras (opcional)
    - Usar regex [^\\w\\s-] para limpieza

    Paso 3 - Tokenización:
    - Dividir el texto en tokens usando split() por espacios
    - Cada token es una palabra individual

    Paso 4 - Eliminar stopwords:
    - Remover palabras vacías sin significado semántico
    - Ej: artículos, preposiciones, pronombres
    - Reduce ruido en análisis posteriores

    Paso 5 (Opcional) - Stemming/Lematización:
    - Reducir palabras a su raíz morfológica
    - Ej: "corriendo", "corrí", "correrán" → "corr"
    - No implementado en este ejercicio
    """
