# StrLib
StrLib is a library for the c programing language, which provides an abstraction layer for strings.
It makes strings easier to work with and brings them closer to higher level languages like C# and Java.
This library's priority was make work with strings easier, so in favour of this priority there may be 
some inefficiencies and in case of inappropriate treatment of pointers and memory allocations there 
might be even memory leaks.
Disclaimer, the last statement about memory is in the users responsibility to handle, not the maintainers.

## Documentation:

### TYPES:
* string - main type when using strings of strlib, struct holding string data and metadata


### FUNCTIONS:
```c
string str(const char* arg)
```
Is used for crating strings, which represents and manipulates a sequence of characters.
* **arg** - any kind of text, which is turned into string type and then returned

```C
string strpush(string base, const char* tail)
```
Is used for extending a string with raw text as "example" or with any const char* just like does the plus operator in other languages.
* **base** - some string to be extended
* **tail** - text to be extended with 

```C
string stradd(string base, string tail)
```
Is also used for extending string, but in this case with another string. It's only purpose is convenience, but you can as well use **strpush**(somestring, **strget**(otherstring)); and get the same result. 
* **base** - some string to be extended
* **tail** - string to be extended with

```C
const char* strget(string arg)
```
Returns a particular strings value.
* **arg** - any kind of string

```C
string strcopy(string arg)
```
Returns an exact copy of the passed string.
* **arg** - any kind of string we want to get copied

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

```C
string substr(string str, int from, int to)
```
Returns a substring as type string determined by the following two parameters.
* **str** - any kind of string
* **from** - substring starting from this index included
* **to** - substring ends at this index included

```C
void strdel(string arg)
```
Frees up the memory of a particular string. CAUTION: the string variable a.k.a. struct will be still available, but the string and it's length itself will be empty.
* **arg** - string we want to free it's memory

```C
void replace(string arg, const char* pattern, const char* filling, int occurrance)
```
Is used for raplacing a section of the string. It replaces based on a pattern like "this is going to be replaced", but only if the string actualy contains the given pattern. Last parameter determines how many occurrances should be replaced. If the parameter is NULL or 0, all of the occurrances going to be replaced.
* **arg** - any kind of string
* **pattern** - portion of the string, which we want to replace (case sensitive)
* **filling** - the replaced portion is going to be replaced with this
* **occurrance** - number of desired replacements, if ALL or 0 (they're the same, ALL is just a macro) every occurance is replaced

```C
int contains(string arg, const char* pattern)
```
Returns truthy value if the given pattern matches with a portion of the string, otherwise returns falsy value
* **arg** - any kind of string
* **pattern** - searched substring (case sensitive)


## Upcoming features:
* parse_int() - returns string converted from an integer
* parse_double() - returns string convered from a double
* tolower() - returns string all lower case
* toupper() - returns string all upper case
* str_t() - creates a string from template just like printf does
* trimstart() - removes whitespace from the beginning of a string 
* trimend() - removes whitespace from the end of a string
* trim() - removes whitespace from both sides of a string
* strpop() - removes the last character and returns it
* strdel_array() - frees a string arrays memory
* print() - prints an arbitrary number of strings and char* without new line 
* println() - prints an arbitrary number of strings and char* with new line 