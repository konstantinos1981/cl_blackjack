from art import logo
import random


def deal():
    """deal function returns a random card from the deck"""
    cards_available = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_drawn = random.choice(cards_available)
    return card_drawn


def check_blackjack(hand):
    """checks if a blackjack has been dealt"""
    if sum(hand) == 21:
        return 0


def check_scores(user, comp):
    if sum(user) == sum(comp):
        return "Its a tie"
    if sum(comp) > 21:
        return "Dealer busts"
    else:
        return "Dealer wins"


def play_game():
    print(logo)
    '''initializing the user and computer cards'''
    user_cards = []
    computer_cards = []
    '''Dealing the user and computer initial hands'''
    for _ in range(2):
        user_cards.append(deal())
        computer_cards.append(deal())

    user = check_blackjack(user_cards)
    comp = check_blackjack(computer_cards)

    if user == 0:
        if comp == 0:
            print("You both have a blackjack. Its a tie")
            return
        else:
            print("You win with a Blackjack")
            return
    if comp == 0:
        print("Dealer has a blackjack. You loose")
        return

    while sum(user_cards) < 21:
        draw_card = input(f"Your hand so far is {user_cards}: Your score is {sum(user_cards)} \n"
                          f"Dealer has {computer_cards[0]} \n"
                          f"Do you wish to draw another card? (y/n) ")
        if draw_card == 'y':
            user_cards.append(deal())
        if sum(user_cards) > 21 and 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
        if draw_card == 'n':
            break

    if sum(user_cards) > 21:
        print("You bust")
        return

    while sum(computer_cards) < 17:
        computer_cards.append(deal())

    print(check_scores(user_cards, computer_cards))


while input("Start a new game of Blackjack? Type 'y'/ 'n' ") == 'y':
    play_game()
