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

    # Custom three-worded command for getting/dropping master sword
    if len(cmd) == 3:
        cmd = ' '.join(cmd)
        if cmd == "get master sword" or cmd == "take master sword":
            print('check')
            player.get('master sword')
        if cmd == "drop master sword":
            player.drop('master sword')

    # Group two-worded commands here
    elif len(cmd) == 2:
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
            player.get(cmd.split(' ')[1])
        elif "drop" in cmd:
            player.drop(cmd.split(' ')[1])
        elif "inspect" in cmd:
            player.inspect_item(cmd.split(' ')[1])
        elif "use" in cmd:
            player.use(cmd.split(' ')[1])
        else:
            print("\nHey! Invalid command, try something else.\n")

    # One-worded commands here
    elif len(cmd) == 1:
        cmd = "".join(cmd)
        if cmd == "q":
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
        elif cmd == 'fight':
            if player.location.enemy:
                fight(player.location.enemy)
                if player.location.enemy.health <= 0:
                    player.location.enemy = {}
                    player.location.clear_path()
                elif player.health <= 0:
                    print(images['game over'])
                    exit()
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
