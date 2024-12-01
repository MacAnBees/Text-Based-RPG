"""
this is a rework of the Generic Text Based RPG, using what ive learned
to improve on the original design and make a much better experience
for players, teachers and the designer alike, Enjoy!
Thanks to our playtesters and educators:
Peyton
Bella as the slime
John "The Princess" Lastname
Ryan "Goliath" Lastname
Tori "The Aunt" Lastname
Mr. Earl, my intro to computing teacher
Teacher Chang who taught me classes
Alex
"""

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
def level_up(player):
    player.lvl = player.lvl + 1
    print(f"{player.name} is now level {player.lvl}!")
    player.sp = 3
    while player.sp > 0:
        print(f"You have {player.sp} skill points avaliable")
        print("")
        choice_stat = input("What stat would you like to put points in (Damage, Health): ")
        print("")
        choice_stat = choice_stat.lower()
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
            if choice_stat == "damage":
                player.dmgstat = player.dmgstat + stat_ammount
                player.damage = player.dmgstat + player.eqwep.dmgbf
                break

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
    
    
    
def drop(monster, player):
    dropch = random.randint(1,100)
    if 1<= monster.drop_chance <= dropch:
        print(monster.name,"dropped a", monster.drop)
        print("")
        player.inv.append(monster.drop)
        print("you picked up a", monster.drop)
        print("")
        
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
def get_monster():
    golem = Monster(10, 4, "golem", 30, "A golem lumbers forth")
    zombie = Monster(3, 3, "zombie", 5, "From the ground rises a zombie!", "health potion", 50)
    ghost = Monster(5, 2, "ghost", 10, "A ghost scares your dad")
    bella = Monster(10, 10, "Weird Ass Slime named Bella", 100, "bro that slime looks like someone I know...", "peanits", 25)
    lovelessone = Monster(5, 6, "Strange Man", 50, "A saggy eyed, very tired looking man wanders forth carrying a sword", "sword of lost love", 100)
    monsnum = random.randint(1,100)
    if monsnum > 98:
        monas = lovelessone
    elif monsnum > 90:
        monas = bella
    elif monsnum > 60:
        monas = golem
    elif monsnum > 30:
        monas = ghost
    elif monsnum < 30:
        monas = zombie
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
            print(f"you you equipped a {self.name}")
            player.inv.remove(item)
            player.eqwep = self
        player.damage = player.dmgstat + self.dmgbf
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
    "sword of lost love":Weapon(20, "Sword of Lost Love", "A sword with the blacksmith's desire for love poored into it, you can feel the sorrow and longing pulsing from the hilt.")
}
class FoodItem:
    def __init__(self,name, hp_recover, strength_buff, lore = "aint nothin here yet foo"):
        self.name = name
        self.hp_recover = hp_recover
        self.strength_buff = strength_buff
        self.lore = lore
FoodItems = {
    "peanits": FoodItem("Peanits", -3, 0, "hehehe penits"),
    "health potion": FoodItem("Health Potion", 5, 0, "A basic red potion, probably wont kill you")
    
}
#Skills
#Monster/Player Classes
class Player():
    def __init__(self,name,eqwep, eqar, hp, dmgst = 0, hpst = 0, sp = 0, inv = [], sklst = [], exp = 0, exp_thr = 20, lvl = 0):
        self.name = name
        self.eqwep = eqwep
        self.eqar = eqar
        self.hp = hp
        self.dmgstat = dmgst
        self.hpstat = hpst
        self.damage = dmgst
        self.sp = sp
        self.inv = inv
        self.sklst = sklst
        self.exp = exp
        self.exp_thr = exp_thr
        self.lvl = lvl
player = Player(playername, no_weapon, no_armor,10, 3, 10, 0, ["base sword", "health potion"], [], 0, 20)

class Monster:
   def __init__(self, hp, damage, name, exp_give, encounter_message = "An unknown monster apears!", drop = "none", drop_chance = 0):
        self.hp = hp
        self.damage = damage
        self.name = name
        self.exp_give = exp_give
        self.encounter_message = encounter_message
        self.drop = drop
        self.drop_chance = drop_chance
#Turns

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
            choice_item = input("what are you eating? ")
            choice_item = choice_item.lower()
            if choice_item in FoodItems:
                if choice_item in player.inv:
                    player.inv.remove(choice_item)
                    player.hp = player.hp + FoodItems[choice_item].hp_recover
                    if player.hp > player.hpstat:
                        player.hpstat = player.hpstat
                    if fooditems[choice_item].hp_recover != 0:
                        print("Your health is now:",(player.health))
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
            print("Your inventory:", str(player.inv)[1:-1])
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
        elif choice == "help":
            print("|GTBA COMMANDS LIST|")
            print("Fight: Regular attack, roll 20, 18 or over is a critical, 6-3 is a graze, and anything lower than 3 is a miss, the rest are hits")
            print("Run: Roll, and if you roll higher than monster hp, you escape")
            print("Check: examine an item in your inventory")
            print("Equip: Equip a weapon or peice of armor from your inventory")
            print("Inv or Inventory: List your inventory")
            print("Eat: allows you to consume a food item")
            print("Stats: Displays your stats sheet")
            print("")
        else:
            print("not an option")
def monster_turn(player, monster):
    dmg = get_damage(monster)
    player.hp = player.hp - (dmg - player.eqar.hpbf)
        
def battle():
    monster = get_monster()
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
        drop(monster, player)
        player.exp = player.exp + monster.exp_give
        level_check(player)
        battle()
    else:
        print("You can no longer continue")
battle()
