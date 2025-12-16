def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    value = int(cislo)
    bin_value = ""
    while value > 0:
        # vyplňte binární číslo zprava doleva (od konce k začátku)
        bin_value = str(value % 2) + bin_value
        # Novou hodnotu celočíselného dělení čísla 2 zapíšeme do "value" a cyklus zopakujeme
        value = value // 2
    return bin_value if bin_value else "0"


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


if __name__ == "__main__":
    test_bin_to_dec()
