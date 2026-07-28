"""
Tests del ejercicio 1: Cifrado César.

Se prueba únicamente la función cifrado_Cesar(), que es la lógica
matemática del ejercicio. El menú interactivo (input/print) no se
testea porque no tiene valor de retorno que verificar.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "cripto"))

from Ejercicio_1 import cifrado_Cesar


def test_cifrado_ejemplo_del_enunciado():
    # Caso mínimo dado en el taller: HOLA UNAL con k=3 -> KROD XQDO
    assert cifrado_Cesar("HOLA UNAL", 3) == "KROD XQDO"


def test_descifrado_recupera_mensaje_original():
    mensaje = "HOLA UNAL"
    k = 3
    cifrado = cifrado_Cesar(mensaje, k)
    descifrado = cifrado_Cesar(cifrado, 26 - k)
    assert descifrado == mensaje


def test_wraparound_al_final_del_alfabeto():
    # 'Z' con desplazamiento 1 debe dar la vuelta a 'A'
    assert cifrado_Cesar("XYZ", 1) == "YZA"


def test_conserva_espacios_numeros_y_puntuacion():
    assert cifrado_Cesar("HOLA 123, MUNDO!", 5) == "MTQF 123, RZSIT!"


def test_fuerza_bruta_incluye_el_mensaje_original():
    # Probar los 26 desplazamientos posibles debe incluir el mensaje
    # original entre los resultados (para k=0 o su equivalente 26).
    mensaje_cifrado = cifrado_Cesar("PRUEBA", 7)
    candidatos = [cifrado_Cesar(mensaje_cifrado, 26 - i) for i in range(1, 26)]
    assert "PRUEBA" in candidatos