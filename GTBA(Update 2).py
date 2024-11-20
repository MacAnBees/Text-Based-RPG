import random
import time
'''
Welcome to Yuri's Text based rpg battle test (MAN this needs a better name)
it currently has 4 monsters but instructions are in the code
and remember, if you wanna edit FORK FORK FORK >:3 or ill send a golem after u
Thanks to our playtesters and educators:
Peyton
Bella as the slime
John "The Princess" Lastname
Ryan "Goliath" Lastname
Tori "The Aunt" Lastname
Mr. Earl, my intro to computing teacher
Teacher Chang who taught me classes
Alex
Owen "The Troll" Lastname
'''
admin = False
print("How this game works: When the turn begins you roll a dice, if you roll a 10 or higher you go first, otherwie the monster goes first, when fighting, rolling an 8-17 or higher does your damage, rolling an 18 or higher does 2x damage, and rolling a 5-8 does half damage, 3-1 is a crit fail, when running, you need to roll more than half the monster's health, in your inventory, you have health potions, use the eat command on your turn and specifiy what you want to eat to use the health potion.")
while True:
    is_start = input("Are you ready to start? (input yes to begin) ")
    if is_start == "yes":
        break
    if is_start == "Starfall, more like LAMEFALL >:D" or is_start == "Yuri is epic fr fr" or is_start == "2172552543":
        print("you are now admin :D :D :D :D")
        admin = True

print("")

#custom roll command for all dice interaction
def roll(n, roll_message = "You rolled a", rolling_message = "rolling dice..."):
    print(rolling_message)
    print("")
    diceroll = random.randint(1, n)
    time.sleep(1)
    print(roll_message, diceroll)
    print("")
    return diceroll
#this is where monster drops are handled
def drop(monster, player):
    dropch = random.randint(1,100)
    if 1<= monster.drop_chance <= dropch:
        print(monster.name,"dropped a", monster.drop)
        print("")
        player.inv.append(monster.drop)
        print("you picked up a", monster.drop)
        print("")
    
#leveling system
def levels(player, level_val):
    player.battle_damage = player.damage
    print("you are now level", str(level_val) + "! You have 3 new stat points avaliable")
    print("")
    player.sp = player.sp + 3
    while player.sp > 0:
        stat_input = input("what would you like to put your stats in?(Health, Damage) ")
        stat_input = stat_input.lower()
        while True:
            try:
                stat_val = int(input("how many stat points would you like to put in? "))
            except ValueError:
                print("enter an integer please")
                print("")
            else:
                break
        if stat_val > player.sp:
            stat_val = player.sp
        player.sp = player.sp - stat_val
        if stat_input == "health":
            player.health = player.health + stat_val
            player.max_health = player.max_health + stat_val
            print("your health is now", (player.health))
            print("")
            print("your max health is now", (player.max_health))
            print("")
        elif stat_input == "damage":
            player.damage = player.damage + stat_val
            player.battle_damage = player.damage + stat_val
            print("your damage is now", (player.damage))
            print("")
def level_check(player):
    if player.level == 0:
        if player.exp >= 20:
            levels(player, 1)
            player.level = player.level+1
    elif player.level ==1:
        if player.exp >= 60:
            levels(player, 2)
            player.level = player.level+1
    elif player.level == 2:
        if player.exp >= 70:
            levels(player, 3)
            player.level = player.level+1
    elif player.level == 3:
        if player.exp >= 100:
            levels(player, 4)
            player.level = player.level+1
    elif player.level == 4:
        if player.exp >= 140:
            levels(player, 5)
            player.level = player.level+1
    elif player.exp > 140:
        print("you are max level!")
        print("")
#Items
class UtilityItem:
    def __init__(self,name, use_message):
        self.name = name
        self.name = use_message
    
utilityitems = {
    'stand arrow': UtilityItem("Stand Arrow", "you stab yourself with the mysterious arrow(why????)")
}

class FoodItem:
    def __init__(self,name, hp_recover, strength_buff):
        self.name = name
        self.hp_recover = hp_recover
        self.strength_buff = strength_buff

fooditems = {
    'health potion': FoodItem("Health Potion", 5, 0),
    'peanits': FoodItem("Peanits", -3, 2)
}

#player class that allows me to keep track of data
class Player:
    def __init__(self, health, damage, exp, sp, max_health, level, battle_damage, strbuff = False):
        self.health = health
        self.damage = damage
        self.exp = exp
        self.sp = sp
        self.max_health = max_health
        self.inv = ["health potion", "health potion", 'peanits']
        self.level = level
        self.skill_list = []
        self.battle_damage = battle_damage
        self.strbuff = strbuff

#player attributes(if you wanna be stronger switch these around)
player = Player(10, 2, 0, 0, 10, 0, 2)
if admin:
    player =  Player(100, 100, 0, 0, 100, 100, 100)

#monster class that allows data to be kept track of
class Monster:
   def __init__(self, health, damage, name, exp_give, encounter_message = "An unknown monster apears!", drop = "none", drop_chance = 0):
        self.health = health
        self.damage = damage
        self.name = name
        self.exp_give = exp_give
        self.encounter_message = encounter_message
        self.drop = drop
        self.drop_chance = drop_chance
#skills go  here, as well as counnters
timestop_counter = 0
def timestop():
    global timestop_counter
    timestop_counter = 3
skill_list = {
    'timestop':timestop()
}

