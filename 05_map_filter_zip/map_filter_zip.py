"""
Ejercicio 5: Map, Filter, Zip
Operaciones funcionales sobre datos de un CSV de estudiantes.
"""
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CSV_PATH = DATA_DIR / "ejemplo.csv"


def leer_csv(ruta: str = None) -> list[dict]:
    """Lee el CSV y retorna lista de diccionarios."""
    ruta = ruta or str(CSV_PATH)
    with open(ruta, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def obtener_edades(datos: list[dict]) -> list[int]:
    """Usa map para extraer las edades."""
    return list(map(lambda x: int(x["edad"]), datos))


def filtrar_aprobados(datos: list[dict], nota_minima: float = 6.0) -> list[dict]:
    """Usa filter para obtener estudiantes con calificación >= nota_minima."""
    return list(filter(lambda x: float(x["calificacion"]) > nota_minima, datos))


def calcular_promedio_edades(datos: list[dict]) -> float:
    """Calcula el promedio de edades usando map."""
    edades = obtener_edades(datos)
    return sum(edades) / len(edades) if edades else 0.0


def emparejar_nombres_edades(datos: list[dict]) -> list[tuple]:
    """Usa zip para emparejar nombres y edades en tuplas."""
    nombres = list(map(lambda x: x["nombre"], datos))
    edades = obtener_edades(datos)
    return list(zip(nombres, edades))


def alumnos_a_mayuscula(datos: list[dict]) -> list[str]:
    """Usa map para convertir nombres a mayúsculas."""
    return list(map(lambda x: x["nombre"].upper(), datos))


def filtrar_por_ciudad(datos: list[dict], ciudad: str) -> list[dict]:
    """Usa filter para obtener estudiantes de una ciudad."""
    return []


def mejores_estudiantes(datos: list[dict], top_n: int = 3) -> list[tuple]:
    """Retorna top_n estudiantes (nombre, calificación) combinando sorted,
    map y zip."""
    ordenados = sorted(
        datos, key=lambda x: float(x["calificacion"]), reverse=True
    )
    nombres = list(map(lambda x: x["nombre"], ordenados[:top_n]))
    califs = list(map(lambda x: float(x["calificacion"]), ordenados[:top_n]))
    return list(zip(nombres, califs))
