from player import Player
from images import images
from room import room

# Main file for running adventure

# Make a new player object that is currently in the 'outside' room.
# May come back to this to allow custom name
player = Player("Link", room['outside'])

# Helper functions

# Defines attempts at movement between rooms


def move(direction):
    try:
        player.location = getattr(player.location, f'{direction}_to')
        player.inspect_room()
    except:
        print("You can't go that way -- try something else.")


# Initial prompt before game loop starts
print(
    f"\n{player.location.image}\nCurrent room: {player.location.name}\n{player.location.description}\n")
user = input(
    f"\nWhat do you do, {player.name}?\n(Listen! Type 'help' to see a list of commands)\n").split(' ')

# Game loop
while True:

    # Group two-worded commands here
    if len(user) == 2:
        user = ' '.join(user)
        if user == 'go north':
            move('n')
        elif user == 'go east':
            move('e')
        elif user == 'go south':
            move('s')
        elif user == 'go west':
            move('w')
        elif "get" in user or 'take' in user:
            player.get(user.split(' ')[1])
        elif "drop" in user:
            player.drop(user.split(' ')[1])
        elif "inspect" in user:
            player.inspect_item(user.split(' ')[1])

        else:
            print("\nInvalid command, try something else.\n")

    # One-worded commands here
    elif len(user) == 1:
        user = "".join(user)
        if user == "q":
            print("\nFarewell...\n")
            break
        elif user == "i" or user == "inventory":
            player.look_in_bag()
        elif user == "inspect":
            player.inspect_room()
        elif user == "m" or user == "map":
            player.map()
        elif user == 'help':
            print(images['help'])
        else:
            print("\nInvalid command, try something else.\n")

    # Catch empty or longer commands
    else:
        print("\nInvalid command, try something else.\n")
    # Await new command after previous output
    user = input(
        f"\nWhat do you do, {player.name}?\n(Listen! Type 'help' to see a list of commands.)\n").split(' ')
