primtalslista = [2] #lista för att lagra primtal, börjar med 2
n = 100001 # primtalet vi vill hitta
antal_primtal = 1 # räknar hur många primtal vi hittat
tal = 3 # Börjar från 3 och letar efter primtal
while antal_primtal < n:
    är_primtal = True
    for primtal in primtalslista:
        if tal % primtal == 0:
            är_primtal = False
    if är_primtal:
        primtalslista.append(tal) # lägg till primtalet i listan
        antal_primtal += 1 
    tal += 2 
print("Det 10001:a primtalet är:", primtalslista[-1])


        