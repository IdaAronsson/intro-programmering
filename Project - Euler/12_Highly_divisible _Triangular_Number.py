
def räkna_delare(tal): #räknar antal delare för ett givet tal
    antal = 0  #antal delare 0
    i = 1 # börjar kolla från talet 1
    while i * i <= tal: #finns alltid en mindre eller lika med tal. 
        if tal % i == 0: #kolla om i är delare av tal
            motsvarande_delare = tal // i #beräkna motsvrande delare
            if i == motsvarande_delare: #om delarna är samma, dvs om man delar 36/6. 
                antal += 1  #om delarna är lika lägg till ett antal
            else:
                antal += 2  #annars lägg till två antal 
        i += 1 
    return antal  
def hitta_triangeltal(gräns): #hitta triangeltalet med visst antal delare
    nummer = 1       # börjar med nummer 1   
    triangeltal = 0   #börjar med triangeltalet 0
    while True: # förtsätter tills vi hittar ett triangeltal med tillräckligt stor delare
        triangeltal += nummer #summan av alla tal upp till aktuella talet
        delare = räkna_delare(triangeltal) #räkna antal delare
        if delare > gräns:  # om triangeltalet är större än 500
            return triangeltal #retunera traingeltalet och programmet slutar
        nummer += 1  #lägga till nästa tal till triangeltalet
resultat = hitta_triangeltal(500) 
print("Det första triangeltalet med över 500 delare är:", resultat)
