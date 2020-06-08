#define _USE_MATH_DEFINES

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// NOTE: for linux users gcc main.c -lm -o main


#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
#define T_CMD "cls"
#define GROUND_TILE 219
#include <Windows.h>
#define timeout(t) (Sleep(t*1000))
#else
#define T_CMD "clear"
#define GROUND_TILE 35
#include <unistd.h>
#define timeout(t) (sleep(t))
#endif

#define ARENA_LENGTH 80
#define ARENA_HEIGHT 20
#define PROJECTILE_TILE '*'
#define PATH_TILE '.'
#define PLAYER_TILE 'K'
#define PC_TILE 'X'
#define G 9.81


// ----------------------- Perlin Noise -----------------------
#define SAMPLE_SIZE 500

float slopes[SAMPLE_SIZE];

void init_noise()
{
    for(int i = 0; i < SAMPLE_SIZE; i++)
        slopes[i] = (float)(rand() - 1) / (float)RAND_MAX * 2 - 1;
}

float noise(float x)
{
	float lo = floor(x);
	float hi = lo + 1.0f;
	float dist = x - lo;
	float loSlope = slopes[(int)lo];
	float hiSlope = slopes[(int)hi];
	float loPos = loSlope * dist;
	float hiPos = -hiSlope * (1.0f - dist);
	float u = dist * dist * (3.0f - 2.0f * dist);
	return (loPos*(1-u) + (hiPos*u));
}

float map(float value, float old_min, float old_max, float new_min, float new_max)
{
    float old_range = old_max - old_min;
    float new_range = new_max - new_min;
    return (value - old_min) * new_range / old_range + new_min;
}

float min_val(float* pool, int pool_size)
{
    float smallest = pool[0];
    for(int i = 1; i < pool_size; i++)
    {
        if(pool[i] < smallest) smallest = pool[i];
    }
    return smallest;
}

float max_val(float* pool, int pool_size)
{
    float biggest = pool[0];
    for(int i = 1; i < pool_size; i++)
    {
        if(pool[i] > biggest) biggest = pool[i];
    }
    return biggest;
}
// ------------------------------------------------------------


typedef struct {
    int x;
    int y;
    int angle;
    int power;
} Entity;


void clear_screen() { system(T_CMD); }

int random_number(int min, int max)
{
    // Does includes max
    return (rand() % (max + 1 - min)) + min;
}

int is_ground(char sb[ARENA_HEIGHT][ARENA_LENGTH], int x, int y)
{
    if(y > 0 && y < 21)
    {
        x -= 1;
        y = ARENA_HEIGHT - y;
        if (sb[y][x] == (char)GROUND_TILE) return 1;
    }
    return 0;
}

void render_game(char sb[ARENA_HEIGHT][ARENA_LENGTH])
{
    clear_screen();
    printf(" ");
    for(int i = 0; i < ARENA_LENGTH; i++)
        printf("_");
    printf("\n");

    for(int i = 0; i < ARENA_HEIGHT; i++)
    {
        printf("|");
        for(int j = 0; j < ARENA_LENGTH; j++)
            printf("%c",sb[i][j]);
        printf("|\n");
    }

    for(int i = 0; i < ARENA_LENGTH + 2; i++)
        printf("-");
    printf("\n");
}

int drop_place(char sb[ARENA_HEIGHT][ARENA_LENGTH], int xpos, char tile)
{
    xpos -= 1;
    for(int i = 0; i < ARENA_HEIGHT - 1; i++)
    {
        char peek_pixel = sb[i + 1][xpos];
        if(peek_pixel == (char)GROUND_TILE)
        {
            sb[i][xpos] = tile;
            return ARENA_HEIGHT - i;
        }
    }
}

void insert_tile(char sb[ARENA_HEIGHT][ARENA_LENGTH], int xpos, int ypos, char tile)
{
    if (xpos < 0 || ypos < 0) return;
    int x = xpos - 1;
    int y = (ypos != 0) ? ARENA_HEIGHT - ypos : -1;
    if ((x < 0 || x > ARENA_LENGTH - 1) || (y < 0 || y > ARENA_HEIGHT - 1))
        return;
    sb[y][x] = tile;
}

void print_array(int* array, int size)
{
    for(int i = 0; i < size; i++)
    {
        printf("%d\n", array[i]);
    }
}

int* generate_terrain(int max_height)
{
    float x = 0.0f;
    float increment = 0.1f;
    float sample[ARENA_LENGTH];
    for(int i = 0; i < ARENA_LENGTH; i++)
    {
        sample[i] = noise(x);
        x += increment;
    }
    float min = min_val(sample, ARENA_LENGTH);
    float max = max_val(sample, ARENA_LENGTH);
    static int normalized_sample[ARENA_LENGTH];
    for(int i = 0; i < ARENA_LENGTH; i++)
    {
        normalized_sample[i] = (int)map(sample[i], min, max, 1.0f, (float)max_height);
    }
    return normalized_sample;
}

void init_game(char sb[ARENA_HEIGHT][ARENA_LENGTH], Entity* t_player, Entity* t_pc)
{
    // Randomly position players
    t_player->x = random_number(1, ARENA_LENGTH / 2 - 1);
    t_pc->x = random_number(ARENA_LENGTH / 2, ARENA_LENGTH);

    // Initialize perlin noise and screen buffer
    init_noise();
    for(int i = 0; i < ARENA_HEIGHT; i++)
        for(int j = 0; j < ARENA_LENGTH; j++)
            sb[i][j] = ' ';

    // Create flat ground
    // for(int i = 0; i < ARENA_LENGTH; i++)
    //     sb[ARENA_HEIGHT - 1][i] = GROUND_TILE;

    // Create proceduaral terrain
    int* terrain = generate_terrain(5);
    for(int i = 0; i < ARENA_LENGTH; i++)
    {
        int offset = ARENA_HEIGHT - terrain[i];
        for(int j = 0; j < terrain[i]; j++)
        {
            sb[j + offset][i] = GROUND_TILE;
        }
    }

    t_player->y = drop_place(sb, t_player->x, PLAYER_TILE);
    t_pc->y = drop_place(sb, t_pc->x, PC_TILE);
}

