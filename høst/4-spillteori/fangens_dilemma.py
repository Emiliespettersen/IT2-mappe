

def beregn_score (valg_spiller1, valg_spiller2):
    if valg_spiller1 == "sammarbeid" and valg_spiller2 == "svik":
        return [5,0]
    elif valg_spiller1 == "svik" and valg_spiller2 == "sammarbeid":
        return [0,5]
    elif valg_spiller1 == "svik" and valg_spiller2 == "svik":
        return [0,0]
    elif valg_spiller1 == "sammarbeid" and valg_spiller2 == "sammarbeid":
        return [2.5,2.5]
    
    
score = beregn_score ("svik", "svik")
print(score)


#OPPAGEV 2
def spill_snilt (motspiller): #det som står mellom () er parameter
    antall_sammarbeid = motspiller.count ("sammarbeid") #.count t eller antall sammarbeid og anntall svik
    antall_svik = motspiller.count ("svik")
    if  antall_svik >  antall_sammarbeid:
        return "svik"
    else:
        return "sammarbeid"
    
#OPPGAVE 3
# Lag tilsvarende som i oppgave 2 en funksjon spill_slemt. Funksjonen skal igjen avgjøre om du ønsker å svike eller samarbeide denne ene gangen basert på informasjon om tidligere spill.
# Her skal du bruke denne regelen:
# - Samarbeid alltid de første 5 spillene
# - Svik hvis det har vært mer enn 5 tidligere spill

def spill_slemt(motspiller):
    antall_spill = len(motspiller)
    if antall_spill <=5:
        return "sammarbeid"
    else:
        return "svik"
    