# -*- coding: utf-8 -*-
"""
@author: melike
"""

import random

card_val = {"As":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, 
        "8":8, "9":9, "10":10, "Bacak":10, "Kız":10, "Papaz":10}

symbol = ["Kupa", "Karo", "Maça", "Sinek"]


def game():
    show_cards()
    decide_win()
    
    
def create_deck():
    deck = []
    for i in symbol:
        for j in card_val:
            deck.append([i, j])
    return deck

def pick_card():
    card = random.choice(deck)
    remove_from_deck(card)
    return card

def pick_init_cards():
    card1 = pick_card()
    card2 = pick_card()
    return [card1, card2]

def remove_from_deck(card):
    return deck.remove(card)

def show_cards():
    print("Croupier's open card is:", card_name(croupier_cards[1]))
    print("Your cards are:")
    for i in gamer_cards:
        print(card_name(i))

def card_name(card):
    return str(card[0] + " " + card[1])

def cards_sum(cards):
    result = 0
    for i in cards:
        result += card_val.get(i[1])
    return result
    
def decide_win():
    if(cards_sum(croupier_cards)) >= 21:
        print("YOU LOSE")
    
    if(cards_sum(croupier_cards) > cards_sum(gamer_cards)):
        print("YOU LOSE")
    elif cards_sum(croupier_cards) < cards_sum(gamer_cards):
        print("YOU WIN!")
    else: 
        print("YOU ALL LOSE")

deck = create_deck()
croupier_cards = pick_init_cards()
gamer_cards = pick_init_cards()

game()
