import pytest
from tipos_datos import (
    operaciones_basicas,
    convertir_tipos,
    manipular_lista,
    operar_conjuntos,
    contar_caracteres,
)


def test_operaciones_basicas():
    r = operaciones_basicas(10, 3)
    assert r["suma"] == 13
    assert r["resta"] == 7
    assert r["multiplicacion"] == 30
    assert r["division"] == pytest.approx(3.333, 0.001)
    assert r["modulo"] == 1


def test_operaciones_basicas_division_por_cero():
    r = operaciones_basicas(5, 0)
    assert r["division"] is None
    assert r["modulo"] is None


def test_convertir_tipos():
    r = convertir_tipos("42")
    assert r["int"] == 42
    assert r["float"] == 42.0
    assert r["str"] == "42"
    assert r["bool"] is True


def test_convertir_tipos_cero():
    r = convertir_tipos("0")
    assert r["bool"] is False


def test_manipular_lista():
    r = manipular_lista([3, 1, 4, 1, 5])
    assert r["primero"] == 3
    assert r["ultimo"] == 5
    assert r["reverso"] == [5, 1, 4, 1, 3]
    assert r["ordenado"] == [1, 1, 3, 4, 5]


def test_manipular_lista_vacia():
    r = manipular_lista([])
    assert r["primero"] is None
    assert r["ultimo"] is None
    assert r["reverso"] == []
    assert r["ordenado"] == []


def test_operar_conjuntos():
    r = operar_conjuntos({1, 2, 3}, {2, 3, 4})
    assert r["union"] == {1, 2, 3, 4}
    assert r["interseccion"] == {2, 3}
    assert r["diferencia"] == {1}
    assert r["diferencia_simetrica"] == {1, 4}


def test_contar_caracteres():
    assert contar_caracteres("abbccc") == {"a": 1, "b": 2, "c": 3}
