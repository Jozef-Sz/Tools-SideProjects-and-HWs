#ifndef STRLIB_H
#define STRLIB_H

#define STR_BACKUP_SIZE 10
#define ALL 0

typedef struct {
    char* str;
    int* length;
    int* capacity;
} string;


void throw_error(const char* msg, ...);

string str(const char* raw_s);

void strpush(string base, const char* tail);

void stradd(string base, string tail);

const char* strget(string arg);

char charat(string arg, int index);

string substr(string arg, int from, int to);

int len(string arg);

void strdel(string arg);

string strcopy(string arg);

int contains(string arg, const char* pattern);

void replace(string arg, const char* pattern, const char* filling, int occurrences);

#endif
