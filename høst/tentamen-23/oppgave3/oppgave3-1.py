

#oppgave 3.1
def per_stream(land):
    utbetalinger = {"Norge": 0.55, "Sverige": 0.44, "Finland": 0.44, "Danmark": 0.52, "island": 0.62}
    # Sjekk om landet er i oversikten over utbetalinger
    if land in utbetalinger:
        return utbetalinger[land]
    else:
        return 0.22
   


print(per_stream("Norge"))
print(per_stream("USA"))


#oppgave 3.2
def andel_til_artist(antall_streams):
    if antall_streams < 399_999:
        return 0
    elif antall_streams < 29_999_999:
        return 0.40
    else:
        return 0.70
    

print(andel_til_artist(50_000))
print(andel_til_artist(5_000_000))
print(andel_til_artist(50_000_000))


#oppgave 3.3
def penger_tjent(antall_streams, land):
    utbetaling = per_stream(land)
    andel_artist = andel_til_artist(antall_streams)
    penger_tjent = antall_streams * utbetaling * andel_artist

    return penger_tjent
print(penger_tjent(5_000_000, "norge"))


#oppgave 3.4
def populære(artistliste):
    populære_artister = []
    for artist_info in artistliste:
        artistnavn, antall_streams = artist_info

        if antall_streams > 100_000_000:
            populære_artister.append(artist_info)

    return populære_artister

artistliste = [
    ["Taylor swift", 106_506_306],
    ["Drake", 104_405_304],
    ["Lady gaga", 84_425_314],
    ["Arif", 50_605_334]
]
resultat = populære(artistliste)
print (resultat)


#oppgave 3.5
def royalties(artistliste, land):

    utbetaling = per_stream(land)
    andel_artist = andel_til_artist(antall_streams)
    penger_tjent = antall_streams * utbetaling * andel_artist
    
    for artist_info in artistliste:
        artistnavn, antall_streams, penger_tjent = artist_info

artister = [
    ["Emma steinbakken", "norge", 3_406_407],
    ["Lasse", "sverige", 500_406_306]
]
print (artister)
#her på den siste så prøvde jeg å kompinere 3.4 og 3.3 for å lage sånn den skulle være.

#JOBBE MER MED!!!!!




    


