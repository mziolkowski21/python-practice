import random

'''
Very basic version of blackjack, player can only hit or stay
'''

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
suits = ("Spades", "Hearts", "Diamonds", "Clubs")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": (1, 11)}


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        return ' '.join([str(card)+'\n' for card in self.all_cards])


class Dealer:

    def __init__(self):
        self.all_cards = []

    def add_cards(self, cards):
        if type(cards) == list:
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def remove_card(self):
        return self.all_cards.pop(0)


def game():
    game_on = True

    while game_on:
        player_turn = True
        dealer_turn = False
        lost = False

        player_sum = 0
        dealer_sum = 0
        game_deck = Deck()
        game_deck.shuffle()
        game_dealer = Dealer()
        game_dealer.add_cards(game_deck.all_cards)

        while player_turn:
            print(f"player sum: {player_sum}")
            action = ''
            if player_sum > 21:
                player_turn = False
                lost = True
            else:
                while action not in ["Hit", "Stay", "S", "H"]:
                    action = input("Hit/Stay? ").capitalize()

                if action == "Hit" or action == "H":
                    card = game_dealer.remove_card()
                    print(f"{card} = {card.value}")
                    if card.rank == "Ace":
                        ace = ''
                        while ace not in ['1', '11']:
                            ace = input("1 or 11? ")
                        if ace == '1':
                            player_sum += 1
                        elif ace == '11':
                            player_sum += 11
                    else:
                        player_sum += card.value
                elif action == "Stay" or action == "S":
                    player_turn = False
                    dealer_turn = True
        while dealer_turn:
            print(f"dealer sum: {dealer_sum}")
            if dealer_sum > 21:
                dealer_turn = False
                dealer_sum -= card.value
                break
            card = game_dealer.remove_card()
            print(f"{card} = {card.value}")
            if card.rank == "Ace":
                if dealer_sum + 11 > 21:
                    dealer_sum += 1
                else:
                    dealer_sum += 11
            else:
                dealer_sum += card.value

        if player_sum > dealer_sum and not lost:
            print(f"Player won: {player_sum} vs {dealer_sum}")

        if player_sum == dealer_sum and not lost:
            print("Draw")

        elif dealer_sum > player_sum or lost:
            if lost:
                print("You exceeded 21 threshold")
            else:
                print(f"p: {player_sum} vs d: {dealer_sum}")
            print(f"You loose all your pennies")

        choice = ''
        while choice not in ["Y", "N"]:
            choice = input("Do you want to play again? (Y/N) ").capitalize()

        if choice == 'N':
            game_on = False


game()