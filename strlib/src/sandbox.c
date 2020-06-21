#include <stdio.h>
#include "strlib.h"

int main() 
{
    string johanes = str("Johannes");
    printf("|%s| and its length %d\n", strget(johanes), len(johanes));

    string name = str("Joco");
    printf("|%s| and its length %d\n", strget(name), len(name));
    return 0;
}
