def sum_of_square(tal):
    summa=0
    for tal in range(1,101):
        summa = summa + tal**2
    return summa
print(sum_of_square(100))

def square_of_sum(tal):
    summa = 0 
    for tal in range(1,101):
        summa = summa + (tal)
    return summa**2
print(square_of_sum(100)-sum_of_square(100))
    
