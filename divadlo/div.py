#Návštěva divadla
#studenti mladší 26 let mají slevu 30 %,
#senioři ve věku 65 let a více mají slevu 20 %,
#pokud přijdou 4 a více osob, získají místo běžných slev skupinovou slevu 25 % na všechny vstupenky.
#Základní cena jedné vstupenky je: 500 Kč

zakladni_cena = 500

pocet_osob = int(input("Zadejte počet osob: "))
student = input("Je návštěvník student? (ano/ne): ")
vek = int(input("Zadejte věk návštěvníka: "))

# Určení typu slevy a ceny za jednu vstupenku
if pocet_osob >= 4:
    typ_slevy = "skupinová sleva (25 %)"
    cena_jedne = zakladni_cena * 0.75
elif student == "ano" and vek < 26:
    typ_slevy = "studentská sleva (30 %)"
    cena_jedne = zakladni_cena * 0.7
elif vek >= 65:
    typ_slevy = "seniorská sleva (20 %)"
    cena_jedne = zakladni_cena * 0.8
else:
    typ_slevy = "žádná sleva"
    cena_jedne = zakladni_cena

celkova_cena = cena_jedne * pocet_osob


print(f"Typ slevy je: {typ_slevy}, Cena za jednu vstupenku po slevě: {cena_jedne} Kč, Celková cena za {pocet_osob} osob je: {celkova_cena} Kč")