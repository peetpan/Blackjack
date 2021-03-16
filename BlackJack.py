import random


def getcard(li):
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_list)
    li.append(card)
    return li


c = 'y'
while c == 'y':
    player_card = []
    com_card = []
    player_card = getcard(player_card)
    player_card = getcard(player_card)
    com_card = getcard(com_card)
    print('\nYour cards: ', player_card)
    print('Computer\'s cards: ', com_card)
    choice = input('Type \'y\' to get another card, type \'n\' to pass: ')
    com_card = getcard(com_card)
    if choice == 'y':
        player_card = getcard(player_card)

    print('Your final cards: ', player_card)
    print('Computer\'s final cards: ', com_card)
    sum_pl = sum(player_card)
    if sum_pl > 21 and 11 in player_card:
        sum_pl -= 10
    if sum_pl > 21:
        print('You lose!')
    elif sum_pl > sum(com_card):
        print('You win!')
    elif sum_pl < sum(com_card):
        print('You lose!')
    else:
        print('Its a draw!')
    c = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')

