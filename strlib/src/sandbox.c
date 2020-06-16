#include <stdio.h>
#include "strlib.h"

int main() 
{
    for (int i = -1; i < 2; i++)
    {
        string snumber = parse_int(i);
        printf("|%s|\n", strget(snumber));
        printf("Size of the string: %d\n", len(snumber));
        strdel(snumber);
    }

    string num = parse_double(-56.3423);
    printf("|%s|\n", strget(num));
    printf("Legth %d\n", len(num));
    printf("Capacity %d\n", *num.capacity);
    strdel(num);

    return 0;
}
