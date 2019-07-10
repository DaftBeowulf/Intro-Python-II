# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items=[], image="", searched=False):
        self.name = name
        self.description = description
        self.image = image
        self.items = items
        self.searched = searched

    def inspect(self):
        if len(self.items) > 0:
            print(f"You spy the following items nearby:\n")
            for item in self.items:
                print(f"{item.name}\n")

        else:
            print("You don't see anything useful nearby.")
