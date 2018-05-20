#otevřít abecedy, uložit je jako seznamy, otevřít stránku, dvě vynulovaná počítadla, u každého znaku stránky
#zjistit, jestli je v nějakém tom seznamu, když jo, zvýšit číslo na počítadle

pocitadlo_hiragana = 0
pocitadlo_katakana = 0

znaky_hiragana = []
znaky_katakana = []

def naplnit_hiraganu():
    with open ("hiragana.txt", encoding="utf-8") as hirabeceda:
        for radek in hirabeceda:
            for znak in radek:
                if znak != "\n":
                    znaky_hiragana.append(znak)

def naplnit_katakanu():
    with open ("katakana.txt", encoding="utf-8") as katabeceda:
        for radek in katabeceda:
            for znak in radek:
                if znak != "\n":
                    znaky_katakana.append(znak)

naplnit_hiraganu()
naplnit_katakanu()

def pocitani_znaku():
    with open ("rozsypany_caj.txt", encoding="utf-8") as zkoumany_soubor:
        for radek in zkoumany_soubor:
            for znak in radek:
                if znak in znaky_hiragana:
                    global pocitadlo_hiragana
                    pocitadlo_hiragana +=1
                elif znak in znaky_katakana:
                    global pocitadlo_katakana
                    pocitadlo_katakana +=1

    print("znaků hiragany je", pocitadlo_hiragana)
    print("znaků hiragany je", pocitadlo_katakana)

pocitani_znaku()
