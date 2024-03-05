	#1. Opprett en liste som inneholder følgende heltallsverdier: 
		#6, -4, 7, -2, 8, -3, 9, -11.
	#2. Bruk en for-løkke til å iterere over alle verdiene i listen og finn den minste verdien. Skriv ut den minste verdien.
		#○ Gjør dette uten å bruke Python sin innebygde min()-funksjon.
	#3. Bruk en ny for-løkke tilsvarende oppgave b, men finn og skriv ut den største verdien.
		#○ Gjør dette uten å bruke Python sin innebygde max()-funksjon.
#Hint 
#Opprett en til variabel for å holde styr på den minste/største verdien. 

#1
liste = [6, -4, 7, -2, 8, -3, 9, -11]

#2
minste = liste [0]
for tall in liste:
    if tall < minste:
        minste = tall

print(minste)

#3
største = liste[0]
for tall in liste:
    if tall > største:
        største = tall
print(største)

