class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'\nYou picked up the {self.name}!')

    def on_drop(self):
        print(f'\nYou dropped the {self.name}...')

    def inspect(self):
        print(f"\n{self.description}")


items = {"torch": Item(
    "torch", "A still-smoldering torch--could be useful in lighting your way through the dungeon"),
    "sword": Item("sword", "A sharp and shiny blade--perfect for stabbing and slashing enemies."),
    "master_sword": Item("Master Sword", "The Sword that Seals the Darkness--the ultimate Hero's weapon"),
    "shield": Item("shield", "A mid-sized wooden shield. It looks sturdy, should be perfect for blocking enemy attacks."),
    "map": Item("map", "A map of this dungeon."),
    "boss_key": Item("boss key", "Unlocks the dungeon's final chamber."),
    "crate": Item("crate", "A large wooden crate. Don't hurt your back carrying this around!"),
    "chest": Item("treasure chest", "A crimson and gold treasure chest, just waiting to be opened to have its contents retrieved.")
}
