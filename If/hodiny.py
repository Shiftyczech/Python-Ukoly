input = float(input("Kolik je hodin?: "))

if input < 0:
    print("Hodina nemůže být záporná.")
elif input > 24:
    print("Hodina nemůže být větší než 24.")
elif 0 < input < 8:
    print("Dobré ráno.")
elif 8 < input < 12:
    print("Dobré dopoledne.")
elif 12 < input < 18:
    print("Dobré odpoledne.")
elif 18 < input < 24:
    print("Dobrý večer.")