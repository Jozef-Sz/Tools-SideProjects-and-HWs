# StrLib
StrLib is a library for the c programing language, which provides an abstraction layer for strings.
It makes strings easier to work with and brings them closer to higher level languages like C# and Java.
This library's priority was make work with strings easier, so in favour of this priority there may be 
some inefficiencies and in case of inappropriate treatment of pointers and memory allocations there 
might be even memory leaks.
Disclaimer, the last statement about memory is in the users responsibility to handle, not the maintainers.

## Documentation:
- [Types](#types)
- [Functions](#functions)
    - [string creation](#string-creation)
    - [string input](#string-input)
    - [extending string](#extending-string)
    - [string properties](#string-properties)
    - [string manipulation](#string-manipulation)
    - [string search](#string-search)
    - [string memory management](#string-memory-management)
    - [string conversion](#string-conversion)
    - [text coloring](#text-coloring)
- [Upcoming features](#upcoming-features)
- [Example code](#example-code)
- [For user's of strlib](#for-user's-of-strlib)
- [For developers](#for-developers)
- [Notes](#notes)

### TYPES:
* **string** - main type when using strings of strlib, struct holding string data and metadata


### FUNCTIONS:
#### String creation
```c
string str(const char* arg)
```
Is used for crating strings, which represents and manipulates a sequence of characters.
* **arg** - any kind of text, which is turned into string type and then returned

```C
string strcopy(string arg)
```
Returns an exact copy of the passed string.
* **arg** - any kind of string we want to get copied

---
#### String input
```C
string strscan(const char* msg, ...)
```
Basicaly works the same as **scanf()** with slight differences. Instead of scanning input to a variable
this returns a string. This function takes in a message which is printed before scannig, just like in 
python. You can create messages the same way as with printf `string input = strscan("Is %d your lucky number? ", 121);`.
* **msg** - can be any formated message

---
#### Extending string
```C
void strpush(string base, const char* tail)
```
Is used for extending a string with raw text as "example" or with any const char* just like does the plus operator in other languages.
* **base** - some string to be extended
* **tail** - text to be extended with 

```C
void stradd(string base, string tail)
```
Is also used for extending string, but in this case with another string. It's only purpose is convenience, but you can as well use **strpush**(somestring, **strget**(otherstring)); and get the same result. 
* **base** - some string to be extended
* **tail** - string to be extended with

---
#### String properties
```C
const char* strget(string arg)
```
Returns a particular strings value.
* **arg** - any kind of string

```C
int len(string arg)
```
Returns a particular strings length.
* **arg** - any kind of string

```C
char charat(string str, int index)
```
Is used for getting a specific character based on an index value from a particular string.
* **str** - any kind of string
* **index** - index value starting from 0

---
#### String manipulation
```C
string substr(string str, int from, int to)
```
Returns a substring as type string determined by the following two parameters.
* **str** - any kind of string
* **from** - substring starting from this index included
* **to** - substring ends at this index included

```C
void replace(string arg, const char* pattern, const char* filling, int occurrance)
```
Is used for raplacing a section of the string. It replaces based on a pattern like "this is going to be replaced", but only if the string actualy contains the given pattern. Last parameter determines how many occurrances should be replaced. If the parameter is NULL or 0, all of the occurrances going to be replaced.
* **arg** - any kind of string
* **pattern** - portion of the string, which we want to replace (case sensitive)
* **filling** - the replaced portion is going to be replaced with this
* **occurrance** - number of desired replacements, if ALL or 0 (they're the same, ALL is just a macro) every occurance is replaced

```C
void tolower_case(string arg)
```
Changes every letter to lower case in the string
* **arg** - any kind of string

```C
void toupper_case(string arg)
```
Changes every letter to upper case in the string
* **arg** - any kind of string

---
#### String search
```C
int contains(string arg, const char* pattern)
```
Returns truthy value if the given pattern matches with a portion of the string, otherwise returns falsy value
* **arg** - any kind of string
* **pattern** - searched substring (case sensitive)

---
#### String memory management
```C
void strdel(string arg)
```
Frees up the memory of a particular string. NOTE: every string should be deleted at the end of it's life cycle if you want to properly finish the program.
* **arg** - string we want to free it's memory

---
#### String conversion
```C
string int_tostr(int number)
```
Returns string converted from an integer
* **number** - integer number

```C
string double_tostr(double number)
```
Returns string converted from a double
* **number** - double decimal number

```C
int parse_int(string strnum)
```
Returns an integer converted from string
* **strnum** - any kind of string 

```C
double parse_double(string strnum)
```
Returns a double converted from string
* **strnum** - any kind of string 

---
#### Text coloring
```C
void set_textcolor(color constant) 
```
Sets the color for every text output after calling this function. For resetting the original text color, as you might have guessed, you need to call `reset_textcolor();`. 
* **color constant** - one color from the listed [color constants](#color-constants)

```C
void reset_textcolor()
```
Calling reset_textcolor resets text color to, which was before the first set_textcolor() call.

#### Color constants:
* BLACK       
* BLUE        
* GREEN       
* AQUA        
* RED         
* PURPLE      
* YELLOW      
* WHITE       
* GRAY        
* LIGHT_BLUE  
* LIGHT_GREEN 
* LIGHT_AQUA  
* LIGHT_RED   
* LIGHT_PURPLE
* LIGHT_YELLOW
* BRIGHT_WHITE

## Upcoming features:
* str_t() - creates a string from template just like printf does
* trimstart() - removes whitespace from the beginning of a string 
* trimend() - removes whitespace from the end of a string
* trim() - removes whitespace from both sides of a string
* strpop() - removes the last character and returns it
* strdel_array() - frees a string arrays memory
* print() - prints an arbitrary number of strings and char* without new line 
* println() - prints an arbitrary number of strings and char* with new line 

## Example code:
```C
#include <stdio.h>
#include "strlib.h"

int main()
{
    string myname = str("James");
    string mylastname = str("Johnson");

    string guest = strscan("What is your name: ");

    strpush(myname, " ");
    stradd(myname, mylastname);

    printf("Nice to meet you %s. I am %s.\n", strget(guest), strget(myname));

    int age;
    printf("How old are you: ");
    scanf("%d", &age);

    string guestage = int_tostr(age);
    printf("That's good. I'm also %s year old.\n", strget(guestage));

    string schedule = str("So today we're going to visit the Eiffel Tower.");
    schedule = replace(schedule, "Eiffel Tower", "Statue of Liberty", ALL);

    printf("%s\n", strget(schedule));

    strdel(myname);
    strdel(mylastname);
    strdel(guestage);
    strdel(schedule);

    return 0;
}
```
#### Expected outpu:
What is your name: Frank<br/>
Nice to meet you Frank. I am James Johnson.<br/>
How old are you: 25<br/>
That's good. I'm also 25 year old.<br/>
So today we're going to visit the Statue of Liberty.

## For user's of strlib
In case you intend to use strlib in your project, you will have to:

a) Clone or download as zip this repository and include strlib.h and strlib.c from the src folder to your project.

b) Create two files in your project, one named strlib.h and one strlib.c, then copy code from coresponding files on github, which are in the src folder. 

## For developers:
To contribute to strlib you will need GNU Make, it's not necessary, but recommended. Anyway please follow these steps:

1. Clone this repository to your local machine.
2. Setup your project structure (only if you want to use Make) by creating directories named **bin** and **obj** so the structure looks like this:<br/>
.<br/>
├── bin<br/>
├── LICENSE<br/>
├── Makefile<br/>
├── obj<br/>
├── README.md<br/>
├── src<br/>
│   ├── sandbox.c<br/>
│   ├── strlib.c<br/>
│   └── strlib.h<br/>
└── test<br/>
  └── test.c

3. Develop and have fun :smile:
4. Create a pull request, which I thank you in advance :wink: :smiley:

### NOTES:
If you find any bug or mistake in the library's code, please make an issue labeled with the strlib label. 
