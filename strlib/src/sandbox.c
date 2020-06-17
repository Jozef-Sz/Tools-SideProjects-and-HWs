#include <stdio.h>
#include "strlib.h"

int main() 
{
    set_textcolor(BLACK);
    printf("This is now black\n");
    set_textcolor(BRIGHT_WHITE);
    printf("And white\n");
    set_textcolor(LIGHT_RED);
    printf("REeeeeed\n");
    reset_textcolor();

    string num = parse_double(-56.3423);
    printf("|%s|\n", strget(num));
    printf("Legth %d\n", len(num));
    printf("Capacity %d\n", *num.capacity);
    strdel(num);

    return 0;
}