#this is the player turn
def player_turn(monster):
    while True:
        ammount_buff = 0
        if not player.strbuff:
            player.battle_damage = player.damage
        if player.strbuff:
            player.battle_damage = player.damage*ammount_buff
            player.strbuff = False
        option = input("What would you like to do? (Fight, Run, Inventory, Eat) ")
        print("")
        option = option.lower()
        if option == "fight":
            turn_roll = roll(20, "You rolled a")
            if turn_roll >= 18:
                time.sleep(0.5)
                print("Critical hit! you did 2x damage!")
                print("")
                monster.health = monster.health - (player.battle_damage*2)
                if monster.health < 0:
                    monster.health = 0
                time.sleep(0.5)
                print(monster.name+"s health is now", (monster.health))
                print("")
                break
            elif turn_roll >= 8:
                time.sleep(0.5)
                print("You hit the monster for", str(player.battle_damage), "health")
                print("")
                monster.health = monster.health - player.battle_damage
                if monster.health < 0:
                    monster.health = 0
                print(monster.name+"s health is now", (monster.health))
                print("")
                break
            elif turn_roll >= 5:
                time.sleep(0.5)
                print("You grazed the monster and did", str(player.battle_damage/2))
                print("")
                monster.health = monster.health - (player.battle_damage/2)
                if monster.health < 0:
                    monster.health = 0
                time.sleep(0.5)
                print(monster.name+"s health is now", (monster.health))
                print("")
                break
            else:
                time.sleep(0.5)
                print("Critical faliure, you did nothing.")
                print("")
                break
        elif option == "debug":
            print(monster.health)
            print(player.battle_damage)
            print("")
        elif option == "run":
            turn_roll = roll(20, "You rolled a")
            if turn_roll >= monster.health/1.5:
                print("Ran Away Successfully")
                print("")
                battle()
            else:
                print("Couldnt run away.")
                print("")
                break
        elif option == "inv" or option == "inventory":
            print("your inventory:", str(player.inv)[1:-1])
            print("")
        elif option == "eat":
            choice_item = input("What would you like to eat? ")
            print("")
            choice_item = choice_item.lower()
            if choice_item in fooditems:
                if choice_item in player.inv:
                    player.inv.remove(choice_item)
                    player.health = player.health + fooditems[choice_item].hp_recover
                    if player.health > player.max_health:
                        player.health = player.max_health
                    if fooditems[choice_item].hp_recover != 0:
                        print("Your health is now:",(player.health))
                    if fooditems[choice_item].strength_buff >= 1:
                        player.strbuff = True
                        ammount_buff = fooditems[choice_item].strength_buff
                    print("")
                else:
                    print("You do not have a",(choice_item))
                    print("")
            else:
                print("That item flat out doesnt exist")
                print("")
        elif option == "wait":
            print("damn thats a lil cocky")
            print("")
            break
        elif option == "skills":
            print("your skills are:", (player.skill_list)[1:-1])
            
        else:
            print("thats not an option.")
            print("")

# this the monster turn           
def monster_turn(player, monster):
    turn_roll = roll(20, "The monster rolled")
    if turn_roll >= 18:
        time.sleep(0.5)
        print("Critical hit! the", monster.name,"did 2x damage!")
        print("")
        player.health = player.health - (monster.damage*2)
        if player.health < 0:
            player.health = 0
        time.sleep(0.5)
        print("your health is now", (player.health))
        print("")
    elif turn_roll >= 8:
        time.sleep(0.5)
        print("The", monster.name , "hit you for", str(monster.damage), "health")
        print("")
        player.health = player.health - monster.damage
        if player.health < 0:
            player.health = 0
        time.sleep(0.5)
        print("your health is now", (player.health))
        print("")
    elif turn_roll >= 5:
        time.sleep(0.5)
        print("The",monster.name, "grazed you and did", str(monster.damage/2), "health)")
        print("")
        player.health = player.health - (monster.damage/2)
        if player.health < 0:
            player.health = 0
        time.sleep(0.5)
        print("your health is now", (player.health))
        print("")
    else:
        print("Critical faliure, Monster did nothing.")
        print("")

# this is where it all comes together, the battle function! this code can evolve forever
# and ever and ever and ever, so have fun! IF YOU WANNA EDIT FORK PLEASE
def battle():

#these are basic monsters, if you wanna add more copy doing this and then scroll
#down and go to the battle function and add this in as a choice, MAKE SURE TO FORK IF YOU EDIT
    golem = Monster(10,4, "golem", 30, "A golem lumbers forth")
    zombie = Monster(3, 3, "zombie", 5, "From the ground rises a zombie!", "health potion", 50)
    ghost = Monster(5, 2, "ghost", 10, "A ghost scares your dad")
    bella = Monster(10, 10, "Weird Ass Slime named Bella", 100, "bro that slime looks like someone I know...", "peanits", 25)
    choice = random.randint(1,102)
    if choice > 101:
        print("you found a secret, not ready yet tho.")
        battle()
    elif choice >90:
        monster = bella
    elif choice > 60:
        monster = golem
    elif choice > 30:
        monster = ghost
    elif choice <= 30:
        monster = zombie
    print(monster.encounter_message)
    print("")
    diceroll = roll(20, "you rolled a")
    if diceroll >= 10:
        print("you go first")
        print("")
        player_turn(monster)
        while True:
            if player.health == 0 or monster.health == 0:
                break
            monster_turn(player, monster)
            if player.health == 0 or monster.health == 0:
                break
            player_turn(monster)
    else:
        print("monster goes first")
        print("")
        monster_turn(player, monster)
        while True:
            if player.health == 0 or monster.health == 0:
                break
            player_turn(monster)
            if player.health == 0 or monster.health == 0:
                break
            monster_turn(player, monster)
    if player.health != 0:
        player.exp = player.exp + monster.exp_give
        print("you gained",monster.exp_give,"exp!")
        print("")
        if player.level != 5:
            er = 5
        if player.level == 5:
            er = 1
        for i in range(er):
            level_check(player)
        drop(monster, player)
        battle()
    else:
        print("you can no longer continue")
        print("")
        quit()
battle()
