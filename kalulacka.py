while True:
    cislo1 = int(input("Zadej první číslo: "))
    cislo2 = int(input("Zadej druhé číslo: "))      
    operace = input("Zadej operaci (+, -, *, /): ")
    if operace == "+":
        vysledek = cislo1 + cislo2  
        print(f"Výsledek: {vysledek}")
    elif operace == "-":
        vysledek = cislo1 - cislo2
        print(f"Výsledek: {vysledek}")
    elif operace == "*":
        vysledek = cislo1 * cislo2
        print(f"Výsledek: {vysledek}")
    elif operace == "/":
        vysledek = cislo1 / cislo2
        print(f"Výsledek: {vysledek}")
    opakovat = input("Chceš opakovat (ano/ne): ")
    if opakovat.lower() != "ano":
        break


