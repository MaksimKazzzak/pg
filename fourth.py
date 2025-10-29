def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda je možné tahnout figurkou na cílovou pozici podle šachových pravidel.
    
    :param figurka: Slovník obsahující typ figury a její současnou pozici.
    :param cilova_pozice: Cílová pozice na šachovnici jako dvojice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """
    
    # Extrahování pozice a typu figury
    typ = figurka["typ"]
    start_radek, start_sloupec = figurka["pozice"]
    cil_radek, cil_sloupec = cilova_pozice

    # Změna řádků a sloupců pro pohyb
    delta_radek = cil_radek - start_radek
    delta_sloupec = cil_sloupec - start_sloupec

    # 1. Ověření, že cílová pozice je uvnitř šachovnice (8x8)
    if not (1 <= cil_radek <= 8 and 1 <= cil_sloupec <= 8):
        return False

    # 2. Ověření, zda je cílová pozice volná
    if cilova_pozice in obsazene_pozice:
        return False

    # 3. Pravidla pohybu pro různé figury
    if typ == "pěšec":
        # Pěšec se může pohnout o jedno pole dopředu, nebo o dvě, pokud je na výchozí pozici (řádek 2)
        if delta_sloupec == 0 and ((delta_radek == 1) or (delta_radek == 2 and start_radek == 2 and (start_radek + 1, start_sloupec) not in obsazene_pozice)):
            return True
        return False

    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru písmene "L" (2 pole jedním směrem, 1 druhým)
        if (abs(delta_radek), abs(delta_sloupec)) in [(2, 1), (1, 2)]:
            return True
        return False

    elif typ == "věž":
        # Věž se pohybuje horizontálně nebo vertikálně a nemůže přeskakovat figury
        if delta_radek == 0:  # Horizontální pohyb
            krok = 1 if delta_sloupec > 0 else -1
            for sloupec in range(start_sloupec + krok, cil_sloupec, krok):
                if (start_radek, sloupec) in obsazene_pozice:
                    return False
            return True
        elif delta_sloupec == 0:  # Vertikální pohyb
            krok = 1 if delta_radek > 0 else -1
            for radek in range(start_radek + krok, cil_radek, krok):
                if (radek, start_sloupec) in obsazene_pozice:
                    return False
            return True
        return False

    elif typ == "střelec":
        # Střelec se pohybuje po diagonále a nemůže přeskakovat figury
        if abs(delta_radek) == abs(delta_sloupec):  # Diagonální pohyb
            krok_radek = 1 if delta_radek > 0 else -1
            krok_sloupec = 1 if delta_sloupec > 0 else -1
            for i in range(1, abs(delta_radek)):
                if (start_radek + i * krok_radek, start_sloupec + i * krok_sloupec) in obsazene_pozice:
                    return False
            return True
        return False

    elif typ == "dáma":
        # Dáma kombinuje pohyby věže a střelce
        if delta_radek == 0 or delta_sloupec == 0:
            return je_tah_mozny({"typ": "věž", "pozice": (start_radek, start_sloupec)}, cilova_pozice, obsazene_pozice)
        elif abs(delta_radek) == abs(delta_sloupec):
            return je_tah_mozny({"typ": "střelec", "pozice": (start_radek, start_sloupec)}, cilova_pozice, obsazene_pozice)
        return False

    elif typ == "král":
        # Král se může pohnout o jedno pole v jakémkoli směru
        if max(abs(delta_radek), abs(delta_sloupec)) == 1:
            return True
        return False

    return False  # Pokud typ figury neodpovídá žádné podmínce


# Testovací příklady pro ověření funkce
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # Očekáváme True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # Očekáváme False
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # Očekáváme False
    print(je_tah_mozny(vez, (8, 1), obsazene_pozice))    # Očekáváme True
    print(je_tah_mozny(strelec, (8, 5), obsazene_pozice)) # Očekáváme True
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))    # Očekáváme True
    print(je_tah_mozny(kral, (1, 5), obsazene_pozice))    # Očekáváme True
