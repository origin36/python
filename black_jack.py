# coding utf-8

"""
simple blackjack game, one player vs the computer, with betting
"""

import random
import time

suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
          'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}


class Deck:
    """This class represents the deck of cards."""
    def __init__(self):
        all_suits = []
        all_ranks = []
        self.deck = []
        for i in range(4, 56):
            all_suits.append(suits[i % 4])
        for x in range(0, 13):
            for y in range(0,4):
                all_ranks.append(ranks[x])
        self.deck = list(zip(all_suits, all_ranks))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def get_length(self):
        return len(self.deck)

    def deal_card(self):
        return self.deck.pop(self.get_length()-1)

    def __str__(self):
        return str(self.deck)


class Hand:
    """This class represents the cards in the users hand."""
    def __init__(self, name, card1, card2):
        self.name = name
        self.cards = [card1, card2]
        self.sum = 0

    def hit(self, hit_card):
        self.cards.append(hit_card)

    def print_hand(self, hide):
        if hide:
            print(f'         {self.name} hand')
            print('*************     *************')
            print('*************     *           *')
            print('*************     *           *')
            print(f'*************     *   {self.cards[1][1]}')
            print(f'*************     *   {self.cards[1][0]}')
            print('*************     *           *')
            print('*************     *           *')
            print('*************     *************')
        else:
            print(f'         {self.name} hand')
            print('*************     *************')
            print('*           *     *           *')
            print('*           *     *           *')
            print(f'*   {self.cards[0][1]}               {self.cards[1][1]}')
            print(f'*   {self.cards[0][0]}             {self.cards[1][0]}')
            print('*           *      *          *')
            print('*           *      *          *')
            print('*************      ************')
        for card in self.cards[2:]:
            print('*************')
            print('*           *')
            print('*           *')
            print(f'*   {card[1]}')
            print(f'* {card[0]}')
            print('*           *')
            print('*           *')
            print('*************')

    def calc_card_sum(self):
        self.sum = 0
        for card in self.cards:
            self.sum += values[card[1]]
        if self.sum == 21:
            return int(self.sum)
        elif self.sum > 21:
            for card in self.cards:
                if values[card[1]] == 11:
                    self.sum -= 10
                    if self.sum == 21:
                        return int(self.sum)
                    elif self.sum < 21:
                        return int(self.sum)
                    else:
                        continue
        return int(self.sum)

    def __str__(self):
        return str(self.cards)


class Chips:
    """This class represents the betting chips."""
    def __init__(self, initial):
        self.current = initial
        self.additions = 0
        self.subtractions = 0

    def add_chips(self, re_up):
        self.current += re_up

    def win_hand(self, additions):
        self.additions += additions
        self.current += additions

    def lose_hand(self, subtractions):
        self.subtractions += subtractions
        self.current -= subtractions

    def check_bet(self, bet):
        if bet > self.current:
            return True
        else:
            return False

    def current_total(self):
        return self.current

    def cash_out(self):
        if self.additions >= self.subtractions:
            print(f'you have won ${self.additions-self.subtractions:.2f} this session.')

        else:
            print(f'you have lost ${self.subtractions-self.additions:.2f} this session.')

    def __str__(self):
        return f'current balance: ${self.current:.2f}'


game_deck = Deck()  # creates a new deck object
game_deck.shuffle_deck()  # shuffles the newly created deck
print('welcome to blackjack!  to begin, enter a dollar amount for your buy in or enter 0 to quit:')

while True:
    try:
        buy_in = int(input())
        break
    except ValueError:
        print('whoops! please enter a dollar amount or enter 0 to quit')

if buy_in > 0:
    play_round = '1'
    player_chips = Chips(buy_in)
    while play_round == '1':

        if player_chips.current_total() == 0:
            print('current balance is $0.00. enter dollar amount for buy in or 0 to exit')
            while True:
                try:
                    buy_more = int(input())
                    break
                except ValueError:
                    print('whoops! please enter a dollar amount or enter 0 to quit')
            if buy_more > 0:
                player_chips.add_chips(buy_more)
            else:
                break

        while play_round == '1':
            print('here we go! enter your bet:')

            while True:
                try:
                    player_bet = int(input())
                    break
                except ValueError:
                    print('whoops! please enter a dollar amount for your bet')

            if player_chips.check_bet(player_bet):
                print('mo money mo problems.  check your math!')
                print(player_chips)
                break

            player_hand = Hand('player', game_deck.deal_card(), game_deck.deal_card())
            computer_hand = Hand('computer', game_deck.deal_card(), game_deck.deal_card())
            print('dealing cards...')
            time.sleep(1)
            player_hand.print_hand(False)
            computer_hand.print_hand(True)

            if player_hand.calc_card_sum() == 21 and computer_hand.calc_card_sum() == 21:
                print('tie game')
                print(player_chips)
                break

            elif computer_hand.calc_card_sum() == 21:
                print('computer blackjack!  you lose')
                player_chips.lose_hand(player_bet)
                print(player_chips)
                break

            elif player_hand.calc_card_sum() == 21:
                print('blackjack!  you win')
                player_chips.win_hand(player_bet * 1.5)
                print(player_chips)
                break

            elif player_hand.calc_card_sum() < 21:
                print('h to hit, s to stay')
                hit = input()
                while hit == 'h':
                    print(f'dealing card to player...')
                    time.sleep(1)
                    player_hand.hit(game_deck.deal_card())
                    if player_hand.calc_card_sum() > 21:
                        break
                    else:
                        player_hand.print_hand(False)
                        computer_hand.print_hand(True)
                        print('h to hit, s to stay')
                        hit = input()

            if player_hand.calc_card_sum() <= 21:
                while computer_hand.calc_card_sum() < 17:
                    print(f'dealing card to computer...')
                    time.sleep(1)
                    computer_hand.hit(game_deck.deal_card())

            player_hand.print_hand(False)
            computer_hand.print_hand(False)

            if player_hand.calc_card_sum() > 21:
                print('player bust')
                player_chips.lose_hand(player_bet)
                print(player_chips)
                break

            elif computer_hand.calc_card_sum() > 21:
                print('computer bust')
                player_chips.win_hand(player_bet)
                print(player_chips)
                break

            elif computer_hand.calc_card_sum() == player_hand.calc_card_sum():
                print('tie')
                print(player_chips)
                break

            elif player_hand.calc_card_sum() > computer_hand.calc_card_sum():
                print('you win')
                player_chips.win_hand(player_bet)
                print(player_chips)
                break

            elif player_hand.calc_card_sum() < computer_hand.calc_card_sum():
                print('computer wins')
                player_chips.lose_hand(player_bet)
                print(player_chips)
                break

            else:
                print('if this prints, troubleshoot bug')
                break

        print('enter 1 to play again or any other key to cash out:')
        play_round = input()

exit_message = 'continue loop'
while exit_message == 'continue loop':
    player_chips.cash_out()
    print('thanks for playing! press any key to quit.')
    exit_message = input()
print('goodbye.')

time.sleep(2)
