"""
Tests del ejercicio 4: ruta mas corta (Dijkstra).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "grafos"))

from Ejercicio_4 import grafo, dijkstra


def test_grafo_cumple_tamano_minimo():
    # el enunciado pide minimo 8 vertices y 12 aristas
    num_vertices = len(grafo)
    num_aristas = sum(len(vecinos) for vecinos in grafo.values()) // 2
    assert num_vertices >= 8
    assert num_aristas >= 12


def test_ruta_directa_con_arista_unica():
    # A-Q tiene una arista directa de peso 2, y no hay atajo mas corto
    ruta, distancia = dijkstra(grafo, "A", "Q")
    assert ruta[0] == "A"
    assert ruta[-1] == "Q"
    assert distancia == 2


def test_ruta_de_un_nodo_a_si_mismo():
    ruta, distancia = dijkstra(grafo, "A", "A")
    assert ruta == ["A"]
    assert distancia == 0


def test_distancia_coincide_con_suma_de_pesos_de_la_ruta():
    # verifica que la ruta devuelta realmente sume la distancia reportada
    ruta, distancia = dijkstra(grafo, "A", "P")
    pesos = {n: dict(vecinos) for n, vecinos in grafo.items()}
    suma = sum(pesos[ruta[i]][ruta[i + 1]] for i in range(len(ruta) - 1))
    assert suma == distancia


def test_nodo_inalcanzable_devuelve_none():
    # se agrega un nodo aislado para probar el caso de "no existe camino"
    grafo_con_aislado = dict(grafo)
    grafo_con_aislado["Z"] = []
    ruta, distancia = dijkstra(grafo_con_aislado, "A", "Z")
    assert ruta is None
    assert distancia == float("inf")