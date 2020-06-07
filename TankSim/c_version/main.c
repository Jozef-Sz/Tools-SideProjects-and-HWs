#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
#define T_CMD "cls"
#define GROUND_TILE 219
#else
#define T_CMD "clear"
#define GROUND_TILE 'G'
#endif

#define ARENA_LENGTH 80
#define ARENA_HEIGHT 20
#define PROJECTILE_TILE '*'
#define PATH_TILE '.'
#define PLAYER_TILE 'K'
#define PC_TILE 'X'
#define G 9.81

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
        if(peek_pixel == GROUND_TILE)
        {
            sb[i][xpos] = tile;
            return ARENA_HEIGHT - i;
        }
    }
}

void insert_char(char sb[ARENA_HEIGHT][ARENA_LENGTH], int xpos, int ypos, char tile)
{
    if (xpos < 0 || ypos < 0) return;
    int x = xpos - 1;
    int y = (ypos != 0) ? ARENA_HEIGHT - ypos : -1;
    if ((x < 0 || x > ARENA_LENGTH - 1) || (y < 0 || y > ARENA_HEIGHT - 1))
        return;
    sb[y][x] = tile;
}

void init_game(char sb[ARENA_HEIGHT][ARENA_LENGTH], Entity* t_player, Entity* t_pc)
{
    // Randomly position players
    t_player->x = random_number(1, ARENA_LENGTH / 2 - 1);
    t_pc->x = random_number(ARENA_LENGTH / 2, ARENA_LENGTH);

    // Initialize screen buffer
    for(int i = 0; i < ARENA_HEIGHT; i++)
        for(int j = 0; j < ARENA_LENGTH; j++)
            sb[i][j] = ' ';

    // Create flat ground
    for(int i = 0; i < ARENA_LENGTH; i++)
        sb[ARENA_HEIGHT - 1][i] = GROUND_TILE;

    t_player->y = drop_place(sb, t_player->x, PLAYER_TILE);
    t_pc->y = drop_place(sb, t_pc->x, PC_TILE);
}

int human_turn() {}

int pc_turn() {}

int game() {}

int main()
{
    char screen_buffer[ARENA_HEIGHT][ARENA_LENGTH];   
    Entity t_player, t_pc;
    srand((unsigned int)time(NULL));

    init_game(screen_buffer, &t_player, &t_pc);
    render_game(screen_buffer);

    

    return 0;
}