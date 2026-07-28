def es_primo(num):
    """Prueba de primalidad por división: revisa divisores hasta sqrt(num)."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def n(p, q):
    """Módulo RSA: n = p*q. Su factorización es lo que da la seguridad real
    (aquí p y q son pequeños, así que romperlo es trivial; es solo ilustrativo)."""
    return p*q

def phi(p, q):
    return (p-1)*(q-1)

def euclides(e, phi):
    if phi == 0:
        return e, 1, 0

    mcd, d1, x1 = euclides(phi, e % phi)
    d = x1
    x = d1 - (e // phi) * x1
    return mcd, d, x

def cifrado(M, e, n):
    return (M**e)%n

def descifrado(C, d, n):
    return (C**d)%n

if __name__ == "__main__":
    p = int(input("ingrese p: "))
    q = int(input("ingrese q: "))
    e = int(input("ingrese e: "))
    M = int(input("ingrese M: "))

    if not es_primo(p) or not es_primo(q):
        print("Error: p y q deben ser numeros primos.")
    elif p == q:
        print("Error: p y q deben ser distintos.")
    elif e <= 1:
        print("Error: e debe ser mayor que 1.")
    else:
        n = n(p, q)
        print(f"n = {n}")
        phi = phi(p, q)
        print(f"phi = {phi}")

        if M >= n:
            print(f"Error: M debe ser menor que n ({n}) para que el descifrado sea correcto.")
        else:
            mcd, d, _ = euclides(e, phi)
            if mcd != 1:
                print(f"el numero e no es valido")
            else:
                if d < 0:
                    d += phi
                c = cifrado(M, e, n)
                print(f"mensaje cifrado: {c}")
                print(f"mensaje descifrado: {descifrado(c, d, n)}")