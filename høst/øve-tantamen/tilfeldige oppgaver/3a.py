#program for reisekrarantene
# land = "grønn"
# vaksinert = True

# #dersom person er vakrinert--> 0 dager
# if vaksinert:
#     print("0 dager")
# # dersom uvaksinert og rød/ organge --> 10 dager
# elif land == "rød" or land == "oransj":
#     print("10 dager")
# #dersom uvaksinert og grønn--> 3 dager
# elif land == "grønn":
#     print("3 dager")




# #fullfør programmet slik at det printer riktig. Dette er en annen versjon:

# if vaksinert == True:
#     print("0 dager i karantene")
# else:
#     if land == "grønn":
#         print("3 dager")
#     elif land == "rød" or land == "oranjs":
#         print("10 dager i karantene")



#gjør dette om til en funksjon som returnerer anntall dager

def karantene(vaksinert, farge):
    if vaksinert:
        return 0
    elif farge == "rød" or farge == "oransj":
        return 10  
    elif farge == "grønn":
        return 3
    

print(karantene(True, "rød"))
print(karantene(False, "grønn"))
print(karantene(False, "rød"))
print(karantene(False, "oransj"))

