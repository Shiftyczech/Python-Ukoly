hodina = float(input("Kolik je hodin?: "))

if hodina < 0:
    print("Hodina nemůže být záporná.")
else:
    if hodina > 24:
        print("Hodina nemůže být větší než 24.")
    else:
        if hodina < 5:
            print("Dobrou noc.")
        else:
            if hodina < 9:
                print("Dobré ráno.")
            else:
                if hodina < 12:
                    print("Dobré dopoledne.")
                else:
                    if hodina == 12:
                        print("Dobré poledne.")
                    else:
                        if hodina < 18:
                            print("Dobré odpoledne.")
                        else:
                            if hodina < 22:
                                print("Dobrý večer.")
                            else:
                                print("Dobrou noc.")