def main():
    navn = input ("hva heter du? ")
    brukernavn = lag_brukernavn (navn)
    print (brukernavn)


def lag_brukernavn (fult_navn):
    navn = fult_navn.lower()
    fornavn, etternavn = navn.split()
    return fornavn[0:2] + etternavn [0]


main()




