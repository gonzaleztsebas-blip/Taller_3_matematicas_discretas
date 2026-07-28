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

def coloreo_voraz(grafo):
    # va asignando colores nodo por nodo, en el orden en que aparecen
    # en el diccionario, sin mirar hacia adelante
    colores = {}

    for nodo in grafo:
        colores_vecinos = set()

        # se fija que colores ya usaron los vecinos que ya tienen color
        for (vecino, _) in grafo[nodo]:
            if vecino in colores:
                colores_vecinos.add(colores[vecino])

        # le da al nodo el primer color disponible que ningun vecino tenga
        color_candidato = 0
        while color_candidato in colores_vecinos:
            color_candidato += 1

        colores[nodo] = color_candidato

    return colores

def verificar_colores(grafo, colores):
    # revisa que no haya dos nodos conectados con el mismo color
    for nodo in grafo:
        for (vecino, _) in grafo[nodo]:
            if colores[nodo] == colores[vecino]:
                return False
    return True

if __name__ == "__main__":
    colores = coloreo_voraz(grafo)
    
    print("Colores asignados por nodo:")
    for nodo in colores:
        print(f"  {nodo}: color {colores[nodo]}")
    
    valido = verificar_colores(grafo, colores)
    print(f"\n¿Coloreo válido? {valido}")
    
    num_colores = len(set(colores.values()))
    print(f"Número de colores usados: {num_colores}")
    
    print("\nVértices por color:")
    for color in range(num_colores):
        vertices_con_ese_color = []
        for nodo in colores:
            if colores[nodo] == color:
                vertices_con_ese_color.append(nodo)
        print(f"  Color {color}: {vertices_con_ese_color}")