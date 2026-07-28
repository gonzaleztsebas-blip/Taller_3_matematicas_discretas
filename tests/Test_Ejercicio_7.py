"""
Tests del ejercicio 7: tablas de verdad y circuitos logicos.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "boole"))

from Ejercicio_7 import or_exclusive, expresion_1, expresion_2, expresion_3


def test_or_exclusive():
    assert or_exclusive(0, 0) == 0
    assert or_exclusive(1, 0) == 1
    assert or_exclusive(0, 1) == 1
    assert or_exclusive(1, 1) == 0


def test_expresion_1_tabla_de_verdad():
    # (A ∧ B) ∨ (¬C)
    assert expresion_1(0, 0, 0) is True   # ¬C = True
    assert expresion_1(0, 0, 1) is False  # A∧B=False, ¬C=False
    assert expresion_1(1, 1, 1) is True   # A∧B=True


def test_expresion_2_tabla_de_verdad():
    # (A ⊕ B) ∧ C
    assert expresion_2(0, 0, 1) is False  # A⊕B=False
    assert expresion_2(1, 0, 1) is True   # A⊕B=True, C=True
    assert expresion_2(1, 0, 0) is False  # A⊕B=True pero C=False


def test_expresion_3_tabla_de_verdad():
    # (A ∨ B) ∧ (¬A ∨ C)
    assert expresion_3(0, 0, 0) is False  # A∨B=False
    assert expresion_3(1, 0, 0) is False  # ¬A∨C = False∨False = False
    assert expresion_3(1, 0, 1) is True   # ¬A∨C = False∨True = True


def test_tabla_completa_tiene_8_combinaciones_por_expresion():
    combinaciones = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    assert len(combinaciones) == 8
    # solo se confirma que las 3 funciones no truenan con ninguna combinacion
    for a, b, c in combinaciones:
        expresion_1(a, b, c)
        expresion_2(a, b, c)
        expresion_3(a, b, c)