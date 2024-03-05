#oppgave 3.3
def fjern_utsolgte (handleliste: list[str], utsolgte: list[str]):
    #returnere en ny liste spm inneholder varene i handleliste bortsettfra, 
    # de som også er i utsolgte
    ny_liste = []
    for vare in handleliste:
        if vare not in utsolgte:
            ny_liste.append(vare)
    return ny_liste

print(fjern_utsolgte(["melk", "brus", "pasta"], ["kanel", "brus"]))


