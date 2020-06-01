#ifndef STRLIB_H
#define STRLIB_H

typedef struct {
    char* str;
    int length;
    int capacity;
} string;


void throw_error(const char* msg);

string str(const char* raw_s);

string strpush(string donkey, const char* tail);

string stradd(string donkey, string tail);

const char* strget(string str);

char charat(string str, int index);

const char* substr_cp(string str, int from, int to);

string substr(string str, int from, int to);

int len(string str);

#endif