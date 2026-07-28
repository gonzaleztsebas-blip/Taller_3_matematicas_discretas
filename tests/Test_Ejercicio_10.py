"""
Tests del ejercicio 10: simulador basico de un qubit.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "cuantica"))

from Ejercicio_10 import aplicar_compuerta, calcular_probabilidades, simular_mediciones


def test_x_invierte_el_qubit():
    # caso obligatorio: X|0> = |1>
    assert aplicar_compuerta("X", [1, 0]) == [0, 1]


def test_h_produce_probabilidades_50_50():
    # caso obligatorio: H|0> da ~50% y ~50%
    estado = aplicar_compuerta("H", [1, 0])
    prob_0, prob_1 = calcular_probabilidades(estado)
    assert round(prob_0, 3) == 0.5
    assert round(prob_1, 3) == 0.5


def test_hh_recupera_el_estado_original():
    # caso obligatorio: HH|0> = |0>, salvo errores numericos pequeños
    estado_h = aplicar_compuerta("H", [1, 0])
    estado_hh = aplicar_compuerta("H", estado_h)
    assert abs(estado_hh[0] - 1) < 1e-9
    assert abs(estado_hh[1] - 0) < 1e-9


def test_z_deja_el_cero_intacto():
    assert aplicar_compuerta("Z", [1, 0]) == [1, 0]


def test_compuerta_desconocida_lanza_error():
    import pytest
    with pytest.raises(ValueError):
        aplicar_compuerta("Y", [1, 0])


def test_simular_mediciones_da_1000_resultados_en_total():
    conteo_0, conteo_1 = simular_mediciones(0.5, 0.5, 1000)
    assert conteo_0 + conteo_1 == 1000


def test_simular_mediciones_con_probabilidad_1_da_siempre_0():
    conteo_0, conteo_1 = simular_mediciones(1.0, 0.0, 500)
    assert conteo_0 == 500
    assert conteo_1 == 0