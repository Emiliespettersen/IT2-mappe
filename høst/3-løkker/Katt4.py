

while True:
    antall = int(input("hvor mange katter har du"))
    if antall > 0:
        break #hoppe ut av løkka
    print("ugyldig! prøv igjen")

antall= int(input("hvor mange katter har du? "))
for _ in range (antall):
    print("mjau")