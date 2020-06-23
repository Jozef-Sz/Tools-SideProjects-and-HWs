#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

#include "strlib.h"

// ------------------------ MESSAGE LOGGING SECTION ------------------------
// ---------------------------------- AND ----------------------------------
// -------------- COLOR HANDLING (FOR _WIN32 AND LINUX _TERM) -------------- 

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
#include <windows.h>

typedef struct {
    unsigned short bg;
    unsigned short fg;
} color_set;

unsigned short encode_color(unsigned short bg, unsigned fg)
{
    return (16 * bg) + fg;
}

color_set decode_color(unsigned short color_c)
{
    color_set cs;
    cs.bg = color_c / 16;
    cs.fg = color_c - cs.bg * 16;
    return cs;
}

// Global variables for hangling text colors
color_set ORIGINAL_CMD_COLOR;
int is_color_saved = 0;

void set_textcolor(unsigned short txt_c) 
{ 
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    if (! is_color_saved) 
    {
        CONSOLE_SCREEN_BUFFER_INFO consoleInfo;
        GetConsoleScreenBufferInfo(hConsole, &consoleInfo);
        ORIGINAL_CMD_COLOR = decode_color(consoleInfo.wAttributes);
        is_color_saved = 1;
    }

    SetConsoleTextAttribute(hConsole, encode_color(ORIGINAL_CMD_COLOR.bg, txt_c));
}

void reset_textcolor() 
{  
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_SCREEN_BUFFER_INFO consoleInfo;

    GetConsoleScreenBufferInfo(hConsole, &consoleInfo);
    SetConsoleTextAttribute(hConsole, encode_color(ORIGINAL_CMD_COLOR.bg, ORIGINAL_CMD_COLOR.fg));
}

void throw_error(const char* msg, ...)
{
    va_list arg;
    va_start(arg, msg);

    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_SCREEN_BUFFER_INFO consoleInfo;
	WORD saved_attributes;

	GetConsoleScreenBufferInfo(hConsole, &consoleInfo);
    saved_attributes = consoleInfo.wAttributes;
    color_set initial_color = decode_color(saved_attributes);

    // Maybe change fg to LIGHT_RED if it's to dark or dim
    SetConsoleTextAttribute(hConsole, encode_color(initial_color.bg, (unsigned short)RED));
    printf("\n[ERROR]: ");
    vfprintf(stdout, msg, arg);
    printf("\n");

    SetConsoleTextAttribute(hConsole, saved_attributes);
    va_end(arg);
    exit(EXIT_FAILURE);
}

void throw_warning(const char* msg, ...)
{
    va_list arg;
	va_start(arg, msg);

    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_SCREEN_BUFFER_INFO consoleInfo;
	WORD saved_attributes;

	GetConsoleScreenBufferInfo(hConsole, &consoleInfo);
    saved_attributes = consoleInfo.wAttributes;
    color_set initial_color = decode_color(saved_attributes);

    // Maybe change fg to LIGHT_RED if it's to dark or dim
    SetConsoleTextAttribute(hConsole, encode_color(initial_color.bg, (unsigned short)YELLOW));
    printf("\n[WARNING]: ");
    vfprintf(stdout, msg, arg);
    printf("\n");

    SetConsoleTextAttribute(hConsole, saved_attributes);
    va_end(arg);
}

#else

void throw_error(const char* msg, ...)
{
    va_list arg;
    va_start(arg, msg);

    printf("\n%s", RED);
    printf("[ERROR]: ");
    vfprintf(stdout, msg, arg);
    printf("\x1b[0m\n");
    va_end(arg);
    exit(EXIT_FAILURE);
}

void throw_warning(const char* msg, ...)
{
	va_list arg;
	va_start(arg, msg);

	printf("\n%s", YELLOW);
	printf("[WARNING]: ");
	vfprintf(stdout, msg, arg);
	printf("\x1b[0m\n");
	va_end(arg);
}

void set_textcolor(const char* txt_c) { printf("%s", txt_c); }

void reset_textcolor() { printf("\x1b[0m"); }

#endif

// -------------------------------------------------------------------------
// ----------------------------- STRLIB SECTION ----------------------------

typedef struct {
    string* strings;
    int len;
    int cap;
} GLOBAL_STRING_STRUCT;

GLOBAL_STRING_STRUCT GSS = { NULL, 0, 0 };

void appendtoGSS(string s)
{
    if (GSS.cap == 0)
    {
        GSS.cap = 10;
        GSS.strings = malloc(GSS.cap * (int)sizeof(string));
    }
    if (GSS.len + 1 > GSS.cap)
    {
        GSS.cap += 5;
        GSS.strings = realloc(GSS.strings, GSS.cap * (int)sizeof(string));
    }
    GSS.strings[GSS.len] = s;
    GSS.len++;
}

typedef struct {
	int amount;
	int* indexes;
} finding;

