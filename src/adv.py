from player import player
from images import images
from room import room
from fight import fight

# Main file for running adventure

# Initial prompt before game loop starts
print(
    f"\n{player.location.image}\nCurrent room: {player.location.name}\n{player.location.description}\n")
cmd = input(
    f"\nWhat do you do, {player.name}?\n(Listen! Type 'navi' to see a list of commands)\n").split(' ')

# Game loop
while True:

    def what(string):
        return string[string.find(' ')+1:]

    # Group multi-worded commands here
    if len(cmd) > 1:
        cmd = ' '.join(cmd)
        if cmd == 'go north':
            player.move('n')
        elif cmd == 'go east':
            player.move('e')
        elif cmd == 'go south':
            player.move('s')
        elif cmd == 'go west':
            player.move('w')
        elif "get" in cmd or 'take' in cmd:
            player.get(what(cmd))
        elif "drop" in cmd:
            player.drop(what(cmd))
        elif "inspect" in cmd:
            player.inspect_item(what(cmd))
        elif "use" in cmd:
            player.use(what(cmd))
        else:
            print("\nHey! Invalid command, try something else.\n")

    # One-worded commands here
    elif len(cmd) == 1:
        cmd = "".join(cmd)
        if cmd == "q" or cmd == "quit":
            print("\nFarewell...\n")
            break
        elif cmd == "i" or cmd == "inventory":
            player.look_in_bag()
        elif cmd == "inspect":
            player.inspect_room()
        elif cmd == "m" or cmd == "map":
            player.map()
        elif cmd == 'navi':
            print(images['navi'])
        elif cmd == 's' or cmd == "stats":
            print(player)
        elif cmd == 'fight':
            if player.location.enemy:
                fight(player.location.enemy)
            else:
                print("\nFight what? There's nobody else here.")
        else:
            print("\nHey! Invalid command, try something else.\n")

    # Catch empty or longer commands
    else:
        print("\nHey! Invalid command, try something else.\n")
    # Await new command after previous output
    cmd = input(
        f"\nWhat do you do, {player.name}?\n(Listen! Type 'navi' to see a list of commands.)\n").split(' ')
