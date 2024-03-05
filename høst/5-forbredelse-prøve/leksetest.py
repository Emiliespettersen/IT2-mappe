# IT2: Uke 5 - Leksetest


# Oppgave 1
# a) Hva bør funksjonen under hete?
# b) Kommenter hver linje

def høyeste_tall (tall_liste):                                        
    høyeste = tall_liste[0]              #Setter "høyeste" til å være det første i en liste
    for tall in tall_liste:              #for et tall i tall_liste så gjelder:
        if tall > høyeste:               #hvis tall er høyere enn det høyeste 
            høyeste = tall               #Hvis det gjelder så bytter vi ut høyeste med tall
    return høyeste                       # da gis tilbake det høyeste tallet.


# Oppgave 2
# a) Hva gjør koden under? Den teller antall ",", ".", "'" i tekst.
# b) Kommenter hver linje
tekst = "International Talk Like a Pirate Day is a parodic holiday created in 1995 by John Baur and Mark Summers of Albany, Oregon, who proclaimed September 19 each year as the day when everyone in the world should talk like a pirate. It has since been adopted by the Pastafarianism movement as an official holiday."
antall = 0
for bokstav in tekst:
    if bokstav in [",", ".", "'"]:
        antall += 1
print(antall)


# Oppgave 3
# a) Hva gjør kode 1? 
# b) Hva gjør break?
# c) Hva er forskjellen på kode 1 og kode 2?
# d) Hva gjør return?
## Kode 1
while True:
    tekst = input("Skriv en tekst: ")
    if not ("Æ" in tekst.upper() or "Ø" in tekst.upper() or "Å" in tekst.upper()):
        break
print(tekst)
## Kode 2
def hent_ASCII_string(spørsmål):
    while True:
        tekst = input(spørsmål)
        if not ("Æ" in tekst.upper() or "Ø" in tekst.upper() or "Å" in tekst.upper()):
            return tekst
        
tekst = hent_ASCII_string("Skriv en tekst: ")
print(tekst)



