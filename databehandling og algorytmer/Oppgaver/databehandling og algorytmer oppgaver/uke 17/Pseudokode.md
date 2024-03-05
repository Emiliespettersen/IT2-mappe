
# Pseudokode


- en måte å beskrive en algoritme eller et program på ved hjelp av naturlig språk
- brukes ofte som et verktøy for å planlegge og designe algoritmer før de faktisk blir kodet i et bestemt programmeringsspråk
- gjør det lettere å kommunisere og samarbeide med andre programmerere, samt å teste og feilsøke algoritmer før de blir kodet.
- en god måte å lære grunnleggende programmeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og logiske uttrykk fungerer sammen for å løse et bestemt problem.


## Eksempel: Penger tjent på spotify

> En algorytme som regner ut hvor mye penger vi tjener på spotify

### Psudokode i "naturlig språk"
```pseudo
Hent inn anntall streams
Hvis anntall streams er større enn 30 000 000:
    returner antall streams gange 70% (0.7)
ellers hvis antall streams er større enn 1 400 000:
    returnerer antall streams gange 40% (0.4)
ellers:
    returnerer 0
```
### Pseudo som følger UDIR-standar
```pseudo
SET antall_streams TO READ "Hvor mnage streams"
IF antall_streams GREATER THAN 30 000 000
    THEN DISPLAY antall_streams * 0.7
ELSE IF antall_streams GREATER THEN 1 400 000
    THEN DISPLAY antall_streams * 0.4
ELSE DISPLAY 0
```

### Python kode
```python
#oppgave: skirv algorytmen i vanlig python-kode:
antall_streams = int(input("hvor mange streams?"))
if antall_streams > 30_000_000:
    print (antall_streams * 0.7)
elif antall_streams > 1_400_000:
    print (antall_streams * 0.4)
else:
    print (0)


```