#include <stdio.h>
#include "strlib.h"

int main() 
{
    string name = str("Joco");
    printf("Here is our string: %s|\n", name.str);
    printf("Length %d\n", *name.length);
    printf("Capacity %d\n", *name.capacity);

    // strpush(name, " is");
    // printf("Here is our string: %s|\n", name.str);
    // printf("Length %d\n", *name.length);
    // printf("Capacity %d\n", *name.capacity);

    // strpush(name, " the b");
    // printf("Here is our string: %s|\n", name.str);
    // printf("Length %d\n", *name.length);
    // printf("Capacity %d\n", *name.capacity);

    // string the = substr(name, 8, 10);
    // printf("Here is out substring: |%s|\n", the.str);
    // printf("Length %d\n", *the.length);
    // printf("Capacity %d\n", *the.capacity);

    // string pika = str("Pika");
    // printf("Here is our string: %s|\n", pika.str);
    // printf("Length %d\n", *pika.length);
    // printf("Capacity %d\n", *pika.capacity);
    // string boo = str("boo");
    // printf("Here is our string: %s|\n", boo.str);
    // printf("Length %d\n", *boo.length);
    // printf("Capacity %d\n", *boo.capacity);
    // stradd(pika, boo);
    // printf("Here is our string: %s|\n", pika.str);
    // printf("Length %d\n", *pika.length);
    // printf("Capacity %d\n", *pika.capacity);
    
    string namecopy = strcopy(name);
    printf("Here is our string: %s|\n", namecopy.str);
    printf("Length %d\n", *namecopy.length);
    printf("Capacity %d\n", *namecopy.capacity);

    strpush(namecopy, " hello");
    printf("Here is our string: %s|\n", namecopy.str);
    printf("Length %d\n", *namecopy.length);
    printf("Capacity %d\n", *namecopy.capacity);
    printf("Here is our string: %s|\n", name.str);
    printf("Length %d\n", *name.length);
    printf("Capacity %d\n", *name.capacity);

    printf("%d", contains(namecopy, "o"));


    strdel(name);
    strdel(namecopy);
    // strdel(the);
    // strdel(pika);
    // strdel(boo);
    return 0;
}