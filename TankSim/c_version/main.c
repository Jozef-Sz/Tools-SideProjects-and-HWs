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
#define G 9.81

typedef struct {
    int x;
    int y;
    int angle;
    int power;
} Entity;


void clear_screen() { system(T_CMD); }

void init_game(char sb[ARENA_HEIGHT][ARENA_LENGTH], Entity* t_player, Entity* t_pc)
{
    sb[0][1] = GROUND_TILE;
}

int main()
{
    char screen_buffer[ARENA_HEIGHT][ARENA_LENGTH];   
    Entity t_player, t_pc;

    init_game(screen_buffer, &t_player, &t_pc);
    printf("\n %c", screen_buffer[0][1]);

    return 0;
}