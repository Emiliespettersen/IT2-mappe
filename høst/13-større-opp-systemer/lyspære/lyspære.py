#lyspære
class Lyspære():
    def __init__(self): #vi kjører denne motoden som kalles self
        self._på = False

    def tenn(self):
        self._på = True

    #Hvsi det står._ så er variablemn privat og skal ikke endres på
    def slukk(self):
        self._på = False

    def er_på(self):
        #skal returnere TRUE hvis pæren er på og FALSE hvis pæren er av
        return self._på



#linja under sørger for at test-koden kun kjøres når vi trykker play på denne fila
if __name__ == "__main__":
    min_pære = Lyspære()
    stue_pære = Lyspære()
    hus_pære = Lyspære

    #tenner på pæren
    stue_pære.tenn()
    hus_pære.tenn()

    #slukker pæren  
    stue_pære.slukk()
    hus_pære.slukk()


    #brukeren trenger ikke å tenke på

    if stue_pære.er_på:
        print("pæra i stua er på!")
    
    if hus_pære.er_på:
        print("Alle pærer er på!")
    #slutt på testkode
