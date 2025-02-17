def summa_av_siffror(i):
    tal = 2**i
    summa = sum(int(siffra) for siffra in str(tal))
    return summa
resultat = summa_av_siffror(1000)
print("Summa av siffrorna i 2^1000 är:", resultat)
