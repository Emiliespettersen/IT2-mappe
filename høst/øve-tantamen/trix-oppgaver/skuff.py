class Skuff():
    def __init__(self):
        self._sokke_liste = []

    def sett_inn_sokk(self, sokk):
        self._sokke_liste.append(sokk)

    def sjekk_status(self):
        antall_venstre = 0
        antall_hoyre = 0

        for sokk in self._sokke_liste:
            if sokk.hent_side() == 'V':
                antall_venstre = antall_venstre + 1

            if sokk.hent_side()== 'H':
                antall_hoyre = antall_hoyre + 1

        if antall_hoyre == antall_venstre:
            print('Alt i orden')
        else:
            print('Ulikt antall høyre- og venstresokker.')