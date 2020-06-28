#ifndef STRLIB_H
#define STRLIB_H

#define STR_BACKUP_SIZE 10
#define ALL 0
#define SCAN_BUFFER 1024

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

void set_textcolor(unsigned short txt_c);
void reset_textcolor();
#else
// Colors for linux terminal
#define BLACK        "\x1b[30m"
#define BLUE         "\x1b[34m"
#define GREEN        "\x1b[32m"
#define AQUA         "\x1b[36m"
#define RED          "\x1b[31m"
#define PURPLE       "\x1b[35m"
#define YELLOW       "\x1b[33m"
#define WHITE        "\x1b[37m"
#define GRAY         "\x1b[90m"
#define LIGHT_BLUE   "\x1b[94m"
#define LIGHT_GREEN  "\x1b[92m"
#define LIGHT_AQUA   "\x1b[96m"
#define LIGHT_RED    "\x1b[91m"
#define LIGHT_PURPLE "\x1b[95m"
#define LIGHT_YELLOW "\x1b[93m"
#define BRIGHT_WHITE "\x1b[97m"

void set_textcolor(const char* txt_c);
void reset_textcolor();
#endif

typedef struct {
    char* str;
    int length;
    int capacity;
    int index;
} str_class;

typedef str_class* string;


void throw_error(const char* msg, ...);

string str(const char* raw_s);

void strpush(string base, const char* tail);

string strnpush(string base, const char* tail);

void stradd(string base, string tail);

string strnadd(string base, string tail);

const char* strget(string arg);

char charat(string arg, int index);

char strpop(string arg);

string substr(string arg, int from, int to);

int len(string arg);

void strdel(string arg);

void strdelall();

string strcopy(string arg);

int contains(string arg, const char* pattern);

void replace(string arg, const char* pattern, const char* filling, int occurrences);

string strscan(const char* msg, ...);

string int_tostr(int number);

string double_tostr(double number);

int parse_int(string strnum); 

double parse_double(string strnum);

void tolower_case(string arg);

void toupper_case(string arg);

void trimstart(string arg);

void trimend(string arg);

void trim(string arg);

#endif
