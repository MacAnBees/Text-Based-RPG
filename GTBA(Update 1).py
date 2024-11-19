import random
import time
'''
Welcome to Yuri's Text based rpg battle test (MAN this needs a better name)
it currently has 3 monsters but instructions are in the code
and remember, if you wanna edit FORK FORK FORK >:3 or ill send a golem after u
Thanks to our playtesters:
Peyton
Bella as the slime
John "The princess" Dare
'''
print("How this game works: When the turn begins you roll a dice, if you roll a 10 or higher you go first, otherwie the monster goes first, when fighting, rolling an 8-17 or higher does your damage, rolling an 18 or higher does 2x damage, and rolling a 5-8 does half damage, 3-1 is a crit fail, when running, you need to roll more than half the monster's health, in your inventory, you have health potions, use the eat command on your turn and specifiy what you want to eat to use the health potion.")
admin = True
#custom roll command for all dice interaction
def roll(n, roll_message = "You rolled a", rolling_message = "rolling dice..."):
    print(rolling_message)
    diceroll = random.randint(1, n)
    time.sleep(1)
    print(roll_message, diceroll)
    return diceroll

#leveling system
def levels(player, level_val):
    print("you are now level", str(level_val) + "! You have 5 new stat points avaliable")
    player.sp = player.sp + 5
    while player.sp > 0:
        stat_input = input("what would you like to put your stats in?(Health, Damage) ")
        stat_input = stat_input.lower()
        while True:
            try:
                stat_val = int(input("how many stat points would you like to put in? "))
            except ValueError:
                print("enter an integer please")
        if stat_val > player.sp:
            stat_val = player.sp
        player.sp = player.sp - stat_val
        if stat_input == "health":
            player.health = player.health + stat_val
            player.max_health = player.max_health + stat_val
            print("your health is now", (player.health))
            print("your max health is now", (player.max_health))
        elif stat_input == "damage":
            player.damage = player.damage + stat_val
            print("your damage is now", (player.damage))
def level_check(player):
    if player.exp >= 10:
        levels(player, 1)
    elif player.exp >= 30:
        levels(player, 2)
    elif player.exp >= 50:
        levels(player, 3)
    elif player.exp >= 70:
        levels(player, 4)
    elif player.exp >= 80:
        levels(player, 5)
    elif player.exp > 80:
        print("you are max level!")
#Items

class FoodItem:
    def __init__(self,name, hp_recover, strength_buff):
        self.name = name
        self.hp_recover = hp_recover
        self.stregth_buff = strength_buff

fooditems = {
    'health potion': FoodItem("Health Potion", 5, 0),
    'peanits': FoodItem("Peanits", -5, 0)
}
#player class that allows me to keep track of data
class Player:
    def __init__(self, health, damage, exp, sp, max_health):
        self.health = health
        self.damage = damage
        self.exp = exp
        self.sp = sp
        self.max_health = max_health
        self.inv = ["health potion", "health potion", "peanits"]
#player attributes(if you wanna be stronger switch these around)
player = Player(10, 2, 0, 0, 10)
if admin:
    player =  Player(100, 100, 0, 0, 100)

#monster class that allows data to be kept track of
class Monster:
   def __init__(self, health, damage, name, exp_give, encounter_message = "An unknown monster apears!", drop = "none", drop_chance_1 = 0, drop_chance_2 = 0):
        self.health = health
        self.damage = damage
        self.name = name
        self.exp_give = exp_give
        self.encounter_message = encounter_message
        self.drop = drop
        self.drop_chance = drop_chance_1
        self.drop_chance = drop_chance_2
#these are basic monsters, if you wanna add more copy doing this and then scroll
#down and go to the battle function and add this in as a choice, MAKE SURE TO FORK IF YOU EDIT


