from random import randint

game_running = True
round_number = 1
player = {'name': 'Eugene', 'attack': 20, 'heal': 15, 'health': 100}
monster = {'name': 'Monster', 'attack_min': 10,
           'attack_max': 20, 'health': 100}
player['name'] = input('Enter Player name:')


while game_running == True:
    new_round = True
    player['health'] = 100
    monster['health'] = 100

    print('- - -' * 7)
    print("{0} has {1} hp".format(player['name'], player['health']))

    print(
        '- - - - - - - - - - -\n    Round {}\n- - - - - - - - - - -'.format(round_number))

    while new_round == True:

        palyer_won = False
        monster_won = False

        print('---' * 7)
        print('Please select action \n 1) Attack \n 2) Heal\n 2) Q to Exit')
        print('---' * 7)

        player_choice = input('Choose an action:')

        if player_choice == '1':
            monster_attack = randint(
                monster['attack_min'], monster['attack_max'])
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                palyer_won = True
            else:
                player['health'] = player['health'] - monster_attack
                if player['health'] <= 0:
                    monster_won = True

            print('Monster health: ' + str(monster['health']))
            print('Monster health: ' + str(player['health']))

        elif player_choice == '2':
            monster_attack = randint(
                monster['attack_min'], monster['attack_max'])
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            print('Monster health: ' + str(monster['health']))
            print('Monster health: ' + str(player['health']))

        elif player_choice == 'Q' or player_choice == 'q':
            print('- - - EXITED - - -')
            new_round = False
            game_running = False
        else:
            print('Invalid Input!')

        if palyer_won == True or monster_won == True:
            round_number = round_number + 1
            print(
                '- - - - - - - - - - -\n    Round {}\n- - - - - - - - - - -'.format(round_number))
            new_round = False
