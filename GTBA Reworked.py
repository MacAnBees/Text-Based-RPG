"""
this is a rework of the Generic Text Based RPG, using what ive learned
to improve on the original design and make a much better experience
for players, teachers and the designer alike, Enjoy!
Thanks to our playtesters and educators:
Peyton(playtester)
Bella as the slime (weirdo slime/playtester)
John "The Princess" Lastname (playtester)
Ryan "Goliath" Lastname (Helped me with f strings and features)
Tori "The Aunt" Lastname (Playtester)
Mr. Earl, my intro to computing teacher (Taught me most of the stuff)
Teacher Chang (taught me classes and told me to look into dictionaries)
Alex(playtester)
THIS IS A PROJECT MADE SOLEY BY YURI, ANYONE WHO SAYS OTHERWISE IS A STINKY LIAR
"""
#quick note, Mr Earl if you see this, a lot more notes will be added on the final project, i need working code first
#imported modules
import random
import time
#initial input
print("run help on your turn to learn more")
playername = input("What is your name adventuerer? ")
print("")
#Needed Functions
def roll(n, roll_message = "You rolled a", rolling_message = "rolling dice..."):
    print(rolling_message)
    print("")
    diceroll = random.randint(1, n)
    time.sleep(1)
    print(roll_message, diceroll)
    print("")
    return diceroll
#Custom Roll Function
def level_up(player):
    player.lvl = player.lvl + 1
    print(f"{player.name} is now level {player.lvl}!")
    print("")
    if player.lvl == 3 or player.lvl == 6:
        print("The monsters have gotten stronger...")
        print("")
    player.hp = player.hpstat
    player.sp = 3
    while player.sp > 0:
        while True:
            print(f"You have {player.sp} skill points avaliable")
            print("")
            choice_stat = input("What stat would you like to put points in (Damage, Health): ")
            print("")
            choice_stat = choice_stat.lower()
            l = ["damage", "health"]
            if choice_stat not in l:
                print("not an optionn")
                print("")
            else:
                break
        while True:
            try:
                stat_ammount = int(input("How many points would you like to put in? "))
                print("")
            except ValueError:
                    print("")
                    print("Enter an integer please.")
                    print("")
                    break
            if stat_ammount > player.sp:
                print(f"You do not have that many stat points, you only have {player.sp} points left.")
                print("")
            player.sp = player.sp - stat_ammount
            if choice_stat == "health":
                player.hp = player.hp + stat_ammount
                player.hpstat = player.hpstat + stat_ammount
                break
            elif choice_stat == "damage":
                player.dmgstat = player.dmgstat + stat_ammount
                player.damage = player.dmgstat + player.eqwep.dmgbf
                break
#Level handling
def level_check(player):
    while player.exp >= player.exp_thr:
        if player.exp > player.exp_thr:
            exp_leftover = player.exp - player.exp_thr
        else:
            exp_leftover = 0
        player.exp = 0
        player.exp_thr = player.exp_thr + 20
        player.exp = exp_leftover
        level_up(player)
        player.exp = exp_leftover
#Level checking   

#get damge command(thanks ryan(he didnt code this but he helped me a ton))        
def get_damage(roller):
    dmgroll = roll(20, f"{roller.name} rolled ", "rolling for damage...")
    if dmgroll > 18:
        print(f"Critical! {roller.name} did {roller.damage*2} damage!")
        print("")
        dmg = roller.damage*2
    elif dmgroll > 6:
        print(f"{roller.name} did {roller.damage} damage!")
        print("")
        dmg = roller.damage
    elif dmgroll > 2:
        print(f"Graze. {roller.name} did {roller.damage/2} damage.")
        print("")
        dmg = roller.damage/2
    else:
        print("Whiffed, no damage dealt or received.")
        print("")
        dmg = 0
        
    return dmg

#These are my current monsters(Ignore the code names, a lot  of em are just inside jokes) all monsters will recive an overhaul at somepoint to make combat more interesting
def get_monster(player):
    golem = Monster(40, 4, "Golem", 80, "A golem lumbers forth")
    zombie = Monster(7, 3, "Zombie", 10, "From the ground rises a zombie!", "health potion", 50)
    ghost = Monster(15, 2, "Ghost", 30, "A ghost scares your dad")
    bella = Monster(20, 10, "Weird Ass Slime named Bella", 100, "bro that slime looks like someone I know...", "peanits", 25)
    lovelessone = Monster(20, 20, "Strange Man", 50, "A saggy eyed, very tired looking man wanders forth carrying a sword", "sword of lost love", 100)
    fallenhuman = Monster(19, 19, "Fallen Human", 20, "A being of determination manifests before you...", "real knife", 25)
    slime = Monster(8, 2, "Slime",10,  "A Slime gloops up from the floor")
    sans = Monster(1, 1, "Weak Skeleton", 10 ,"For a second you feel like you're gonna have a bad time, then you see this skeleton and the fear vanishes", "hot dog", 50)
    emoboy = Monster(15, 8, "Dark Figure", 70, "You hear papa roach playing as a dark figure aproaches", "serated knife", 10)
    knight = Monster(25, 5, "Knight", 30, "A knight clad in armor rumbles his way onto the battlefield", "health potion", 50)
    owen = Monster(9, 6, "Troll", 20, "A troll ermerged from the dark")
    #look i ran out of ideas and needed a working code
    fillermonster = Monster(8, 7, "Generic Filler Monster", 40, "A Generic Filler Monster nervously shuffles onto the battlefeild")
    if player.lvl >= 6:
        monsnum = random.randint(1,12)
    elif player.lvl >= 3:
        monsnum = random.randint(1,8)
    else:
        monsnum = random.randint(1,4)
    if monsnum == 12:
        monas = lovelessone
    elif monsnum == 11:
        monas = fallenhuman
    elif monsnum == 10:
        monas = bella
    elif monsnum == 9:
        monas = emoboy
    if monsnum == 8:
        monas = golem
    elif monsnum == 7:
        monas = knight
    elif monsnum == 6:
        monas = owen
    elif monsnum == 5:
        monas = fillermonster
    if monsnum == 4:
        monas = slime
    elif monsnum == 3:
        monas = ghost
    elif monsnum == 2:
        monas = zombie
    elif monsnum == 1:
        monas = sans
            
            
    print(monas.encounter_message)
    print("")
    return monas
    
