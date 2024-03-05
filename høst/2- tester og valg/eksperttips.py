prosent =int(input("hvor mange prosen t fikk du riktig på prøven? "))

if prosent>= 93.33:
    print("karakter: 6")
elif prosent < 93.33 and prosent >=85:
    print("karakter 5")
elif prosent < 85 and prosent >65:
    print("karakter 4")
elif prosent < 65 and prosent >40:
    print("karakter 3")
elif prosent < 40 and prosent >20:
    print("karakter 2")
elif prosent < 20:
    print("karakter 1")

#if-setgning på 1 linje
x=12
y=14
print("x") if x >y else print ("y")
