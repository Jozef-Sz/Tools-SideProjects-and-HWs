#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "strlib.h"


void throw_error(const char* msg)
{
    printf("\x1b[31;1m");
    printf("\nError occurred: %s\n", msg);
    printf("\x1b[0m");
    exit(EXIT_FAILURE);
}

string str(const char* raw_s)
{
    string s;
    s.length = (int)strlen(raw_s);
    s.capacity = s.length + 5;
    s.str = malloc(sizeof(char) * s.capacity);

    strcpy(s.str, raw_s);
 
    return s;
}

string strpush(string donkey, const char* tail)
{
    string new_str = donkey;
    size_t tail_len = strlen(tail);
    if (donkey.length + tail_len > donkey.capacity)
    {
        new_str.length = donkey.length + (int)tail_len;
        new_str.capacity = new_str.length + 5;
        new_str.str = realloc(donkey.str, new_str.capacity);
        strcat(new_str.str, tail);
    } else {
        new_str.length = donkey.length + (int)tail_len;
        strcat(new_str.str, tail);
    }
    return new_str;
}

const char* strget(string s)
{
    return s.str;
}

char charat(string str, int index)
{
    if (index < 0 || index > str.length - 1) throw_error("String index out of range");
    return str.str[index];
}

string substr(string str, int from, int to)
{

}

const char* substr_cp(string str, int from, int to)
{

}
