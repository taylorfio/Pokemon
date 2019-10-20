import random
import time


def PrintText(first, last):  # prints ascii from text file
    printfile = open('acsii_art.txt').readlines()
    for line in range(first, last):
        time.sleep(0.3)  # the print slowed down to give it a retro look
        print(printfile[line], end="")


def action(attacker_type, health):
    global attacker_name
    if attacker_type == "trainer":
        lines = open('trainer_names.txt').read().splitlines()
        attacker_name = random.choice(lines)
        print("")
        print("Pokémon Trainer " + attacker_name + " challenges you")
        print(str(name) + " I challenge you to a fight!")
        print("")
    elif attacker_type == "pokemon":
        lines = open('pokemon_names.txt').read().splitlines()
        attacker_name = random.choice(lines)
        print("")
        print("A Wild " + attacker_name + " Pokémon Appears")
        print("")

    run_choice = input("would you like to 1_run or 2_fight?")  # use 1 or 2
    while run_choice != "1" and run_choice != "2":  # defencive coding loop
        print("error")
        run_choice = input("would you like to 1_run or 2_fight?")
    if run_choice == "1" and attacker_type == "trainer":  # one of the input options
        while run_choice != "2":  # loops the defencive coding because you can't progress with option 1
            print("you can't run away")
            time.sleep(0.5)
            run_choice = input("would you like to 1_run or 2_fight?")  # use 1 or 2
            while run_choice != "1" and run_choice != "2":  # defencive coding loop
                print("error")
                run_choice = input("would you like to 1_run or 2_fight?")
    if run_choice == "1" and attacker_type == "pokemon":  # one of the input options
        print("")
        print("you ran away")
        print("")
        time.sleep(0.5)
        return health

    if run_choice == "2":
        global attacker_damage, attacker_health
        if attacker_type == "trainer":
            attacker_health = random.randint(5, 20)  # the attackers health and damage is randomized
            attacker_damage = random.randint(5, 13)
        elif attacker_type == "pokemon":
            attacker_health = random.randint(5, 12)
            attacker_damage = random.randint(1, 6)
        damage = 8  # damage is stated so it goes back to normal at the start of each new battle
        print("")
        print(str(attacker_name) + "'s damage is " + str(attacker_damage))  # intro to fight and stating stats
        print(str(attacker_name) + "'s health is " + str(attacker_health))
        print("")
        print(str(pokemon_name) + "'s damage is " + str(damage))
        print(str(pokemon_name) + "'s health is " + str(health))
        print("")

        while attacker_health > 0:  # loop causes fight to continue until you or the opponent dies

            time.sleep(0.5)
            attack_choice = input("do you want to attack 1, use Drain 2 or use Rage 3")  # use 1, 2 or 3
            if attack_choice.isdigit():  # defencive coding checking if the input is a number
                attack_choice = int(attack_choice)
            while attack_choice != 1 and attack_choice != 2 and attack_choice != 3:  # defencive coding loop
                print("error")
                print("")
                attack_choice = input("do you want to attack 1, use Drain 2 or use Rage 3")
                if attack_choice.isdigit():  # defencive coding checking if the input is a number
                    attack_choice = int(attack_choice)

            if attack_choice == 1:  # attack options
                print(str(pokemon_name) + " used " + str(attack))  # this option lowers the opponents health
                attacker_health = attacker_health - damage
                if attacker_health > 0:
                    print(str(attacker_name) + "'s health = " + str(attacker_health))
                    print("")
                elif attacker_health <= 0:  # this is to keep the opponents health from displaying as a negative
                    print(str(attacker_name) + " is defeated ")
                    print("")
                    return health
            elif attack_choice == 2:
                print(str(pokemon_name) + " used Drain")  # this option lowers the opponents health
                attacker_damage = attacker_damage * 0.8
                print(str(attacker_name) + "'s attack has weakened")
                print(str(attacker_name) + "'s attack is " + str(round(attacker_damage, 1)))  # round function for displaying the reduced damage of the opponet
                print("")
            elif attack_choice == 3:
                print(str(pokemon_name) + " used Rage")  # this option raises your damage and health by 3
                print(str(pokemon_name) + "'s attack and defence has been raised")
                damage = damage + 3
                health = health + 3
                print(str(pokemon_name) + "'s health = " + str(health) + " and damage = " + str(damage))
                print("")

            # opponent attack options and details are the same as the one above
            time.sleep(0.5)
            opponent_choice = random.randint(1, 12)  # this randomizes the opponent choice
            if opponent_choice in range(1, 10):  # this made it so that most of the turns are normal attack moves and makes it more rare to use rage or drain
                print(str(attacker_name) + " attacks")
                health = health - attacker_damage
                if health > 0:
                    print(str(pokemon_name) + "'s health is " + str(health))
                    print("")
                elif health <= 0:
                    print(str(pokemon_name) + " has been defeated")
                    print("")
                    return health
            elif opponent_choice == 11:
                print(str(attacker_name) + " used Drain")
                damage = damage * 0.9
                print(str(pokemon_name) + "'s attack has weakened")
                print(str(pokemon_name) + "'s attack is " + str(round(damage, 1)))
                print("")
            elif opponent_choice == 12:
                print(str(attacker_name) + " used Rage")
                print(str(attacker_name) + "'s attack and defence has been raised")
                attacker_damage = attacker_damage + 1
                attacker_health = attacker_health + 1
                print(str(attacker_name) + "'s health = " + str(attacker_health) + " and damage = " + str(attacker_damage))
                print("")


