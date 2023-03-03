# -*- coding: utf-8 -*-
"""
Created on Wed May  4 23:14:16 2022

@author: melike
"""

from random import choice

def create_deck():
    deck = []
    for i in symbol:
        for j in card_val:
            deck.append([i, j])
    return deck

def pick_card(deck):
    card = choice(deck)
    deck.remove(card)
    return card

def init_cards(deck):
    card1 = pick_card(deck)
    card2 = pick_card(deck)
    return [card1, card2]

def show_cards(show_who, gamer_cards, croupier_cards):
    print()
    if show_who == 1: # start of the game
        print("Croupier's open card is:", card_name(croupier_cards[1]))
        print("Your cards are:", card_name(gamer_cards[0]), card_name(gamer_cards[1]), end=" ")
        print("(Total: ", cards_sum(gamer_cards), ")", sep="", end="\n")
    elif show_who == 2: # show only gamer cards
        print("Your cards are:", end=" ")
        for i in gamer_cards:
            print(card_name(i), end=" ")
        print("(Total: ", cards_sum(gamer_cards), ")", sep="", end="\n")
    elif show_who == 3: # show only croupier cards
        print("Croupier's cards are:", end=" ")
        for i in croupier_cards:
            print(card_name(i), end=" ")
        print("(Total: ", cards_sum(croupier_cards), ")", sep="", end="\n")

def card_name(card):
    return str(card[0] + " " + card[1])

def cards_sum(cards):
    result = 0
    for i in cards:
        result += card_val.get(i[1])
    return result

def add_new_card(deck, gamer_cards):
    card = pick_card(deck)
    gamer_cards.append(card)

def decide_winner(gamer_cards, croupier_cards):
    gamer_result = cards_sum(gamer_cards)
    croupier_result = cards_sum(croupier_cards)
    if croupier_result > 21:
        print("YOU WIN!")
    elif croupier_result == 21:
        print("Blackjack!", end=" ")
        if gamer_result == 21:
            print("It's a draw.")
        else:
            print("Croupier wins.")
    else:
        if croupier_result < gamer_result:
            print("You win.")
        elif croupier_result == gamer_result:
            print("It's a draw.")
        else:
            print("You lose.")


card_val = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, 
        "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}

symbol = ["Heart", "Diamond", "Spade", "Club"]

def game():
    deck = create_deck()
    croupier_cards = init_cards(deck)
    gamer_cards    = init_cards(deck)

    show_cards(1, gamer_cards, croupier_cards)
    
    card_or_pass = "c"
    while cards_sum(gamer_cards) < 21 and card_or_pass == "c":
        card_or_pass = input("Card or Pass (c/p): ")
        if card_or_pass.lower() == "c":
            add_new_card(deck, gamer_cards)
            show_cards(2, gamer_cards, croupier_cards)
        elif card_or_pass.lower() == "p":
            break
        else:
            print("c or p")
    
    if cards_sum(gamer_cards) > 21:
        print("YOU LOSE :(")
        return
    elif cards_sum(gamer_cards) == 21:
        print("\nBlackjack! It's croupier's turn now.", end="\n")
    else:
        print("\nCroupier's turn.", end="\n")
    
    # show croupier's cards
    show_cards(3, gamer_cards, croupier_cards)
    
    while cards_sum(croupier_cards) < 17:
        add_new_card(deck, croupier_cards)
        show_cards(3, gamer_cards, croupier_cards)
    
    decide_winner(gamer_cards, croupier_cards)
