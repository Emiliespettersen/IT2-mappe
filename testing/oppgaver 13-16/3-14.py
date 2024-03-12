"""
Lag et program som genrerer mailadresser fra fornavn og etternavn. 
Mailen skal bestå av hele det første fornavnet og første bokstav i 
etternavnet etterfulgt av @afk.no. For eksempel skal Thor Christian Coward 
bli thorc@afk.no. Som input til programmet må brukeren skrive inn minst 
to navn (fornavn og etternavn), hvis ikke skal brukeren få en feilmelding 
og få lov til å skrive input på nytt.
"""
while True:
    navn = input("Hva heter du? ") # --> Emilie Sethsmith Pettersen
    splittet_navn = navn.split(" ") # --> ["Emilie", "Sethsmith", "Pettersen"]
    antall_navn = len(splittet_navn) # --> 3
    if antall_navn < 2:
        print("ugyldig input. Imput må bestå av minst to navn")
    else:
        break #bryter ut av løkka

fornavn = splittet_navn[0] # --> Emilie
første_bokstav_etternavn = splittet_navn[-1][0] # ---> P
mail = fornavn + første_bokstav_etternavn + "@viken.no" # --> EmilieP@viken.no

print (mail)

