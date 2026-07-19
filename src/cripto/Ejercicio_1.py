# ==========================================================
# Cifrado César: Encriptación por desplazamiento de letras
# ==========================================================
def cifrado_Cesar(cadena, desplazamiento):
    mensaje_cifrado = ""

    for letra in cadena:
        if letra.isalpha():
            # Desplaza y vuelve a la 'A' si pasa la 'Z' (ASCII 90)
            if (ord(letra) + desplazamiento) > 90:
                letra_nueva = chr(ord(letra) + desplazamiento - 26)
            else:
                letra_nueva = chr(ord(letra) + desplazamiento)
        else:
            letra_nueva = letra

        mensaje_cifrado += letra_nueva

    return mensaje_cifrado


# ==========================
# Programa principal
# ==========================
while True:
    print("\n===========================================")
    print(" Cifrado César: romper un mensaje antiguo ")
    print("===========================================")
    print("1. Cifrar un mensaje")
    print("2. Descifrar un mensaje")
    print("3. Probar todas las claves posibles")
    print("0. Salir")
    print("===========================================")

    try:
        switch = int(input("\nIngrese el número de la opción deseada: "))
    except ValueError:
        print("\nIngrese un valor númerico")
        continue

    match switch:
        case 1:
            try:
                desplazamiento = int(input("Ingrese el desplazamiento para cifrar el mensaje (1-25): "))
                if desplazamiento < 1 or desplazamiento > 25:
                    raise ValueError()
            except ValueError:
                print("\nIngrese un valor dentro del rango")
                continue

            mensaje = input("Ingrese el mensaje a cifrar: ").upper()
            print("Mensaje Cifrado:", cifrado_Cesar(mensaje, desplazamiento))

        case 2:
            try :
                desplazamiento = int(input("Ingrese el desplazamiento para cifrar el mensaje (1-25): "))
                if desplazamiento < 1 or desplazamiento > 25:
                    raise ValueError()
            except ValueError:
                print("\nIngrese un valor dentro del rango")
                continue

            mensaje = input("Ingrese el mensaje cifrado: ").upper()
            print("Mensaje Real:", cifrado_Cesar(mensaje, 26 - desplazamiento))

        case 3:
            mensaje = input("Ingrese el mensaje cifrado: ").upper()
            
            # Fuerza bruta: prueba los 25 desplazamientos posibles
            for i in range(1, 26):
                print(str(i) + ") Mensaje: " + cifrado_Cesar(mensaje, 26 - i))

        case 0:
            break

        case _:
            print("\nError. Opción inválida.")