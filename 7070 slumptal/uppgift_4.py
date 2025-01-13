import random 

kassa = 0
svar = 'j'
while svar !='a':
    svar = input("välj att spela(s), sätta in pengar (i), eller avsluta (a): ")
    if svar == "s":
        kassa -= 1
        tärning_1 = random.randint(1,6)
        tärning_2 = random.randint(1,6)
        print(tärning_1,tärning_2)
        if tärning_1 == tärning_2 +1 or tärning_1==tärning_2-1:
            print("steg- vinst +3kr")
            kassa += 3
        elif tärning_1==6 and tärning_2==6:
            print("sex-vinst + 3kr")
            kassa += 3
        elif tärning_1 == tärning_2: 
            print("vinst + 5kr")
            kassa +=5
        else: 
            print("förlust")
    elif svar == "i":
        mängd=input("Ange mängden pengar du vill sätta in: ")
        kassa +=int(mängd)
        print("Att spela för: " + str(kassa))

    elif svar == "a": 
        print("Vad roligt att du spela!")
