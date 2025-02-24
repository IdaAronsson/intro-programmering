def primtal (n):
    tal = 2
    while tal * tal <= n:
        if n % tal == 0:
            n//=tal
        else:
            tal +=1
    return n
nummer = 600851475143
resultat = primtal(nummer)

print("Den största primtalsfaktorn av 600851475143 är: ", resultat)
