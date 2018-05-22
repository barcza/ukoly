vstup = input("jaký soubor? ")
vystup = input("jaký nový soubor? ")

with open (vstup, encoding="windows-1250") as soubor, open (vystup, mode="w", encoding="windows-1250") as ulozim:
    for radek in soubor:
        ulozim.write(radek)
