from os import system, name
from math import tan, cos, radians
from random import randint

import time


ARENA_LENGTH = 80
ARENA_HEIGHT = 20
G = 9.81


def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def create_screen_buffer(height, width):
    matrix = []
    for row in range(height):
        matrix.append([])
        for _ in range(width):
            matrix[row].append(" ")
    return matrix


def init_game(screen_buffer):




def render_game(screen_buffer):
    print(" " + "".join(["_"] * ARENA_LENGTH))
    for row in screen_buffer:
        print("|" + "".join(row) + "|")
    print("-" + "".join(["-"] * ARENA_LENGTH) + "-")


def game(t_player, t_pc):
    pass


def main():
    screen_buffer = create_screen_buffer(ARENA_HEIGHT, ARENA_LENGTH)
    tank_player, tank_pc = init_game(screen_buffer)
    render_game(screen_buffer)


if __name__ == "__main__":
    main()