string str(const char* raw_s)
{
    string s = malloc(sizeof(str_class));
    s->index = GSS.len;
    appendtoGSS(s);

    s->length = (int)strlen(raw_s);
    s->capacity = s->length + STR_BACKUP_SIZE;
    s->str = malloc(s->capacity * (int)sizeof(char));
    strcpy(s->str, raw_s);
    return s;
}

string strscan(const char* msg, ...)
{
    va_list arg;
    va_start(arg, msg);
    char input_buffer[SCAN_BUFFER];
    string s = malloc(sizeof(str_class));
    s->index = GSS.len;
    appendtoGSS(s);
    
    vfprintf(stdout, msg, arg);
    scanf("%s", input_buffer);
    s->length = (int)strlen(input_buffer);
    s->capacity = s->length * STR_BACKUP_SIZE;
    s->str = malloc(s->capacity * (int)sizeof(char));
    strcpy(s->str, input_buffer);
    va_end(arg);
    return s;
}

void strpush(string base, const char* tail)
{
    size_t tail_length = strlen(tail);
    /* (*base.capacity - 1) is because of the null termiantion.
       I am not sure, if it's necessary, anyway it doesn't 
       hurts even if it's not necessary. */
    if (base->length + tail_length > base->capacity - 1)
    {
        base->length += (int)tail_length;
        base->capacity = base->length + (int)STR_BACKUP_SIZE;
        base->str = realloc(base->str, base->capacity);
        if (base->str == NULL)
            throw_error("Couldn't allocate memory for the string");
        strcat(base->str, tail);
    } 
    else 
    {
        base->length = base->length + (int)tail_length;
        strcat(base->str, tail);
    }
}

void stradd(string base, string tail)
{
    const char* str = tail->str;
    strpush(base, str);
}

char charat(string arg, int index)
{
    if (index < 0 || index > arg->length - 1)
        throw_error("String index out of range");
    return arg->str[index];
}

string substr(string arg, int from, int to)
{
    if (from < 0 || from > arg->length - 1) throw_error("String index out of range");
    if (to < 0 || to > arg->length - 1) throw_error("String index out of range");
    if (from > to) throw_error("Cannot retrieve substring from index %d to index %d", from, to);
    string subs;
    subs.length = malloc(sizeof(int));
    subs.capacity = malloc(sizeof(int));
    *subs.length = to - from + 1;
    *subs.capacity = *subs.length + (int)STR_BACKUP_SIZE;
    subs.str = malloc(*subs.capacity * sizeof(char));
    int i = 0, ssindex = from;
    for (; i < *subs.length; i++)
    {
        subs.str[i] = arg.str[ssindex];
        ssindex++;
    }
    subs.str[i] = '\0';
    subs.is_initialized = "Initialized";
    return subs;
}

// string strcopy(string arg)
// {
//     string copy;
//     copy.length = malloc(sizeof(int));
//     copy.capacity = malloc(sizeof(int));
//     *copy.length = *arg.length;
//     *copy.capacity = *arg.capacity;
//     copy.str = malloc(*copy.capacity * sizeof(char));
//     strcpy(copy.str, arg.str);
//     copy.is_initialized = "Initialized";
//     return copy;
// }
// /* Returns a structure, which consists of a number of occurrances
//    and an integer array of indexes where the found pattern begins. */
// finding search(const char* searchable, const char* pattern)
// {
// 	finding res;
// 	res.amount = 0;
// 	res.indexes = malloc(sizeof(int));
// 	int score = 0, pattern_len = (int)strlen(pattern);

// 	for (int i = 0; i < (int)strlen(searchable); i++)
// 	{
// 		if (searchable[i] == pattern[score])
// 		{
// 			score++;
// 			if (score == pattern_len)
// 			{
// 				score = 0;
// 				res.amount++;
// 				if (res.amount == 1)
// 					res.indexes[res.amount - 1] = i - pattern_len + 1;
// 				else
// 				{
// 					res.indexes = realloc(res.indexes, res.amount * sizeof(int));
// 					res.indexes[res.amount - 1] = i - pattern_len + 1; 
// 				}
// 			}
// 		}
// 		else
// 			score = 0;
// 	}
// 	return res;
// }

// int contains(string arg, const char* pattern)
// {
//     finding res = search(arg.str, pattern);
//     if (res.amount == 0) return 0;
//     return 1;
// }

// void replace(string arg, const char* pattern, const char* filling, int occurrences)
// {
//     finding res = search(arg.str, pattern);
//     if (res.amount == 0) return;
//     int replacements;
//     if (occurrences == 0)
//         replacements = res.amount;
//     else if (occurrences > res.amount)
//     {
//         replacements = res.amount;
//         throw_warning("Too many occurances are given (%d), actual occurrances (%d)", occurrences, res.amount);
//     }
//     else
//         replacements = occurrences;
    
