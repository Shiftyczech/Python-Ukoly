POCET_MESICU_MAX = 12

pocet_mesicu = int(input("Zadej počet měsíců simulace (1 až 12): "))

while pocet_mesicu < 1 or pocet_mesicu > POCET_MESICU_MAX:
	pocet_mesicu = int(input("Zadej číslo od 1 do 12: "))

a = 1
b = 1
mesic = 1

while mesic <= pocet_mesicu:
	if mesic > 2:
		dopredu = a + b
		a = b
		b = dopredu

	if b == 1:
		nazev = "pár"
	elif b < 5:
		nazev = "páry"
	else:
		nazev = "párů"

	print(f"Měsíc {mesic}: {b} {nazev}")
	print("🐇" * b)
	mesic = mesic + 1
