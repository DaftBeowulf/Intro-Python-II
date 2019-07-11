from player import Player
from images import images
from room import room
# Declare all the rooms

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['pool']
room['foyer'].w_to = room['storage']
room['pool'].w_to = room['foyer']
room['treasure'].s_to = room['pool']
room['storage'].e_to = room['foyer']
room['vault'].n_to = room['storage']
room['overlook'].s_to = room['foyer']
room['boss_door'].s_to = room['overlook']

# locked until conditions are met:
room['pool'].n_to = room['treasure']
room['storage'].s_to = room['vault']
room['overlook'].n_to = room['boss_door']
room['boss_door'].w_to = room['boss_chamber']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Link", room['outside'])

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


print(
    f"\n{player.location.image}\nCurrent room: {player.location.name}\n{player.location.description}\n")
user = input(
    f"\nWhat do you do, {player.name}?\n(Type 'help' to see a list of commands)\n").split(' ')
while True:
    if len(user) == 2:
        user = ' '.join(user)
        if user == 'go north':
            if hasattr(player.location, "n_to"):
                player.location = player.location.n_to
                player.inspect_room()
            else:
                print("You can't go that way -- try something else.")
        elif user == 'go east':
            if hasattr(player.location, "e_to"):
                player.location = player.location.e_to
                player.inspect_room()
            else:
                print("You can't go that way -- try something else.")
        elif user == 'go south':
            if hasattr(player.location, "s_to"):
                player.location = player.location.s_to
                player.inspect_room()
            else:
                print("You can't go that way -- try something else.")
        elif user == 'go west':
            if hasattr(player.location, "w_to"):
                player.location = player.location.w_to
                player.inspect_room()
            else:
                print("You can't go that way -- try something else.")
        elif "get" in user or 'take' in user:
            player.get(user.split(' ')[1])
        elif "drop" in user:
            player.drop(user.split(' ')[1])
        elif "inspect" in user:
            player.inspect_item(user.split(' ')[1])

        else:
            print("\nDoes not compute, try another command.\n")
    elif len(user) == 1:
        user = "".join(user)
        if user == "q":
            print("\nFarewell...\n")
            break
        elif user == "i" or user == "inventory":
            player.look_in_bag()
        elif user == "inspect":
            player.inspect_room()
        elif user == "map":
            player.map()
        elif user == 'help':
            print("""\ngo <direction> -- moves player to another room
inspect [item] -- inspect an item in your inventory, or the current room 
get/take <item> -- pick up an item and add it to player inventory
drop <item> -- drop an item from player inventory
use <item> -- use an item from player inventory
i/inventory -- list all items currently held by player\n""")
        else:
            print("\nDoes not compute, try another command.\n")
    user = input(
        f"\nWhat do you do, {player.name}?\n(Type 'help' to see a list of commands)\n").split(' ')
