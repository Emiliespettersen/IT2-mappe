# et program som finner fødselsår basert på alder

år = 2024
try:
    alder = int(input("hvor gammel blir du i år? "))
    fødselsår = år - alder
    print(f"du er førdt i {fødselsår}")
except:
    print("Ugyldig input. Input må være et tall")

print("Koden fortsetter...")

#et annet eksempel
try:
    tall= int(input("skriv et tall: "))
except:
    print("Ugyldig print. Setter 'tall' til 10 ")
    tall = 10

print(tall) # tall er 10 hvis brukeren ikke 