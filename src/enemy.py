from character import Character


class Enemy(Character):
    def __init__(self, name):
        self.name = name
        super().__init__()


enemies = {
    'ganon': Enemy('ganon'),
    'dodongo': Enemy('dodongo')
}

enemies['ganon'].attack = 30
enemies['ganon'].defense = 15
