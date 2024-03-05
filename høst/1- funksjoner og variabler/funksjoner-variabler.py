#innebygde funksjoner
print("hei på deg") #en innebygd funksjon som printer "hei på deg" i terminalen
input("hva heter du") #en innebygd som printer argumentet (hva heter du), lar brukeren skrive inn noe og returnere det brukeren skriver inn

#argumenter
print("hei på deg!")# funskjoner kan ta i mot argumenter, de skrives mellom parantesene
print ("hello, ", "emilie") #noen funksjoner kan ta i mot flere argumenter, da skiller vi argumentene med komma
print("hei", end="!!!", sep="!") #end er i dette tilfelle et navngitt argument (named argument)
print("verden")

#methoder
##metoder er funksjoner som hører til "ting", eksempel metoder som hører til strings
navn="emilie seth-smith pettersen"
fornavn, mellomnavn, etternavn= navn.split(" ") #split er en metode som splitter en string på argument
print(fornavn)
print(mellomnavn)
print(etternavn)


#strings (tekst)
##strings skrives mellom anførselstegn, enten enkle " eller doble " "


#egne funksjoner 

def si_hei(til):
    print("hei", til)

print("Hello, verden")
si_hei("Emilie")
