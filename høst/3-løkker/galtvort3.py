hus = {
    "hermine": "griffing",
    "harry": "griffing",    #"harry" er en nøkkel
    "draco": "Smygard"
}

#print(hus["hermine"])    #får ut huset til hermine

for elev in hus:
    #print(elev, hus[elev], sep=": ")    #sep = ": " er mellomrom
    print(f"{elev}({hus[elev]})")