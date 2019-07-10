# Write a class to hold player information, e.g. what room they are in
# currently.
from item import items


class Player():
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory

    def get(self, obj):
        result = any(elem.name == obj for elem in self.location.items)
        if result:
            for i in self.location.items:
                if i.name == obj:
                    self.location.items.remove(i)
            self.inventory.append(items[obj])
            print(f'{obj} has been added to your inventory.')

        else:
            print("No such item exists in this room.")

    def lookInBag(self):
        if len(self.inventory) > 0:
            print("\nDigging around in your bag, you find:")
            for item in self.inventory:
                print(f"\n{item.name}")
        else:
            print(
                "\nYou dig around in your bag and empty pockets--not an item or rupee in sight.")
