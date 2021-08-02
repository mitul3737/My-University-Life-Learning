#Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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


move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()

