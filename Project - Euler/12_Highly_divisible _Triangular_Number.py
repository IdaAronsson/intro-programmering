
def räkna_delare(tal):
    antal = 0  
    i = 1      
    while i * i <= tal:
        if tal % i == 0: 
            motsvarande_delare = tal // i
            if i == motsvarande_delare:
                antal += 1  
            else:
                antal += 2  
        i += 1 
    return antal  
def hitta_triangeltal(gräns):
    nummer = 1          
    triangeltal = 0    
    while True:
        triangeltal += nummer 
        delare = räkna_delare(triangeltal) 
        if delare > gräns:  
            return triangeltal
        nummer += 1  
resultat = hitta_triangeltal(500)
print("Det första triangeltalet med över 500 delare är:", resultat)
