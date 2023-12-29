import random
from functions import draw_card


def reset_hand():
    dealer_hand = []
    player_hand = []


def blackjack():
    while True:
        reset_hand()
        user_input = input(f"Would you like to play? Y or N: ").lower()
        dealer_hand = []
        player_hand = []
        if user_input == 'y':
            draw1 = draw_card()
            draw2 = draw_card()
            draw3 = draw_card()
            draw4 = draw_card()
            dealer_hand.append(draw2 + draw4)
            player_hand.append(draw1 + draw3)
            print(f"Your cards: {draw1, draw3}")
            print(f"Computers first card: {dealer_hand[0]}")
        if user_input == 'n':
            print('Good don\'t gamble!')
            break

        player_hand = sum(player_hand)
        dealer_hand = sum(dealer_hand)

        while user_input == 'y':
            action = input("Type 'y' to draw another card 'n' to pass: ")
            if action == 'y':
                drawn_card = draw_card()
                player_hand += drawn_card
                print(f"You drew a {drawn_card}")
                if dealer_hand <= 17:
                    drawn_card = draw_card()
                    dealer_hand += drawn_card
                    print(f"Computer drew a {drawn_card}")
                if player_hand > 21:
                    print(f"{player_hand}: You lose, Dealer had {dealer_hand}")
                    user_input = ''
                elif player_hand == 21:
                    print(f"{player_hand}: You win!")
                    user_input = ''
                elif dealer_hand > 21:
                    print(f"{player_hand}: You win!, Dealer had {dealer_hand}")
                    user_input = ''
                elif dealer_hand == 21:
                    print(f"{player_hand}: You Lose!")
                    user_input = ''
                else:
                    print(f"You have: {player_hand}, Dealer has: {dealer_hand}")
            if action == 'n':
                if dealer_hand < 17:
                    drawn_card = draw_card()
                    dealer_hand += drawn_card
                    print(f"Computer drew a {drawn_card}")
                elif dealer_hand > 21:
                    print(f"{player_hand}: You win!, Dealer had {dealer_hand}")
                elif 21 > player_hand > dealer_hand:
                    print(f"{player_hand}: You win!, Dealer had {dealer_hand}")
                    user_input = ''
                elif player_hand < dealer_hand:
                    print(f"{player_hand}: You Lose, Dealer had {dealer_hand}")
                    user_input = ''
                elif player_hand == dealer_hand:
                    print('Tie')
                    user_input = ''


blackjack()
