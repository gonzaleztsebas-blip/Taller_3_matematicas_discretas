"""
Tests del ejercicio 3: MPC basico (suma secreta con 3 servidores).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "cripto"))

from Ejercicio_3 import dividir_y_reconstruir


def test_ejemplo_del_enunciado():
    # notas [40,35,50,25] -> suma 150, promedio 37.5
    suma, promedio = dividir_y_reconstruir([40, 35, 50, 25])
    assert suma == 150
    assert promedio == 37.5


def test_reconstruccion_correcta_repetida():
    # como las partes son aleatorias, se corre varias veces para
    # confirmar que la suma siempre se reconstruye bien
    for _ in range(20):
        suma, promedio = dividir_y_reconstruir([10, 20, 30])
        assert suma == 60
        assert promedio == 20.0


def test_una_sola_nota():
    suma, promedio = dividir_y_reconstruir([50])
    assert suma == 50
    assert promedio == 50.0


def test_promedio_con_lista_de_tamano_variable():
    numeros = [1, 2, 3, 4, 5, 6, 7]
    suma, promedio = dividir_y_reconstruir(numeros)
    assert suma == sum(numeros)
    assert promedio == sum(numeros) / len(numeros)