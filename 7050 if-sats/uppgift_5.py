tal_1= float(input("mata in ett tal: "))
tal_2 = float(input("mata in ett andra tal: "))
tal_3 = float(input("mata in ett tredje tal: "))
if tal_2 < tal_1 and tal_2 < tal_3:
    print('det andra talet är minst')
elif tal_1 < tal_2 and tal_1 < tal_3:
    print('det första talet är minst')
elif tal_3 < tal_2 and tal_3 < tal_1:
    print('det tredje talet är minst')