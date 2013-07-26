import simplegui
def init(num):
    global value
    value = num

def update():
    global value
    print str(value)
    if value % 2 == 0:
        value /= 2
    elif value == 1:
        timer.stop()
    else:
        value *= 3
        value += 1

timer = simplegui.create_timer(200, update)

# start program
init(217)
timer.start()
