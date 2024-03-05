import random

def main():
    print("velkommen til Troskapsteten")
    resultat = spill ()
    print(resultat)

def snill (beløp):      #to forskjellige stategier
    return "behold"     #en funkjson for en snill strategi

def slem(beløp):        #en funksjon for en slem/dårlig stategi, som alltid kaster kula
    return "kast"
    
def halveis(beløp):
    if beløp >= 150000:
        return "kast"
    else:
        return "behold"
    
def veldig_usikker (beløp):
    # en spiller som kaster kula  50% av gangene
    tilfeldig_tall = random.randint(1,100)
    if tilfeldig_tall <= 50:
        return "behold"
    else: 
        return "kast"
    
def usikker (beløp):                                     #en funksjonf or en spiller som 30% av gangene kaster kula når beløpet er under 50000,
     tilfeldig_tall = random.randint(1,100)
     if beløp < 50000:                                   #og kaster kula 70% av gangene når beløpet er 50000 eller mer
        if tilfeldig_tall <= 30:
            return "kast"
        else:
            return "behold"
     else: 
         if tilfeldig_tall <= 70:
             return "kast"
         else:
            return "behold"
         
def spill():
    #en spiller som spiller troskapstesten fra paradise hotell
    #funksjonen returnerer en liste med gevinster til hver spiller
    #f.eks. [100000, 0] eller [150000, 150000] eller  [0,80000] og så vidre...

    pott = 0 #potten er 0 i starten
    for i in range (30):
        pott += 10000       #øker potten med 10000
        if veldig_usikker (pott) =="kast":
            return [pott, 0]
        elif snill (pott) == "kast":
            return [0, pott]


    return [pott / 2, pott / 2]   #ingen kastet kula, spillerene deler potten

main()