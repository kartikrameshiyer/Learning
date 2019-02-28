from classes.game import person,bcolors



# creating array of magic
magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizard", "cost": 10, "dmg": 50}]


#player = person(500, 65, 34, 60, magic)
player = person(1000,65, 34, 60, magic)
enemy = person(500, 65, 34, 60, magic)


running = True
i =  0

print(bcolors.WARNING + bcolors.BOLD + " Enemy Attacks!" + bcolors.ENDC )

# add print statement with colors that enemy attacks

while running:

    player.choose_actions()
    choice = input("choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("Enemy attacked: ", dmg, " Points of Damage, new Hp: ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int( input("Choose Magic:")) - 1
        spell = player.get_spell_name(magic_choice)
        magic_dmg = player.generate_damage()
        cost = player.get_magic_cost(magic_choice)

        current_mp = player.get_mp()

    enemy_choice = 1


    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg, "Player hp: ", player.get_hp())

    if enemy.get_hp() == 0:
        print("You Win")
        running = False
    elif player.get_hp() == 0:
        print("You Loose!!!!")
        running = False






