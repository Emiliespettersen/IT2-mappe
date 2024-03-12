
while True:                                             #en evig løkke. Hvis det er sant så..
    try:                                                #prøv:
        alder = int(input("Hvor gammel er du? "))       #alder skal være et tall. Skriv inn et tall
        break                                           #bryter ut av løkken hvis du har skrevet inn riktig
    except:                                             #Hvis det er noe galt så...
        print("Ugyldig input. Alder må være et tall")   # printer den dette

år = 2024                                               #året vi er i er 2024. vi trenger denne til regnestykket under
fødselsår = år - alder                                  # måten man regner ut fødselsår
print(f"Du er født i {fødselsår}")                      #printer hvilket år du er født