from os import system, name
from math import tan, cos, radians
from random import randint
# NOISE MODULE is not a built in module. Must be installed via pip or other methods!
from noise import pnoise1

import time

'''
TODO:
    1) DONE Recreate create_projectile_trajectory function, because
      it has flaws in collision detection
    2) DONE Finish the gameloop
    3) Make sort of ai for pc 
    4) Health bar for each tank
    5 ) Terrain damage
'''


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
ai_angle = randint(100, 160) 
ai_power = randint(100, 500)


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

    if cos(radians(angle)) > 0:
        # creating trajectory from left to right
        start, end, step = player["x"], ARENA_LENGTH + 1, 1
    else :
        # creating trajecory from right to left
        start, end, step = player["x"], 0, -1

    for x in range(start, end, step):
        y = shoot_function(x, angle, velocity, -player["x"], player["y"])
        if y == player["y"] and x == player["x"]:
            # Then this is the shooting player, skip it!
            continue
        elif is_ground(x, y) or y < 0:
            xoffset = -1 if x > player["x"] else 1
            y = y if y > 0 else 1
            hit_point = climb_up(x, y)
            insert_char(hit_point[0] + xoffset, hit_point[1], PROJECTILE_TILE)
            return (hit_point[0] + xoffset, hit_point[1])
        else:
            insert_char(x, y, PATH_TILE)
    return -1


def climb_up(x, y):
    if not is_ground(x, y):
        return (x, y)
    return climb_up(x, y + 1)


def clear_projectiles_trajectory():
    for row in range(ARENA_HEIGHT):
        for col in range(ARENA_LENGTH):
            tile = screen_buffer[row][col]
            if tile == PROJECTILE_TILE or tile == PATH_TILE:
                screen_buffer[row][col] = " " 


def adjust_parameters(angle, power, hit, target):
    if hit == -1: return (angle-10, power - 100)
    if hit[0] > target["x"]:
        # We need to increase power 
    else:
        # Decrease power 
        pass


def human_turn(pos):
    global turn
    clear_projectiles_trajectory()

    indent = "   "
    print(f"\n{indent}PLAYER'S TURN ({PLAYER_TILE}) | TURN NO. {turn}")
    angle = int(input(f"{indent}Angle (deg): "))
    power = int(input(f"{indent}Power (m/s): "))

    hit_point = create_projectile_trajectory(angle, power, pos)
    
    hit = None
    if hit_point != -1:
        hit = { "x": hit_point[0], "y": hit_point[1] }
        print(f"{indent}Hit inside of area X: {hit['x']}, Y: {hit['y']}")
    else:
        hit = {"x": None, "y": None}
        print(f"{indent}Hit outside of area...")
        
    time.sleep(1)
    turn += 1
    return hit


def pc_turn(t_pc, target):
    global turn, ai_angle, ai_power
    clear_projectiles_trajectory()

    indent = "   " + "".join([" "] * int(ARENA_LENGTH / 2))
    print(f"\n{indent}PC'S TURN ({PC_TILE}) | TURN NO. {turn}")
    print(f"{indent}Angle (deg): {ai_angle}")
    print(f"{indent}Power (m/s): {ai_power}")

    hit_point = create_projectile_trajectory(ai_angle, ai_power, t_pc)

    new_parameters = adjust_parameters(ai_angle, ai_power, hit_point, target)
    ai_angle = new_parameters[0]
    ai_power = new_parameters[1]
    
    hit = None
    if hit_point != -1:
        hit = { "x": hit_point[0], "y": hit_point[1] }
        print(f"{indent}Hit inside of area X: {hit['x']}, Y: {hit['y']}")
    else:
        hit = {"x": None, "y": None}
        print(f"{indent}Hit outside of area...")

    time.sleep(1)
    turn += 1
    return hit


def print_winner(winner):
    if winner == 0:
        print(f"Tank {PLAYER_TILE} is the winner")
    elif winner == 1:
        print(f"Tank {PC_TILE} won, by suicide of the enemy")
    elif winner == 2:
        print(f"Tank {PC_TILE} is the winner")
    else:
        print(f"Tank {PLAYER_TILE} won, by suicide of the enemy")


def game(t_player, t_pc):
    render_game()
    while True:
        hit = human_turn(t_player)
        render_game()
        if hit["x"] == t_pc["x"]: return 0
        if hit["x"] == t_player["x"]: return 1

        hit = pc_turn(t_pc, t_player)
        render_game()
        if hit["x"] == t_player["x"]: return 2
        if hit["x"] == t_pc["x"]: return 3


def main():
    create_screen_buffer(ARENA_HEIGHT, ARENA_LENGTH)
    t_player, t_pc = init_game()
    winner = game(t_player, t_pc)
    print_winner(winner)


if __name__ == "__main__":
    main()