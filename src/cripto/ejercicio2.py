def n(p, q):
    return p*q

def phi(p, q):
    return (p-1)*(q-1)

def euclides(e, phi):
    
    if phi == 0:
        return e, 1, 0 #MCD, d, x

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

    n = n(p, q)
    print(f"n = {n}")
    phi = phi(p, q)
    print(f"phi = {phi}")
    mcd, d, _ = euclides(e, phi)
    if mcd != 1:
        print (f"el numero e no es valido")
    else:
        if d < 0:
            d += phi
        c = cifrado (M, e, n)
        print(f"mensaje cifrado: {c}")
        print(f"mensaje descifrado: {descifrado(c, d, n)}")