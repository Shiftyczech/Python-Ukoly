import math

# KONTROLA PRVOČÍSLA
je_prvocislo = True #stanovená proměná

print("Kontrola prvočísla")
cislo = int(input("Zadejte číslo: "))

if cislo < 2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True
elif cislo % 2 == 0:
    je_prvocislo = False
else:
    delitel = 3
    while delitel * delitel <= math.isqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel += 2


if je_prvocislo:
    print(f"Číslo {cislo} je prvočíslo")
else:
    print(f"Číslo {cislo} není prvočíslo")