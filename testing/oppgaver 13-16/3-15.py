"""
I denne oppgaven skal du lage en funksjon som returnerer True 
om et årstall er skuddår og False hvis årstallet ikke er et skuddår.
Skuddår er år som er delelige på 4 og som ikke er delelige med 100, med 
unntak for år som er delelige på 400.
Bruk assert og lag tester som sjekker alle tilfellene av skuddår
Lag funksjonen, slik at alle testene er OK
"""


def skuddår(årstall: int):
    # 2. lag funksjonen
    if årstall % 400 == 0: #hvis årstallet delt på 400 gir 0 i rest:
        return True
    if årstall % 4 == 0 and årstall % 100 != 0: #hvis årstallet delt på 4 gir 0 i rest OG årstallet delt på 100 IKKE gir 0 i rest
        return True
    else:
        return False
 
# 1. Lag tester her
# assert skuddår(2024) == True
# assert skuddår(2004) == True
# assert skuddår(2023) == False
# assert skuddår(2000) == True

år_skudd = [1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 
            1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 
            1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 
            1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 
            1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 
            1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 
            1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 
            2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 
            2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 
            2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 
            2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196]

for år in range(1704, 2197, 1): #første tallet er starten, den i midten er siste tallet og den til høyre er hvor mye den øker med
    print(år)
    if år in år_skudd:   
        assert skuddår(år) == True, f"FEIL! årstall{år} er et skuddår"
    else:
        assert skuddår(år) == False,f"FEIL! årstall {år} er IKKE et skuddår."

print("Ingen feil. Koden funerer som den skal")