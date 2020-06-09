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

    printf("%s\n", name.str);

    strdel(name);

    printf("%s", name.str);

    return 0;
}