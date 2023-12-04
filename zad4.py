def jakiwynik(pierwszaliczba: int, drugaliczba: int, trzecialiczba: int):
    wynikdwoch = pierwszaliczba+drugaliczba
    if wynikdwoch > trzecialiczba:
        return ("suma dwóch pierwszych jest wieksza niż trzecia liczba")
    elif wynikdwoch == trzecialiczba:
        return ("suma dwóch pierwszych jest równa trzeciej liczbie")
    else:
        return ("suma dwóch pierwszych jest mniejsza niż trzecia liczba")


print(jakiwynik(1, 2, 3))
