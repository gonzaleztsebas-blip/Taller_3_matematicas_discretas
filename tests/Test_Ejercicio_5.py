"""
Tests del ejercicio 5: impacto de cerrar un vertice o una arista.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "grafos"))

from Ejercicio_5 import grafo, dijkstra, cerrar_vertice, cerrar_arista, comparar_impacto


def test_cerrar_vertice_lo_elimina_del_grafo():
    grafo_sin_F = cerrar_vertice(grafo, "F")
    assert "F" not in grafo_sin_F
    # tampoco debe quedar ninguna arista que apunte a F
    for vecinos in grafo_sin_F.values():
        assert all(destino != "F" for destino, _ in vecinos)


def test_cerrar_arista_la_elimina_en_ambos_sentidos():
    grafo_sin_GK = cerrar_arista(grafo, "G", "K")
    assert all(v != "K" for v, _ in grafo_sin_GK["G"])
    assert all(v != "G" for v, _ in grafo_sin_GK["K"])
    # los nodos siguen existiendo, solo se quito la conexion
    assert "G" in grafo_sin_GK and "K" in grafo_sin_GK


def test_cerrar_arista_no_afecta_otras_conexiones():
    grafo_sin_GK = cerrar_arista(grafo, "G", "K")
    # G segui­a conectado con J antes del cierre, eso no deberia cambiar
    vecinos_de_G = [v for v, _ in grafo_sin_GK["G"]]
    assert "J" in vecinos_de_G


def test_comparar_impacto_detecta_desconexion():
    # aislar Q por completo para forzar un caso de "Desconectado"
    grafo_sin_Q = cerrar_vertice(grafo, "Q")
    reporte = comparar_impacto(grafo, grafo_sin_Q, [("A", "Q")])
    assert reporte[0]["estado"] == "Desconectado"
    assert reporte[0]["despues"] == float("inf")


def test_comparar_impacto_detecta_desconexion():
    # aislar Q por completo para forzar un caso de "Desconectado"
    grafo_sin_Q = cerrar_vertice(grafo, "Q")
    reporte = comparar_impacto(grafo, grafo_sin_Q, [("A", "Q")])
    assert reporte[0]["estado"] == "Desconectado"
    assert reporte[0]["despues"] == "inf"