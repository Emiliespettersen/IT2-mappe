#oppgave: lag et program som spør brukeren: "hva er x og hva er y?" Og lagre verdier i to veriabler x og y
x=50
y=10

x= int (input("hva er x "))
y= int (input("hva er y "))

if x > y:
    print ("x er større enn y")
if x >= y:
    print("y er større eller lik x")
if x == y:
    print("x er lik y")

print ("ferdig")