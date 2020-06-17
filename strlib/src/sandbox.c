#include <stdio.h>
#include "strlib.h"

int main() 
{
    string myname = str("James");
    string mylastname = str("Johnson");

    string guest = strscan("What is your name: ");

    strpush(myname, " ");
    stradd(myname, mylastname);

    printf("Nice to meet you %s. I am %s.\n", strget(guest), strget(myname));

    int age;
    printf("How old are you: ");
    scanf("%d", &age);

    string guestage = parse_int(age);
    printf("That's good. I'm also %s year old.\n", strget(guestage));

    string schedule = str("So today we're going to visit the Eiffel Tower.");
    replace(schedule, "Eiffel Tower", "Statue of Liberty", ALL);

    printf("%s\n", strget(schedule));

    strdel(myname);
    strdel(mylastname);
    strdel(guestage);
    strdel(schedule);

    return 0;

    return 0;
}