#Items
class Weapon():
    def __init__(self, dmgbf, name, lore, givskl = "none"):
        self.dmgbf = dmgbf
        self.name = name
        self.lore = lore
        self.givskl = givskl
        
        
    def equip(self, item, player):
        if self.givskl != "none":
            player.sklst.append(self.givskl)
            print(f"you equipped a {self.name} and got the skill {self.givskl}")
            player.inv.remove(item)
            player.eqwep = self
        else:
            print(f"you equipped a {self.name}")
            player.inv.remove(item)
            player.eqwep = self
        print("")
no_weapon = Weapon(0, "No Weapon", "There is nothing here")

class Armor():
    def __init__(self, hpbf, name, lore, givskl = "none"):
        self.hpbf = hpbf
        self.name = name
        self.lore = lore
        self.givskl = givskl
        
        
    def equip(self, item, player):
        if self.givskl != "none":
            player.inv.remove(item)
            player.eqar = self
            player.sklst.append(self.givskl)
            print(f"you equipped a {self.name} and got the skill {self.givskl}")
        else:
            player.inv.remove(item)
            player.eqar = self
            print(f"you equipped a {self.name}")
        print("")
no_armor = Armor(0, "No Armor", "There is nothing here")

Equips = {
    "base sword":Weapon(2, "Base Sword", "A regular sword, there is nothing special about it."),
    "serated knife":Weapon(4, "Serated Knife", "An insanley sharp knife, it has bloodstains, You wonder what it could be from..."),
    "sword of lost love":Weapon(20, "Sword of Lost Love", "A sword with the blacksmith's desire for love poored into it, you can feel the sorrow and longing pulsing from the hilt."),
    "real knife":Weapon(10, "Real Knife", "You are filled with determination just looking at it...", "determination")
}

class FoodItem:
    def __init__(self,name, hp_recover, strength_buff, lore = "aint nothin here yet foo"):
        self.name = name
        self.hp_recover = hp_recover
        self.strength_buff = strength_buff
        self.lore = lore
FoodItems = {
    "peanits": FoodItem("Peanits", -3, 0, "hehehe penits"),
    "health potion": FoodItem("Health Potion", 5, 0, "A basic red potion, probably wont kill you"),
    "hot dog": FoodItem("Hot Dog", 3,0, "Seems fake... but its food I suppose")
}
#Skills COMING SOON™ ngl might add classes as in warrior bard an sh... yknow for class specific skills

#Monster/Player Classes
class Player():
    def __init__(self,name,eqwep, eqar, hp, dmgst = 0, hpst = 0, sp = 0, inv = [], sklst = [], exp = 0, exp_thr = 20, lvl = 0):
        self.name = name
        self.eqwep = eqwep
        self.eqar = eqar
        self.hp = hp
        self.dmgstat = dmgst + eqwep.dmgbf
        self.hpstat = hpst
        self.damage = dmgst
        self.sp = sp
        self.inv = inv
        self.sklst = sklst
        self.exp = exp
        self.exp_thr = exp_thr
        self.lvl = lvl
player = Player(playername, no_weapon, no_armor,10, 3, 10, 0, ["base sword", "health potion"], [], 0, 20)
if playername == "Yuri Durkin":
    print("Welcome back Yuri. Hope you are well.")
    print("")
    player = Player(playername, no_weapon, no_armor,100, 100, 100, 0, ["real knife"], [], 0, 10000, 100)

class Monster:
    def __init__(self, hp, damage, name, exp_give, encounter_message = "An unknown monster apears!", drop = "none", drop_chance = 0):
        self.hp = hp
        self.damage = damage
        self.name = name
        self.exp_give = exp_give
        self.encounter_message = encounter_message
        self.item = drop
        self.drop_chance = drop_chance
    
    def drop(self, player):
        dropchac = random.randint(1, 101)
        if dropchac <= self.drop_chance:
            player.inv.append(self.item)
            print(f"{self.name} dropped a {self.item}, and you picked it up.")
            print("")

