#ifndef STRLIB_H
#define STRLIB_H

#define STR_BACKUP_SIZE 10
#define ALL 0

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
// Colors
#define BLACK         0
#define BLUE          1
#define GREEN         2
#define AQUA          3
#define RED           4
#define PURPLE        5
#define YELLOW        6
#define WHITE         7
#define GRAY          8
#define LIGHT_BLUE    9
#define LIGHT_GREEN  10
#define LIGHT_AQUA   11
#define LIGHT_RED    12
#define LIGHT_PURPLE 13
#define LIGHT_YELLOW 14
#define BRIGHT_WHITE 15
#endif

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
