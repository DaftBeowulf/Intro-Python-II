from player import player
from enemy import enemies
from images import images


def fight(enemy):
    print(
        f"\n{enemy.name} stands before you, full of hate and killing intent!")
    cmd = input(
        f"\nWatch out, {player.name}!\n(Listen! Type 'navi' to see a list of battle commands)\n").split(' ')

# fight loop
    while player.health > 0 and enemy.health > 0:
        if len(cmd) == 1:
            cmd = ''.join(cmd)
            if cmd == "a" or cmd == "attack":
                player.attack(enemy)
                if enemy.health > 0:
                    enemy.attack(player)
            elif cmd == "d" or cmd == "defend":
                player.defense = player.defense * 2
                enemy.attack(player)
                player.defense = player.defense // 2
            elif cmd == 'navi':
                print(images['battle navi'])
            elif cmd == "s" or cmd == 'stats':
                print(player)
            elif cmd == 'q':
                print("\nCOWARD!")
                exit()
            elif cmd == "e" or cmd == 'escape':
                if enemy.name == 'ganon':
                    print(
                        f'\nBooming laughter fills the chamber as Ganon mocks your attempt to run away.\nThere\'s no escape, brat!')
                else:
                    print(f'\nYou successfully run from battle!')
                    break
            else:
                print(
                    f"\nStay focused, {player.name}! You can't do anything else until the battle is over!")
        else:
            print("\nHey! Invalid command, try something else.\n")

        # await new command
        if player.health > 0 and enemy.health > 0:
            cmd = input(
                f"\nWatch out, {player.name}!\n(Listen! Type 'navi' to see a list of battle commands)\n").split(' ')
        else:
            break

    if enemy.health <= 0 and not enemy.name == 'Ganon':
        player.location.enemy = {}
        player.location.clear_path()
    if enemy.health <= 0 and enemy.name == 'Ganon':

        print("""\nGanon has been defeated, you beat the game! 
Wait... a golden glow shines from above, 
and a holy object from the Goddesses floats down towards you...!""", images['triforce'], """\nYou got the Triforce! Thanks for playing :)""")
        exit()
    elif player.health <= 0:
        print(
            images['game over'], "\nYou died! Maybe try again after you find some better equipment?")
        exit()
