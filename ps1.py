# recent updates:
# camera updates recording camera/entity positon separate from map/entity position aside from the player
# enemy visuals arent synching properly to player movement
# enemy is walking back and forth left and right from 25 pixels to 500 pixels at a rate of 5 pixels per second
# tested the theory for using a list of changed items and updating the positions of only those 
# scrubbing the older images with that space of background
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
        """setting the rect for the camera at position 100 100 with a set width and height for 720p screen"""
#        """create dynamic screen later"""
        self.camera = pygame.Rect(100, 100, width, height)
        """width and height just to keep track"""
        self.width = width
        self.height = height
        """start the game off with no offset this will change when player moves"""
        self.offset_x = 0
        self.offset_y = 0

    def update(self, player):
        """set the x and y position for the camera based on player position"""
        self.x = -player.x + int(WIDTH / 2)
        self.y = -player.y + int(HEIGHT / 2)
        """moving the camera using new coordinates"""
        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)

class Player:
    """initialize the player"""
    def __init__(self):
        self.rect = 0
        """position in center screen"""
#        change to dynamic screen size later
        self.x = CENTERWIDTH
        self.y = CENTERHEIGHT
        """maximum amount of pixels per frame of movement"""
        self.speed = 5
        self.width = 40
        self.height = 60
        """sprite image location"""
        self.sprite = r"Sprites\Red_Player_RECT.png"
        
    """move player to mouse click coordinates"""
    def move_player(self, x_final, y_final):
        """calculate distance to identify how far to run"""
        distance = int(((self.x - x_final)** 2 + (self.y - y_final)** 2)** 0.5)

        """stop when close enough (pixels)"""
        if distance > 15:
            """set x and y distance for each frame of movement based on the speed of the character"""
            """the ratio of the distance over the speed gives us the lengths of the rise and the run for the frame"""
            move_x = int((distance / self.speed) * (x_final - self.x))
            move_y = int((distance / self.speed) * (y_final - self.y))
            """change the player position accordingly"""
            self.x = self.x + move_x
            self.y = self.y + move_y
            print(Fore.RED + "Player y: " + str(self.y))
            """increment the offsets by the distance traveled"""
            camera.offset_x = camera.offset_x - move_x
            camera.offset_y = camera.offset_x - move_y
            """move enemy visual coordinates (did not move the base x and y values)"""
            enemy.cam_x = enemy.cam_x - move_x
            enemy.cam_y = enemy.cam_y - move_y
            print(Fore.MAGENTA + "Enemy cam_y: " + str(enemy.cam_y))
        else:
            print(Fore.GREEN + "Player didn't move")
            return
        
class Enemy:
    def __init__(self):
        """first position for enemy"""
        self.x = 50
        self.y = 100
        """matching screen position"""
        self.cam_x = 50
        self.cam_y = 100
        """speed"""
        self.speed = 2
        self.dist = 1
        self.sprite = r"Sprites\Blue_Enemy_RECT.png"
        self.rect = 0
        
    def move_enemy(self):
        """just a simple back and forth movement script"""
        if self.dist:
            """goes right until 501 pixels or more"""
            self.x = self.x + self.vel
            self.cam_x = self.cam_x + self.speed
            print(Fore.BLUE + "Enemy: " + str(self.x))
            if self.x > 500:
                self.dist = 0
            
        else:
            """goes left until 25 pixels or less"""
            self.x = self.x - self.speed
            self.cam_x = self.cam_x - self.speed
            print(Fore.CYAN + "Enemy: " + str(self.x))
            if self.x < 20:
                self.dist = 1
        

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

    def __init__(self):
        """storage for all items dropped in the map"""
        self.ItemsList = []
        self.name = ""
        """sprite image location"""
        self.sprite = r"Sprites\Background_RECT.png"
        self.name = "This is a map"
        self.rect = 0
        print("It's just stars all the way down")

    def print_types(self):
        """print the types of each item on the map"""
        for i in range(len(live_map.ItemsList)):
            print(live_map.ItemsList[i].type)

