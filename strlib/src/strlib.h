#ifndef STRLIB_H
#define STRLIB_H

typedef struct {
    char* str;
    int length;
    int capacity;
} string;


void throw_error(const char* msg, ...);

string str(const char* raw_s);

string strpush(string donkey, const char* tail);

string stradd(string donkey, string tail);

const char* strget(string arg);

char charat(string arg, int index);

string substr(string arg, int from, int to);

int len(string arg);

void strdel(string arg);

#endif