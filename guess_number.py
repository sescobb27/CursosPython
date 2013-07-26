# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
from random import randrange

# initialize global variables used in your code
secret_num = 0
guesses_num = 0
range_game = 100

# define event handlers for control panel

def print_remaining_guesses():
    print "Number of remaining guesses is ->", str(guesses_num)
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_num, guesses_num, range_game
    secret_num = randrange(0, 100)
    guesses_num = 7
    range_game = 100
    print
    print "New game. Range is from 0 to 100"
    print_remaining_guesses()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_num, guesses_num, range_game
    secret_num = randrange(0, 1000)
    guesses_num = 10
    range_game = 1000
    print
    print "New game. Range is from 0 to 1000"
    print_remaining_guesses()
    
def get_input(guess):
    # main game logic goes here
    global guesses_num
    print
    print "Guess was ->", guess
    guesses_num -= 1
    print_remaining_guesses()
    user_guess = int(guess)
    if user_guess > secret_num:
        print "Lower!"
    elif user_guess < secret_num:
        print "Higher!"
    else:
        print "Correct!"
        initialize()
        return
    if guesses_num == 0:
        print "You ran out of guesses. the number was", str(secret_num)
        initialize()
        return

def initialize():
    if range_game == 100:
        range100()
    elif range_game == 1000:
        range1000()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess",get_input, 100)

initialize()

# start frame
frame.start()

# always remember to check your completed program against the grading rubric
