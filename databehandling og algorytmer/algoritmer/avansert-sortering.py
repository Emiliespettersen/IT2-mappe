personer= [
    {
        "navn": "Thor",
        "alder": 33
    },
    {
        "navn": "Ravi",
        "alder": 39
    },
    {
        "navn": "Ingrid",
        "alder": 21
    }
]

#sorterer lista med ordbøker (personer) i synkende rekkefølge på nøkkelen alder
# reverse = True betyr i synkende rekkefølge
#reverse = False er stigende rekkefølge
# ingen reverse = ... i stigende rekkefølge
sortert_personer = sorted(personer, key = lambda person:person ["alder"], reverse = True)
topp_2 = sortert_personer [:2]
print(topp_2)
print(sortert_personer)