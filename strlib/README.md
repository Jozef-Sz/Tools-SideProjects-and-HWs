# StrLib
StrLib is a library for the c programing language, which provides an abstraction layer for strings.
It makes strings easier to work with and brings them closer to higher level languages like C# and Java.
This library's priority was make work with strings easier, so in favour of this priority there may be 
some inefficiencies and in case of inappropriate treatment of pointers and memory allocations there 
might be even memory leaks.
Disclaimer, the last statement about memory is in the users responsibility to handle, not the maintainer's.

Documentation:

TYPES:
    string - is a typedef struct
    usage(example): string varname; 


FUNCTIONS:
    str ( const char* text ) return type {string} - Returns a string, which is created from the given text(necessary parameter).
    usage(example): string varname = str("Hello, world!");

    strpush (string donkey, const char* tail) return type {string} - String concatination. Takes in two parameters base string and a text to be added.
    usage(example): string new_string = strpush(old_string, " this is going to be at the end.");  

    stradd () return type {string} - 

    strget (string str) return type {const char*} - 
