import random

def multiplicar_matriz_vector(matriz, vector):
    # multiplicacion normal de una matriz 2x2 por un vector de 2 entradas
    # (asi es como una compuerta cuantica transforma el estado del qubit)
    a, b = matriz[0]
    c, d = matriz[1]
    x, y = vector

    nuevo_x = a * x + b * y
    nuevo_y = c * x + d * y

    return [nuevo_x, nuevo_y]


def aplicar_compuerta(nombre_compuerta, estado):
    # arma la matriz de la compuerta pedida y la aplica al estado actual
    raiz2 = 2 ** 0.5

    if nombre_compuerta == "X":
        # X invierte el qubit: manda |0> a |1> y viceversa
        matriz = [[0, 1],
                  [1, 0]]
    elif nombre_compuerta == "Z":
        # Z deja |0> igual y le cambia el signo a |1>
        matriz = [[1, 0],
                  [0, -1]]
    elif nombre_compuerta == "H":
        # H pone el qubit en superposicion, mitad |0> mitad |1>
        matriz = [[1/raiz2, 1/raiz2],
                  [1/raiz2, -1/raiz2]]
    else:
        raise ValueError(f"Compuerta desconocida: {nombre_compuerta}")

    return multiplicar_matriz_vector(matriz, estado)


def calcular_probabilidades(estado):
    # la probabilidad de medir cada resultado es la amplitud al cuadrado
    alpha, beta = estado
    prob_0 = alpha ** 2
    prob_1 = beta ** 2
    return prob_0, prob_1


def simular_mediciones(prob_0, prob_1, num_mediciones=1000):
    # simula mediciones repetidas: en cada una se saca un numero al azar
    # y se decide 0 o 1 segun las probabilidades calculadas antes
    conteo_0 = 0
    conteo_1 = 0

    for _ in range(num_mediciones):
        r = random.random()
        if r < prob_0:
            conteo_0 += 1
        else:
            conteo_1 += 1

    return conteo_0, conteo_1


if __name__ == "__main__":
    estado_inicial = [1, 0]  # |0>

    print("=== Caso de prueba 1: X|0> ===")
    resultado = aplicar_compuerta("X", estado_inicial)
    print(f"Estado resultante: {resultado}  (esperado: [0, 1])")

    print("\n=== Caso de prueba 2: H|0> ===")
    resultado_h = aplicar_compuerta("H", estado_inicial)
    print(f"Estado resultante: {resultado_h}")
    prob_0, prob_1 = calcular_probabilidades(resultado_h)
    print(f"Probabilidad de 0: {prob_0:.3f}, Probabilidad de 1: {prob_1:.3f}")
    print("(esperado: cercano a 50% y 50%)")

    conteo_0, conteo_1 = simular_mediciones(prob_0, prob_1, 1000)
    print(f"Simulación de 1000 mediciones -> 0: {conteo_0} veces, 1: {conteo_1} veces")

    print("\n=== Caso de prueba 3: HH|0> ===")
    resultado_hh = aplicar_compuerta("H", resultado_h)
    print(f"Estado resultante: {resultado_hh}  (esperado: cercano a [1, 0])")