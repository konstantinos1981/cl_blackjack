from art import logo
import random


def deal():
    cards_available = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_index = random.randint(0,12)
    dealed_card = cards_available[card_index]
    return dealed_card


def check_for_blackjack():
    user_score = sum(user_cards)
    comp_score = sum(computer_cards)
    if user_score == 21:
        if comp_score < 21:
            print("You win. Blackjack!!")
            return True
        elif comp_score == 21:
            print("Its a tie. Both you and the dealer have Blackjack")
            return True

    if comp_score == 21:
        print("You loose... Dealer has Blackjack")
        return True

def check_for_winner(user , computer):

    if sum(user) > 21:
        return "You bust"

    if sum(user) == sum(computer):
        return "It is a tie"

    if sum(user) > sum(computer):
        return f"You win. Dealer has {sum(computer)}"

    if sum(computer) > 21:
        return f"Dealer busts with {sum(computer)}. You win"

    else:
        return f"Dealer wins with {sum(computer)}"


while True:
    print(logo)
    play = input(f"Start a new game of BlackJack? Type 'y' or 'n' ")
    if play == 'y':
        user_cards = []
        computer_cards = []
        user_cards.append(deal())
        computer_cards.append(deal())
        user_cards.append(deal())
        computer_cards.append(deal())
        while True:
            blackjack = check_for_blackjack()
            if blackjack:
                break

            while sum(user_cards) < 21:
                deal_card = input(f"Your score is {sum(user_cards)}. Dealer has {computer_cards[0]}. "
                                  f" Do you wish to draw another one? y/n")

                if deal_card == 'y':
                    user_cards.append(deal())
                    print(user_cards)
                    for index, item in enumerate(user_cards):
                        if item == 11:
                            if sum(user_cards) > 21:
                                user_cards[index] = 1
                                print(user_cards)
                                continue

                elif deal_card == 'n':
                    break

            while sum(computer_cards) < 17:
                computer_cards.append(deal())



            print(check_for_winner(user_cards, computer_cards))
            break

    elif play == 'n':
        print("Thank you for playing...")
        break

    else:
        print("Incorrect selection. Try again")
        continue


