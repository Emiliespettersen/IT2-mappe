
# OPPGAVE 1

# Lag en fil lovetester.py som du skriver all koden i. Skriv et enkelt Python-program som leser inn navnet på to personer og lagrer navnene i to variable. Definer en variabel match som har verdien 0.
# Vi ønsker å starte med å konvertere navnene til små bokstaver slik at sammenligningene vi skal gjøre blir enklere. Du kan konvertere et navn til små bokstaver slik:
#        navn1 = navn1.lower()
# Denne enkle boten bryr seg kun om navnene til de to personene:

# • Tips: •

# Hvisnavneneerlikelangeerbotenganskefornøyd,ogsieratmatchener60%.
# Hvis navnene ikke er like lange, men begynner med samme forbokstav, er boten fortsatt litt optimistisk, og spår at matchen er 40%. Hvisingenavkraveneoveroppfylles,erbotenmistfornøyd,ogmatchenerbare15%.
# Dukanhenteutdenførsteboktaventilenstrengslik:
# Lengdentilenstrengkanhentesutmedfunksjonenlen:
#        navn = "Ola"
#        forste_bokstav = navn[0]
#        lengde = len(navn)
# Test programmet ditt med et par navn, og sjekk at riktig match-prosent printes.
match = 0

navn1 = input("hva er det første navnet? ")
navn2 = input("hva er det andre navnet? ")

navn1 = navn1.lower()
navn2 = navn2.lower()

første_bokstav1 = navn1[0] #denne sier av første bokstaven"[0]" som er den første bokstaven i f.eks navnet Emilie så er 0 = e.
første_bokstav2 = navn2[0]


#hvis navnet har like mange bukstaver så får den 60%
if len(navn1) == len(navn2):
    match = 60
elif første_bokstav1 == første_bokstav2:
    match = 40
else: match = 15



print("match:", match, "%")
print(f"{navn1} og {navn2} matcher {match} %")

#oppgave 2
