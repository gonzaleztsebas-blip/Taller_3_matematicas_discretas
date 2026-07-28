"""
Tests del ejercicio 6: coloreo de grafos (algoritmo voraz).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "grafos"))

from Ejercicio_6 import grafo, coloreo_voraz, verificar_colores


def test_grafo_cumple_tamano_minimo():
    # el enunciado pide minimo 10 vertices
    assert len(grafo) >= 10


def test_coloreo_es_valido():
    colores = coloreo_voraz(grafo)
    assert verificar_colores(grafo, colores) is True


def test_todos_los_nodos_tienen_color():
    colores = coloreo_voraz(grafo)
    assert set(colores.keys()) == set(grafo.keys())


def test_verificar_colores_detecta_coloreo_invalido():
    # se fuerza un coloreo malo: todos con el mismo color
    colores_malos = {nodo: 0 for nodo in grafo}
    assert verificar_colores(grafo, colores_malos) is False


def test_numero_de_colores_es_razonable():
    # con este grafo el voraz deberia usar pocos colores, nunca uno
    # por cada nodo (eso significaria que todos son vecinos entre si)
    colores = coloreo_voraz(grafo)
    num_colores = len(set(colores.values()))
    assert 1 < num_colores < len(grafo)