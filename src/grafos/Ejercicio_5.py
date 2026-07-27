 
import heapq
import copy
 
 
# ---------------------------------------------------------------------------
# 1. Grafo de la red (el mismo del punto anterior)
# ---------------------------------------------------------------------------
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
    "Q": [("A", 2), ("C", 1), ("I", 5), ("O", 4), ("P", 10)],
}
 
 
# ---------------------------------------------------------------------------
# 2. Algoritmo de Dijkstra (ruta mas corta entre un origen y un destino)
# ---------------------------------------------------------------------------
def dijkstra(grafo, origen, destino):
    """
    Devuelve la distancia minima entre 'origen' y 'destino' usando el
    algoritmo de Dijkstra. Si alguno de los dos nodos no existe en el
    grafo, o no hay camino entre ellos, devuelve float('inf').
    """
    if origen not in grafo or destino not in grafo:
        return float("inf")
 
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[origen] = 0
    visitados = set()
    heap = [(0, origen)]
 
    while heap:
        dist_actual, nodo_actual = heapq.heappop(heap)
 
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
 
        if nodo_actual == destino:
            return dist_actual
 
        for vecino, peso in grafo.get(nodo_actual, []):
            if vecino in visitados:
                continue
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(heap, (nueva_dist, vecino))
 
    return distancias[destino]
 
 
# ---------------------------------------------------------------------------
# 3. Simular el cierre de un vertice (estacion)
# ---------------------------------------------------------------------------
def cerrar_vertice(grafo, vertice):
    """
    Devuelve una COPIA del grafo en la que 'vertice' y todas las aristas
    que llegan o salen de el han sido eliminadas (simula el cierre de
    esa estacion).
    """
    nuevo_grafo = copy.deepcopy(grafo)
 
    # Eliminar el vertice como nodo
    if vertice in nuevo_grafo:
        del nuevo_grafo[vertice]
 
    # Eliminar todas las aristas que apuntaban hacia ese vertice
    for nodo in nuevo_grafo:
        nuevo_grafo[nodo] = [
            (vecino, peso) for vecino, peso in nuevo_grafo[nodo] if vecino != vertice
        ]
 
    return nuevo_grafo
 
 
def cerrar_arista(grafo, u, v):
    """
    Devuelve una COPIA del grafo en la que se elimina la arista (u, v)
    en ambos sentidos (simula el cierre de un tramo/via entre dos
    estaciones, sin cerrar las estaciones en si).
    """
    nuevo_grafo = copy.deepcopy(grafo)
    if u in nuevo_grafo:
        nuevo_grafo[u] = [(w, p) for w, p in nuevo_grafo[u] if w != v]
    if v in nuevo_grafo:
        nuevo_grafo[v] = [(w, p) for w, p in nuevo_grafo[v] if w != u]
    return nuevo_grafo
 
 
# ---------------------------------------------------------------------------
# 4. Comparar distancias antes/despues del cierre para varios pares
# ---------------------------------------------------------------------------
def formatear_dist(d):
    return "inf" if d == float("inf") else str(d)
 
 
def comparar_impacto(grafo_original, grafo_cerrado, pares):
    """
    pares: lista de tuplas (origen, destino)
    Devuelve una lista de diccionarios con el reporte de cada par.
    """
    reporte = []
    for origen, destino in pares:
        d_antes = dijkstra(grafo_original, origen, destino)
        d_despues = dijkstra(grafo_cerrado, origen, destino)
 
        if d_antes == float("inf") and d_despues == float("inf"):
            diferencia = "-"
            estado = "Ya estaban desconectados"
        elif d_despues == float("inf"):
            diferencia = "-"
            estado = "Desconectado"
        else:
            diferencia = d_despues - d_antes
            if diferencia == 0:
                estado = "Sin cambio"
            elif diferencia > 0:
                estado = "Aumento"
            else:
                estado = "Disminuyo"  # no deberia pasar al quitar elementos, pero se deja por robustez
 
        reporte.append({
            "origen": origen,
            "destino": destino,
            "antes": formatear_dist(d_antes),
            "despues": formatear_dist(d_despues),
            "diferencia": diferencia,
            "estado": estado,
        })
    return reporte
 
 
def imprimir_tabla(reporte, titulo):
    print("\n" + titulo)
    print("-" * 78)
    encabezado = f"{'Origen':<8}{'Destino':<9}{'Dist. antes':<13}{'Dist. despues':<15}{'Diferencia':<12}{'Estado'}"
    print(encabezado)
    print("-" * 78)
    for fila in reporte:
        print(f"{fila['origen']:<8}{fila['destino']:<9}{fila['antes']:<13}"
              f"{fila['despues']:<15}{str(fila['diferencia']):<12}{fila['estado']}")
    print("-" * 78)
 
 
# ---------------------------------------------------------------------------
# 5. Programa principal
# ---------------------------------------------------------------------------
if __name__ == "__main__":
 
    # --- Escenario 1: cierre de un VERTICE (estacion) ---------------------
    ESTACION_CERRADA = "F"   # F es un nodo "hub": conecta A,B,C,D,E,G,K
 
    pares_prueba = [
        ("A", "G"),   # cruza la red usando F como atajo tipico
        ("I", "J"),
        ("Q", "N"),
        ("B", "K"),
        ("H", "O"),
        ("D", "C"),
        ("P", "A"),
    ]
 
    print("=" * 78)
    print(f"ESCENARIO 1: Cierre del vertice (estacion) '{ESTACION_CERRADA}'")
    print("=" * 78)
 
    grafo_sin_F = cerrar_vertice(grafo, ESTACION_CERRADA)
    reporte_1 = comparar_impacto(grafo, grafo_sin_F, pares_prueba)
    imprimir_tabla(reporte_1, f"Impacto de cerrar la estacion '{ESTACION_CERRADA}'")
 
    # --- Escenario 2: cierre de una ARISTA (tramo entre dos estaciones) ---
    ORIGEN_ARISTA, DESTINO_ARISTA = "G", "K"   # tramo con peso muy bajo (1)
 
    print("\n" + "=" * 78)
    print(f"ESCENARIO 2: Cierre del tramo (arista) '{ORIGEN_ARISTA}-{DESTINO_ARISTA}'")
    print("=" * 78)
 
    grafo_sin_GK = cerrar_arista(grafo, ORIGEN_ARISTA, DESTINO_ARISTA)
    reporte_2 = comparar_impacto(grafo, grafo_sin_GK, pares_prueba)
    imprimir_tabla(reporte_2, f"Impacto de cerrar el tramo '{ORIGEN_ARISTA}-{DESTINO_ARISTA}'")