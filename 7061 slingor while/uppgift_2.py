svar = int(input("ange ett tal: "))
while svar !=42:
    if svar < 42:
        print('talet är för litet')
    if svar > 42:
        print('talet är för stort')
    svar = int(input('fel gissning. Gissa igen: '))
print('rätt')