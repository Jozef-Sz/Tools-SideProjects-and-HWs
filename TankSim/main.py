from os import system, name
from math import tan, cos, radians
from random import randint

import time


ARENA_LENGTH = 80
ARENA_HEIGHT = 20
G = 9.81

screen_buffer = []
turn = 1

def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def create_screen_buffer(height, width):
    for row in range(height):
        screen_buffer.append([])
        for _ in range(width):
            screen_buffer[row].append(" ")


def drop_place(posx, char):
    posx -= 1
    if posx < 0 or posx > ARENA_LENGTH - 1: raise Exception("Invalid x position")
    for i in range(ARENA_HEIGHT - 1):
        peek_pixel = screen_buffer[i + 1][posx]
        if peek_pixel == chr(0x2588):
            screen_buffer[i][posx] = char
            return ARENA_HEIGHT - i


def init_game():
    t_player = {
        "x": randint(1, ARENA_LENGTH / 2 - 1),
        "y": None
    }

    t_pc = {
        "x": randint(ARENA_LENGTH / 2, ARENA_LENGTH),
        "y": None
    }

    for i in range(ARENA_LENGTH):
        screen_buffer[ARENA_HEIGHT - 1][i] = chr(0x2588)

    t_player["y"] = drop_place(t_player["x"], "H")
    t_pc["y"]     = drop_place(t_pc["x"], "P")

    return (t_player, t_pc)


def render_game():
    print(" " + "".join(["_"] * ARENA_LENGTH))
    for row in screen_buffer:
        print("|" + "".join(row) + "|")
    print("-" + "".join(["-"] * ARENA_LENGTH) + "-")


def game(t_player, t_pc):
    print(t_player["x"], t_player["y"])
    print(t_pc["x"], t_pc["y"])


def main():
    create_screen_buffer(ARENA_HEIGHT, ARENA_LENGTH)
    t_player, t_pc = init_game()
    render_game()
    game(t_player, t_pc)


if __name__ == "__main__":
    main()