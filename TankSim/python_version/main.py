from os import system, name
from math import tan, cos, radians
from random import randint
# NOISE MODULE is not a built in module. Must be installed via pip or other methods!
from noise import pnoise1

import time


ARENA_LENGTH = 80
ARENA_HEIGHT = 20

GROUND_TILE  = chr(0x2588)
PROJECTILE_TILE = "*"
PATH_TILE = "."
PLAYER_TILE = "K"
PC_TILE = "X"

G = 9.81

screen_buffer = []
turn = 1

def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def remap(value, old_min, old_max, new_min, new_max):
    '''
    Maps a number value from an old range to a new 
    range and returns new value between the new 
    range, same function as in processing. 
    '''
    old_range = old_max - old_min
    new_range = new_max - new_min
    return (((value - old_min) * new_range) / old_range) + new_min


def is_ground(x, y):
    if y > 0 and y < 21:
        x -= 1
        y = ARENA_HEIGHT - y
        if screen_buffer[y][x] == GROUND_TILE:
            return True
    return False


def compare(xmissile, xplayer, op):
    if op == "greaterthan":
        if xmissile > xplayer:
            return True
        return False
    else:
        if xmissile < xplayer:
            return True
        return False


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
        if peek_pixel == GROUND_TILE:
            screen_buffer[i][xpos] = char
            return ARENA_HEIGHT - i


def insert_char(xpos, ypos, char):
    if xpos < 0 or ypos < 0:
        return
    x = xpos - 1
    y = ARENA_HEIGHT - ypos if ypos != 0 else -1    
    if (x < 0 or x > ARENA_LENGTH - 1) or (y < 0 or y > ARENA_HEIGHT - 1):
        return
    screen_buffer[y][x] = char


def generate_terrain(max_height):
    noise_seed = randint(0, 20)
    # defines the roughness, smaller is smoother
    increment = 0.1 
    sample = []
    for _ in range(ARENA_LENGTH):
        sample.append(pnoise1(noise_seed, octaves=1))
        noise_seed += increment
    # print(sample)
    min_val, max_val = min(sample), max(sample)
    normalized_sample = map(
        lambda x: round(remap(x, min_val, max_val, 1, max_height)), 
        sample)
    return list(normalized_sample)


def init_game():
    t_player, t_pc = {
        "x": randint(1, ARENA_LENGTH / 2 - 1),
        "y": None
    }, {
        "x": randint(ARENA_LENGTH / 2, ARENA_LENGTH),
        "y": None
    }

    # Create flat ground
    # for i in range(ARENA_LENGTH):
    #     screen_buffer[ARENA_HEIGHT - 1][i] = GROUND_TILE

    # Create proceduaral terrain
    terrain = generate_terrain(5)

    for col in range(ARENA_LENGTH):
        offset = ARENA_HEIGHT - terrain[col]
        for h in range(terrain[col]):
            screen_buffer[h + offset][col] = GROUND_TILE

    t_player["y"] = drop_place(t_player["x"], PLAYER_TILE)
    t_pc["y"]     = drop_place(t_pc["x"], PC_TILE)

    return (t_player, t_pc)


def render_game():
    clear_screen()
    print(" " + "".join(["_"] * ARENA_LENGTH))
    for row in screen_buffer:
        print("|" + "".join(row) + "|")
    print("-" + "".join(["-"] * ARENA_LENGTH) + "-")


def shoot_function(x, angle, velocity, xoffset, yoffset):
    '''
    Equation of projectile motion. For more details see
    https://en.wikipedia.org/wiki/Projectile_motion#Displacement
    '''
    velocity /= 20  # Normalize velocity
    a = tan(radians(angle)) * (x + xoffset)
    b = G * ((x + xoffset)**2)
    c = 2 * (velocity**2) * (cos(radians(angle))**2)
    b /= c
    return round(a - b) + yoffset 


def create_projectile_trajectory(angle, velocity, player):
    '''
    This function cares only about calculating the trajectory 
    and retrieving x y coords of the landed projectile. In case
    the projectile landed outside of the arena, the function
    returns -1
    '''
    start, end, step = None, None, None
    rel_op = None

    if cos(radians(angle)) > 0:
        # creating trajectory from left to right
        start, end, step = player["x"], ARENA_LENGTH + 1, 1
        rel_op = "greaterthan"
    else :
        # creating trajecory from right to left
        start, end, step = player["x"], 0, -1
        rel_op = "lessthan"
    
    for x in range(start, end, step):
        y = shoot_function(x, angle, velocity, -player["x"], player["y"])

        # Guard for the last layer of the ground and of the shooter
        if y == player["y"] and x == player["x"]:
            # Then this is the shooting player, skit it!
            continue
        elif is_ground(x, y):
            # Then it is the very bottom ground
            if compare(x, player["x"], rel_op):
                xoffset = -1 if x > player["x"] else 1
                hit_ycoord = y + 1
                hit_xcoord = x + xoffset
                insert_char(hit_xcoord, hit_ycoord, PROJECTILE_TILE)
                return (hit_xcoord, hit_ycoord)
            
            continue
        else:
            insert_char(x, y, PATH_TILE)
    return -1


def clear_projectiles_trajectory():
    pass


def human_turn(pos):
    global turn
    indent = "   "
    print(f"\n{indent}PLAYER'S TURN ({PLAYER_TILE}) | TURN NO. {turn}")
    angle = int(input(f"{indent}Angle (deg): "))
    power = int(input(f"{indent}Power (m/s): "))

    res = create_projectile_trajectory(angle, power, pos)
    print(res)

    turn += 1


def pc_turn(pos):
    global turn
    indent = "   " + "".join([" "] * int(ARENA_LENGTH / 2))
    print(f"\n{indent}PC'S TURN ({PC_TILE}) | TURN NO. {turn}")
    angle = int(input(f"{indent}Angle (deg): "))
    power = int(input(f"{indent}Power (m/s): "))

    res = create_projectile_trajectory(140, 310, pos)
    print(res)
    turn += 1


def game(t_player, t_pc):
    render_game()
    while True:
        human_turn(t_player)
        render_game()
        pc_turn(t_pc)
        render_game()
    # print("H", t_player["x"], t_player["y"])
    # print("P", t_pc["x"], t_pc["y"])
    return 0


def main():
    create_screen_buffer(ARENA_HEIGHT, ARENA_LENGTH)
    t_player, t_pc = init_game()
    winner = game(t_player, t_pc)
    print(winner)


if __name__ == "__main__":
    main()