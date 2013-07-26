# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
play = False
message = ""
score = 0
LOSE_VALUE = -1
open_card = False

# strings
LOSE = "YOU LOSE!!!!"
WIN = "YOU WIN!!!!"
DEALER = "Dealer"
NEW = "New Deal?"
PLAYER = "Player"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self, card1, card2):
        self.cards = []
        self.value = 0
        self.add_card(card1)
        self.add_card(card2)

    def __str__(self):
        # return a string representation of a hand
        value = ""
        for card in self.cards:
            value += "|"+card.get_suit()+"|"+card.get_rank()+"|\n"
        return value

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)
        self.value += VALUES[card.get_rank()]

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        if self.value > 21:
            return LOSE_VALUE
        else:
            aces_count = 0
            with_aces_value = 0
            for card in self.cards:
                if card.get_rank() == 'A':
                    aces_count += 1
                    if aces_count == 2:
                        return 21
                    elif self.value + 10 <= 21:
                        with_aces_value = self.value + 10
            if with_aces_value != 0:
                return with_aces_value
            else:
                return self.value 
   
    def draw(self, canvas, pos, is_dealer = False):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            if is_dealer:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, pos, CARD_SIZE)
                is_dealer = False
            else:
                card_center = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                               CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
                canvas.draw_image(card_images, card_center, CARD_SIZE, pos, CARD_SIZE)
            pos[0] += CARD_SIZE[0]
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        
    def start_deck(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        self.start_deck()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop(0)
    
    def __str__(self):
        # return a string representing the deck
        value = ""
        for card in self.cards:
            value += card.get_suit() + "|" + card.get_rank() + "\n"
        value += str(len(self.cards))
        return value


#define event handlers for buttons
def deal():
    global message, play, dealer, player, deck, open_card, score
    if play:
        score -= 1 
    #print deck
    deck.shuffle()
    #print deck
    open_card = False
    dealer = Hand(deck.deal_card(),deck.deal_card())
    player = Hand(deck.deal_card(),deck.deal_card())
    message = "Hit or Stand?"
    play = True

def hit():
    global player, deck, score, play, message
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    if play:
        player.add_card(deck.deal_card())
        if LOSE_VALUE == player.get_value():
            score -= 1
            message = LOSE
            play = False
       
def stand():
    global play, score, dealer, player, deck, message, open_card
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    if play:
        open_card = True
        while dealer.get_value() < 17 and dealer.get_value() != LOSE_VALUE:
            dealer.add_card(deck.deal_card())
        if LOSE_VALUE == dealer.get_value():
            score += 1
            message = WIN
        elif dealer.get_value() >= player.get_value():
            score -= 1
            message = LOSE
        else:
            score += 1
            message = WIN
        play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    # DEALER
    canvas.draw_text(DEALER,[70,200],50, "Black")
    dealer.draw(canvas, [100,250], not open_card)
    # PLAYER
    canvas.draw_text(PLAYER,[70,390],50, "Black")
    player.draw(canvas, [100,450])
    # TITLE
    canvas.draw_text("Let's play BlackJack",[100,100],50, "Blue")
    # SCORE
    canvas.draw_text("Player Score: "+str(score),[250,150],50, "White")
    canvas.draw_text(message,[270,350],50,"Yellow")
    if not play:
        canvas.draw_text(NEW,[270,400],50,"Yellow")


#global deck, we just need one deck
deck = Deck()
deal()
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric