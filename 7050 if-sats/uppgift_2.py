text = input("ange näst sista siffran i ditt personnummer")
tal = int(text)
if tal % 2 == 0:
    print('talet är jämnt')
    print("du är tjej")
else:
    print('talet är udda')
    print("du är kille")
