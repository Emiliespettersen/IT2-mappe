def main():
    antall = hent_nummer()
    print_mjau (antall)

def hent_nummer():
    while True:
        antall = int(input("skriv et posetivt tall: "))
        if antall > 0:
            return antall #return brukes 
        print("ugyldig tall")

def print_mjau(antall):
    print("Mjau\n" * antall, end="")

main()