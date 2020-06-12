#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

#include "strlib.h"


typedef struct {
	int amount;
	int* indexes;
}finding;

/* TODO: Error and warning message color currently works properly on
         unix based environments so windows support is needed*/
void throw_error(const char* msg, ...)
{
    va_list arg;
    va_start(arg, msg);

    printf("\n\x1b[31m");
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

	printf("\n\x1b[33m");
	printf("[WARNING]: ");
	vfprintf()stdout, msg, arg;
	printf("\x1b[0m\n");
	va_end(arg);
}

string str(const char* raw_s)
{
    string s;
    s.length = malloc(sizeof(int));
    s.capacity = malloc(sizeof(int));
    *s.length = (int)strlen(raw_s);
    *s.capacity = *s.length + (int)STR_BACKUP_SIZE;
    s.str = malloc(*s.capacity * sizeof(char));
    strcpy(s.str, raw_s);
    return s;
}

void strpush(string base, const char* tail)
{
    size_t tail_length = strlen(tail);
    /* (*base.capacity - 1) is because of the null termiantion.
       I am not sure, if it's necessary, anyway it doesn't 
       hurts even if it's not necessary. */
    if (*base.length + tail_length > *base.capacity - 1)
    {
        *base.length = *base.length + (int)tail_length;
        *base.capacity = *base.length + (int)STR_BACKUP_SIZE;
        base.str = realloc(base.str, *base.capacity);
        strcat(base.str, tail);
    } 
    else 
    {
        *base.length = *base.length + (int)tail_length;
        strcat(base.str, tail);
    }
}

void stradd(string base, string tail)
{
    const char* str = tail.str;
    strpush(base, str);
}

char charat(string arg, int index)
{
    if (index < 0 || index > *arg.length - 1)
        throw_error("String index out of range");
    return arg.str[index];
}

string substr(string arg, int from, int to)
{
    if (from < 0 || from > *arg.length - 1) throw_error("String index out of range");
    if (to < 0 || to > *arg.length - 1) throw_error("String index out of range");
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
    return subs;
}

string strcopy(string arg)
{
    string copy;
    copy.length = malloc(sizeof(int));
    copy.capacity = malloc(sizeof(int));
    *copy.length = *arg.length;
    *copy.capacity = *arg.capacity;
    copy.str = malloc(*copy.capacity * sizeof(char));
    strcpy(copy.str, arg.str);
    return copy;
}
/* Returns a structure, which consists of a number of occurrances
   and an integer array of indexes where the found pattern begins. */
finding search(const char* searchable, const char* pattern)
{
	finding res;
	res.amount = 0;
	res.indexes = malloc(sizeof(int));
	int score = 0, pattern_len = (int)strlen(pattern);

	for (int i = 0; i < (int)strlen(searchable); i++)
	{
		if (searchable[i] == pattern[score])
		{
			score++;
			if (score == pattern_len)
			{
				score = 0;
				res.amount++;
				if (res.amount == 1)
					res.indexes[res.amount - 1] = i - pattern_len + 1;
				else
				{
					res.indexes = realloc(res.indexes, res.amount * sizeof(int));
					res.indexes[res.amount - 1] = i - pattern_len + 1; 
				}
			}
		}
		else
		{
			score = 0;
		}
	}
	return res;
}

int contains(string arg, const char* pattern)
{
    finding res = search(arg.str, pattern);
    if (res.amount == 0) return 0;
    return 1;
}

void replace(string arg, const char* pattern, const char* filling, int occurrences)
{
    finding res = search(arg.str, pattern);
    if (res.amount == 0) return;
    int replacements;
    if (occurrences == 0 || occurrences > res.amount)
        replacements = res.amount;
    else
        replacements = occurrences;
    
    if (strlen(pattern) == strlen(filling))
    {
        for (int i = 0; i < replacements; i++)
        {
            int str_index = res.indexes[i];
            for(int j = 0; j < (int)strlen(filling); j++)
            {
                arg.str[str_index] = filling[j];
                str_index++;
            }
        }
    }
    else
    {
        int new_size = *arg.length - replacements * (int)strlen(pattern) + 
                       replacements * (int)strlen(filling);
		*arg.length = new_size;
		*arg.capacity = new_size + (int)STR_BACKUP_SIZE;
		const char* old_str = arg.str;
		arg.str = malloc(*arg.capacity * sizeof(char));

		int current_index = 0;
		for (int i = 0; i < (int)strlen(old_str); i++)
		{
			
		}

		free(old_str);
    }
    
}

void strdel(string arg) 
{ 
    free(arg.str);
    free(arg.length);
    free(arg.capacity); 
}

int len(string arg) { return *arg.length; }

const char* strget(string arg) { return arg.str; }
