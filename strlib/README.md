# StrLib
StrLib is a library for the c programing language, which provides an abstraction layer for strings.
It makes strings easier to work with and brings them closer to higher level languages like C# and Java.
This library's priority was make work with strings easier, so in favour of this priority there may be 
some inefficiencies and in case of inappropriate treatment of pointers and memory allocations there 
might be even memory leaks.
Disclaimer, the last statement about memory is in the users responsibility to handle, not the maintainer's.

## Documentation:

### TYPES:
* string - main type when using strings of strlib, struct holding string data and metadata


### FUNCTIONS:
```c
string str(const char* arg)
```
Is used for crating strings, which represents and manipulates a sequence of characters
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
Is also used for extending string, but in this case with another string and returns a merged string
* **base** - some string to be extended
* **tail** - string to be extended with