class Sang():
    def __init__(self, tittel, artist):
        self.tittel = tittel
        self.artist = artist
        self.avspillinger = 0


    def spill(self):
        print(self.tittel, self.artist, self.avspillinger + 1) #spiller av 1 gang
        return self.artist, self.avspillinger, self.tittel
        


    def skjekk_tittel(self, tittel): #skjekker om tittelenen du hars krevet inn er den samme som din sang
        if tittel == self.tittel:
            return True
        else:
            return False

    def skjekk_artist(self, artist): #samme med artisten
        if artist == self.artist:
            return True
        else:
            return False

min_sang = Sang("Supergud", "Fieh")
print(min_sang.skjekk_tittel("Supergud"))
print(min_sang.skjekk_artist("Ha det!"))
min_sang.spill()

#lage noe som kan spille av sangene. Da spill_av vil øke med 1 hver gang

