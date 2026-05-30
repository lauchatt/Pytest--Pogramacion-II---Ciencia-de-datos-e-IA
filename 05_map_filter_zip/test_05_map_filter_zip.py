import pytest
from map_filter_zip import (
    leer_csv,
    obtener_edades,
    filtrar_aprobados,
    calcular_promedio_edades,
    emparejar_nombres_edades,
    alumnos_a_mayuscula,
    filtrar_por_ciudad,
    mejores_estudiantes,
)


@pytest.fixture
def datos():
    return leer_csv()


def test_leer_csv(datos):
    assert len(datos) > 0
    assert all(k in datos[0] for k in ("nombre", "edad", "calificacion", "ciudad"))


def test_obtener_edades(datos):
    edades = obtener_edades(datos)
    assert all(isinstance(e, int) for e in edades)
    assert len(edades) == len(datos)


def test_filtrar_aprobados(datos):
    aprobados = filtrar_aprobados(datos)
    for a in aprobados:
        assert float(a["calificacion"]) >= 6.0


def test_filtrar_aprobados_nota_personalizada(datos):
    aprobados = filtrar_aprobados(datos, 8.0)
    for a in aprobados:
        assert float(a["calificacion"]) >= 8.0


def test_calcular_promedio_edades(datos):
    promedio = calcular_promedio_edades(datos)
    assert 15 <= promedio <= 30


def test_emparejar_nombres_edades(datos):
    pares = emparejar_nombres_edades(datos)
    for nombre, edad in pares:
        assert isinstance(nombre, str)
        assert isinstance(edad, int)


def test_alumnos_a_mayuscula(datos):
    nombres = alumnos_a_mayuscula(datos)
    assert all(n == n.upper() for n in nombres)


def test_filtrar_por_ciudad(datos):
    madrilenos = filtrar_por_ciudad(datos, "Madrid")
    for m in madrilenos:
        assert m["ciudad"].lower() == "madrid"


def test_mejores_estudiantes(datos):
    top = mejores_estudiantes(datos, 3)
    assert len(top) == 3
    califs = [c for _, c in top]
    assert califs == sorted(califs, reverse=True)
