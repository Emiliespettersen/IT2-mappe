class Politiker:        
    def __init__(self, politiker_ordbok: dict) -> None:
            self.fornavn: str = politiker_ordbok["fornavn"]
            self.etternavn: str = politiker_ordbok["etternavn"]
            self.parti: str = politiker_ordbok["parti"]["navn"]
            self.fylke: str = politiker_ordbok["fylke"]["navn"]
            self.kjønn: str = "kvinne" if politiker_ordbok ["kjoenn"] == 1 else "mann"

            #kan gjøres sånn også:
            #self.komiteer = []
            #for komite in politiker_ordbok ["komiteer"]:
                #komite_navn = komite["navn"]
                #self.komiteer.append(komite_navn)
            self.komiteer: list[str] = [komite["navn"] for komite in politiker_ordbok["komiteer_liste"]]
            self.verdi: int = 1000
            self.ukepoeng: list[int] = []
    
    def __str__(self):
          #spesiell-metode som bestemmer hvordan en politiker skal printes
          return f"{self.fornavn}{self.etternavn}({self.parti})"

if __name__ == "__main__":
      print("Tester Politiker-klassen")
      