#this is the player turn
def player_turn(monster):
    while True:
        option = input("What would you like to do? (Fight, Run, Inventory, Eat) ")
        option = option.lower()
        if option == "fight":
            turn_roll = roll(20, "You rolled a")
            if turn_roll >= 18:
                time.sleep(0.5)
                print("Critical hit! you did 2x damage!")
                monster.health = monster.health - (player.damage*2)
                if monster.health < 0:
                    monster.health = 0
                time.sleep(0.5)
                print(monster.name+"s health is now", (monster.health))
                break
            elif turn_roll >= 8:
                time.sleep(0.5)
                print("You hit the monster for", str(player.damage), "health")
                monster.health = monster.health - player.damage
                if monster.health < 0:
                    monster.health = 0
                print(monster.name+"s health is now", (monster.health))
                break
            elif turn_roll >= 5:
                time.sleep(0.5)
                print("You grazed the monster and did", str(player.damage/2))
                monster.health = monster.health - (player.damage/2)
                if monster.health < 0:
                    monster.health = 0
                time.sleep(0.5)
                print(monster.name+"s health is now", (monster.health))
                break
            else:
                time.sleep(0.5)
                print("Critical faliure, you did nothing.")
                break
        elif option == "debug":
            print(monster.health)
        elif option == "run":
            turn_roll = roll(20, "You rolled a")
            if turn_roll >= monster.health/1.5:
                print("Ran Away Successfully")
                battle()
            else:
                print("Couldnt run away.")
                break
        elif option == "inv" or option == "inventory":
            print("your inventory:", str(player.inv)[1:-1])
        elif option == "eat":
            choice_item = input("What would you like to eat? ")
            choice_item = choice_item.lower()
            if choice_item in fooditems:
                if choice_item in player.inv:
                    player.inv.remove(choice_item)
                    player.health = player.health + fooditems[choice_item].hp_recover
                    if player.health > player.max_health:
                        player.health = player.max_health
                    print("Your health is now:",(player.health))
                else:
                    print("You do not have a",(choice_item))
            else:
                print("That item flat out doesnt exist")
        else:
            print("thats not an option.")

# this the monster turn           
def monster_turn(player, monster):
    turn_roll = roll(20, "The monster rolled")
    if turn_roll >= 18:
        time.sleep(0.5)
        print("Critical hit! the", monster.name,"did 2x damage!")
        player.health = player.health - (monster.damage*2)
        if player.health < 0:
            player.health = 0
        time.sleep(0.5)
        print("your health is now", (player.health))
    elif turn_roll >= 8:
        time.sleep(0.5)
        print("The", monster.name , "hit you for", str(monster.damage), "health")
        player.health = player.health - monster.damage
        if player.health < 0:
            player.health = 0
        time.sleep(0.5)
        print("your health is now", (player.health))
    elif turn_roll >= 5:
        time.sleep(0.5)
        print("The",monster.name, "grazed you and did", str(monster.damage/2), "health)")
        player.health = player.health - (monster.damage/2)
        if player.health < 0:
            player.health = 0
        time.sleep(0.5)
        print("your health is now", (player.health))
    else:
        print("Critical faliure, Monster did nothing.")

# this is where it all comes together, the battle function! this code can evolve forever
# and ever and ever and ever, so have fun! IF YOU WANNA EDIT FORK PLEASE
def battle():

#these are basic monsters, if you wanna add more copy doing this and then scroll
#down and go to the battle function and add this in as a choice, MAKE SURE TO FORK IF YOU EDIT
    golem = Monster(10,4, "golem", 30, "A golem lumbers forth")
    zombie = Monster(3, 3, "zombie", 5, "From the ground rises a zombie!")
    ghost = Monster(5, 2, "ghost", 10, "A ghost scares your dad")
    choice = random.randint(1,3)
    if choice == 1:
        monster = zombie

    if choice == 2:
        monster = golem

    if choice == 3:
        monster = ghost
        

    print(monster.encounter_message)
    diceroll = roll(20, "you rolled a")
    if diceroll >= 10:
        print("you go first")
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
        level_check(player)
        battle()
    else:
        print("you can no longer continue")
        quit()
battle()
