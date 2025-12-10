def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    value = binarni_cislo if isinstance(binarni_cislo, str) else str(binarni_cislo)
    # transfer binarni_cislo into an iterable instance (str)
    result = 0
    for power,value in enumerate(value[::-1]):
        # enumerate from the back side of the sting
        result += int(value) * 2**power
    return result

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

if __name__ == "__main__":
 # Algoritmus pro převod z binární do desítkové formy
 # Každá číslice v binárním tvaru má pozici (index), začínající od nuly zprava doleva.
 # Každá číslice se násobí 2 na mocninu své pozice.
 # Všechny přijaté hodnoty se sečtou a vytvoří se desetinné číslo.

 # Algoritmus pro převod z desítkové soustavy do dvojkové soustavy
 # Vydělte číslo 2 a zapište zbytek dělení.
 # Výsledný podíl opět vydělte 2 a zapište zbytek.
 # Opakujte proces, dokud se podíl nerovná nule.
 # Zbytky zapsané v opačném pořadí tvoří binární reprezentaci čísla.
    test_funkce()
