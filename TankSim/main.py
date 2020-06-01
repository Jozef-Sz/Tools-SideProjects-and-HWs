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


def drop_place(xpos, char):
    xpos -= 1
    if xpos < 0 or xpos > ARENA_LENGTH - 1: raise Exception("Invalid x position")
    for i in range(ARENA_HEIGHT - 1):
        peek_pixel = screen_buffer[i + 1][xpos]
        if peek_pixel == chr(0x2588):
            screen_buffer[i][xpos] = char
            return ARENA_HEIGHT - i


def insert_char(xpos, ypos, char):
    print("Inside insert char")
    if xpos < 0 or ypos < 0:
        return
    print("Passed first filter")
    x = xpos - 1
    y = ARENA_HEIGHT - ypos if ypos != 0 else -1
    print("x of f", x, "y of f", y)    
    if (x < 0 or x > ARENA_LENGTH - 1) or (y < 0 or y > ARENA_HEIGHT - 1):
        return
    print("Passed second filter")
    screen_buffer[y][x] = char


def init_game():
    t_player, t_pc = {
        "x": randint(1, ARENA_LENGTH / 2 - 1),
        "y": None
    }, {
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


def shoot_function(x, angle, velocity, xoffset, yoffset):
    velocity /= 20  # Normalize velocity
    a = tan(radians(angle)) * (x + xoffset)
    b = G * ((x + xoffset)**2)
    c = 2 * (velocity**2) * (cos(radians(angle))**2)
    b /= c
    return round(a - b) + yoffset 


def create_projectile_trajectory(angle, velocity, player):
    for x in range(1, ARENA_LENGTH + 1):
        y = shoot_function(x, angle, velocity, -player["x"], player["y"])
        print(x, y)
        insert_char(x, y, ".")
    return 0


def human_turn(pos):
    create_projectile_trajectory(45, 300, pos)


def pc_turn(pos):
    pass


def game(t_player, t_pc):
    human_turn(t_player)
    render_game()
    print(t_player["x"], t_player["y"])
    return 0


def main():
    create_screen_buffer(ARENA_HEIGHT, ARENA_LENGTH)
    t_player, t_pc = init_game()
    winner = game(t_player, t_pc)


if __name__ == "__main__":
    main()