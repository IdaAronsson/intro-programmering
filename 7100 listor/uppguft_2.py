tal_lista = list(range(2, 101))
primtal_lista = []
while tal_lista: #När lista tal_lista inte är tim
    last =tal_lista.pop(0) #Ta bort det första elementet
    primtal_lista.append(last) #lägger det i pimtal_lista
    tal_lista =[tal for tal in tal_lista if tal % last !=0] #kontrollerar att tal inte är delbart med last
    # Ta bort alla tal i tal_lista som är delbara med det sista primtalet i primtal, alla mutipler av last tas bort
print("primtal mellan 1 och 100:", primtal_lista)