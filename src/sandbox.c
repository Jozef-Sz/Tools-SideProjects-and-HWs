#include <stdio.h>
#include "strlib.h"

int main() 
{
    string name = str("Joco");

    printf("Here is our string: %s|\n", name.str);
    printf("%d\n", name.length);

    name = strpush(name, " is");
    printf("Here is our string: %s|\n", name.str);
    printf("%d\n", name.length);

    name = strpush(name, " the best");
    printf("Here is our string: %s|\n", name.str);
    printf("%d\n", name.length);

    // printf("%c\n", charat(name, -1));
    printf("%c\n", charat(name, 15));
    printf("%c\n", charat(name, 8));

    string is = substr(name, 5, 7);
    return 0;
}