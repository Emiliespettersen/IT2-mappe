#input er en funksjon som tar inn et argument og retjrnerer det brukeren skriver inn
navn = input("hva heter du? (fornavn og etternavn)") 
#navn er en variabel som inneholder en string
#split e en stringmetode som splitter en sting (tekst)
fornavn, etternavn = navn.split(" ")
fornavn = fornavn.capitalize() #gjør av fornavnet får stor boktav
navn= navn.title()

print ("hello ", fornavn)
print("ditt fulle navn er:", navn)