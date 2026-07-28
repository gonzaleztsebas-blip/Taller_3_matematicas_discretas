"""
Tests del ejercicio 2: RSA de juguete.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "cripto"))

from Ejercicio_2 import es_primo, n, phi, euclides, cifrado, descifrado


def test_caso_obligatorio_del_enunciado():
    p, q, e, M = 61, 53, 17, 65
    nn = n(p, q)
    ph = phi(p, q)
    mcd, d, _ = euclides(e, ph)
    if d < 0:
        d += ph

    assert nn == 3233
    assert ph == 3120
    assert d == 2753

    c = cifrado(M, e, nn)
    assert c == 2790
    assert descifrado(c, d, nn) == M


def test_es_primo():
    assert es_primo(61) is True
    assert es_primo(53) is True
    assert es_primo(1) is False
    assert es_primo(4) is False


def test_ciclo_completo_con_otros_primos():
    # p, q distintos a los del ejemplo obligatorio, para confirmar
    # que el ciclo cifrar->descifrar funciona en general, no solo
    # para ese caso puntual.
    p, q, e, M = 17, 11, 7, 88
    nn = n(p, q)
    ph = phi(p, q)
    mcd, d, _ = euclides(e, ph)
    if d < 0:
        d += ph

    assert mcd == 1
    c = cifrado(M, e, nn)
    assert descifrado(c, d, nn) == M


def test_euclides_devuelve_inverso_modular_valido():
    # e*d debe ser congruente con 1 modulo phi cuando mcd(e,phi)==1
    e, ph = 17, 3120
    mcd, d, _ = euclides(e, ph)
    if d < 0:
        d += ph
    assert mcd == 1
    assert (e * d) % ph == 1