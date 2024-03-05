from rom import Rom

    #OPPAVE
# a. lag en hus klasse som inneholder rom
# b. lag en metode legg_til_rom som legger til rom i huset
# c. lag en metode:skru_av_strøm som skruk av alle lys i hele huset
# d. TEST HUSET DITT

class Hus():
    def __init__(self): #vi kjører denne motoden som kalles self
        self._rom = [] 
        self._rom: list[Rom] = [] # en liste med rom.

    def legg_til_rom(self,rom: Rom):
        self._rom.append(rom)


    def skru_av_strøm(self):
        for rom in self._rom:
            rom.skru_av_lys()


if __name__ == "__main__":
    emilies_hus = Hus()
    emilies_hus.legg_til_rom(Rom())
    
