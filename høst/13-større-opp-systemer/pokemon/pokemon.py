import pokemon

class Pokemon():
    def __init__(self, nummer, name, type_1, type_2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary):
        self.nummer = nummer
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def angrip(self, motstander):
        ny_hp = self.attack - motstander.defense
        if ny_hp < 0:
            motstander.hp = 0
        else:
            motstander.hp = ny_hp
        #self.hp -= motstander.attack - self.defense

    def __str__(self):
        return f"{self.name} ({self.hp})"


if __name__ == "__main__":
    charizard = Pokemon (6,"Charizard","Fire","Flying",534,78,84,78,109,85,100,1,False)
    bulba = (1,"Bulbasaur","Grass","Poison",318,45,49,49,65,65,45,1,False)
    print(charizard) #charizard(78)
    print(bulba)

    charizard.angrip(bulba)
    charizard.angrip(bulba)

    print(charizard)
    print(bulba)