#Battle Turns/Steps
def player_turn(player, monster):
    runcoun = 0
    while True:
        choice = input("what would you like to do ")
        print("")
        choice = choice.lower()
        if choice == "fight":
            dmg = get_damage(player)
            monster.hp = monster.hp - dmg
            if monster.hp < 0:
                monster.hp = 0
            print(f"{monster.name}'s health is now {monster.hp}")
            print("")
            break
        elif choice == "run":
            if runcoun < 1:
                runcha = roll(20, "You rolled a ", "Rolling to run...")
                if runcha > monster.hp:
                    print("Successfully ran away")
                    battle()
            else:
                print("Couldn't escape")
                runcoun = 1
        elif choice == "eat":
            #note to self, make this a function
            choice_item = input("what are you eating? ")
            print("")
            choice_item = choice_item.lower()
            if choice_item in FoodItems:
                if choice_item in player.inv:
                    player.inv.remove(choice_item)
                    player.hp = player.hp + FoodItems[choice_item].hp_recover
                    if player.hp > player.hpstat:
                        player.hp = player.hpstat
                    print(f"Consumed {FoodItems[choice_item].name} and recovered {FoodItems[choice_item].hp_recover} hp.")
                    print("")
                else:
                    print(f"you do not have a {choice_item}")
                    print("")
            else:
                print(f"{choice_item} does not exist or is not a food")
                print("")
        elif choice == "equip":
            choice_item = input("what would you like to equip? ")
            print("")
            choice_item = choice_item.lower()
            if choice_item in Equips:
                if choice_item in player.inv:
                    Equips[choice_item].equip(choice_item, player)
                else:
                    print(f"You do not have a {choice_item}")
                    print("")
            else:
                print(f"{choice_item} does not exist or cannot be equiped")
        elif choice ==  "run":
            runchance = roll(20)
            if runchance > 10:
                print("ran away")
                print("")
                battle()
            else:
                print("failed to run")
                print("")
                break
        elif choice == "stats":
            print(f"Your damage is: {player.damage}")
            print(f"Your hp is: {player.hp}/{player.hpstat}")
            print(f"Your level progress is: {player.exp}/{player.exp_thr}")
            print(f"Your level is {player.lvl}")
            print(f"Your equiped weapon is: {player.eqwep.name}")
            print(f"Your equiped armor is: {player.eqar.name}")
            print("")
        elif choice == "inv" or choice == "inventory":
            printedinv =  ", ".join(player.inv)
            print("Your inventory:", str(printedinv))
            print("")
        elif choice == "check":
            checked = input("What are you checking(must be in inventory): ")
            print("")
            if checked in player.inv:
                if checked in FoodItems:
                    print(FoodItems[checked].lore)
                    print("")
                elif checked in Equips:
                    print(Equips[checked].lore)
                    print("")
            else:
                print(f"You do not have a {checked}, or you mispelled it")
                print("")
        elif choice == "help":
            print("|GTBA COMMANDS LIST|")
            print("Fight: Regular attack, roll 20, 18 or over is a critical, 6-3 is a graze, and anything lower than 3 is a miss, the rest are hits")
            print("Run: Roll, and if you roll higher than monster hp, you escape")
            print("Check: examine an item in your inventory")
            print("Equip: Equip a weapon or peice of armor from your inventory")
            print("Inv or Inventory: List your inventory")
            print("Eat: allows you to consume a food item")
            print("Stats: Displays your stats sheet")
            print("|GTBA GAME MECHANICS|")
            print("As you level monsters will get stronger(every 3 levels)")
            print("Skills can be unlocked via equiping armor/weapons (Not Quite Implimented)")
            print("")
        elif choice == "skill list":
            print(f"Your skills are: {str(player.sklst)[1:-1]}")
            print("")
        else:
            print("not an option")
            print("")
def monster_turn(player, monster):
    dmg = get_damage(monster)
    player.hp = player.hp - (dmg - player.eqar.hpbf)
    if player.hp < 0:
        player.hp = 0
    print(f"{player.name}'s health is now {player.hp}")
    print("")
        
def battle():
    monster = get_monster(player)
    first = roll(20)
    if first > 10:
        print("Player goes first")
        print("")
        while True:
            if player.hp <= 0 or monster.hp <= 0:
                break
            player_turn(player, monster)
            if player.hp <= 0 or monster.hp <= 0:
                break
            monster_turn(player, monster)

    else:
        print(f"{monster.name} goes first")
        print("")
        while True:
            if player.hp <= 0 or monster.hp <= 0:
                break
            monster_turn(player, monster)
            if player.hp <= 0 or monster.hp <= 0:
                break
            player_turn(player, monster)
    if player.hp > 0:
        print(f"You killed {monster.name}")
        print("")
        monster.drop(player)
        player.exp = player.exp + monster.exp_give
        level_check(player)
        battle()
    else:
        print("You can no longer continue")
        if "determination" in player.sklst:
            time.sleep(2)
            print(...)
            time.sleep(2)
            print("But it refused")
            player.hp = player.hpstat
            print("")
            battle()
battle()
