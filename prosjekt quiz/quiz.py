#lag quiz med et spørsmål og få oss til å få poeng hvis vi får riktig svar

poeng = 0

spørsmål1 = input("Hva er hovedstaden i Norge? (husk stor bokstav) ")

if spørsmål1 == "Oslo":
    poeng += 1
    print("RIKTIG SVAR.")
else: 
    poeng -= 1
    print("Feil svar. Du får 1 - poeng ")

spørsmål2 = int(input("Hva er 2*2-2+2? "))

if spørsmål2 == 4:
    poeng += 1
    print("RIKTIG SVAR.")
else: 
    poeng -= 1
    print("Feil svar. Du får 1 - poeng ")

print("Din totale poengsum er:", poeng)
