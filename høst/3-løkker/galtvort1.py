elever = ["hermine", "harry", "ronny"]
#print hermine. harry og ronny i terminalen ved bruk av lista.

#metode 1- Uten løkke
print(elever[0])
print(elever[1])
print(elever[2])

# metode 2- med for-løkke
for elev in elever:
    print(elev)

#metode 3-med for-løkke og range
for i in range (len(elever)):
    print(i + 1, elever[i])