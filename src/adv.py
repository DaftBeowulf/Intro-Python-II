from player import Player
from images import images
from room import room

# Main file for running adventure

# Make a new player object that is currently in the 'outside' room.
# May come back to this to allow custom name
player = Player("Link", room['outside'])

# Initial prompt before game loop starts
print(
    f"\n{player.location.image}\nCurrent room: {player.location.name}\n{player.location.description}\n")
user = input(
    f"\nWhat do you do, {player.name}?\n(Listen! Type 'navi' to see a list of commands)\n").split(' ')

# Game loop
while True:

    # Custom three-worded command for getting/dropping master sword
    if len(user) == 3:
        user = ' '.join(user)
        if user == "get master sword" or user == "take master sword":
            print('check')
            player.get('master sword')
        if user == "drop master sword":
            player.drop('master sword')

    # Group two-worded commands here
    elif len(user) == 2:
        user = ' '.join(user)
        if user == 'go north':
            player.move('n')
        elif user == 'go east':
            player.move('e')
        elif user == 'go south':
            player.move('s')
        elif user == 'go west':
            player.move('w')
        elif "get" in user or 'take' in user:
            player.get(user.split(' ')[1])
        elif "drop" in user:
            player.drop(user.split(' ')[1])
        elif "inspect" in user:
            player.inspect_item(user.split(' ')[1])
        elif "use" in user:
            player.use(user.split(' ')[1])
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
        elif user == 'navi':
            print(images['navi'])
        else:
            print("\nInvalid command, try something else.\n")

    # Catch empty or longer commands
    else:
        print("\nInvalid command, try something else.\n")
    # Await new command after previous output
    user = input(
        f"\nWhat do you do, {player.name}?\n(Listen! Type 'navi' to see a list of commands.)\n").split(' ')