double deg2rad(double deg)
{
    return deg * M_PI / 180;
}

int shoot_function(int x, int angle, int velocity, int xoffset, int yoffset)
{
    velocity /= 20;  // Normalize velocity
    float a = tan(deg2rad(angle)) * (x + xoffset);
    float b = G * pow(x + xoffset, 2);
    float c = 2 * pow(velocity, 2) * pow(cos(deg2rad(angle)), 2);
    b /= c;
    return round(a - b) + yoffset;
}

int climb_up(char sb[ARENA_HEIGHT][ARENA_LENGTH], int x, int y)
{
    if (! is_ground(sb, x, y)) return y;
    return climb_up(sb, x, y + 1);
}

Entity create_projectile_trajectory(char sb[ARENA_HEIGHT][ARENA_LENGTH], int angle, int velocity, Entity* player)
{
    Entity projectile;
    int start, end, step;

    if (cos(deg2rad(angle)) > 0)
    {
        start = player->x;
        end = ARENA_LENGTH + 1;
        step = 1;
    } else {
        start = player->x;
        end = 0;
        step = -1;
    }

    for(int x = start; x != end; x += step)
    {
        int y = shoot_function(x, angle, velocity, -player->x, player->y);
        if (y == player->y && x == player->x) continue;
        else if (is_ground(sb, x, y) || y < 0)
        {
            int xoffset = (x > player->x) ? -1 : 1;
            y = ( y > 0) ? y : 1;
            y = climb_up(sb, x, y);
            insert_tile(sb, x+xoffset, y, PROJECTILE_TILE);
            projectile.x = x + xoffset;
            projectile.y = y;
            return projectile;
        } else {
            insert_tile(sb, x, y, PATH_TILE);
        }
    }
    projectile.x = -1;
    return projectile;
}

void clear_projectiles_trajectory(char sb[ARENA_HEIGHT][ARENA_LENGTH])
{
    for(int row = 0; row < ARENA_HEIGHT; row++)
    {
        for(int col = 0; col < ARENA_LENGTH; col++)
        {
            if(sb[row][col] == (char)PROJECTILE_TILE || sb[row][col] == (char)PATH_TILE)
            {
                sb[row][col] = ' ';
            }
        }
    }
}

int human_turn(char sb[ARENA_HEIGHT][ARENA_LENGTH], Entity* t_player) 
{
    clear_projectiles_trajectory(sb);
    int angle, power;
    const char* indent = "    ";
    printf("\n%sPLAYER'S TURN (%c)\n", indent, PLAYER_TILE);
    printf("%sAngle (deg): ", indent);
    scanf("%d", &angle);
    printf("%sPower (m/s): ", indent);
    scanf("%d", &power);

    Entity proj = create_projectile_trajectory(sb, angle, power, t_player);

    if (proj.x != -1)
    {
        printf("%sHit inside of area X: %d, Y: %d\n", indent, proj.x, proj.y);
    } else 
    {
        printf("%sHit outside of area...\n", indent);
    }

    timeout(1);
    return proj.x;
}

int pc_turn(char sb[ARENA_HEIGHT][ARENA_LENGTH], Entity* t_pc, Entity* target) 
{
    clear_projectiles_trajectory(sb);
    int angle, power;
    const char* indent = "                                            ";
    printf("\n%sPC'S TURN (%c)\n", indent, PC_TILE);
    printf("%sAngle (deg): ", indent);
    scanf("%d", &angle);
    printf("%sPower (m/s): ", indent);
    scanf("%d", &power);

    Entity proj = create_projectile_trajectory(sb, angle, power, t_pc);

    if (proj.x != -1)
    {
        printf("%sHit inside of area X: %d, Y: %d\n", indent, proj.x, proj.y);
    } else 
    {
        printf("%sHit outside of area...\n", indent);
    }

    timeout(1);
    return proj.x;
}

int game(char sb[ARENA_HEIGHT][ARENA_LENGTH], Entity* t_player, Entity* t_pc) 
{
    render_game(sb);
    int hit;
    while(1)
    {
        hit = human_turn(sb, t_player);
        render_game(sb);
        if (hit == t_pc->x) return 0;
        if (hit == t_player->x) return 1;

        hit = pc_turn(sb, t_pc, t_player);
        render_game(sb);
        if (hit == t_player->x) return 2;
        if (hit == t_pc->x) return 3;
    }
}

void print_winner(int wn)
{
    if (wn == 0)
        printf("\nTank %c is the winner", PLAYER_TILE);
    else if (wn == 1)
        printf("\nTank %c won, by suicide of the enemy", PC_TILE);
    else if (wn == 2)
        printf("\nTank %c is the winner", PC_TILE);
    else
        printf("\nTank %c won, by suicide of the enemy", PLAYER_TILE);
}

int main()
{
    char screen_buffer[ARENA_HEIGHT][ARENA_LENGTH];   
    Entity t_player, t_pc;
    srand((unsigned int)time(NULL));

    init_game(screen_buffer, &t_player, &t_pc);
    int winner = game(screen_buffer, &t_player, &t_pc);

    print_winner(winner);

    return 0;
}
