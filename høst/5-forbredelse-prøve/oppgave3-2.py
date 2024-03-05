def main():
    navn = input ("hva heter du? ") #spør hva som er ditt navn
    skole = input ("Hvilken skole går du på? ") #spør hva som er din skole
    epost = lag_epost (navn, skole) # eposten din blir laget av funskjonen "lag_epost". med navn og skole
    print (epost)


def lag_epost (fult_navn, min_skole):
    skole = min_skole.lower()# gir skole små bokstaver
    navn = fult_navn.lower()# gir navn små bokstaver
    fornavn, etternavn = navn.split() # da splitter den fornavn og etternavn fra navn på linje 2.
    return fornavn + etternavn[0] + "@"  + skole + ".viken.no" #returnerer  fornavnet og førstebokstav i etternavnet. og @, så skolen som du skrev inn i linje 3.


main()