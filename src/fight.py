from adv import player
from enemy import enemies
from image import images


def fight(enemy):
    print(
        f"\n{enemy.name} stands before you, full of hate and killing intent!")
    cmd = input(
        f"\nWatch out, {player.name}!\n(Listen! Type 'navi' to see a list of battle commands)\n").split(' ')

# fight loop
    while player.health > 0 and enemy.health > 0:
        if len(cmd == 1):
            cmd = ''.join(cmd)
            if cmd == "attack":
                player.attack(enemy)
                if enemy.health > 0:
                    enemy.attack(player)
                else:
                    player.location.enemies = []
                    player.location.cleared = True
            elif cmd == "defend":
                player.defense = player.defense * 2
                enemy.attack(player)
                player.defense = player.defense // 2
            elif cmd == 'navi':
                print(images['battle navi'])
            elif cmd == 'q':
                print("COWARD!")
                exit()
            else:
                print(
                    f"Stay focused, {player.name}! You can't do anything else until the battle is over!")
        else:
            print("\nHey! Invalid command, try something else.\n")

        # await new command
        cmd = input(
            f"\nWatch out, {player.name}!\n(Listen! Type 'navi' to see a list of battle commands)\n").split(' ')
