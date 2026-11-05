import random

tajne_cislo = random.randint(1, 20)

tip = 0
pokusy = 0
max_pokusy = 5

while tip != tajne_cislo and pokusy < max_pokusy:
    tip = int(input("Uhádni tajné číslo od 1 do 20: "))
    
    if 1 <= tip <= 20:
        pokusy += 1
        if tip > tajne_cislo:
            print("Tvoje číslo je větší než tajné číslo.")
        elif tip < tajne_cislo:
            print("Tvoje číslo je menší než tajné číslo.")
        else:
            print(f"Gratuluji! Uhodl jsi tajné číslo ({tajne_cislo}) na {pokusy}. pokus.")
    else:
        print("Zadal jsi číslo mimo rozsah 1-20. Zkus to znovu.")
       

if tip != tajne_cislo and pokusy >= max_pokusy:
    print(f"Překročil jsi {max_pokusy} pokusů. Tajné číslo bylo {tajne_cislo}.")

    