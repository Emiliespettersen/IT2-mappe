# Ordboken under har navn på land som nøkler og fargene på flagget til landene som verdier. Kopier ordboken inn i en python-fil.


# 	1. Skriv ut hele flaggOrdbok.
# 	2. Legg til et nytt land og flagget sine farger i ordboken.
# 	3. Lag en funksjon som tar inn et land som parameter, og returnerer fargene på landets flagg.
# 	4. Hvis landet ikke finnes i ordboken, skal funksjonen returnere None
# 	5. Funksjonen skal være ufølsom for store og små bokstaver (f.eks. skal brukeren kunne skrive "norge", "Norge", "NORGE", osv.)


flaggOrdbok = {
    "norge": ["rødt", "hvitt", "blått"],
    "sverige": ["blått", "gult"],
    "danmark": ["rødt", "hvitt"],
    "finland": ["hvitt", "blått"],
    "japan": ["rødt", "hvitt"],2
    "gabon": ["grønt", "gult", "blått"],
    "storbritannia": ["rødt", "blått", "hvitt"],
    "chile": ["blått", "hvitt", "rødt"]
}

print (flaggOrdbok)