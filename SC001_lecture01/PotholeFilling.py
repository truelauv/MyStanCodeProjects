"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: karel is at the (2,1)
    post-condition: karel is at the (2,7)
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    """
    pre-condition: karel is at the upper left of the pothole
    post-condition: karel is in the pothole
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition: karel is in the pothole
    post-condition: karel is at the upper left of the pothole
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
        turn_right()
        turn_right()


def put_99_beepers():
    """
    karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
