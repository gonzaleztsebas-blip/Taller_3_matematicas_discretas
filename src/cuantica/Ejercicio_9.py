import math

def frecuencia_texto(texto):
    # cuenta cuantas veces aparece cada simbolo (letra) en el texto
    frecuencia = {}

    for letra in texto:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
    return frecuencia


def entropia_texto(frecuencia, texto):
    # entropia de Shannon: mide la incertidumbre del texto, no su longitud
    # un texto repetitivo tiene probabilidades muy concentradas en pocos
    # simbolos, entonces la entropia sale baja (o 0 si es un solo simbolo)
    suma = 0
    for letra in frecuencia:
        probabilidad = frecuencia[letra] / len(texto)
        suma -= probabilidad * math.log2(probabilidad)
    return suma


if __name__ == "__main__":
    print("\n===========================================")
    print(" Shannon: medir información en un mensaje ")
    print("===========================================")
    text = input("Ingrese un texto para calcular su entropia: ").upper()
    text_2 = input("Ingrese otro texto para comparar: ").upper()
    print("===========================================")

    frecuencia_1 = frecuencia_texto(text)
    frecuencia_2 = frecuencia_texto(text_2)

    entropia_1 = entropia_texto(frecuencia_1, text)
    entropia_2 = entropia_texto(frecuencia_2, text_2)

    if entropia_1 > entropia_2:
        print("El texto 1 tienen mayor antropia que el texto 2")
        print(f"Entropia 1:  {entropia_1:.3f}")
        print(f"Entropia 2: {entropia_2:.3f}")

    elif entropia_1 < entropia_2:
        print("El texto 2 tienen mayor antropia que el texto 1")
        print(f"Entropia 2: {entropia_2:.3f}")
        print(f"Entropia 1:  {entropia_1:.3f}")

    else:
        print("Tienen la misma entropía los dos textos ")
        print(f"Entropia 1 y 2: {entropia_2:.3f}")