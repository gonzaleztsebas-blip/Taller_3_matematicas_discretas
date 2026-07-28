import random

# =======================================================
# MPC: Suma secreta dividiendo datos en 3 servidores (mod M)
# =======================================================

def dividir_y_reconstruir(numeros, M=1000003):
    """
    Simula el protocolo de suma secreta con 3 servidores.

    Cada numero i se reparte en tres partes aleatorias (S1, S2, S3)
    tal que (S1 + S2 + S3) mod M == i. Ningun servidor por separado
    ve el numero original, solo su pedacito. Al final se suman las
    tres partes de cada numero para reconstruir la suma total,
    sin que en ningun momento se junten los numeros originales.

    Devuelve (suma_total, promedio).
    """
    S_1, S_2, S_3 = [], [], []
    suma_total = 0

    for i in numeros:
        S_1.append(random.randint(51, 1000002))
        S_2.append(random.randint(51, 1000002))

        # la 3ra parte se calcula para que (S1+S2+S3) mod M = i
        S_3.append((i - S_1[-1] - S_2[-1]) % M)

        # se reconstruye el numero original sumando las 3 partes mod M
        suma_total += (S_1[-1] + S_2[-1] + S_3[-1]) % M

    promedio = suma_total / len(numeros)
    return suma_total, promedio


if __name__ == "__main__":
    while True:
        print("\n=======================================================")
        print(" MPC básico: calcular un promedio sin mostrar los datos ")
        print("========================================================")
        print("1. Ingresar una lista de numeros")
        print("0. Salir")
        print("========================================================")

        M = 1000003  # Módulo para el secreto compartido

        try:
            switch = int(input("\nIngrese el número de la opción deseada: "))
        except ValueError:
            print("\nIngrese un valor numérico.")
            continue

        match switch:
            case 1:
                listado = input(
                    "Ingrese el listado de números separados por comas (1-50): "
                )

                # validacion de entrada y rangos
                try:
                    numeros = [int(n.strip()) for n in listado.split(",")]
                    for i in numeros:
                        if i < 1 or i > 50:
                            raise ValueError()
                except ValueError:
                    print("\nIngrese valores numéricos separados por comas dentro del rango.")
                    continue

                suma_total, promedio = dividir_y_reconstruir(numeros, M)

                print("\nLa suma total es:", suma_total)
                print("El promedio es:", promedio)

            case 0:
                break

            case _:
                print("\nError. Opción inválida. Ingrese un valor correcto.")