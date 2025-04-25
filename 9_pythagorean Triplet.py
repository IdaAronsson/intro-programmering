
for a in range(1,1000):
    for b in range(1,1000):
        c = (a**2 + b**2)**(1/2)
        num = c
        if int(num) == num:
            if c + b + a == 1000:
                print("a är", a)
                print("b är", b)
                print("c är", c)
                print(a*c*b)