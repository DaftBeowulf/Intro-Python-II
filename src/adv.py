from player import Player
from room import Room
from images import images
from item import items
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['torch']], images['outside']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east, and a small set of stairs leads down into west.""", [items['sword'], items['shield']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
away into the darkness. Ahead to the north, a light flickers on the other side of the impassable chasm. The vague impression of a raised drawbridge is barely visible. An unlit torch stands next to the edge."""),

    'boss_door': Room("Boss Door", """An imposing, giant door blocks your path north. Black chains cover its surface, all connected to a shining gold lock in the shape of a horned demon skull. You cannot go forward without a key.""", [items['crate']]),
    'boss_chamber': Room("Boss Room", """The door slams shut behind you as you enter. You are in a dimly-lit, immense circular chamber with no other exits. Out of the darkness, a voice laughs menacingly.'So, you've finally arrived... time to die like the insect you are! The enormous Ganon lumbers into view, wielding enormous twin blades. He leers at you menacingly and prepares to fight!"""),
    'pool': Room("Pool", """A hole in the cavern's ceiling illuminates a crystal-clear pool of water. To the north, a small alcove is embedded in the wall with a treasure chest inside. A snarling dodongo blocks your path to the chest."""),
    'treasure': Room("Treasure Chest", "A resplendant treasure chest sits in the alcove before you.", [items['chest']]),
    'storage': Room("Storage Room", """Various supplies litter the small, stone room. A steel plate lies in the corner of the room, embedded into the floor."""),
    'vault': Room('Vault', """Angelic hymns fill the air. A stone pedestal sits on a raised dais before you. From the cracked ceiling above, a thin sunbeam shines down to illuminate the legendary blade set into the pedestal--the Master Sword!""", [items['master_sword']])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['pool']
room['foyer'].w_to = room['storage']
room['pool'].w_to = room['foyer']
room['treasure'].s_to = room['pool']
room['storage'].e_to = room['foyer']
room['vault'].s_to = room['storage']
room['overlook'].s_to = room['foyer']
room['boss_door'].s_to = room['overlook']

# locked until conditions are met:
room['pool'].n_to = room['treasure']
room['storage'].n_to = room['vault']
room['overlook'].n_to = room['boss_door']
room['boss_door'].n_to = room['boss_chamber']

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
    f"What do you do, {player.name}?\n(Type 'help' to see a list of commands)\n").split(' ')
while True:
    if len(user) == 2:
        user = ' '.join(user)
        if user == 'go north':
            print(user)
            if hasattr(player.location, "n_to"):
                player.location = player.location.n_to
            else:
                print("You can't go that way -- try something else.")
        elif user == 'go east':
            if hasattr(player.location, "e_to"):
                player.location = player.location.e_to
            else:
                print("You can't go that way -- try something else.")
        elif user == 'go south':
            if hasattr(player.location, "s_to"):
                player.location = player.location.s_to
            else:
                print("You can't go that way -- try something else.")
        elif user == 'go west':
            if hasattr(player.location, "w_to"):
                player.location = player.location.w_to
            else:
                print("You can't go that way -- try something else.")
        elif "get" in user:
            player.get(user.split(' ')[1])
        else:
            print("\nDoes not compute, try another command.")
    elif len(user) == 1:
        user = "".join(user)
        if user == "q":
            print("\nFarewell...\n")
            break
        elif user == "i" or user == "inventory":
            player.lookInBag()
        elif user == 'help':
            print("""\ngo <direction> -- moves player to another room
inspect [item] -- inspect the current room, or an item if included in the command 
get/take <item> -- pick up an item and add it to player inventory
drop <item> -- drop an item from player inventory
use <item> -- use an item from player inventory
i/inventory -- list all items currently held by player\n""")
        else:
            print("\nDoes not compute, try another command.")

    print(
        f"\nCurrent room: {player.location.name}\n{player.location.description}\n")
    user = input(
        f"What do you do, {player.name}?\n(Type 'help' to see a list of commands)\n").split(' ')
