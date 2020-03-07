# -*- coding: utf-8 -*-
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
    reduced mana cost
    
"""
import random
from colorama import Fore, Style


class CharacterBase:
    Level = 1;
    Class = "";
    
    """Character base stats"""
    Armorplating = 0;
    Aerodynamics = 0;
    Quantumshield = 0;
    Criticalchance = 0;
    Ciriticalmulti = 0;
    Attackspeed = 0;
    Hullprotection = 100;
    Quantumentanglement = 0;
    Aerodynamics = 0;
    LifeSteal = 0;
    CoolDownReduction = 0;
    ManaCostReduction = 0;
    Allattributesmod = 0;
    HullProtectionmod = 0;
    Quantumentanglementmod = 0;
    Aerodynamicsmod = 0;
    Physicallow = 0;
    Physicalhigh = 0;
    Electriclow = 0;
    Electrichigh = 0;
    Icelow = 0;
    Icehigh = 0;
    Heatlow = 0;
    Heathigh = 0;
    Radiationlow = 0;
    Radiationhigh = 0;
    
    """Sanpshot of characters stats"""
    ArmorplatingSNAP = 0;
    AerodynamicsSNAP = 0;
    QuantumshieldSNAP = 0;
    CriticalchanceSNAP = 0;
    CiriticalmultiSNAP = 0;
    AttackspeedSNAP = 0;
    HullprotectionSNAP = 100;
    QuantumentanglementSNAP = 0;
    AerodynamicsSNAP = 0;
    LifeStealSNAP = 0;
    CoolDownReductionSNAP = 0;
    ManaCostReductionSNAP = 0;
    AllattributesmodSNAP = 0;
    HullProtectionmodSNAP = 0;
    QuantumentanglementmodSNAP = 0;
    AerodynamicsmodSNAP = 0;
    PhysicallowSNAP = 0;
    PhysicalhighSNAP = 0;
    ElectriclowSNAP = 0;
    ElectrichighSNAP = 0;
    IcelowSNAP = 0;
    IcehigSNAP = 0;
    HeatlowSNAP = 0;
    HeathighSNAP = 0;
    RadiationlowSNAP = 0;
    RadiationhighSNAP = 0;
    
        
class MapTile:
    ItemsList = []
    name = "";
    
    def __init__(self, name):
        self.name = name
        print("It's just stars all the way down");
    
    """def PrintTypes(self, NewItem):"""
        
"""Item Class"""    
class Item:
    Type = ""
    Implicit = ""
    Prefix1 = ""
    Prefix2 = ""
    Prefix3 = ""
    Suffix1 = ""
    Suffix2 = ""
    Suffix3 = ""    
    
    def __init__(self, rand, LiveMap):
        """what kind of item is it"""
        if rand == 1:
            self.GeneratePistol(LiveMap)
        elif rand == 2:
            self.GenerateSMG(LiveMap)
        elif rand == 3:
            self.GenerateSniper(LiveMap)
        elif rand == 4:
            self.GenerateGem(LiveMap)

    def GeneratePistol(self, LiveMap):
        self.Type = "Pistol"
        
        print(Fore.WHITE + "GeneratePistol is working!")
        mods = 0;
        
        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,3); 
        
        if rarity == 2:
            print(Fore.RED + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + "Common Item");
        
        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items")
            
            """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self)
            
        print("\n");
    
    def GenerateSMG(self, LiveMap):
        self.Type = "SMG"
        
        print(Fore.WHITE + "GenerateSMG is working!");
        mods = 0;
        
        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,3); 
        
        if rarity == 2:
            print(Fore.RED + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + "Common Item");
            
        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items")
        
        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self)
            
        print("\n");
    
    
    def GenerateSniper(self, LiveMap):
        self.Type = "Sniper"
        
        print(Fore.WHITE + "GenerateSniper is working!")
        mods = 0;
        
        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,3); 
        
        if rarity == 2:
            print(Fore.RED + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + "Common Item");
        
        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items")
        
        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self)
        
        print("\n");
        
    def GenerateGem(self, LiveMap):
        self.Type = "Gem"
        
        print(Fore.WHITE + "GenerateGem is working!");
        mods = 0;
        
        """rarity determines gem """
        rarity = random.randrange(0,3);
        
        if rarity == 2:
            print(Fore.MAGENTA + "Alpha Gem increasing tier of modifiers by 3");
        elif rarity == 1:
            print(Fore.YELLOW + Style.BRIGHT + "Beta Gem increasing tier of modifiers by 1");
        elif rarity == 0:
            print(Fore.GREEN + "Gamma Gem increasing tier of modifiers by 1");
            
        """quantity of mods"""
        if rarity > 0:
            mods = 1;
            count = 1;
        elif rarity == 0: 
            print("no modifiers on Gamma Gems")
            
        """Generate modifiers for Alpha and Beta gems"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self)
            
        print("\n");
    
def GenerateMap(name):
    LiveMap = MapTile(name)
    return (LiveMap)
    
def EnemyDies(LiveMap):
    rand = random.randrange(1,5);
    NewItem = Item(rand, LiveMap)
    return (NewItem)
    
"""equiping or using an item"""
def UpdateCharacterStats():
    return(0);


    
        

"""  
def MakeFiftyItems():    
    numberofitems = 50;
    
    while numberofitems > 0:
        rand = random.randrange(1,5);
        GenerateItem(rand);
        numberofitems = numberofitems-1;"""
    
"""Main"""
newitem = 0;
rand = 0;
mods = 0;
rarity = 0;
name = "I am a new Map"

print(Fore.WHITE + Style.BRIGHT + "rand is " + str(rand) + "\n");


print(Fore.WHITE + Style.BRIGHT + "\n");
LiveMap = GenerateMap(name);
NewItem = EnemyDies(LiveMap);
    
print(Fore.WHITE + "End of runtime successful");