# Write a class to hold player information, e.g. what room they are in
# currently.
from item import items
from images import images


class Player():
    def __init__(self, name, location, inventory=[items['map']]):
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
            items[obj].on_take()
            self.location.searched = True
        else:
            print("\nNo such item exists in this room.")

    def drop(self, obj):
        result = any(elem.name == obj for elem in self.inventory)
        if result:
            for i in self.inventory:
                if i.name == obj:
                    self.inventory.remove(i)
            self.location.items.append(items[obj])
            items[obj].on_drop()
        else:
            print("\nYou don't have that in your inventory.")

    def look_in_bag(self):
        if len(self.inventory) > 0:
            print("\nDigging around in your bag, you find:")
            for item in self.inventory:
                print(f"{item.name}")
        else:
            print(
                "\nYou dig around in your bag and empty pockets--not an item or rupee in sight.")

    def inspect_room(self):
        if not self.location.searched:
            print(
                f"\nCurrent room: {self.location.name}\n{self.location.description}\n")
        else:
            print(
                f"\nCurrent room: {self.location.name}\n{self.location.looted}\n")

    def inspect_item(self, obj):
        result = any(elem.name == obj for elem in self.inventory)
        if result:
            for i in self.inventory:
                if i.name == obj:
                    i.inspect()

        else:
            print("\nYou don't have that in your inventory.")

    def map(self):
        if any(elem.name == 'map' for elem in self.inventory):
            print(
                f"\n{images['map']}\nYou take out your map and inspect the area.")
        else:
            print("\nUhh, did you drop your map? Why would you do that?")
