
#Pseudo koden
"""
PRINT "Skriv inn poengsummen din:"
READ poengsum
IF poengsum LESSER THAN 50
  PRINT "Ikke bestått"  
ELSE IF poengsum GREATER THAN 50 AND poengsum LESSER THAN 69
  PRINT "Bestått"     
ELSE IF poengsum GREATER THAN 70 AND poengsum LESSER THAN 89
  PRINT "Godt bestått"      
ELSE IF poengsum GREATER THAN 90 AND poengsum LESSER THAN 100
  PRINT "Meget godt bestått"         
ELSE
  PRINT "Ikke gyldig poengsum!"
ENDIF
"""

print("skriv inn poengsummen din")
poengsum = int (input("> "))
if poengsum < 50:
    print("ikke bestått")
elif poengsum > 50 and poengsum < 69:
    print("bestått")
elif poengsum > 70 and poengsum < 89:
    print("godt bestått")
elif poengsum > 90 and poengsum < 100:
    print("mye godt bestått")
else:
    print("ikke gyldig poengsum")


#Hvordan man fikser på koden
print("skriv inn poengsummen din")
poengsum = int (input("> "))
if poengsum < 50 and poengsum >= 0:
    print("ikke bestått")
elif poengsum >= 50 and poengsum <= 69:
    print("bestått")
elif poengsum >= 70 and poengsum <= 89:
    print("godt bestått")
elif poengsum >= 90 and poengsum <= 100:
    print("mye godt bestått")
else:
    print("ikke gyldig poengsum")