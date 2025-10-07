def sudy_nebo_lichy(cislo): 
    if cislo % 2 == 0: 
        print("Číslo", cislo, "je sudé") 
    else: 
        print("Číslo",cislo ," je liché") 
 
cislo = int(input("Zadejte čislo:")) 
sudy_nebo_lichy(cislo)
