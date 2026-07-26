def convertir_a_binario(n, num_variables):
    bits = []
    for i in range (num_variables):
        bit = (n//2**i) % 2
        bits.append(bit)
    bits.reverse()
    return bits

def difieren_en_un_bit(bits1, bits2):
    if len(bits1) != len(bits2):
        return False, -1

    contador_diferencias = 0
    posicion_diferencia = 0

    for i in range(len(bits1)):
        if bits1[i] != bits2[i]:
            contador_diferencias += 1
            posicion_diferencia = i

    if contador_diferencias == 1:
        return True, posicion_diferencia

    else:
        return False, -1

def de_bits_a_string(bits):
    resultado = ""

    for bit in bits:
        resultado += str(bit)

    return resultado

def combinacion(bits, posicion_diferencia):
    resultado = ""

    for i in range(len(bits)):
        if i == posicion_diferencia:
            resultado += "-"
        else:
            resultado += bits[i]

    return resultado

def agrupar_terminos(terminos):
    combinados = set()
    usados = set()

    for i in range(len(terminos)):
        for j in range(i+1, len(terminos)):
            t1 = terminos[i]
            t2 = terminos[j]

            posible, posicion = difieren_en_un_bit(t1, t2)

            if posible:
                nuevo = combinacion(t1, posicion)
                combinados.add(nuevo)
                usados.add(t1)
                usados.add(t2)

    no_combinados = set()
    for termino in terminos:
        if termino not in usados:
            no_combinados.add(termino)

    return combinados, no_combinados

def simplificar(min_terminos, num_variables):
    terminos_actuales = []
    for m in min_terminos:
        bits = convertir_a_binario(m, num_variables)
        string_binario = de_bits_a_string(bits)
        terminos_actuales.append(string_binario)
    terminos_finales = []

    while True:
        combinados, no_combinados = agrupar_terminos(terminos_actuales)

        for termino in no_combinados:
            terminos_finales.append(termino)

        if not combinados:
            break

        terminos_actuales = list(combinados)

    return list(set(terminos_finales))

def termino_a_expresion(termino, nombres_variables):
    partes = []
    for i in range(len(termino)):
        caracter = termino[i]
        if caracter == "1":
            partes.append(nombres_variables[i])
        elif caracter == "0":
            partes.append(f"¬{nombres_variables[i]}")

    if not partes:
        return "1"

    resultado = partes[0]
    for parte in partes[1:]:
        resultado = resultado + " ∧ " + parte
    return "(" + resultado + ")"


def verificar_equivalencia(mintermos_originales, terminos_simplificados, num_variables):
    total_combinaciones = 2 ** num_variables

    for n in range(total_combinaciones):
        bits = convertir_a_binario(n, num_variables)

        original = 0
        if n in mintermos_originales:
            original = 1

        simplificado = 0
        for termino in terminos_simplificados:
            coincide = True
            for i in range(len(termino)):
                if termino[i] == "1" and bits[i] != 1:
                    coincide = False
                if termino[i] == "0" and bits[i] != 0:
                    coincide = False
            if coincide:
                simplificado = 1
                break

        if original != simplificado:
            return False

    return True


if __name__ == "__main__":
    mintermos = [1, 3, 5, 7]
    num_variables = 3
    nombres_variables = ["A", "B", "C"]

    terminos = simplificar(mintermos, num_variables)

    print(f"Mintérminos: {mintermos}")
    print(f"Términos simplificados (con guiones): {terminos}")

    expresiones = []
    for termino in terminos:
        expresiones.append(termino_a_expresion(termino, nombres_variables))
    expresion_final = " ∨ ".join(expresiones)
    print(f"Expresión simplificada: {expresion_final}")

    valido = verificar_equivalencia(mintermos, terminos, num_variables)
    print(f"¿Misma tabla de verdad que el original? {valido}")