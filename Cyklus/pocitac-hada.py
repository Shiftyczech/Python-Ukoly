print("Myslím si číslo od 1 do 100. Zkus ho uhodnout!")

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

while odpoved != "s":
    # Výpočet středu intervalu
    tip = (dole + nahore) // 2
    pokusy += 1
    
    # Výpis tipu a získání odpovědi od uživatele
    print(f"Můj tip je: {tip}")
    odpoved = input("Moje číslo je (v / m / s): ")
    
    # Úprava hranic podle odpovědi
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print(f"Počítač uhodl číslo na {pokusy} pokusů.")
    else:
        print("Neplatná odpověď! Zadej prosím pouze 'v', 'm' nebo 's'.")
        pokusy -= 1