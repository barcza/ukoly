with open (input("jaký soubor? "), encoding="windows-1250") as soubor, open (input("jaký nový soubor? "), mode="w", encoding="windows-1250") as ulozim:
    for radek in soubor:
        ulozim.write(radek)
