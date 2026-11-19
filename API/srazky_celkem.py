import urllib.request

url = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

# otevření komunikace s webovým serverem
odpoved = urllib.request.urlopen(url)

pocet_dnu = 0
srazky_celkem = 0

radek = odpoved.readline()          # čtu první řádek (V Bytech

while bool(radek):
    # tělo cyklu while se provádí, dokud je radek neprázdný
    text_radku = radek.decode("utf-8")  # dekóduji řádek z bytů na text
    srazky = float(text_radku)  # získám druhý prvek (srážky) a převedu na float
    if srazky > 0:
        pocet_dnu += 1
        srazky_celkem += srazky
    radek = odpoved.readline()      # čtu další řádky
odpoved.close()

print(srazky_celkem / pocet_dnu)  # vypíšu průměrné srážky