# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user11_hSVhbMDVPD_24.py
import simplegui
# define global variables
time = 0
sec = 0
min = 0
mil = 0
count = 0
asserts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global sec, min, mil
    mil = t % 10
    time = (t // 10)
    sec = time % 60
    min = (time % 3600) // 60
    return "%d:%.2d.%d" % (min, sec, mil)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global count, asserts
    if timer.is_running():
        count += 1
        if mil == 0:
            asserts += 1
    timer.stop()

def reset():
    global timer, time, sec, min, mil, count, asserts
    timer.stop()
    timer = simplegui.create_timer(100,time_handler)
    time = 0
    min = 0
    sec = 0
    mil = 0
    count = 0
    asserts = 0

# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),(90,120),50,"Yellow")
    score = "%d/%d" % (asserts,count)
    canvas.draw_text(score,(250,30),30,"Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
frame.add_button("start",start,100)
frame.add_button("stop",stop,100)
frame.add_button("reset",reset,100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100,time_handler)
# start frame
frame.start()
# Please remember to review the grading rubric

#print format(0) == "0:00.0"
#print format(11) == "0:01.1"
#print format(321) == "0:32.1"
#print format(613) == "1:01.3"