# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:39:49 2020

@author: Marc
"""

class Rarity :
    
    RarityList = ["common", "uncommon", "rare"];


    def genRarity();
        return random.randrange(0,len(RarityList)); 

    def isRare(rarity)
        if rarity == RarityList.rare:
            return true
        else return false;
    def isUncommon(rarity)
        if rarity == RarityList.uncommon:
            return true
        else return false;
    def isCommon(rarity)
        if rarity == RarityList.common:
            return true
        else return false;
        
  