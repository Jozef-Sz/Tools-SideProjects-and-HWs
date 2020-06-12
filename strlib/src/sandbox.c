#include <stdio.h>
#include "strlib.h"

int main() 
{
    string name = str("Joco szarhazi szar");
    printf("|%s|\n", strget(name));
    printf("Size of the string: %d\n", len(name));

    replace(name, "szar", "senki", NULL);
    printf("|%s|\n", strget(name));

    strdel(name);
    return 0;
}