import random
import time

restart = 0
while restart == 0:  # variable for restarting code
    health = 30  # stating variables so it gets reset when the games starts over
    attack = 10
    pokemon_name = 0  # stating the variable so the code doesn't freak out when I start

    time.sleep(0.3)  # the intro picture slowed down to give it a retro look
    print("                                  ,'\ ")
    time.sleep(0.3)
    print("    _.----.        ____         ,'  _\   ___    ___     ____")
    time.sleep(0.3)
    print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`. ")
    time.sleep(0.3)
    print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  | ")
    time.sleep(0.3)
    print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  | ")
    time.sleep(0.3)
    print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  | ")
    time.sleep(0.3)
    print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     | ")
    time.sleep(0.3)
    print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    | ")
    time.sleep(0.3)
    print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   | ")
    time.sleep(0.3)
    print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   | ")
    time.sleep(0.3)
    print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   | ")
    time.sleep(0.3)
    print("                                `'                            '-._| ")
    time.sleep(0.3)
    print("     ")
    time.sleep(0)

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

    for x in range(0, 30):  # creates 30 moves by repeating the move code under it 30 times
        time.sleep(0.5)  # gives the code a delay for retro effect
        num_holder = random.randint(1, 16)  # this chooses the random moves options out of 15 so your odds of getting everything at least twice is increaced

        if num_holder == 1:  # one of the random options
            print("a trainer challenges you")
            print(str(name) + " I challenge you to a fight!")
            trainer_choice = input("would you like to 1_run or 2_fight?")  # use 1 or 2
            if trainer_choice.isdigit():  # defencive coding checking if the input is a number
                trainer_choice = int(trainer_choice)
            while trainer_choice != 1 and trainer_choice != 2:  # defencive coding loop
                print("error")
                trainer_choice = input("would you like to 1_run or 2_fight?")
                if trainer_choice.isdigit():  # defencive coding checking if the input is a number
                    trainer_choice = int(trainer_choice)

            if trainer_choice == 1:  # one of the input options
                while trainer_choice != 2:  # loops the defencive coding because you can't progress with option 1
                    print("you can't run away")
                    trainer_choice = input("would you like to 1_run or 2_fight?")  # use 1 or 2
                    if trainer_choice.isdigit():  # defencive coding checking if the input is a number
                        trainer_choice = int(trainer_choice)
                    while trainer_choice != 1 and trainer_choice != 2:  # defencive coding loop
                        print("error")
                        trainer_choice = input("would you like to 1_run or 2_fight?")
                        if trainer_choice.isdigit():  # defencive coding checking if the input is a number
                            trainer_choice = int(trainer_choice)

            if trainer_choice == 2:
                trainer_health = random.randint(5, 20)  # the trainers health and damage is randomized
                trainer_damage = random.randint(1, 13)
                damage = 10  # damage is stated so it goes back to normal at the start of each new battle
                print("opponents damage is " + str(trainer_damage))  # intro to fight and stating stats
                print("opponents health is " + str(trainer_health))
                print("your damage is " + str(damage))
                print("your health is " + str(health))
                while trainer_health >= 0:  # loop causes fight to continue until you or the opponent dies
                    attack_choice = input("do you want to attack 1, use Drain 2 or use Rage 3")  # use 1, 2 or 3
                    if attack_choice.isdigit():  # defencive coding checking if the input is a number
                        attack_choice = int(attack_choice)
                    while attack_choice != 1 and attack_choice != 2 and attack_choice != 3:  # defencive coding loop
                        print("error")
                        attack_choice = input("do you want to attack 1, use Drain 2 or use Rage 3")
                        if attack_choice.isdigit():  # defencive coding checking if the input is a number
                            attack_choice = int(attack_choice)
                        # attack options
                    if attack_choice == 1:
                        print(str(pokemon_name) + " used " + str(attack))  # this option lowers the opponents health
                        trainer_health = trainer_health - damage
                        if trainer_health >= 0:
                            print("opponents health = " + str(trainer_health))
                        elif trainer_health <= 0:  # this is to keep the opponents health from displaying as a negative
                            print("opponents health = 0 ")
                    elif attack_choice == 2:
                        print(str(pokemon_name) + " used Drain")  # this option lowers the opponents health
                        trainer_damage = trainer_damage * 0.8
                        print("the opponents attack has weakened")
                        print("opponents attack is " + str(round(trainer_damage, 1)))  # I used the round function for when I display the reduced damage of the opponet
                    elif attack_choice == 3:
                        print(str(pokemon_name) + " Rage")  # this option raises your damage and health by 3
                        print(str(pokemon_name) + "'s attack and defence has been raised")
                        damage = damage + 3
                        health = health + 3
                        print(str(pokemon_name) + "'s health = " + str(health) + " and damage = " + str(damage))
                    elif health <= 0:  # I used break so the loop will end when either you or your opponet health goes to zero or under
                        break
                    elif trainer_health <= 0:
                        break
                        # opponent attack options and drtails are the same as the one above
                    trainer_choice = random.randint(1, 12)  # this randomizes the opponrts choice
                    if trainer_choice in range(1, 10):  # this mades it so that most of the turns are normal attack moves and makes it more rare to use rage or drain
                        print("trainer attacked")
                        health = health - trainer_damage
                        if health >= 0:
                            print("your health is " + str(health))
                        elif health <= 0:
                            print("your health is 0")
                    elif trainer_choice == 11:
                        print("trainer used Drain")
                        damage = damage * 0.9
                        print("your attack has weakened")
                        print("your attack is " + str(round(damage, 1)))
                    elif trainer_choice == 12:
                        print("the trainer used Rage")
                        print("the trainer's attack and defence has been raised")
                        trainer_damage = trainer_damage + 1
                        trainer_health = trainer_health + 1
                        print("the trainer's health = " + str(trainer_health) + " and damage = " + str(trainer_damage))
                    elif health <= 0:  # the break function used again to end the loop if your health goes zero or under
                        break

        if num_holder == 2:  # one of the random options and same as num_holder 1
            print("a wild pokemon challenges you")
            wildpokemon_choice = input("would you like to 1_run or 2_fight?")  # use 1 or 2
            if wildpokemon_choice.isdigit():
                wildpokemon_choice = int(wildpokemon_choice)
            while wildpokemon_choice != 1 and wildpokemon_choice != 2:
                print("error use the numbers")
                wildpokemon_choice = input("would you like to 1_run or 2_fight?")
                if wildpokemon_choice.isdigit():
                    wildpokemon_choice = int(wildpokemon_choice)

            if wildpokemon_choice == 1:  # this allows you to not fight if you don't want to
                print("you ran away")

            elif wildpokemon_choice == 2:  # same as the battle options above
                pokemon_health = random.randint(5, 12)
                pokemon_damage = random.randint(1, 6)
                damage = 10
                print("opponents damage is " + str(pokemon_damage))
                print("opponents health is " + str(pokemon_health))
                print("your damage is " + str(damage))
                print("your health is " + str(health))
                while pokemon_health >= 0:
                    attack_choice = input("do you want to attack 1, use Drain 2 or use Rage 3")  # use 1, 2 or 3
                    if attack_choice.isdigit():
                        attack_choice = int(attack_choice)
                    while attack_choice != 1 and attack_choice != 2 and attack_choice != 3:
                        print("error")
                        attack_choice = input("do you want to attack 1, use Drain 2 or use Rage 3")
                        if attack_choice.isdigit():
                            attack_choice = int(attack_choice)
                        # attack options
                    if attack_choice == 1:
                        print(str(pokemon_name) + " used " + str(attack))
                        pokemon_health = pokemon_health - damage
                        if pokemon_health >= 0:
                            print("opponents health = " + str(pokemon_health))
                        elif pokemon_health <= 0:
                            print("opponents health = 0 ")
                    if attack_choice == 2:
                        print(str(pokemon_name) + " used Drain")
                        pokemon_damage = pokemon_damage * 0.8
                        print("the opponents attack has weakened")
                        print("opponents attack is " + str(round(pokemon_damage, 1)))
                    elif attack_choice == 3:
                        print(str(pokemon_name) + " Rage")
                        print(str(pokemon_name) + "'s attack and defence has been raised")
                        damage = damage + 3
                        health = health + 3
                        print(str(pokemon_name) + "'s health = " + str(health) + " and damage = " + str(damage))
                    elif health <= 0:
                        break
                    elif pokemon_health <= 0:
                        break
                        # opponent attack options and same as above
                    pokemon_choice = random.randint(1, 12)
                    if pokemon_choice in range(1, 10):
                        print("opponent attacked")
                        health = health - pokemon_damage
                        if health >= 0:
                            print("your health is " + str(health))
                        elif health <= 0:
                            print("your health is 0")
                    elif pokemon_choice == 11:
                        print("opponent used Drain")
                        damage = damage * 0.9
                        print("your attack has weakened")
                        print("your attack is " + str(round(damage, 1)))
                    elif pokemon_choice == 12:
                        print("the opponent used Rage")
                        print("the opponent's attack and defence has been raised")
                        pokemon_damage = pokemon_damage + 1
                        pokemon_health = pokemon_health + 1
                        print("the opponent's health = " + str(pokemon_health) + " and damage = " + str(pokemon_damage))

                    elif health <= 0:
                        break

        if num_holder == 3:  # one of the random options
            health = 30
            print("you come across a town and heal " + str(pokemon_name))
            print(str(pokemon_name) + "'s health is at " + str(health))

        elif num_holder in range(4, 16):  # the rest of the random options are displayed as move as a filler
            print("move")

        elif health <= 0:  # this is here to break the loop if your health is zero or under
            break

    if health >= 0:  # the ending if you wim and your health is above zero
        print("  ")
        print("you made it to the master gym!")
        print("you get a badge!")
        print("  ")
        print("   ,   /\   , ")
        print("  / '-'  '-' \ ")
        print("  |  Pokemon | ")
        print("  |   .--.   | ")
        print("  |  (    )  | ")
        print("  \   '--'   / ")
        print("   '--.  .--' ")
        print("       \/ ")
        print("  ")
    elif health <= 0:  # the ending if you loss and your health is zero or under
        print(" ")
        print("you lose")
        print(" ")
    ending = input("do you want to continue: yes or no  ")  # code to restart the entire game
    while ending != "no" and ending != "yes":  # defencive coding
        print("error")
        ending = input("do you want to continue: yes or no  ")
    if ending == "no":
        restart = restart + 1
    elif ending == "yes":
        restart = restart + 0
