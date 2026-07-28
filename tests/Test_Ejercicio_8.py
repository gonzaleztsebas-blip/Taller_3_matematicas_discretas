"""
Tests del ejercicio 8: simplificacion booleana (Quine-McCluskey reducido).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "boole"))

from Ejercicio_8 import (
    convertir_a_binario,
    difieren_en_un_bit,
    simplificar,
    termino_a_expresion,
    verificar_equivalencia,
)


def test_caso_sugerido_del_enunciado():
    # mintermos {1,3,5,7} con 3 variables -> equivale a C
    terminos = simplificar([1, 3, 5, 7], 3)
    assert terminos == ["--1"]
    expresion = termino_a_expresion(terminos[0], ["A", "B", "C"])
    assert expresion == "(C)"


def test_verificar_equivalencia_confirma_el_caso_sugerido():
    terminos = simplificar([1, 3, 5, 7], 3)
    assert verificar_equivalencia([1, 3, 5, 7], terminos, 3) is True


def test_convertir_a_binario():
    assert convertir_a_binario(5, 3) == [1, 0, 1]
    assert convertir_a_binario(0, 3) == [0, 0, 0]
    assert convertir_a_binario(7, 3) == [1, 1, 1]


def test_difieren_en_un_bit():
    assert difieren_en_un_bit(['1', '0', '1'], ['1', '1', '1']) == (True, 1)
    assert difieren_en_un_bit(['1', '0', '1'], ['0', '1', '1']) == (False, -1)
    assert difieren_en_un_bit(['1', '0', '1'], ['1', '0', '1']) == (False, -1)


def test_verificar_equivalencia_detecta_simplificacion_incorrecta():
    # se le pasa a proposito un termino que no corresponde
    assert verificar_equivalencia([1, 3, 5, 7], ["000"], 3) is False