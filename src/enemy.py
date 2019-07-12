from character import Character


class Enemy(Character):
    def __init__(self, name):
        self.name = name
        super().__init__()


enemies = {
    'ganon': Enemy('Ganon'),
    'dodongo': Enemy('Dodongo')
}

enemies['ganon'].power = 30
enemies['ganon'].defense = 15
enemies['dodongo'].health = 50
