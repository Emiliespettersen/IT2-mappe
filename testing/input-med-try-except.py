# et program som fortsetter helt til bruker har skrevet riktig inout

år = 2024

while True:
    try:
        alder = int(input("Hvor gammel blir du i år"))
        break
    except:
        print("Ugyldig input. Alder må være et tall")

fødselsår = år - alder
print(f"Du er født i {fødselsår}")