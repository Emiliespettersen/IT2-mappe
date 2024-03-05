fil = open("input.txt")
data = fil.read()
linjer = data.split("\n")
sum = 0

for linje in linjer:
    tall = []
    for bokstav in linje:
        if bokstav.isdigit():
            #putt bokstav i lista tall
            tall.append(bokstav)


    først_og_sist = tall[0] + tall[-1] #plusser sammen første og siste tall i lista
    sum += int(først_og_sist)
    print(først_og_sist)
    print("summen av tallene er:", sum)