//     if (strlen(pattern) == strlen(filling))
//     {
//         for (int i = 0; i < replacements; i++)
//         {
//             int str_index = res.indexes[i];
//             for(int j = 0; j < (int)strlen(filling); j++)
//             {
//                 arg.str[str_index] = filling[j];
//                 str_index++;
//             }
//         }
//     }
//     else
//     {
//         string copy = strcopy(arg);
//         int new_size = *arg.length - replacements * (int)strlen(pattern) + 
//                        replacements * (int)strlen(filling);
// 		*arg.length = new_size;
// 		*arg.capacity = new_size + (int)STR_BACKUP_SIZE;
// 		const char* old_str = copy.str;
// 		arg.str = realloc(arg.str, *arg.capacity * sizeof(char));

// 		int old_str_index = 0;
//         int new_str_index = 0;
//         int replaces_index = 0;
//         while (new_str_index < *arg.length)
//         {
//             if (old_str_index == res.indexes[replaces_index])
//             {
//                 if (replaces_index < replacements)
//                 {
//                     for (int i = 0; i < (int)strlen(filling); i++)
//                     {
//                         arg.str[new_str_index] = filling[i];
//                         new_str_index++;
//                     }
//                     old_str_index += (int)strlen(pattern);
//                     replaces_index++;
//                 }
//                 arg.str[new_str_index] = old_str[old_str_index];
//                 old_str_index++;
//                 new_str_index++;
//             }
//             else 
//             {
//                 arg.str[new_str_index] = old_str[old_str_index];
//                 old_str_index++;
//                 new_str_index++;
//             }
//         }
//         arg.str[new_str_index] = '\0';
//         strdel(copy);
//     }
// }

// void tolower_case(string arg)
// {
//     for (int i = 0; i < *arg.length; i++)
//     {
//         if (arg.str[i] >= 'A' && arg.str[i] <= 'Z')
//         {
//             arg.str[i] += 32;
//         }
//     }
// }

// void toupper_case(string arg)
// {
//     for (int i = 0; i < *arg.length; i++)
//     {
//         if (arg.str[i] >= 'a' && arg.str[i] <= 'z')
//         {
//             arg.str[i] -= 32;
//         }
//     }
// }

// int get_int_length(int nu)
// {
//     if (nu == 0) return 1;
//     int length = 0;
//     long temp = 1;
//     while (temp <= nu)
//     {
//         length++;
//         temp *= 10;
//     }
//     return length;
// }

// string int_tostr(int number)
// {
//     string s;
//     s.length = malloc(sizeof(int));
//     s.capacity = malloc(sizeof(int));
//     if (number < 0)
//     {
//         // Plus 1, because of the minus sign.
//         *s.length = get_int_length(abs(number)) + 1;
//         *s.capacity = *s.length + STR_BACKUP_SIZE;
//         s.str = malloc(*s.capacity * sizeof(char));
//         sprintf(s.str, "%d", number);
//     }
//     else 
//     {
//         *s.length = get_int_length(number);
//         *s.capacity = *s.length + STR_BACKUP_SIZE;
//         s.str = malloc(*s.capacity * sizeof(char));
//         sprintf(s.str, "%d", number);
//     }
//     s.is_initialized = "Initialized";
//     return s;
// }

// string double_tostr(double number)
// {
//     string s;
//     s.length = malloc(sizeof(int));
//     s.capacity = malloc(sizeof(int));
//     // The largest possible long double takes 4934 characters 
//     // including the dot and possible minus sign.
//     char* tmp = malloc(4934 * sizeof(char));
//     sprintf(tmp, "%f", number);

//     // Trim zeros from the end, btw asci zero is 48.
//     int last_char = (int)strlen(tmp) - 1;
//     while (tmp[last_char] == '0' || tmp[last_char] == 48)
//     {
//         tmp[last_char] = '\0';
//         last_char--;
//     }
//     *s.length = (int)strlen(tmp);
//     *s.capacity = *s.length + STR_BACKUP_SIZE;
//     s.str = malloc(*s.capacity * sizeof(char));
//     strcpy(s.str, tmp);
//     s.is_initialized = "Initialized";
//     free(tmp);
//     return s;
// }

// int parse_int(string strnum)
// {
//     return atoi(strnum.str);
// }

// double parse_double(string strnum)
// {
//     return atof(strnum.str);
// }

void strdel(string arg) 
{
    int str_index = arg->index;
    free(arg->str);
    free(GSS.strings[arg->index]);

    // Defragmenting GSS.strings
    for (int i = str_index;  i < GSS.len - 1; i++)
    {
        GSS.strings[i] = GSS.strings[i+1];
    }
    GSS.strings[GSS.len - 1] = NULL;
    GSS.len--;

    if (GSS.len == 0)
    {
        free(GSS.strings);
        GSS.cap = 0;
    }
}

int len(string arg) { return arg->length; }

const char* strget(string arg) { return arg->str; }
