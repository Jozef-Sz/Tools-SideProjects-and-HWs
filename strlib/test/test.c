#include <stdio.h>
#include <stdlib.h>

#include "test.h" 


TEST* create_testpool()
{
    static TEST pool;
    pool.test_subjects = malloc((int)DEFAULT_POOL_SIZE * (int)sizeof(testresult_func_ptr));
    pool.amount = 0;
    pool.cap = DEFAULT_POOL_SIZE;
    return &pool;
}

void add_testsubject(TEST* pool, testresult_func_ptr fn)
{
    if (pool->amount + 1 > pool->cap)
    {
        pool->cap += 5;
        // Realloc could return NULL, so this edge case should be treated. For now it stays untreated.
        pool->test_subjects = realloc(pool->test_subjects, pool->cap * (int)sizeof(testresult_func_ptr));
        pool->test_subjects[pool->amount] = fn;
        pool->amount++;
        printf("Reallocation was needed!\n");
    }
    else
    {
        pool->test_subjects[pool->amount] = fn;
        pool->amount++;
        printf("Adding went fine!\n");
    }
}