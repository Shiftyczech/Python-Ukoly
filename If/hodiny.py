input = float(input("Kolik je hodin?: "))

if input < 0:
    print("Hodina nemůže být záporná.")
elif input > 24:
    print("Hodina nemůže být větší než 24.")
elif 0 <= input < 5:
    print("Dobrou noc.")
elif 5 < input < 9:
    print("Dobré ráno.")
elif 9 < input < 12:
    print("Dobré dopoledne.")
elif 12 < input < 17:
    print("Dobré odpoledne.")
elif 17 < input < 22:
    print("Dobré večer.")
elif 22 < input < 24:
    print("Dobrý noc.")