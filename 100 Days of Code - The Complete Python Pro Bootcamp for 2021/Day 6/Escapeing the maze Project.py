#Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_round():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_round()


def make_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
