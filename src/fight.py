from player import player
from enemy import enemies
from images import images

test = "test"


def fight(enemy):
    print(
        f"\n{enemy.name} stands before you, full of hate and killing intent!")
    cmd = input(
        f"\nWatch out, {player.name}!\n(Listen! Type 'navi' to see a list of battle commands)\n").split(' ')

# fight loop
    while player.health > 0 and enemy.health > 0:
        if len(cmd) == 1:
            cmd = ''.join(cmd)
            if cmd == "attack":
                player.attack(enemy)
                if enemy.health > 0:
                    enemy.attack(player)
            elif cmd == "defend":
                player.defense = player.defense * 2
                enemy.attack(player)
                player.defense = player.defense // 2
            elif cmd == 'navi':
                print(images['battle navi'])
            elif cmd == 'q':
                print("\nCOWARD!")
                exit()
            elif cmd == 'escape':
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
