# recent updates:
#correct syntax for using Surfaces and rects appropriately for our player
#havent oriented the camera correctly i belive the movement is all working 
#but the player is locked in the top left so i cant see the movement effect
#i.e. we can only go right or down
"""
Spyder Editor

pistol mods available:
    critical strike chance
    critical strike multi
    attack speed
    armor
    evasion
    quantum shield
    aerodynamics
    hull strength
    quantum entaglement
    life steal
    reduced mana cost"""
from colorama import Fore, Style
import random, pygame
pygame.init()

class Camera:
    """initialize the camera position"""
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)

class Player:
    """initialize the player for rendering"""
    def __init__(self):
        self.x = 100
        self.y = 100
        self.vel = 5
        self.width = 40
        self.height = 60
        self.sprite = r"C:\Users\VIRID\Desktop\Sprites\Red_Player_RECT.png"
        self.rect = 0
        pygame.Vector2()
    """move player to mouse click coordinates"""
    def move_player(self, x_final, y_final):
        distance = int(((self.x - x_final)** 2 + (self.y - y_final)** 2)** 0.5)

        if distance:
            self.x = self.x + (self.vel / distance)*(x_final - self.x)
            self.y = self.y + (self.vel / distance)*(y_final - self.y)
        else:
            return

class CharacterBase:
    """define all parameters"""
    Level = 1
    Class = ""
    StatList = ["Armorplating", "Aerodynamics", "Quantumshield", "Criticalchance",
                "Criticalmulti", "Attackspeed", "Hullprotection",
                "Quantumentanglement", "Aerodynamics", "LifeSteal",
                "CoolDownReduction", "ManaCostReduction", "Allattributesmod",
                "HullProtectionmod", "Quantumentanglementmod", "Aerodynamicsmod",
                "Physicallow", "Physicalhigh", "Electriclow",
                "Electrichigh", "Icelow", "Icehigh", "Heatlow", "Heathigh",
                "Radiationlow", "Radiationhigh"]

    StatArray = []

class MapTile:
    """define all parameters"""
    ItemsList = []
    name = ""

    def __init__(self):
        self.name = "This is a map"
        print("It's just stars all the way down")

    def print_types(self):
        """print the types of each item on the map"""
        for i in range(len(live_map.ItemsList)):
            print(live_map.ItemsList[i].type)

class Item:
    """define all parameters"""
    type = ""
    rarity_string = ""
    Implicit = ""
    Prefix1 = ""
    Prefix2 = ""
    Prefix3 = ""
    Suffix1 = ""
    Suffix2 = ""
    Suffix3 = ""

    """initialize the item"""
    def __init__(self, rand):
        self.Rarity = self.Rarity()
        self.Modifiers = self.Modifiers()
        string = GENERATORS[(rand-1)]
        print(string)
        print("self.Generate(string)")
        eval("self.Generate(string)")

    def Generate(self, generator):
        """define object details"""
        self.type = generator
        print(Fore.WHITE + Style.BRIGHT + "generate" + generator + " is working!")
        self.rarity_string = self.Rarity.rarity_gen()
        eval("self.Modifiers." + self.rarity_string + "(rarity)")
        live_map.ItemsList.append(self)
        print("\n")

    class Rarity:
        """list of rarities"""
        rarityList = ["Common", "Uncommon", "Rare"]

        def rarity_gen(self):
            """identify rarity"""
            temp = random.randrange(0, len(self.rarityList))
            return self.rarityList[temp]

    class Modifiers:
        """define all parameters"""
        ModPool = [""]
        WeaponModPool = [""]
        SupportModPool = [""]
        BridgeModPool = [""]
        PowerCoreModPool = [""]
        LifeSupportModPool = [""]
        HullMaterialModPool = [""]
        ThrusteModPool = [""]
        AccessoryModPool = [""]

#       draw from 1 general mod and 2 type specific mods
        def Rare(self, rarity):
            """placeholder for pulling mods from mod lists"""
            print("Generating 1 GenMod and 2 typeMods")

#       draw from 1 general mod and 1 type specific mod
        def Uncommon(self, rarity):
            """placeholder for pulling mods from mod lists"""
            print("Generating 1 GenMod and 1 typeMod")

#       draw from 1 general mod
        def Common(self, rarity):
            """placeholder for pulling mods from mod lists"""
            print("Generating 1 GenMod")

def EnemyDies():
    """loot drops from dead enemies"""
    rand = random.randrange(1, (len(GENERATORS) + 1))
#        will use in future updates
#            player call for item stats for instance
    Item(rand)

#"""equiping or using an item"""
def UpdateCharacterStats():
    """placeholder for checking effects placed on the player"""

def MakeFiftyItems():
    """number of items to print"""
    numberofitems = 50

    while numberofitems > 0:
        rand = random.randrange(1, (len(GENERATORS) + 1))
#        will use in future updates
#            player call for item stats for instance
        Item(rand)
        numberofitems = numberofitems-1

#"""Main"""
GENERATORS = ["Weapon", "Support", "Bridge", "PowerCore", "LifeSupport", "Thruster", "HullMaterial",
              "Accessory", "Gem"]
RAND = 0
live_map = 0
player = Player()
clock = pygame.time.Clock()
x_final = 100
y_final = 100
SIZE = WIDTH, HEIGHT = 1280, 720
camera = Camera(WIDTH, HEIGHT)

print(Fore.WHITE + Style.BRIGHT + "RAND is " + str(RAND) + "\n")

print(Fore.WHITE + Style.BRIGHT + "\n")
live_map = MapTile()

active_window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My Game")


player.image = pygame.image.load(player.sprite).convert()
player.rect = player.image.get_rect()


run = True

while run:
    clock.tick(144)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            x_final = mouse_position[0] - 20
            y_final = mouse_position[1] - 60

    player.move_player(x_final, y_final)
    
    
    active_window.blit(player.image, player.rect) 
    camera.update(player)
    pygame.display.update()

pygame.quit()

print(Fore.WHITE + Style.BRIGHT + "End of runtime successful")
