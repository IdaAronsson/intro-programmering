tal_lista = list(range(2, 101)) #satte in 3
primtal_lista = [] # satte in 2
while tal_lista: #När lista tal_lista inte är tim
    last =tal_lista.pop(0) 
    primtal_lista.append(last) #lägger det i pimtal_lista
    tal_lista =[tal for tal in tal_lista if tal % last !=0] 
    #kontrollerar att tal inte är delbart med last, resten inte blir noll vid modulo, tar bort alla mutipler av promtalet last från tal_lista
    # Ta bort alla tal i tal_lista som är delbara med det sista primtalet i primtal, alla mutipler av last tas bort
print("primtal mellan 1 och 100:", primtal_lista)

# för att komma ihåg: exempelvis börjar vi ta för tal = 3. 3 mod2 ger en rest på 1. Det innebär att det inte är 0, därför behålls 3. Om vi sätter in 4mod 2, kommer resten bli 0 vilket är 0, därför tas 4 bort. Fortsätter så för varje tal till 100