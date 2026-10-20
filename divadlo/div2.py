zakladni_cena = 500

# Vstupy (pořadí podle ukázky)
vek = int(input("Zadejte věk: "))
student = input("Jste student? (ano/ne): ")
pocet_osob = int(input("Zadejte počet osob: "))
den = input("Zadejte den v týdnu: ")

# Výzva C: validace vstupů
if vek < 0:
    print("Neplatný věk!")
elif pocet_osob < 1:
    print("Neplatný počet osob!")
else:
    # Výzva B: víkendový příplatek
    priplatek = 50 if (den == "sobota" or den == "neděle") else 0
    cena_pred_slevou = zakladni_cena + priplatek

    # Určení slevy
    if pocet_osob >= 4:
        typ_slevy = "Skupinová sleva (25 %)"
        sleva = 0.75
    elif student == "ano" and vek < 26:
        typ_slevy = "Studentská sleva (30 %)"
        sleva = 0.7
    elif vek >= 65:
        typ_slevy = "Seniorská sleva (20 %)"
        sleva = 0.8
    else:
        typ_slevy = "Žádná sleva"
        sleva = 1

    cena_jedne = cena_pred_slevou * sleva
    celkova_cena = cena_jedne * pocet_osob

    # Výzva A: skloňování
    slovo = "osoba" if pocet_osob == 1 else ("osoby" if 2 <= pocet_osob <= 4 else "osob")
    vikend = " (Víkendové představení)" if priplatek > 0 else ""

    print("--- Výsledná účtenka ---")
    print(f"Typ lístku: {pocet_osob} {slovo}{vikend}")
    print(f"Druh slevy: {typ_slevy}")
    print(f"Cena za 1 vstupenku: {cena_jedne} Kč")
    print(f"Celková cena: {celkova_cena} Kč")