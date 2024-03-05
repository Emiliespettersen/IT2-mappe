
class Person:
    """
        Klasse for en person.

        Paramentre:
            fornavn(str): Personenes fornavn
            etternavn(str): Personenens etternavn
            fødselsdato (int): Personens fødselsdato på formen YYYY
    """
    def __init__(self, fornavn: str, etternavn: str, fødselsår: int):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår
      
    
    def beregn_alder (self):
        return 2023 - self.fødselsår
    
    def vis_info(self):
        print(f"{self.fornavn} {self.etternavn} ({self.beregn_alder()})")


person1 = Person("Emilie", "Pettersen", 2005)
person2 = Person("Isabel", "Pettersen", 1975)
person3 = Person("Egil", "Pettersen", 1976)

person1.vis_info()
person2.vis_info()
person3.vis_info()

class Lærer (Person):
    def __init__(self, fornavn, etternavn, fødselsår, fag):
        super(). __init__(fornavn, etternavn, fødselsår)
        self.fag = fag

class Elev (Person):
    def __init__(self, fornavn, etternavn, fødselsår, klassetrinn):
        super(). __init__(fornavn, etternavn, fødselsår)
        self.klassetrinn = klassetrinn

class Rektor (Person):
    def __init__(self, fornavn: str, etternavn: str, fødselsår: int, skole: str):
        super().__init__(fornavn, etternavn, fødselsår)
        self.skole = skole

emilie = Lærer("Emilie", "Pettersen", 2005)
isabel = Elev("Isabel", "Pettersen", 1975)
egil = Rektor("Egil", "Pettersen", 1976, "Sandvika VGS")