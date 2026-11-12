#Výpočet celkové výměry (v m²) bytu

# definice funkce pro výpočet obsahu obdelníka
def obsah_obdelnika( a, b):

    if a <= 0 or b <= 0:
        return  None and print("Zadané rozměry nejsou platné. Zadej kladné hodnoty.")
    obsah = a * b
    return obsah

# hlavní tělo programu

print("Výpočet celkové výměry bytu")
print("***************************")

pocet_mistnosti = int(input("Zadej počet místností: "))

mistnost = 1 # cislo mistnosti
celkova_vyměra = 0 # celková výměra bytu

while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost}. místonosti:")
    strana_a = int(input("Zadej délku strany \"a\" (v metrech): "))
    strana_b = int(input("Zadej délku strany \"b\" (v metrech): "))
    obsah = obsah_obdelnika(strana_a, strana_b)
    
    if obsah != None:
        # přičtení obsahu místnosti k celkové výměře bytu
        celkova_vyměra += obsah
    mistnost += 1

    print(f"Celková výměra bytu je: {celkova_vyměra} m²")

    