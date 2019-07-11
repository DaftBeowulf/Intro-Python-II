# Implement a class to hold room information. This should have name and
# description attributes.
from item import items
from images import images


class Room():
    def __init__(self, name, description, items=[], image="", searched=False, looted=""):
        self.name = name
        self.description = description
        self.items = items
        self.image = image
        self.searched = searched
        self.looted = looted


room = {
    'outside':  Room("Outside Cave Entrance",
                     "\nNorth of you, the cave mount beckons. A torch is set in the wall next to the entrance.",
                     [items['torch']], images['outside'],
                     looted="\nNorth of you, the cave mount beckons. There's an empty hole in the wall where the torch was once set."),

    'foyer': Room("Foyer", """\nDim light filters in from the south. Dusty passages run north and east, and 
a small set of stairs leads down into west. The skeletal remains of a fallen warrior 
are nearby, sword and shield still gripped tightly.""",
                  [items['sword'], items['shield']],
                  looted="""\nDim light filters in from the south. Dusty passages run north and east, and a small 
set of stairs leads down into west. The skeleton's hands are now empty."""),

    'overlook': Room("Grand Overlook", """\nA steep cliff appears before you, falling
away into the darkness. Ahead to the north, 
a light flickers on the other side of the impassable chasm. 
The vague impression of a raised drawbridge is barely visible.
An unlit torch stands next to the edge.""",
                     looted="""\nA steep cliff appears before you, falling
away into the darkness. Ahead to the north, 
a light flickers on the other side of the impassable chasm. 
The vague impression of a raised drawbridge is barely visible.
The torch has been lit and the way north across the bridge is clear!"""),

    'boss_door': Room("Boss Door", """\nAn imposing, giant door blocks your path north. 
Black chains cover its surface, all connected to a 
shining gold lock in the shape of a horned demon skull. 
You cannot go forward without a key.""",
                      looted="""\nThe lock has fallen away from the door, the chains
loosened and pooled on the floor. The way
west is clear... if you dare.
    """),

    'boss_chamber': Room("Boss Room", """\nThe door slams shut behind you as you enter. 
You are in a dimly-lit, immense circular chamber with no other exits. 
Out of the darkness, a voice laughs menacingly.
'So, you've finally arrived... time to die like the insect you are!'
The enormous Ganon lumbers into view, wielding enormous twin blades. 
He leers at you menacingly and prepares to fight!""",
                         looted="""\nGanon's corpse lays on the ground, dark blood smoking as it drips onto the floor.
The great evil has been defeated... for now."""),

    'pool': Room("Pool", """\nA hole in the cavern's ceiling illuminates a crystal-clear pool of water.
To the north, a small alcove is embedded in the wall with a treasure chest inside.
A snarling dodongo blocks your path to the chest.""",
                 looted="""\nA hole in the cavern's ceiling illuminates a crystal-clear pool of water.
To the north, a small alcove is embedded in the wall with a treasure chest inside.
The path to the chest is clear now that the dodongo has been slain."""),

    'treasure': Room("Treasure Chest", "\nA resplendant treasure chest sits in the alcove before you.", [items['chest']],
                     looted="\nThe treasure chest has been emptied, there's nothing of interest here anymore"),

    'storage': Room("Storage Room", """\nVarious supplies and heavy crates litter the small, stone room. 
A steel plate lies in the corner of the room, embedded into the floor.""",
                    [items['crate']],
                    looted="""\nThe switch has been weighed down with the crate, 
    and an eerie passageway has appeared in the southern wall.
    An ethereal glow can be seen, gently piercing the darkness within."""),

    'vault': Room('Vault', """\nAngelic hymns fill the air. A stone pedestal sits on a raised dais before you.
From the cracked ceiling above, a thin sunbeam shines down
to illuminate the legendary blade set into the pedestal--the Master Sword!""",
                  [items['master_sword']],
                  looted="""\nWith the pedestal empty and the Master Sword in your grasp, there's nothing of interest here.""")
}
