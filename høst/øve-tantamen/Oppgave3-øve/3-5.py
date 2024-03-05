def forkort_lagliste(full):
    forkortet = []
    for lag in full:
        if not lag in forkortet:
            forkortet.append(lag) 
    return forkortet
    