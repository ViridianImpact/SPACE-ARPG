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
    
    StatList = ["Armorplating", "Aerodynamics", "Quantumshield", "Criticalchance", "Criticalmulti", 
                "Attackspeed", "Hullprotection", "Quantumentanglement", "Aerodynamics", "LifeSteal", 
                "CoolDownReduction", "ManaCostReduction", "Allattributesmod", "HullProtectionmod", 
                "Quantumentanglementmod", "Aerodynamicsmod", "Physicallow", "Physicalhigh", "Electriclow", 
                "Electrichigh", "Icelow", "Icehigh", "Heatlow", "Heathigh", "Radiationlow", "Radiationhigh"];
                
    StatArray = [];
    
        
class MapTile:
    ItemsList = [];
    name = "";
    
    def __init__(self, name):
        self.name = name;
        print("It's just stars all the way down");
    
    def PrintTypes(self, NewItem):        
        for i in range(len(LiveMap.ItemsList)):
            print(LiveMap.ItemsList[i].Type);
        
        
    
#"""Item Class"""    
class Item:
    Type = "";
    Implicit = "";
    Prefix1 = "";
    Prefix2 = "";
    Prefix3 = "";
    Suffix1 = "";
    Suffix2 = "";
    Suffix3 = "";
    
    #make a dynamic method
    def __init__(self, rand, LiveMap):
#       
        string = generators[(rand-1)];
        
        eval("self." + string + "(LiveMap)");
        
    def GenerateWeapon(self, LiveMap):
        self.Type = "Weapon";
        
        print(Fore.WHITE + Style.BRIGHT + "GenerateWeapon is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
        
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
            
#            """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
            
        print("\n");
    
    def GenerateSupport(self, LiveMap):
        self.Type = "Support";
        
        print(Fore.WHITE + "GenerateSupport is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
            
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
        
#        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
            
        print("\n");
    
    
    def GenerateBridge(self, LiveMap):
        self.Type = "Bridge";
        
        print(Fore.WHITE + Style.BRIGHT + "GenerateBridge is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
        
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
        
#        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
        
        print("\n");
        
    def GeneratePowerCore(self, LiveMap):
        self.Type = "Power Core";
        
        print(Fore.WHITE + Style.BRIGHT + "GeneratePowerCore is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
        
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
        
#        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
        
        print("\n");
        
    def GenerateLifeSupport(self, LiveMap):
        self.Type = "Life Support";
        
        print(Fore.WHITE + Style.BRIGHT + "GenerateLifeSupport is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
        
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
        
#        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
        
        print("\n");
        
    def GenerateThruster(self, LiveMap):
        self.Type = "Thruster";
        
        print(Fore.WHITE + Style.BRIGHT + "GenerateThruster is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
        
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
        
#        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
        
        print("\n");
        
    def GenerateHullMaterial(self, LiveMap):
        self.Type = "Hull Material";
        
        print(Fore.WHITE + Style.BRIGHT + "GenerateHullMaterial is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
        
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
        
#        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
        
        print("\n");
        
    def GenerateAccessory(self, LiveMap):
        self.Type = "Accessory";
        
        print(Fore.WHITE + Style.BRIGHT + "GenerateAccessory is working!");
        mods = 0;
        
#        """rarity determines quantity of modifiers"""
        rarity = random.randrange(0,RarityDef); 
        
        if rarity == 2:
            print(Fore.RED + Style.BRIGHT + "Rare Item: Maximum 2 mods");
        elif rarity == 1:
            print(Fore.GREEN + Style.BRIGHT + "Uncommon Item: Maximum 1 mod");
        elif rarity == 0:
            print(Fore.WHITE + Style.BRIGHT + "Common Item");
        
#        """quantity of mods"""
        if rarity > 0:
            mods = random.randrange(1, rarity+1);
            count = 1;
            print("we have selected " + str(mods) + " mods");        
        elif rarity == 0: 
            print("no modifiers on common items");
        
#        """generate modifiers"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
        
        print("\n");
        
    def GenerateGem(self, LiveMap):
        self.Type = "Gem";
        
        print(Fore.WHITE + Style.BRIGHT + "GenerateGem is working!");
        mods = 0;
        
#        """rarity determines gem """
        rarity = random.randrange(0,RarityDef);
        
        if rarity == 2:
            print(Fore.MAGENTA + Style.BRIGHT + "Alpha Gem increasing tier of modifiers by 3");
        elif rarity == 1:
            print(Fore.YELLOW + Style.BRIGHT + "Beta Gem increasing tier of modifiers by 1");
        elif rarity == 0:
            print(Fore.GREEN + Style.BRIGHT + "Gamma Gem increasing tier of modifiers by 1");
            
#        """quantity of mods"""
        if rarity > 0:
            mods = 1;
            count = 1;
        elif rarity == 0: 
            print("no modifiers on Gamma Gems");
            
#        """Generate modifiers for Alpha and Beta gems"""
        while (mods > 0):
            print("generating mod " + str(count));
            mods = mods - 1;
            count = count + 1;
            
        LiveMap.ItemsList.append(self);
            
        print("\n");
  
def GenerateMap(name):
    LiveMap = MapTile(name);
    return (LiveMap);
    
def EnemyDies(LiveMap):
    rand = random.randrange(1,(len(generators) + 1));
    NewItem = Item(rand, LiveMap);
    return (NewItem);
    
#"""equiping or using an item"""
def UpdateCharacterStats():
    return(0);


    
        

 
def MakeFiftyItems(LiveMap):    
    numberofitems = 50;
    
    while numberofitems > 0:
        rand = random.randrange(1,(len(generators) + 1));
        NewItem = Item(rand, LiveMap);
        numberofitems = numberofitems-1;
        
    return(NewItem);
    
#"""Main"""
newitem = 0;
rand = 0;
mods = 0;
rarity = 0;
name = "I am a new Map"
generators = ["GenerateWeapon", "GenerateSupport", "GenerateBridge", "GeneratePowerCore", "GenerateLifeSupport", "GenerateThruster", "GenerateHullMaterial", 
              "GenerateAccessory", "GenerateGem"]
RarityDef = 3;

print(Fore.WHITE + Style.BRIGHT + "rand is " + str(rand) + "\n");

print(Fore.WHITE + Style.BRIGHT + "\n");
LiveMap = GenerateMap(name);
NewItem = EnemyDies(LiveMap);
    
print(Fore.WHITE + "End of runtime successful");