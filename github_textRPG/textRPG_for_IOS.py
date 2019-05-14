#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:25:24 2019

@author: sheepsee
"""

import time
import random

### player setup ###
class player:
    def __init__(self):
        self.maxHp = 100
        self.hp = self.maxHp
        self.dmg = 30
        self.maxXp = 100
        self.xp = 0
        self.level = 0
player = player()
## enemy stuff ##
 
class enemy:
    def __init__(self):
        self.HP = 0
        self.dmg = 0
        self.name = ""
   
   
   
   
   
   
   
    ## start game ##
def startGame():
    gameStarted = True
    Enemy = enemy()
    def randomEnemy():
        Enemy.HP = player.level + random.randint(6,9) * random.randint(player.level + 6, player.level + 9)
        Enemy.dmg = player.level + random.randint(4,5) * random.randint(player.level + 4, player.level + 6)
        EnemyNames = ["Skeleton", "Zombie", "Bush","Jamie","Tree","Spider","Scorpion","Cyclops","Tiger"]
        Enemy.name = random.choice(EnemyNames)
   
   
    randomEnemy()
    battle(Enemy.name, Enemy.HP, Enemy.dmg)
   
   
   
 
 
 
gameStarted = False
 
 
print("###########################")
print(" Welcome to the text RPG!  ")
print("###########################")
print("         Type Play         ")
print("###########################")
## battle script ##
def battle(name,HP,dmg):
 
   
    print("###################################")
    print(" You\'ve encountered a monster! ")
    print(" "+str(name)+": HP:"+str(HP)+" DMG:"+str(dmg)    + "        ")
    print(" Player: HP:"+str(player.hp)+" DMG:"+str(player.dmg)+ " Level: "+str(player.level))
    print("###################################")
    choice = input(" Attack: \"a\" or defend: \"d\"?  ")
    print("###################################")
   
 
   
    while choice == "a":
        if choice == "a":
            if player.xp >= player.maxXp:              
                    player.level += 1
                    player.maxHp += 15
                    player.hp = player.maxHp
                    player.dmg += 5
                    player.xp = 0
                    player.maxXp += 50 
            HP -= player.dmg
           
            print(" "+str(name)+": HP:"+str(HP)+" DMG:"+str(dmg)    + "        ")
            player.hp -= dmg
            time.sleep(0.1)
            
            print(" Player: HP:"+str(player.hp)+" DMG:"+str(player.dmg)+ " Level: "+str(player.level))
            if HP <= 0 and player.hp >= 0 or HP <= 0 and player.hp > HP:
                print("")
                print("You won!")
                time.sleep(0.5)
                
                print("")
                player.xp += 25
                player.hp = player.maxHp
                startGame()
               
            if player.hp <= 0 and HP >= 0 or player.hp <= 0 and HP <= 0:
                time.sleep(0.5)
                print("")
                print("You lost!")
                print("")
               
            print("###################################")
            choice = input(" Attack: \"a\" or defend: \"d\"?  ")
            print("###################################")
    while choice == "d":
        if choice == "d":
            if player.xp >= player.maxXp:              
                    player.level += 1
                    player.maxHp += 15
                    player.hp = player.maxHp
                    player.dmg += 15   
                    player.xp = 0
                    player.maxXp += 50 
            player.hp -= dmg / 2
            HP -= player.dmg / 2
            time.sleep(0.1)
            print(" "+str(name)+": HP:"+str(HP)+" DMG:"+str(dmg)    + "        ")
            time.sleep(0.1)
            print(" Player: HP:"+str(player.hp)+" DMG:"+str(player.dmg)+ " Level: "+str(player.level))
            print("###################################")
            print(" "+str(name)+": HP:"+str(HP)+" DMG:"+str(dmg)    + "        ")
            print(" Player: HP:"+str(player.hp)+" DMG:"+str(player.dmg)+" Level: "+str(player.level))
            print("###################################")
            choice = input(" Attack: \"a\" or defend: \"d\"?  ")
            print("###################################")
            if HP <= 0 and player.hp >= 0 or HP <= 0 and player.hp > HP:
                print("")
                print("You won!")
                time.sleep(0.5)
                print("")
                player.xp += 25
                player.hp = player.maxHp
                startGame()
               
               
            if player.hp <= 0 and HP >= 0:
                time.sleep(0.5)
                print("")
                print("You lost!")
                print("")
            print("###################################")
            choice = input(" Attack: \"a\" or defend: \"d\"?  ")
            print("###################################")
    while choice == "a":
        if choice == "a":
            if player.xp >= player.maxXp:              
                    player.level += 1
                    player.maxHp += 15
                    player.hp = player.maxHp
                    player.dmg += 5
                    player.xp = 0
                    player.maxXp += 50 
            HP -= player.dmg
            print(" "+str(name)+": HP:"+str(HP)+" DMG:"+str(dmg)    + "        ")
            player.hp -= dmg
            time.sleep(0.1)
            print(" Player: HP:"+str(player.hp)+" DMG:"+str(player.dmg)+ " Level: "+str(player.level))
            if HP <= 0 and player.hp >= 0 or HP <= 0 and player.hp > HP:
                print("")
                print("You won!")
                time.sleep(0.5)
                print("")
                player.xp += 25
                player.hp = player.maxHp
                startGame()
               
            if player.hp <= 0 and HP >= 0 or player.hp <= 0 and HP <= 0:
                time.sleep(0.5)
                print("")
                print("You lost!")
                print("")
               
            print("###################################")
            choice = input(" Attack: \"a\" or defend: \"d\"?  ")
            print("###################################")
           
 
    while choice == "d":
        if choice == "d":
            if player.xp >= player.maxXp:              
                    player.level += 1
                    player.maxHp += 15
                    player.hp = player.maxHp
                    player.dmg += 15   
                    player.xp = 0
                    player.maxXp += 50 
            player.hp -= dmg / 2
            HP -= player.dmg / 2
            time.sleep(0.1)
            print(" "+str(name)+": HP:"+str(HP)+" DMG:"+str(dmg)    + "        ")
            time.sleep(0.1)
            print(" Player: HP:"+str(player.hp)+" DMG:"+str(player.dmg)+ " Level: "+str(player.level))
            print("###################################")
            print(" "+str(name)+": HP:"+str(HP)+" DMG:"+str(dmg)    + "        ")
            print(" Player: HP:"+str(player.hp)+" DMG:"+str(player.dmg)+" Level: "+str(player.level))
            print("###################################")
            choice = input(" Attack: \"a\" or defend: \"d\"?  ")
            print("###################################")
            if HP <= 0 and player.hp >= 0 or HP <= 0 and player.hp > HP:
                print("")
                print("You won!")
                time.sleep(0.5)
                print("")
                player.xp += 25
                player.hp = player.maxHp
                startGame()
               
               
            if player.hp <= 0 and HP >= 0:
                time.sleep(0.5)
                print("")
                print("You lost!")
                print("")
            print("###################################")
            choice = input(" Attack: \"a\" or defend: \"d\"?  ")
            print("###################################")
   
   
 
       
               
           
               
 
   
option = ""
while option != "play":
    option = input()
    if option == "play":
        print("Loading...")
        time.sleep(2)
        startGame()
        break
# Copyright© Sheepsee 2019.
