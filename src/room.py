# Implement a class to hold room information. This should have name and
# description attributes.
from item import items
from images import images
from enemy import enemies


class Room():
    def __init__(self, name, description, items=[], image="", looted=False, looted_msg="", interactive=[], next_room={}, cleared=True, cleared_msg=""):
        self.name = name
        self.description = description
        self.items = items
        self.image = image
        self.looted = looted
        self.looted_msg = looted_msg
        self.interactive = interactive
        self.next_room = next_room
        self.cleared = cleared
        self.cleared_msg = cleared_msg
        self.enemy = []

    def clear_path(self):
        self.cleared = True
        setattr(self, f'{self.next_room["direction"]}_to',
                room[f'{self.next_room["name"]}'])


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "\nNorth of you, the entrance to Ganon's lair beckons. A torch is set in the wall next to the entrance.",
                     [items['torch']], images['outside'],
                     looted_msg="\nNorth of you, the entrance to Ganon's lair beckons. There's an empty hole in the wall where the torch was once set."),

    'foyer': Room("Foyer", """\nDim light filters in from the south. Dusty passages run north and east, and 
a small set of stairs leads down into west. The skeletal remains of a fallen warrior 
are nearby, sword and shield still gripped tightly.""",
                  [items['sword'], items['shield']],
                  looted_msg="""\nDim light filters in from the south. Dusty passages run north and east, and a small 
set of stairs leads down into west. The skeleton's hands are now empty."""),

    'overlook': Room("Grand Overlook", """\nA steep cliff appears before you, falling
away into the darkness. Ahead to the north, 
a light flickers on the other side of the impassable chasm. 
The vague impression of a raised drawbridge is barely visible.
An unlit torch stands next to the edge.""",
                     cleared_msg="""\nA steep cliff appears before you, falling
away into the darkness. The torch has been lit and the way north across the bridge is clear!""",
                     cleared=False,
                     interactive=[items['torch']],
                     next_room={'direction': 'n', 'name': 'boss_door'}),

    'boss_door': Room("Boss Door", """\nAn imposing, giant door blocks your path north. 
Black chains cover its surface, all connected to a 
shining gold lock in the shape of a horned demon skull. 
You cannot go forward without a key.""",
                      cleared_msg="""\nThe lock has fallen away from the door, the chains
loosened and pooled on the floor. The way
west is clear... if you dare.
    """,
                      cleared=False,
                      interactive=[items['key']],
                      next_room={'direction': 'w', 'name': 'boss_chamber'}),

    'boss_chamber': Room("Boss Room", """\nThe door slams shut behind you as you enter. 
You are in a dimly-lit, immense circular chamber with no other exits. 
Out of the darkness, a voice laughs menacingly.
'So, you've finally arrived... time to die like the insect you are!'
The enormous Ganon lumbers into view, wielding enormous twin blades. 
He leers at you menacingly and prepares to fight!""",
                         cleared=False,
                         cleared_msg="""\nGanon's corpse lays on the ground, dark blood smoking as it drips onto the floor.
The great evil has been defeated... for now."""),

    'pool': Room("Pool", """\nA hole in the cavern's ceiling illuminates a crystal-clear pool of water.
To the north, a small alcove is embedded in the wall with a treasure chest inside.
A snarling dodongo blocks your path to the chest.""",
                 cleared=False,
                 next_room={'direction': 'n', 'name': 'treasure'},
                 cleared_msg="""\nA hole in the cavern's ceiling illuminates a crystal-clear pool of water.
To the north, a small alcove is embedded in the wall with a treasure chest inside.
The path to the chest is clear now that the dodongo has been slain."""),

    'treasure': Room("Treasure Chest", "\nA resplendant treasure chest sits in the alcove before you. Golden light beams out as you open it, to find... a key!", [items['key']],
                     looted_msg="\nThe treasure chest has been emptied, there's nothing of interest here anymore"),

    'storage': Room("Storage Room", """\nVarious supplies and heavy crates litter the small, stone room. 
A steel plate lies in the corner of the room, embedded into the floor.""",
                    [items['crate']],
                    cleared_msg="""\nThe switch has been weighed down with the crate, 
    and an eerie passageway has appeared in the southern wall.
    An ethereal glow can be seen, gently piercing the darkness within.""",
                    interactive=[items['crate']],
                    next_room={'direction': 's', 'name': 'vault'},
                    cleared=False,
                    looted_msg="""\nThere's one less crate in the pile of crates. You stare at the steel plate in the ground thoughtfully. It kind of looks like a switch, now that you think about it..."""),

    'vault': Room('Vault', """\nAngelic hymns fill the air. A stone pedestal sits on a raised dais before you.
From the cracked ceiling above, a thin sunbeam shines down
to illuminate the legendary blade set into the pedestal--the Master Sword!""",
                  [items['master sword']],
                  looted_msg="""\nWith the pedestal empty and the Master Sword in your grasp, there's nothing of interest here.""")
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
room['vault'].n_to = room['storage']
room['overlook'].s_to = room['foyer']
room['boss_door'].s_to = room['overlook']

# Add enemies to rooms
room['pool'].enemy = enemies['dodongo']
room['boss_chamber'].enemy = enemies['ganon']

# locked until conditions are met:
# room['pool'].n_to = room['treasure']
# room['storage'].s_to = room['vault']
# room['overlook'].n_to = room['boss_door']
# room['boss_door'].w_to = room['boss_chamber']
