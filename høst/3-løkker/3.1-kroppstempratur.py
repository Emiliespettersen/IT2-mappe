# Hos friske mennesker varierer kroppstemperaturen vanligvis mellom 36.5 og 37.5 grader.
#Lag et program som ber brukeren skrive inn kroppstemperaturen sin, avgjør om kroppstemperaturen 
#ligger henholdsvis under, innenfor eller over normal kroppstemperatur og skriver ut en passende melding.

tempratur = int(input("Hvilken kropstempratur har du? "))

if tempratur > 36.5:
    print("du har lav kroppstempratur! ring en lege")
elif tempratur < 37.5:
    print("Du har feber! ta parasett")
else:
    print("du har normal kroppstempratur")
