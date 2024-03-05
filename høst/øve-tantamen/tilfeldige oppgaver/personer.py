class Person:
    def __init__(self, fornavn: str, etternavn: str, år: int) -> None:
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = år
        self.familie = []


    def beregn_alder (self):
        return 2023 - self.fødselsår


    def vis_info(self):
        print (self.fornavn, self.etternavn, self.beregn_alder())

    def legg_til_familiemedlem(self, person):
        self.familie.append(person)

    def vis_familie_info(self):
        for medlemmer in self.familie:
            medlemmer.vis_info()


charly = Person("charlotte", "gundby", 2005)
emilie = Person ("emilie", "pettersen", 2004)
charly.legg_til_familiemedlem(emilie)
charly.vis_familie_info()


charly.vis_info()
emilie.vis_info()
