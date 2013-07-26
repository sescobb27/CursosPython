# Implementation of classic arcade game Pong

import simplegui
from random import randrange

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
HALF_HEIGHT = HEIGHT/2
HALF_WIDTH = WIDTH/2
X1 = 0
Y1 = 1
X2 = 2
Y2 = 3
SCORE1_POS = [HALF_WIDTH/2,60]
SCORE2_POS = [HALF_WIDTH+HALF_WIDTH/2,60]
score1 = 0
score2 = 0
w_press = False
s_press = False
up_press = False
down_press = False

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [HALF_WIDTH,HALF_HEIGHT]
    vel_x = randrange(120,240)/60
    vel_y = randrange(60,180)/60
    if right:
        ball_vel = [-vel_x,-vel_y]
    else:
        ball_vel = [vel_x,-vel_y]


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos # these are floats
    global score1, score2  # these are ints
    ball_init(True)
    paddle1_pos = [0, HALF_HEIGHT - HALF_PAD_HEIGHT, 0, HALF_HEIGHT + HALF_PAD_HEIGHT]
    paddle2_pos = [WIDTH, HALF_HEIGHT - HALF_PAD_HEIGHT, WIDTH, HALF_HEIGHT + HALF_PAD_HEIGHT]
    score1 = 0
    score2 = 0

def update_ball():
    global score1, score2
    if ball_pos[0]-BALL_RADIUS <= PAD_WIDTH:
        if (ball_pos[1] <= paddle1_pos[Y2]) and (ball_pos[1] >= paddle1_pos[Y1]):
            #ball_vel[0] *= -1
            increment_vel()
        else:
            score2 += 1
            ball_init(False)
    elif ball_pos[0]+BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if (ball_pos[1] <= paddle2_pos[Y2]) and (ball_pos[1] >= paddle2_pos[Y1]):
            #ball_vel[0] *= -1
            increment_vel()
        else:
            score1 += 1
            ball_init(True)
    if ball_pos[1]-BALL_RADIUS <= 0:
        ball_vel[1] *= -1
    elif ball_pos[1]+BALL_RADIUS >= HEIGHT:
        ball_vel[1] *= -1
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

def increment_vel():
    ball_vel[0] += ball_vel[0]/10
    ball_vel[1] += ball_vel[1]/10
    ball_vel[0] *= -1

    
def update_paddle():
    if w_press and (paddle1_pos[Y1] >= 0):
        paddle1_pos[Y1] -= 5
        paddle1_pos[Y2] -= 5
    if s_press and (paddle1_pos[Y2] <= HEIGHT):
        paddle1_pos[Y1] += 5
        paddle1_pos[Y2] += 5
    if up_press and (paddle2_pos[Y1] >= 0):
        paddle2_pos[Y1] -= 5
        paddle2_pos[Y2] -= 5
    if down_press and (paddle2_pos[Y2] <= HEIGHT):
        paddle2_pos[Y1] += 5
        paddle2_pos[Y2] += 5
    
def draw(c):
    # update paddle's vertical position, keep paddle on the screen
    update_paddle()
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw paddles
    c.draw_line([paddle1_pos[X1],paddle1_pos[Y1]],[paddle1_pos[X2],paddle1_pos[Y2]],PAD_WIDTH*2,"White")
    c.draw_line([paddle2_pos[X1],paddle2_pos[Y1]],[paddle2_pos[X2],paddle2_pos[Y2]],PAD_WIDTH*2,"White")
    # update ball
    update_ball()
    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,2,"White","White")
    c.draw_text(str(score1),SCORE1_POS,70,"White")
    c.draw_text(str(score2),SCORE2_POS,70,"White")
        
def keydown(key):
    global w_press, s_press, up_press, down_press
    if key == simplegui.KEY_MAP["w"]:
        w_press = True
        s_press = False
    elif key == simplegui.KEY_MAP["s"]:
        s_press = True
        w_press = False
    if key == simplegui.KEY_MAP["up"]:
        up_press = True
        down_press = False
    elif key == simplegui.KEY_MAP["down"]:
        down_press = True
        up_press = False
   
def keyup(key):
    global w_press, s_press, up_press, down_press
    if key == simplegui.KEY_MAP["w"]:
        w_press = False
    elif key == simplegui.KEY_MAP["s"]:
        s_press =  False
    if key == simplegui.KEY_MAP["up"]:
        up_press =  False
    elif key == simplegui.KEY_MAP["down"]:
        down_press = False


new_game()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Restart",new_game,200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()