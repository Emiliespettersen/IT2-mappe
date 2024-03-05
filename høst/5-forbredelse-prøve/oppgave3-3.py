# Lag en funksjon fjern_falske_brukere som tar inn en liste med brukernavn 
#og et nøkkelord, og returnerer en liste med brukernavn som ikke inneholder 
#nøkkelordet. For eksempel skal 
#fjern_falske_brukere(["thorc", "ravim", "ceiliet", "fredrikg"], "fred") returnere["thorc", "ravim", "ceciliet"]

def main():  #Dette er definisjonen av hovedfunksjonen i programmet. Alle instruksjoner som skal kjøres, er inneholdt innenfor denne funksjonen.
    alle_brukere= ["thorc", "ravim", "ceiliet", "fredrikg"] # Her definerer vi en liste kalt "alle_brukere" som inneholder fire strenger (brukernavn).
    nokkelord = "fred"  #Dette oppretter en variabel kalt "nokkelord" og gir den verdien "fred". Dette er nøkkelordet vi skal bruke til å filtrere brukerlisten.
 #Her kaller vi funksjonen fjern_falske_brukere med to argumenter: "alle_brukere" (brukerlisten) og "nokkelord" (det nøkkelordet vi ønsker å filtrere etter). Resultatet av denne funksjonskallet blir skrevet ut.
    print (fjern_falske_brukere(alle_brukere, nokkelord))


#Dette er definisjonen av en annen funksjon kalt "fjern_falske_brukere". 
# Denne funksjonen tar to argumenter: "brukerliste" (en liste med brukernavn) og "nokkelord" (et ord vi vil bruke til å filtrere brukerlisten).
def fjern_falske_brukere(brukerliste, nokkelord):
    ekte_brukere = [] #Her oppretter vi en tom liste kalt "ekte_brukere", som vi vil bruke til å lagre brukernavnene som passerer filtreringen.
    for bruker in brukerliste: #Dette er en for-løkke som itererer gjennom hvert element (brukernavn) i "brukerliste".
        if nokkelord not in bruker: #Dette er en betinget setning som sjekker om "nokkelord" ikke er en del av "bruker" (brukernavnet). Hvis nøkkelordet ikke finnes i brukernavnet, legges brukernavnet til i "ekte_brukere"-listen.
            ekte_brukere.append(bruker) #Hvis betingelsen i linje 8 er sann (nøkkelordet finnes ikke i brukernavnet), legger vi brukernavnet til i "ekte_brukere"-listen ved hjelp av append-metoden.
    return ekte_brukere #Til slutt returnerer funksjonen listen "ekte_brukere" som inneholder brukernavnene som bestod filtreringen.

main()