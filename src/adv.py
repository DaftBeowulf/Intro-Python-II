from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def move(direction):
    n = "n_to"
    s = "s_to"
    e = "e_to"
    w = "w_to"
    if True:
        player.location = player.location["n_to"]
    else:
        print("You cannot go in that direction.")


print(
    f"\nCurrent room: {player.location.name}\n{player.location.description}\n")
user = input("Where do you go?\n[n] North\n[e] East\n[s] South\n[w] West\n")

while True:
    if user == "n":
        if hasattr(player.location, "n_to"):
            player.location = player.location.n_to
        else:
            print("You can't go that way -- try something else.")
    elif user == "e":
        if hasattr(player.location, "e_to"):
            player.location = player.location.e_to
        else:
            print("You can't go that way -- try something else.")
    elif user == "s":
        if hasattr(player.location, "s_to"):
            player.location = player.location.s_to
        else:
            print("You can't go that way -- try something else.")
    elif user == "w":
        if hasattr(player.location, "s_to"):
            player.location = player.location.s_to
        else:
            print("You can't go that way -- try something else.")

    if user == "q":
        print("\nFarewell...\n")
        break
    print(
        f"\nCurrent room: {player.location.name}\n{player.location.description}\n")
    user = input(
        "Where do you go?\n[n] North\n[e] East\n[s] South\n[w] West\n")
