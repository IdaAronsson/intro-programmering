import random 

kassa = 100
svar = 'j'
while svar !='n':
    svar = input("välj att spela (j), välj att inte spela (n): ")
    if svar == "j":
        kassa -= 1
        tal_1 = random.randint(0,9)
        tal_2 = random.randint(0,9)
        tal_3 = random.randint(0,9)
        print(tal_1, tal_2, tal_3)
        if tal_1 == tal_2 == tal_3:
            mängd = input("Kvar att spela för: ")
            kassa += int(mängd)
            print("kvar att spela för: " + str(kassa))
            print("vinst + 50kr")
            kassa += 50
            svar = input("Vill du spela mer? j/n: ")
        elif tal_1 == 7 and tal_2 == 7 and tal_3 == 7:
            print("dubbelvinst")
            svar = input("Vill du spela mer? j/n: ")
        elif tal_1 == tal_2 or tal_1 == tal_3 or tal_3 == tal_2:
            print("minivinst + 5kr")
            kassa += 5
            svar = input("Vill du spela mer? j/n: ")
        elif tal_1== 7 or tal_2== 7 or tal_3== 7:
            print("sjuvinst + 2kr")
            kassa += 2
            svar = input("Vill du spela mer? j/n: ")
        

    

                
    


        




