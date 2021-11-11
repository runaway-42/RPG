'''
Brooke Farrell
Kevin Perez
10/25/21
This program will allow you to 'build' a fighter and compete
against a randomly generated computer opponent.
Honor Code:

we spent
'''
import random
keep_going = 'y'

def play ():
    user1 = int(input('Are you a: Bard(1), Mage(2), or Warrior(3)? '))
    user2 = int(input('Do you use: Dagger(1), Fireballs(2), or Greatsword(3)?'))
    user3 = int(input('Do you fear: Snakes(1), Heights(2), or Confrontation(3)?'))

    comp1 = random.randint(1, 3)
    comp2 = random.randint(1, 3)
    comp3 = random.randint(1, 3)

    user_fighter = (user1 + user2) - user3
    comp_fighter = (comp1 + comp2) - comp3

    if user_fighter == comp_fighter:
        print('Your fighter score is:', user_fighter)
        print('The computers fighter score is:', comp_fighter)
        print('Its a draw! Cant have that, one must be victorious!')
        return play()
    if user_fighter <= comp_fighter:
        print('Your fighter score is:', user_fighter)
        print('The computers fighter score is:', comp_fighter)
        print('You died! Your fighter was too weak!')
    if user_fighter >= comp_fighter:
        print('Your fighter score is:', user_fighter)
        print('The computers fighter score is:', comp_fighter)
        print('Huzzah! You emerge victorious!')

    keep_going = input('Would you like to play again?(y/n)')
    if keep_going == 'y':
        return play()
    else:
        exit()

play()