class Item:
    """define all possible parameters"""
    type = ""
    rarity_string = ""
    Implicit = ""
    Prefix1 = ""
    Prefix2 = ""
    Prefix3 = ""
    Suffix1 = ""
    Suffix2 = ""
    Suffix3 = ""

    """initialize the item dynamically using rand to determine the details of the item"""
    def __init__(self, rand):
        """initialize rarity class"""
        self.Rarity = self.Rarity()
        """initialize modifiers class"""
        self.Modifiers = self.Modifiers()
        """randomly choose one of the items to generate"""
        string = GENERATORS[(rand-1)]
        print(string)
        print("self.Generate(string)")
        eval("self.Generate(string)")

    def Generate(self, generator):
        """define object type"""
        self.type = generator
        print(Fore.WHITE + Style.BRIGHT + "generate" + generator + " is working!")
        """use rand to determine the """
        self.rarity_string = self.Rarity.rarity_gen()
        """determine quantity of modifiers"""
        eval("self.Modifiers." + self.rarity_string + "(rarity)")
        """add to list of items"""
        live_map.ItemsList.append(self)
        print("\n")

    class Rarity:
        """list of rarities"""
        rarityList = ["Common", "Uncommon", "Rare"]

        def rarity_gen(self):
            """identify rarity using rand"""
            temp = random.randrange(0, len(self.rarityList))
            return self.rarityList[temp]

    class Modifiers:
        """define all parameters"""
#        fill with actual strings for modifiers later
        ModPool = [""]
        WeaponModPool = [""]
        SupportModPool = [""]
        BridgeModPool = [""]
        PowerCoreModPool = [""]
        LifeSupportModPool = [""]
        HullMaterialModPool = [""]
        ThrusteModPool = [""]
        AccessoryModPool = [""]

       """draw from 1 general mod and 2 type specific mods"""
        def Rare(self, rarity):
            """placeholder for pulling mods from mod lists"""
            print("Generating 1 GenMod and 2 typeMods")

       """draw from 1 general mod and 1 type specific mod"""
        def Uncommon(self, rarity):
            """placeholder for pulling mods from mod lists"""
            print("Generating 1 GenMod and 1 typeMod")

       """draw from 1 general mod"""
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
#    """placeholder for checking effects placed on the player"""

def MakeFiftyItems():
    """number of items to print"""
    numberofitems = 50

    while numberofitems > 0:
        rand = random.randrange(1, (len(GENERATORS) + 1))
#        will use in future updates
#            player call for item stats for instance
        Item(rand)
        numberofitems = numberofitems - 1

#"""Main"""
GENERATORS = ["Weapon", "Support", "Bridge", "PowerCore", "LifeSupport", "Thruster", "HullMaterial",
              "Accessory", "Gem"]
RAND = 0
live_map = 0
player = Player()
enemy = Enemy()
SIZE = WIDTH, HEIGHT = 1280, 720
CENTERWIDTH = WIDTH / 2
CENTERHEIGHT = HEIGHT / 2
clock = pygame.time.Clock()
camera = Camera(WIDTH, HEIGHT)
x_final = CENTERWIDTH
y_final = CENTERHEIGHT

print(Fore.WHITE + Style.BRIGHT + "RAND is " + str(RAND) + "\n")

print(Fore.WHITE + Style.BRIGHT + "\n")
"""initialize the map class"""
live_map = MapTile()

"""initialize the screen"""
active_window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My Game")

#placeholder for when i learn how to make maps
#live_map.image = pygame.image.load(live_map.sprite).convert()
#live_map.rect = live_map.image.get_rect()
#live_map.rect.topleft = (0, 0)

"""initialize player sprite and rect and position"""
player.image = pygame.image.load(player.sprite).convert()
player.rect = player.image.get_rect()
player.rect.center = (CENTERWIDTH, CENTERHEIGHT)

"""initialize enemy sprite and rect and position"""
enemy.image = pygame.image.load(enemy.sprite).convert()
enemy.rect = player.image.get_rect()
enemy.rect.center = (50, 100)

run = True

"""the main running loop"""
while run:
    """running speed in frames per second"""
    clock.tick(144)

    """event tracker"""
    for event in pygame.event.get():
        """quit the game if "x" button in corner is pressed"""
        if event.type == pygame.QUIT:
            run = False
            
        """check if mouse button one was clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            """grab mouse screen coordinate"""
            mouse_position = pygame.mouse.get_pos()
            """calculate world coordinates"""
            x_final = mouse_position[0] + camera.offset_x
            y_final = mouse_position[1] + camera.offset_y
            print(Fore.GREEN + "CLICK")

    """move player"""
    player.move_player(x_final, y_final)
    """move enemy"""
#    enemy.move_enemy()
    """position enemy rect"""
    enemy.rect.midbottom = (enemy.cam_x, enemy.cam_y)

    """blit everything"""
    active_window.blit(player.image, player.rect) 
    active_window.blit(enemy.image, enemy.rect)
#    active_window.blit(live_map.image, live_map.rect)
    camera.update(player)
    pygame.display.update()

pygame.quit()
print(Fore.WHITE + Style.BRIGHT + "End of runtime successful")
