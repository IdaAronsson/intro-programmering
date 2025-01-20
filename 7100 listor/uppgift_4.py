import random #tärningar och kast
def kasta_tärningar(antal_tärningar):
    return [random.randint(1, 6)for _ in range(antal_tärningar)]
#välj vilka tärningar som ska kastas
def välj_tärningar(tärningar):
    print(f"Tärningarna: {tärningar}")
