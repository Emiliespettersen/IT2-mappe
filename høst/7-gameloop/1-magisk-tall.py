import random

# Gamelook-mønsteret

# 1. oppsett
magisk_tall = random.randit(1,10)
antall_forsøk = 0
# Game loop:
spill = True
while spill:
    # 2. Håndter input
    brukerinput = int (input ("Hva er det magniske tallet? "))
    if brukerinput == "avslutt":
        break
    # 3. Oppdater spill
    antall_forsøk += 1
    # 4. Tegn (print)
    if brukerinput > magisk_tall:
        print ("for høyt")
    elif brukerinput < magisk_tall:
        print ("for lavt")
    else:
        print("Riktig! Antall forsøk: {antall_forsøk}")
        break