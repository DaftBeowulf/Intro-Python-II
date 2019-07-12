

class Item():
    def __init__(self, name, description, action=''):
        self.name = name
        self.description = description
        self.action = action
        self.type = 'item'

    def on_take(self):
        print(f'\nYou picked up the {self.name}!')

    def on_drop(self):
        print(f'\nYou dropped the {self.name}...')

    def use_item(self):
        print(f'\n{self.action}')

    def __str__(self):
        return f'\n{self.description}'


class Equipment(Item):
    def __init__(self, name, description, action="", power=0, defense=0):
        self.type = 'equip'
        self.power = power
        self.defense = defense
        super().__init__(name, description, action)

    def __str__(self):
        return f"""\n{self.description}
+{self.power} ATK
+{self.defense} DEF"""


items = {"torch": Item(
    "torch", "A still-smoldering torch--could be useful in lighting your way through the dungeon",
    """Touching your torch to the unlit brazier by the chasm's edge, it flares to life, filling the room with light. 
A loud grinding sound is heard from the far side of the chasm, and the drawbridge lowers until it thuds against the edge by your feet. 
The way north across the bridge is clear!"""),
    "sword": Equipment("sword", "A sharp and shiny blade--perfect for stabbing and slashing enemies.", power=10),
    "master sword": Equipment("master sword", "The Sword that Seals the Darkness--the ultimate Hero's weapon", power=30),
    "shield": Equipment("shield", "A mid-sized wooden shield. It looks sturdy, should be perfect for blocking enemy attacks.", defense=15),
    "map": Item("map", "A map of this dungeon."),
    "key": Item("key", "The Boss key! Unlocks the dungeon's final chamber.",
                """You insert the golden Boss key into the imposing lock on the door. 
With great effort, it turns and you hear the lock's tumblers clicking. 
The lock falls to the floor, the chains which had been covering the door 
likewise falling uselessly to the door. The way west is clear...
Do not go further unless you're certain you've collected everything in the dungeon!"""),
    "crate": Item("crate", "A large wooden crate. Don't hurt your back carrying this around!",
                  """With a grunt of effort, you slide the large crate onto the steel plate. 
    The weight makes the plate sink further into the floor, and a sudden sound 
    of stone grinding on stone draws your attention. The southern wall of the room has opened, 
    revealing a set of stairs leading down away from you."""),
}
