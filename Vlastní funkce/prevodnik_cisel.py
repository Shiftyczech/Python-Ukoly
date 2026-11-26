#Převodník IT číselných soustav a převodní tabulka

#Definice funkcí

def cifra_na_znak(hodnota):
    if 0 <= hodnota <= 9:
        return str(hodnota)
    elif 10 <= hodnota <= 15:
        return chr(ord('A') + hodnota - 10)
    else:
        return None  # Hodnota mimo rozsah


def preved_soustavu(cislo, zaklad):
    if cislo < 0:
        return None  # Záporná čísla nejsou podporována
    if zaklad not in (2,8,10,16):
        return None  # Pouze IT soustavy (BIN, OCT, DEC, HEX)
    if cislo == 0:
        return "0"

    vysledek = ""
    while cislo > 0:
        zbytek = cislo % zaklad
        vysledek = cifra_na_znak(zbytek) + vysledek
        cislo //= zaklad

    return vysledek

#Hlavní tělo programu

print("DEC | BIN   | OCT | HEX")
print("----|-------|-----|----")

cislo = 0
while cislo <= 16:
    dvojkova = preved_soustavu(cislo, 2)
    osmickova = preved_soustavu(cislo, 8)
    sestnactkova = preved_soustavu(cislo, 16)
    
    # Zarovnání sloupců doleva (např. :<5 znamená šířka 5 znaků)
    print(f"{cislo:<3} | {dvojkova:<5} | {osmickova:<3} | {sestnactkova}")
    cislo += 1

print()
print("Test neplatného čísla:", preved_soustavu(-5, 2))
print("Test neplatného základu:", preved_soustavu(10, 5))