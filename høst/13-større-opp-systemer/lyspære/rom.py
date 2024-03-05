from lyspære import Lyspære

class Rom:
    def __init__(self):
        self._pærer = [] #i hvert rom er det mange pærer i en liste
        self._pærer: list[Lyspære] = [] # en liste med lyspærer. 

    def legg_til_pære(self,pære):
        self._pærer.append(pære)


    def skru_på_lys(self):
        for pære in self._pærer:
            pære.tenn()

    def skru_av_lys(self):
        for pære in self._pærer:
            pære.slukk()
    
    def skru_av_lys_n(self, n: int):
        self._pærer[n].slukk()

    def __str__(self): # sier hvordan stringen til et rom skal se ut
        return f"Rom:({len(self._pærer)}pærer)"

       
  

if __name__ == "__main__":
    print ("tester rom.py")
    #opprett 3 lyspærer
    stue = Rom()
    for i in range (3):
        stue.legg_til_pære(Lyspære())

    stue.skru_på_lys()
    print(stue)

                        #kan også gjøres på denne måten
                                        # pære1 = Lyspære()
                                        # pære2 = Lyspære()
                                        # pære3 = Lyspære()

                                        #opprett 1 rom
                                        # stue = Rom()

                                        # legg pærene til rommet
    
                                        # stue.legg_til_pære(pære1)
                                        # stue.legg_til_pære(pære2)
                                        # stue.legg_til_pære(pære3)

        
        