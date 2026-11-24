# Program vykresluje geokmetrické tvary složené ze znaků hvězdička.

# funkce pro vykreslení čtverce
def ctverec(strana):
    radek = 0
    while radek < strana:
        print(strana * "*")
        radek += 1

#funkce pro vykreslení obdelníka
def obdelník(šířka, výška):
    radek = 0
    while radek < výška:
        print(šířka * "*")
        radek += 1

#funce pro vykreslení prázdného čtverce
def prazdny_ctverec(strana):
    radek = 0
    while radek < strana:
        if radek == 0 or radek == strana - 1:
            print(strana * "*")
        else:
            print("*" + (strana - 2) * " " + "*")
        radek += 1

#funkce pro vykreslení prázdného obdelníka
def prazdny_obdelník(šířka, výška):
    radek = 0
    while radek < výška:
        if radek == 0 or radek == výška - 1:
            print(šířka * "*")
        else:
            print("*" + (šířka - 2) * " " + "*")
        radek += 1

# hlavní program
print("Kreslím geometrické tvary složené ze znaků hvězdička.")

pokracovat = True
while pokracovat:
    typ = input("Zadejte typ tvaru (ctverec/obdelník): ").lower()
    plnost = input("Chcete, aby byl tvar plný? (ano/ne): ").lower()
    if typ == "ctverec":
        strana = int(input("Zadejte délku strany čtverce: "))
        if plnost == "ano":
            ctverec(strana)
        else:
            prazdny_ctverec(strana)
    elif typ == "obdelník":
        šířka = int(input("Zadejte šířku obdelníka: "))
        výška = int(input("Zadejte výšku obdelníka: "))
        if plnost == "ano":
            obdelník(šířka, výška)
        else:
            prazdny_obdelník(šířka, výška)
    else:
        print("Neplatný typ tvaru. Zadejte 'ctverec' nebo 'obdelník'.")
    odpoved = input("Chceš to zkusit znovu? (ano/ne): ").lower()
    if odpoved != "ano":
        pokracovat = False