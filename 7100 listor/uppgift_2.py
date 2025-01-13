tal_lista = list(range(2, 101))
primtal=[]
while tal_lista != []:
    print(primtal)
    last = tal_lista.pop(0)
    primtal.append(last)
    # ta bort sista talet i listan
    i = len(tal_lista) - 1
    # längden på listan minus 1
    while i > -1:
        if tal_lista[i] % primtal[-1] == 0:
            tal_lista.remove(i)
            len(tal_lista)-1
        #ta bort talet i ur lista tal_lista
        # delbar med sista taler i listan primtal
    else:
        primtal = []
            
        


