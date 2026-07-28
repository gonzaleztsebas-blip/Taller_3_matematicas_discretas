"""
Tests del ejercicio 9: entropia de Shannon.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "cuantica"))

from Ejercicio_9 import frecuencia_texto, entropia_texto


def test_frecuencia_cuenta_bien_los_simbolos():
    assert frecuencia_texto("AAB") == {"A": 2, "B": 1}


def test_texto_de_un_solo_simbolo_tiene_entropia_cero():
    texto = "AAAAAAAA"
    frecuencia = frecuencia_texto(texto)
    entropia = entropia_texto(frecuencia, texto)
    assert entropia == 0.0


def test_texto_repetitivo_tiene_menor_entropia_que_uno_variado():
    repetitivo = "AAAAAAAAAA"
    variado = "HOLA MUNDO"

    f1 = frecuencia_texto(repetitivo)
    f2 = frecuencia_texto(variado)

    e1 = entropia_texto(f1, repetitivo)
    e2 = entropia_texto(f2, variado)

    assert e1 < e2


def test_entropia_maxima_con_simbolos_equiprobables():
    # con 4 simbolos igual de frecuentes, la entropia teorica es log2(4) = 2
    texto = "ABCD"
    frecuencia = frecuencia_texto(texto)
    entropia = entropia_texto(frecuencia, texto)
    assert round(entropia, 3) == 2.0


def test_frecuencias_suman_la_longitud_del_texto():
    texto = "MISSISSIPPI"
    frecuencia = frecuencia_texto(texto)
    assert sum(frecuencia.values()) == len(texto)