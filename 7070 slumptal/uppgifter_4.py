import random
print('välkommen att spela')
print('Ett spel kostar en krona')
print('vinstplan:')
print('två lika - 5 kr')
print('en sexa - 3kr')
print('stege - 3 kr')
spela = input('vill du spela: j/n ')
pengar = input('vill du sätta in pengar: j/n ')
avsluta = input('Vill du avsluta?: j/n')
if spela = n 




    tärning_1 = random.randint(2, 3)
    tärning_2 = random.randint(1, 6)
    print(tärning_1, tärning_2)
    if tärning_1 == tärning_2 + 1 or tärning_1== tärning_2 -1:
        print('stege - vinst')
    elif tärning_1 == 6 and tärning_2 == 6:
        print('6 - vinst')
    elif tärning_1 == tärning_2: 
        print('vinst') 
    else: 
        print('förlust')
    svar = input('vill du spela mer? j/n: ')
if svar== 'n':
    print('vad roligt att spelade en stund')