#include <stdio.h>
#include "strlib.h"

int main() 
{
    string var = str("Buzz lightyear is a cartoon toy");
    printf("|%s| ptr %x\n", strget(var), var->str);

    replace(var, "is", "je", ALL);
    printf("|%s| ptr %x\n", strget(var), var->str);

    replace(var, "lightyear", "SMALL STEP FOR A HUMAN", ALL);
    printf("|%s| ptr %x\n", strget(var), var->str);

    strdel(var);

    return 0;
}
