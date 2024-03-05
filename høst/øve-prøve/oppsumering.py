print("emilie")
print(1 + 2)

#variabler
a = 5 #dette er en variabel
b = 8
print(a + b)


#Input
navn = input("hva heter du?")
print("Hei" + navn)


#if-setninger
spørsmål = input("Hva lurer du i dag? ")        #spørsmål er det vi spør om

if spørsmål == "Hva er pinkoden min":           #det første alternativet som gir et svar
    print("Pinkoden din er 1814")  
elif spørsmål == "Hvor mye data har jeg igjen": #eller det andre alternativet som gir et svar
    print("Du har 8 GB")
else:
    print("Nå skjønner jeg ikke hva du mener!") #hvis du ikke spiller noen av disse to spørsmålene så printes dette svaret


#gjøre tekst til tall
inpTall = input("Gi meg et tall")
tall = int(inpTall)
print(1000 + tall)


#mer om if-setninger (flere dimensjoner)
inpAlder = input("Hvor gammel er du?")  
alder = int(inpAlder)# Gjør om input fra bruker til et heltall - int

if alder < 7:
    print("Velkommen til barnehagen")
    if alder < 4:
        print("Du skal til småbarna")
    else:
        print("Du skal til de store barna")  
        
else:
    print("Du har kommet feil. Du skal på skolen")
#oppagve
voksen = input("Er du voksen? (ja/nei): ")
gravid = input("Er du gravid? (ja/nei): ")

if voksen == "ja":
    print("Du er voksen")
    if gravid == "ja":
        print("Du kan ikke kjøre karusell når du er gravid")
    else:
        print("Du er voksen og ikke gravid. Velkommen til karusellen")
    
    
else:
    print("Du er ikke voksen. Kom tilbake senere")


#If-setninger med and og or
#and
if voksen == "ja" and gravid == "nei":      #Hvis du er begge så kan du kjøre karusell
    print("Du kan kjøre karusell")
else:
    print("Du må være voksen og ikke gravid")

#or 
if voksen == "ja" or gravid == "nei":       #hvis du er en av delene så kan du kjøre karusell
    print("Du kan kjøre karusell")
else:
    print("Du må være voksen og ikke gravid")