#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define ARENA_LENGTH 80
#define ARENA_HEIGHT 20
#define G 9.81


void clear_screen()
{
    #if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
    system("cls");
    #elif defined(__APPLE__)
        system("clear");
    #elif defined(__linux__)
        system("clear");
    #else
    #error "Unknown OS"
    #endif 
}

int main()
{
    printf("a");

    return 0;
}