def czyparzysta(liczba: int):
    if liczba % 2 == 0:
        return("liczba jest parzysta")
    else:
        return("liczba jest nieparzysta")

print(czyparzysta(24))