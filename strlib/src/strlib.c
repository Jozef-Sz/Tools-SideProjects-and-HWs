#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

#include "strlib.h"


void throw_error(const char* msg, ...)
{
    va_list arg;
    va_start(arg, msg);

    printf("\x1b[31;1m");
    printf("\nError occurred: ");
    vfprintf(stdout, msg, arg);
    printf("\x1b[0m");
    va_end(arg);
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
    } else 
    {
        new_str.length = donkey.length + (int)tail_len;
        strcat(new_str.str, tail);
    }
    return new_str;
}

char charat(string arg, int index)
{
    if (index < 0 || index > arg.length - 1) throw_error("String index out of range\n");
    return arg.str[index];
}

string substr(string arg, int from, int to)
{
    if (from < 0 || from > arg.length - 1) throw_error("String index out of range\n");
    if (to < 0 || to > arg.length - 1) throw_error("String index out of range\n");
    if (from > to) throw_error("Cannot retrieve substring from index %d to index %d\n", from, to);
    string ss;
    ss.length = to - from + 1;
    ss.capacity = ss.length + 5;
    ss.str = malloc(sizeof(char) * ss.capacity);
    int i = 0, ssindex = from;
    for (; i < ss.length; i++)
    {
        ss.str[i] = arg.str[ssindex];
        ssindex++;
    }
    ss.str[i] = '\0';
    return ss;
}

void strdel(string arg) { free(arg.str); }

int len(string arg) { return arg.length; }

const char* strget(string arg) { return arg.str; }
