# Write a class to hold player information, e.g. what room they are in
# currently.
from item import items
from images import images
from character import Character


class Player(Character):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = [items['map']]
        self.equipped = []
        super().__init__()

    def move(self, direction):
        try:
            self.location = getattr(self.location, f'{direction}_to')
            self.inspect_room()
        except:
            print("You can't go that way -- try something else.")

    def get(self, obj):
        available = any(elem.name == obj for elem in self.location.items)
        if available:
            for i in self.location.items:
                if i.name == obj:
                    self.location.items.remove(i)
            self.inventory.append(items[obj])
            items[obj].on_take()
            self.location.looted = True
        else:
            print("\nNo such item exists in this room.")

    def drop(self, obj):
        held = any(elem.name == obj for elem in self.inventory)
        if held:
            for i in self.inventory:
                if i.name == obj:
                    self.inventory.remove(i)
            self.location.items.append(items[obj])
            items[obj].on_drop()
        else:
            print("\nYou don't have that in your inventory.")

    def look_in_bag(self):
        if len(self.inventory) > 0:
            print("\nDigging around in your bag, you find:\n")
            for item in self.inventory:
                print(f"{item.name}")
        else:
            print(
                "\nYou dig around in your bag and empty pockets--not an item or rupee in sight. You even dropped your map somewhere, geeze.")

    def inspect_room(self):
        if len(self.location.looted_msg) > 0 and len(self.location.cleared_msg) > 0:
            # currently only storage room has both
            if not self.location.looted and not self.location.cleared:
                print(
                    f"\nCurrent room: {self.location.name}\n{self.location.description}\n")
            elif self.location.looted and not self.location.cleared:
                print(
                    f"\nCurrent room: {self.location.name}\n{self.location.looted_msg}\n")
            elif self.location.looted and self.location.cleared:
                print(
                    f"\nCurrent room: {self.location.name}\n{self.location.cleared_msg}\n")
        elif len(self.location.looted_msg) > 0:
            if not self.location.looted:
                print(
                    f"\nCurrent room: {self.location.name}\n{self.location.description}\n")
            elif self.location.looted:
                print(
                    f"\nCurrent room: {self.location.name}\n{self.location.looted_msg}\n")
        elif len(self.location.cleared_msg) > 0:
            if not self.location.cleared:
                print(
                    f"\nCurrent room: {self.location.name}\n{self.location.description}\n")
            elif self.location.cleared:
                print(
                    f"\nCurrent room: {self.location.name}\n{self.location.cleared_msg}\n")

    def inspect_item(self, obj):
        held = any(elem.name == obj for elem in self.inventory)
        if held:
            for i in self.inventory:
                if i.name == obj:
                    i.inspect()

        else:
            print("\nYou don't have that in your inventory.")

    def use(self, obj):
        held = any(elem.name == obj for elem in self.inventory)
        if held:
            usable = any(
                elem.name == obj for elem in self.location.interactive)
            if usable:
                for i in self.inventory:
                    if i.name == obj:
                        self.inventory.remove(i)
                        i.use_item()
                self.location.clear_path()
            else:
                print("\nI don't think you can use that here...")
        else:
            print("\nYou don't have that in your inventory.")

    def map(self):
        if any(elem.name == 'map' for elem in self.inventory):
            print(
                f"\n{images['map']}\nYou take out your map and inspect the area.")
        else:
            print("\nUhh, did you drop your map? Why would you do that?")