restart = True
while restart:  # variable for restarting code
    health = 30  # stating variables so it gets reset when the games starts over
    pokemon_name = ""  # stating the variable so the code doesn't freak out when I start 

    PrintText(0, 12)  # prints intro image
    print("Welcome to the Kanto region")  # intro
    name = input("what is your name? ")  # input asking your name
    if len(name) >= 12:  # defencive coding for the length of the name
        while len(name) >= 12:
            print("error: to long keep under 12")
            name = input("what is your name ")
    chosen_pokemon = input("Chose your pokemon: 1_Charmander, 2_Bulbasaur, 3_Squirtle ")  # input for pokemon choice, use 1, 2, 3, 4
    if chosen_pokemon.isdigit():  # defencive coding checking if the input is a number
        chosen_pokemon = int(chosen_pokemon)
    while chosen_pokemon != 1 and chosen_pokemon != 2 and chosen_pokemon != 3 and chosen_pokemon != 4:  # defencive coding for the pokemon input choice if you don't use the proper numbers
        print("error, use the numbers")
        chosen_pokemon = input("Chose your pokemon: 1_Charmander, 2_Bulbasaur, 3_Squirtle ")
        if chosen_pokemon.isdigit():
            chosen_pokemon = int(chosen_pokemon)

    if chosen_pokemon == 1:  # this determines the name and attack for the pokemon from the chosen_pokemon input
        pokemon_name = "Charmander"
        attack = "blaze"
    elif chosen_pokemon == 2:
        pokemon_name = "Bulbasaur"
        attack = "overgrow"
    elif chosen_pokemon == 3:
        pokemon_name = "Squirtle"
        attack = "torrent"
    elif chosen_pokemon == 4:
        pokemon_name = "Pikachu"
        attack = "static"

    print("    ")  # end of intro, uses your name and pokemon name input to personalize
    print(str(name) + ", your mission is to travel through Kanto region from Pallet Town to the master gym")
    print("take " + str(pokemon_name) + " as your pokemon and head out on your adventure")
    print("    ")

    for x in range(0, 60):  # creates 60 moves by repeating the move code under it 60 times
        time.sleep(0.5)  # gives the code a delay for retro effect
        num_holder = random.randint(1, 20)  # this chooses the random moves options out of 15 so your odds of getting everything is tripled
        if health <= 0:  # this is here to break the loop if your health is zero or under
            break
        if num_holder == 1:  # random option for trainer
            health = action("trainer", health)
        elif num_holder == 2:  # random options for pokemon
            health = action("pokemon", health)
        elif num_holder == 3:  # one of the random options
            health = 30
            print("you come across a town and heal " + str(pokemon_name))
            print(str(pokemon_name) + "'s health is at " + str(health))
        else:
            print("move")

    if health >= 0:  # the ending if you wim and your health is above zero
        PrintText(12, 23)
    elif health <= 0:  # the ending if you loss and your health is zero or under
        PrintText(23, 38)
    ending = input("do you want to restart: yes or no  ")  # code to restart the entire game
    while ending != "no" and ending != "yes":  # defencive coding
        print("error")
        ending = input("do you want to restart: yes or no  ")
    if ending == "no":
        restart = False
    elif ending == "yes":
        restart = True
