elever = [
    {"navn": "hermine", "hus": "griffing", "patronus": "oter"},
    {"navn": "harry", "hus": "griffing", "patronus": "hjort"},
    {"navn": "ronny", "hus": "griffing", "patronus": "Jack Russel Terrier"},
    {"navn": "Draco", "hus": "Smygard", "patronus": None}
]

#OPPGAVE: print denne infoen i terminalen
#hermine, griffing, oter

for elev in elever:
    print(elev["navn"], elev["hus"], elev ["patronus"])