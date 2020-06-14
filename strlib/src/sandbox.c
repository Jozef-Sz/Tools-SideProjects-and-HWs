#include <stdio.h>
#include "strlib.h"

int main() 
{
    string name = str("Joco a szarhazi szar");
    printf("|%s|\n", strget(name));
    printf("Size of the string: %d\n", len(name));

    replace(name, "a", "", ALL);
    printf("|%s|\n", strget(name));
    printf("Size of the string: %d\n", len(name));
	// char a = charat(name, 122);

    printf("res: %d\n", contains(name, "szar"));

    strdel(name);
    return 0;
}
