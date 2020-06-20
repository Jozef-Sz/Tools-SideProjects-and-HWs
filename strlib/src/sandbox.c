#include <stdio.h>
#include "strlib.h"

int main() 
{
    string number = str("45");
    printf("From string %s, to integer %d\n", strget(number), parse_int(number));

    strpush(number, "hello");
    printf("From string %s, to integer %d\n", strget(number), parse_int(number));

    string decimal = str("34343.54453");
    printf("From string %s, to double %f\n", strget(decimal), parse_double(decimal));

    strpush(decimal, "asdgadsfg");
    printf("From string %s, to double %f\n", strget(decimal), parse_double(decimal));

    string upper = str("NEW BALANCE 547");
    tolower_case(upper);
    printf("|%s|\n", strget(upper));

    toupper_case(upper);
    printf("Back to upper case |%s|\n", strget(upper));

    upper = strnpush(upper, "as");
    printf("|%s|\n", strget(upper));

    strdel(number);
    strdel(decimal);
    strdel(upper);
    return 0;
}
