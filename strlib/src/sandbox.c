#include <stdio.h>
#include "strlib.h"

int main() 
{
    string var = str("Buzz lightyear");
    printf("|%s| ptr %x\n", strget(var), var->str);

    strpush(var, " ");
    printf("|%s| ptr %x\n", strget(var), var->str);

    strpush(var, "is the name of a cartoon toy");
    printf("|%s| ptr %x\n", strget(var), var->str);

    string eh = str(" a sdkjfas");
    stradd(var, eh);
    printf("|%s| ptr %x\n", strget(var), var->str);

    strpush(var, "is the name of a cartoon toy");
    printf("|%s| ptr %x\n", strget(var), var->str);

    stradd(var, eh);
    printf("|%s| ptr %x\n", strget(var), var->str);

    strdel(eh);
    strdel(var);

    return 0;
}
