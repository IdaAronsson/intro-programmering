def primtal(n):
    if n < 2: # primtal är större än 1
        return False
    if n == 2: # 2 är det enda jämna primtalet
        return False
    if n % 2 == 0: # Alla jämna tal är inte primtal
        return False
        for i in range (3, int(n**0.5)+ 1, 2):
            if n % i == 0:
                return False
        