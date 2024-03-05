import os
import sys

def rens_terminal():
    if sys.platform == "windows":
        os.system("cls")
    else: 
        os.system("clear")


#3.1 - Hovedmeny
#Lag en hovedmeny i terminalen med valgene:
# 1. Se pokemonoversikt
# 2. Se treneroversikt
# 3. Lag trener
# 4. Avslutt

print("--velkommen til pokemon-spill--")

while True:
    rens_terminal ()
    print("--Pokemon-spill--")

    print("1: Vis pokemonoversikt oversikt")
    print("2: Se treneroversikt")
    print("3: Lag trener")
    print("4: Avslutt")
    brukervalg = input("> ")


    if brukervalg == "1":
        rens_terminal ()
        print("Pokemonoversikt")
        #for pokemon in pokemoner:
            #print(pokemon)
        input("trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("treneroversikt")
        input("trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "3":
        print("lag en trener")
        input("trykk enter for å gå tilbake til hovedmenyen")

    elif brukervalg == "4":
        print("avslutt..")
        break
    else:
        print("ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmenyen")

print("Takk for nå!")


#3.2 - Lese inn data
#Last ned filen pokemon.json (opens in a new tab).
#Les inn filen i et python-program og lagre innholdet i en variabel.
