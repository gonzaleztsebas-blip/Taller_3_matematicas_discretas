import random

# =======================================================
# MPC: Suma secreta dividiendo datos en 3 servidores (mod M)
# =======================================================

while True:
    print("\n=======================================================")
    print(" MPC básico: calcular un promedio sin mostrar los datos ")
    print("========================================================")
    print("1. Ingresar una lista de numeros")
    print("0. Salir")
    print("========================================================")

    # Listas de fragmentos para cada servidor
    S_1 = []
    S_2 = []
    S_3 = []

    suma_total = 0
    k = 0
    M = 1000003 # Módulo para el secreto compartido

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

            # Validación de entrada y rangos
            try:
                numeros = [int(n.strip()) for n in listado.split(",")]
                for i in numeros:
                    if i < 1 or i > 50:
                        raise ValueError()
            except ValueError:
                print("\nIngrese valores numéricos separados por comas dentro del rango.")
                continue

            # Generación de fragmentos aleatorios y reconstrucción
            for i in numeros:
                S_1.append(random.randint(51, 1000002))
                S_2.append(random.randint(51, 1000002))
                
                # La 3ra parte garantiza que (S1+S2+S3) mod M = i
                S_3.append((i - S_1[k] - S_2[k]) % M)
                
                # Se reconstruye el valor para la suma
                suma_total += (S_1[k] + S_2[k] + S_3[k]) % M
                k += 1

            promedio = suma_total / len(numeros)

            print("\nLa suma total es:", suma_total)
            print("El promedio es:", promedio)

        case 0:
            break

        case _:
            print("\nError. Opción inválida. Ingrese un valor correcto.")