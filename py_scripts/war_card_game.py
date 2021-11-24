import random

'''
Additional rules:
    If there is a war (tie), each player draws 5 additional cards
    Player loses if they don't have at least 5 cards to play the war
'''

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
suits = ("Spades", "Hearts", "Diamonds", "Clubs")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


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

    def deal_one(self):
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


def game():
    game_on = True

    turns = 0
    player1 = Player(input("Enter a name of first player: "))
    player2 = Player(input("Enter a name of second player: "))
    game_deck = Deck()
    game_deck.shuffle()
    half_of_deck = int(len(game_deck.all_cards) / 2)
    player1.all_cards = game_deck.all_cards[:half_of_deck]
    player2.all_cards = game_deck.all_cards[half_of_deck:]

    while game_on:
        turns += 1

        if len(player1.all_cards) == 0:
            print(f"{player2.name} wins in {turns} turns")
            game_on = False
            break
        elif len(player2.all_cards) == 0:
            print(f"{player1.name} wins in {turns} turns")
            game_on = False
            break

        p1_card, p2_card = player1.remove_one(), player2.remove_one()
        print(f"{p1_card} vs {p2_card}", end='\t')
        print(f"{len(player1.all_cards)} vs {len(player2.all_cards)}")

        if p1_card.value > p2_card.value:
            player1.add_cards([p1_card, p2_card])

        elif p1_card.value < p2_card.value:
            player2.add_cards([p1_card, p2_card])

        elif p1_card.value == p2_card.value:
            print("WAR")
            war_deck = [p1_card, p2_card]
            while p1_card.value == p2_card.value:

                if len(player1.all_cards) < 5:
                    print(f"{player2.name} wins in {turns} turns")
                    game_on = False
                    break

                elif len(player2.all_cards) < 5:
                    print(f"{player1.name} wins in {turns} turns")
                    game_on = False
                    break

                for i in range(4):
                    p1_card, p2_card = player1.remove_one(), player2.remove_one()
                    war_deck.extend([p1_card, p2_card])

            if p1_card.value > p2_card.value:
                player1.add_cards(war_deck)

            elif p1_card.value < p2_card.value:
                player2.add_cards(war_deck)


game()
