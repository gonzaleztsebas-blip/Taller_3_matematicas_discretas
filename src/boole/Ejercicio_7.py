# ==========================================================
# Función or_exclusive: Simula la operación lógica XOR
# ==========================================================
def or_exclusive(A, B):
    operacion = (A + B) % 2
    return operacion

# ==========================================================
# Programa principal: Generación de tablas de verdad 
# y evaluación de expresiones lógicas
# ==========================================================
while True:
    print("\n===========================================")
    print(" Tablas de verdad y circuitos lógicos ")
    print("===========================================")
    print("1. (A ∧ B) ∨ (¬C)")
    print("2. (A ⊕ B) ∧ C")
    print("3. (A ∨ B) ∧ (¬A ∨ C)")
    print("0. Salir")
    print("===========================================")
    
    try:
        switch = int(input("\nIngrese el número de la opción deseada: "))
    except ValueError:
        print("\nIngrese un valor númerico")
        continue

    match switch:
        # ==========================================
        # Expresión 1: (A ∧ B) ∨ (¬C)
        # ==========================================
        case 1:
            print("\n=====================")
            print(" Menú ")
            print("1. Tabla Total")
            print("2. Entrada Especifica")
            print("======================")
            try:
                switch = int(input("\nIngrese el número de la opción deseada: "))
            except ValueError:
                print("\nIngrese un valor númerico")
                continue

            match switch:
                # Genera la tabla completa
                case 1:
                    print("----------------------------------------------------------")
                    print("  A   |   B   |   C   |  A ∧ B  |   ¬C  | (A ∧ B) ∨ (¬C) ")
                    print("----------------------------------------------------------")
                    for i in range(0,2):
                        A=i
                        for j in range(0,2):
                            B=j
                            for k in range(0,2):
                                C=k
                                print(f"{str(bool(A)):5} | {str(bool(B)):5} | {str(bool(C)):5} |  {str(bool(A and B)):5}  | {str(bool(not C)):5} |     {str(bool((A and B) or (not C))):16}")
                    print("----------------------------------------------------------")
                    
                # Evalúa una entrada específica
                case 2:
                    try:
                        A = int(input("¿Cuál es el valor de A? (0/1): "))
                        B = int(input("¿Cuál es el valor de B? (0/1): "))
                        C = int(input("¿Cuál es el valor de C? (0/1): "))
                        
                        if 0>A or A>1 or 0>B or B>1 or 0>C or C>1:
                            raise ValueError()
                        
                        A = bool(A)
                        B = bool(B)
                        C = bool(C)
                        
                    except ValueError:
                        print("\nError. Ingrese un valor correcto dentro del rango.")
                        continue

                    print("----------------------------------------------------------")
                    print("  A   |   B   |   C   |  A ∧ B  |   ¬C  | (A ∧ B) ∨ (¬C) ")
                    print("----------------------------------------------------------")
                    print(f"{str(bool(A)):5} | {str(bool(B)):5} | {str(bool(C)):5} |  {str(bool(A and B)):5}  | {str(bool(not C)):5} |     {str(bool((A and B) or (not C))):16}")                    
                    print("----------------------------------------------------------")
                
                case _:
                    print("\nError. Opción inválida. Ingrese un valor correcto.")

        # ==========================================
        # Expresión 2: (A ⊕ B) ∧ C
        # ==========================================
        case 2:
            print("\n=====================")
            print(" Menú ")
            print("1. Tabla Total")
            print("2. Entrada Especifica")
            print("======================")
            switch = int(input("\nIngrese el número de la opción deseada: "))

            match switch:
                # Genera la tabla completa
                case 1:
                    print("------------------------------------------------")
                    print("  A   |   B   |   C   |  A ⊕ B  | (A ⊕ B) ∧ C ")
                    print("------------------------------------------------")
                    for i in range(0,2):
                        A=i
                        for j in range(0,2):
                            B=j
                            for k in range(0,2):
                                C=k
                                print(f"{str(bool(A)):5} | {str(bool(B)):5} | {str(bool(C)):5} |  {str(bool(or_exclusive(A,B))):5}  |     {str(bool(or_exclusive(A,B) and C)):16}")
                    print("------------------------------------------------")
                    
                # Evalúa una entrada específica
                case 2:
                    try:
                        A = int(input("¿Cuál es el valor de A? (0/1): "))
                        B = int(input("¿Cuál es el valor de B? (0/1): "))
                        C = int(input("¿Cuál es el valor de C? (0/1): "))
                        
                        if 0>A or A>1 or 0>B or B>1 or 0>C or C>1:
                            raise ValueError()
                        
                        A = bool(A)
                        B = bool(B)
                        C = bool(C)
                        
                    except ValueError:
                        print("\nError. Ingrese un valor correcto dentro del rango.")
                        continue

                    print("------------------------------------------------")
                    print("  A   |   B   |   C   |  A ⊕ B  | (A ⊕ B) ∧ C ")
                    print("------------------------------------------------")
                    print(f"{str(bool(A)):5} | {str(bool(B)):5} | {str(bool(C)):5} |  {str(bool(or_exclusive(A,B))):5}  |     {str(bool(or_exclusive(A,B) and C)):16}")
                    print("------------------------------------------------")

                case _:
                    print("\nError. Opción inválida. Ingrese un valor correcto.")
        
        # ==========================================
        # Expresión 3: (A ∨ B) ∧ (¬A ∨ C)
        # ==========================================
        case 3:
            print("\n=====================")
            print(" Menú ")
            print("1. Tabla Total")
            print("2. Entrada Especifica")
            print("======================")
            switch = int(input("\nIngrese el número de la opción deseada: "))

            match switch:
                # Genera la tabla completa
                case 1:
                    print("-------------------------------------------------------------------------")
                    print("  A   |   B   |   C   |  A ∨ B  |  ¬A   |  ¬A ∨ C  | (A ∨ B) ∧ (¬A ∨ C) ")
                    print("-------------------------------------------------------------------------")
                    for i in range(0,2):
                        A=i
                        for j in range(0,2):
                            B=j
                            for k in range(0,2):
                                C=k
                                print(f"{str(bool(A)):5} | {str(bool(B)):5} | {str(bool(C)):5} |  {str(bool(A or B)):5}  | {str(bool(not A)):5} |   {str(bool(not A or C)):5}  |       {str(bool((A or B)and(not A or C))):16}")
                    print("-------------------------------------------------------------------------")
                
                # Evalúa una entrada específica
                case 2:
                    try:
                        A = int(input("¿Cuál es el valor de A? (0/1): "))
                        B = int(input("¿Cuál es el valor de B? (0/1): "))
                        C = int(input("¿Cuál es el valor de C? (0/1): "))
                        
                        if 0>A or A>1 or 0>B or B>1 or 0>C or C>1:
                            raise ValueError()
                        
                        A = bool(A)
                        B = bool(B)
                        C = bool(C)

                    except ValueError:
                        print("\nError. Ingrese un valor correcto dentro del rango.")
                        continue

                    print("------------------------------------------------")
                    print("  A   |   B   |   C   |  A ⊕ B  | (A ⊕ B) ∧ C ")
                    print("------------------------------------------------")
                    print(f"{str(bool(A)):5} | {str(bool(B)):5} | {str(bool(C)):5} |  {str(bool(A or B)):5}  | {str(bool(not A)):5} |   {str(bool(not A or C)):5}  |       {str(bool((A or B)and(not A or C))):16}")
                    print("------------------------------------------------")
            
                case _:
                    print("\nError. Opción inválida. Ingrese un valor correcto.")
            
        case 0:
            break
            
        case _:
            print("\n Error, Valor invalido. Ingrese un valor correcto")