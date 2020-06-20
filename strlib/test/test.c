#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../src/strlib.h"

#define DEFAULT_POOL_SIZE 10

// TESTRESULT is the return type of a testing function
typedef struct {
	int success;
	char* status_msg;
} TESTRESULT;

// testresult_func_ptr is the type declaration for
// pointers to testing functions
typedef TESTRESULT (*testresult_func_ptr)();

// TEST contains testing subjects(which is btw 
// a pointer pointer) and their amount
typedef struct {
    testresult_func_ptr* test_subjects;
    int* amount;
    int* cap;
} TEST;

TEST create_testpool()
{
    TEST pool;
    pool.test_subjects = malloc((int)DEFAULT_POOL_SIZE * (int)sizeof(testresult_func_ptr));
    pool.amount = malloc(sizeof(int));
    pool.cap = malloc(sizeof(int));
    *pool.amount = 0;
    *pool.cap = DEFAULT_POOL_SIZE;
    return pool;
}

void add_testsubject(TEST pool, testresult_func_ptr* fn)
{
    printf("status %d %d\n", *pool.amount, *pool.cap);
    if (*pool.amount + 1 > *pool.cap)
    {
        *pool.cap += 5;
        pool.test_subjects = realloc(pool.test_subjects, *pool.cap * (int)sizeof(testresult_func_ptr));
        printf("Inserting %d address %x\n", *pool.amount, fn);
        pool.test_subjects[*pool.amount] = fn;
        (*pool.amount)++;
        printf("Reallocation was needed!\n");
    }
    else
    {
        printf("Inserting %d address %x\n", *pool.amount, fn);
        pool.test_subjects[*pool.amount] = fn;
        (*pool.amount)++;
        printf("Adding went fine!\n");
    }
}

TESTRESULT str_test()
{
    printf("If u're reading this, ur job today is finished\n");
    TESTRESULT result = { 0, "Failed at x y." };
    return result;
}

int main()
{
    TEST testing = create_testpool();
    
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);
    add_testsubject(testing, &str_test);

    printf("Fuuuuuuuck %x\n", testing.test_subjects[0]);
    testing.test_subjects[1]();

    return 0;
}
