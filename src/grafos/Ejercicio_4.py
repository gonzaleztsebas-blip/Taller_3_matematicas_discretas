grafo = {
    "A": [("B", 5), ("F", 7), ("C", 4), ("I", 6), ("Q", 2)],
    "B": [("A", 5), ("C", 10), ("D", 19), ("E", 4), ("F", 8), ("H", 11)],
    "C": [("B", 10), ("A", 4), ("F", 9), ("K", 5), ("I", 9), ("Q", 1)],
    "D": [("B", 19), ("H", 2), ("E", 5), ("F", 2), ("J", 9)],
    "E": [("D", 5), ("H", 11), ("J", 10), ("B", 4), ("G", 8), ("F", 5)],
    "F": [("E", 5), ("D", 2), ("B", 8), ("A", 7), ("C", 9), ("K", 2), ("G", 2)],
    "G": [("E", 8), ("J", 1), ("L", 4), ("M", 8), ("N", 5), ("K", 1), ("F", 2)],
    "H": [("B", 11), ("D", 2), ("L", 10), ("J", 5), ("E", 11)],
    "I": [("A", 6), ("C", 9), ("K", 10), ("O", 8), ("Q", 5)],
    "J": [("G", 1), ("E", 10), ("H", 5), ("D", 9), ("M", 8), ("L", 1)],
    "K": [("C", 5), ("F", 2), ("G", 1), ("N", 2), ("O", 11), ("I", 10)],
    "L": [("G", 4), ("J", 1), ("H", 10), ("P", 7), ("M", 4)],
    "M": [("G", 8), ("L", 4), ("J", 8), ("O", 12), ("P", 7), ("N", 3)],
    "N": [("O", 5), ("K", 2), ("G", 5), ("M", 3), ("P", 3)],
    "O": [("I", 8), ("K", 11), ("N", 5), ("P", 18), ("M", 12), ("Q", 4)],
    "P": [("N", 3), ("M", 7), ("L", 7), ("O", 18), ("Q", 10)],
    "Q": [("A", 2), ("C", 1), ("I", 5), ("O", 4), ("P", 10)]
}

def encontrar_menor(distancias, visitados):
    actual = None
    menor_distancia = float('inf')
    for nodo in distancias:
        if nodo not in visitados:
            if distancias[nodo] < menor_distancia:
                menor_distancia = distancias[nodo]
                actual = nodo
    return actual

origen = input("Ingrese el nodo de salida (A-Q) ").upper().strip()
destino = input("Ingrese el nodo de destino (A-Q) ").upper().strip()

if origen not in grafo or destino not in grafo:
    print("Error: uno de los nodos ingresados no existe en el grafo.")
else:
    distancias = {}
    anteriores = {}
    visitados = set()

    for nodo in grafo:
        if nodo == origen:
            distancias[nodo] = 0
        else:
            distancias[nodo] = float('inf')
        anteriores[nodo] = None

    while True:
        actual = encontrar_menor(distancias, visitados)
        
        if actual is None:
            break
        if actual == destino:
            break
        
        visitados.add(actual)
        
        for vecino, peso in grafo[actual]:
            if vecino not in visitados:
                nueva_distancia = distancias[actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual

    if distancias[destino] == float('inf'):
        print(f"No existe camino entre {origen} y {destino}.")
    else:
        ruta = []
        nodo = destino
        while nodo is not None:
            ruta.append(nodo)
            nodo = anteriores[nodo]
        ruta.reverse()

        print(f"Ruta: {ruta}")
        print(f"Distancia total: {distancias[destino]}")