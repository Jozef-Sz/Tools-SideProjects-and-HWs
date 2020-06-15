#include <stdio.h>
#include "strlib.h"

int main() 
{
    for (int i = -100; i < 101; i++)
    {
        string snumber = parse_int(i);
        printf("|%s|\n", strget(snumber));
        printf("Size of the string: %d\n", len(snumber));
        strdel(snumber);
    }

    return 0;
}
