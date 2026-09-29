# **************
# Kalkulačka spropitného
# 29.9.2026
# **************

print("Spočítej si svoje spropitné!")

ucet = float(input("Celková částka účtu? "))

procento_spropitneho = int(input("Kolik procent spropitného chcete dát? (např. 10, nebo 15): "))

pocet_lidi = int(input("Mezi kolik lidí se účet dělí? "))


dysko = ucet * procento_spropitneho / 100
celkova_suma = ucet + dysko
podil = celkova_suma / pocet_lidi

vysledek = round(podil, 2)

print(f"Zaplatíš 1/{pocet_lidi} z {ucet} Kč, což je {vysledek} Kč na osobu.")