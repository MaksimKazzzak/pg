def cislo_text(cislo):
    # Slovníky pro převod čísel na text
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky_do_20 = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    sto = "sto"
    
    # Převod řetězce na celé číslo
    cislo = int(cislo)
    
    # Textová reprezentace čísla
    if cislo == 100:
        return sto
    elif cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        return desitky_do_20[cislo - 10]
    else:
        desitkova_cast = desitky[cislo // 10]
        jednotkova_cast = jednotky[cislo % 10]
        if cislo % 10 == 0:
            return desitkova_cast  # Např. 20, 30, 40
        else:
            return desitkova_cast + " " + jednotkova_cast  # Např. 25 -> "dvacet pět"
if __name__ == "__main__":
    cislo = input("Zadej číslo od 0 do 100: ")
    text = cislo_text(cislo)
    print(text)
