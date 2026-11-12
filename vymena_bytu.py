#Výpočet celkové výměry (v m²) bytu

# definice funkce pro výpočet obsahu obdelníka
def obsah_obdelnika( a, b):

    if a <= 0 or b <= 0:
        return  None
    obsah = a * b
    return obsah
