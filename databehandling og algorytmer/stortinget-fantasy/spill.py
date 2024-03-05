import os
import sys
import json
from politiker import Politiker

def rens_terminal():
    if sys.platform == "windows":
        os.system("cls")
    else: 
        os.system("clear")

# 1. Oppsett
with open("representanter.json", "r", encoding = "utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"] # henter ut lista med representanter

#opretter en liste med politiker objekter (objekter av klassen politiker):
politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)



print("--velkommen til Stortinget-fantasy--")

while True:
    rens_terminal ()
    print("--Stortinget-fantasy--")

    print("1: Vis politiker oversikt")
    print("2: avslutt")
    brukervalg = input("> ")


    if brukervalg == "1":
        rens_terminal ()
        print("politikeroversikt")
        for politiker in politikere:
            print(politiker)
        input("trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("avslutter..")
        break
    else:
        print("ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmenyen")

print("Takk for nå!")
