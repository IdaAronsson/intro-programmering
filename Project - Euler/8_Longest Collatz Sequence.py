def collatz_sequence_längd(n):
    längd = 1 #börjar sätta längden till 1
    while n !=1: #fortsätter sålänge n inte är 1
        if n%2 == 0: #kollar om n är jämnt
            n=n//2 #uppdatera värden av n när det är jämnt
        else:
            n = 3*n+1 #om det är udda
        längd +=1 #nytt tal, hålla reda på antal tal i kedjan
    return längd #när sekvensen når 1 (regeln)
def längsta_collatz_kedja(gräns):
    max_längd = 0 #längsta kedjans längd
    nummer_med_max_kedja = 0 #vilket tal som gav längsta kedjan
    for i in range(1,gräns):
        längd = collatz_sequence_längd(i) #för varje i beräknas längden på collatx sekvensen
        if längd > max_längd: 
            max_längd  = längd
            nummer_med_max_kedja = i
    return nummer_med_max_kedja, max_längd
resultat = längsta_collatz_kedja(1000000)
print(resultat)