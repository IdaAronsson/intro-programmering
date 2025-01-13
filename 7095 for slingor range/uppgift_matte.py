from math import* 

n=0
summa = 0 
while n < 12: 
    n += 1
    summa += 4000 +2000 * cos(pi*n/6)
print("Under året föddes",summa,"barn")