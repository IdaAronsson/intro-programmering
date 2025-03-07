def fib(n):
    F1, F2 = 1, 1 # de två första fib talen
    n = 2 # n håller ordning på fib sekvensen, vi börjar med andra termen därav n = 2
    while len(str(F2))<1000:# while loop som fortsätter tills längden av F2 (antal siffror) är minst 1000. Omvandla till sträng. Räknar siffrorna i F2. 
        F1, F2 = F2, F1 + F2 # beräkna nästa fib tal med formeln given i frågan
        n += 1 # vi ökar (n) eftersom vi går vidare till nästa fib tal 
    return n # När F2 har 1000 siffror, retunerar man index n, alltsp vilken term som når 1000 siffror först. 
print(fib(1000))