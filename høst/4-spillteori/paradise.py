#simulering av troskapetstesten i paradise hotell

def main():
    pott = 0
    print("Velkommen til troskapstesten")
    for i in range (10):
        pott = pott + 10000 #vi har en pott i staten og den øker med 10k hver runde
        print(f"runde {i + 1}: {pott},-") #vi plusser på 1 for at rundene skal gå fra 1-10 istedet for 0-9
        if snill_spiller (pott) == False:
            print("snill spiller kastet kula")
            break
        elif halveis(pott) == False:
            print("slem spiller kastet kula")
            break

#oppgave: øk potten med 10k hver runde

def snill_spiller (beløp):
    return True #beholder kula

#oppagve1 lag en slem spiller
def slem_spiller(beløp):
    return False #kaster kulen

#oppgave 2 lag en spiller som kaster kula på 50000
def halveis (beløp):
    if beløp >= 50000:
        return False #kaste kula
    else:
        return True #beholde kula


main()