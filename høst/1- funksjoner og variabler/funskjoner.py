
#egne funksjoner 

def si_hei(til): #definerer en egen funksjon med navn si_hei som tar inn en parameter med navn til
    print("hei", til)

def spør_om_navn(): #denne funksjonen returnerer en string
    navn = input("hva heter du? ")
    return navn

person1 = spør_om_navn()
person2 = spør_om_navn()
si_hei(person1)
si_hei(person2)



print("Hello, verden")
si_hei("Emilie")
si_hei("Egil")
si_hei("Isabel")