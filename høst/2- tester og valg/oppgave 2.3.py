valg= input("Vil du ha fanta? ")

if valg == "ja":
    print("Her er Fantaen din")
elif valg == "nei":
    valg = input("Vil du heller ha Cola?")
    if valg == "ja":
        print("her er Colaen din")
    elif valg == "nei":
        valg = input("Vil du heller ha pepsi?")
        if valg=="ja":
            print("her er pepsien din")
        elif valg == "nei":
            print("synd da får du ikke brus.")


