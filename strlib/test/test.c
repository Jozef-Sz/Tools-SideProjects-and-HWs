#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "test.h" 


TEST* create_testpool()
{
    static TEST pool;
    pool.test_subjects = malloc((int)DEFAULT_POOL_SIZE * (int)sizeof(testresult_func_ptr));
    pool.indetifiers = malloc(sizeof(char*) * 10);
    pool.amount = 0;
    pool.cap = DEFAULT_POOL_SIZE;
    return &pool;
}

void add_testsubject(TEST* pool, testresult_func_ptr fn, char* identifier)
{
    if (pool->amount + 1 > pool->cap)
    {
        pool->cap += 5;
        // Realloc could return NULL, so this edge case should be treated. For now it stays untreated.
        pool->test_subjects = realloc(pool->test_subjects, pool->cap * (int)sizeof(testresult_func_ptr));
        pool->indetifiers = realloc(pool->indetifiers, pool->cap * (int)sizeof(char*));
        pool->test_subjects[pool->amount] = fn;
        pool->indetifiers[pool->amount] = identifier;
        pool->amount++;
    }
    else
    {
        pool->test_subjects[pool->amount] = fn;
        pool->indetifiers[pool->amount] = identifier;
        pool->amount++;
    }
}

void evaluate_testpool(TEST* pool)
{
    clock_t start, end;
    double cpu_time_used;
    double time_elapsed = 0;
    int failures = 0;

    for (int i = 0; i < pool->amount; i++)
    {
        char* func_name = pool->indetifiers[i];
        printf("=== RUN       %s\n", func_name);
        start = clock();
        TESTRESULT result = pool->test_subjects[i]();
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        if (result.success == 1)
            printf("--- PASS:     %s (%.4fs)\n", func_name, cpu_time_used);
        else
        {
            printf("--- FAIL:     %s (%.4fs)\n", func_name, cpu_time_used);
            failures++;
        }
    }
    printf("----------------------------------------\n");
    printf("----------------------------------------\n");
    if (failures == 0) printf("Succes tests passed.");
    else printf("Test failed. Failed %d test out of %d.\n", failures, pool->amount);

    

    free(pool->test_subjects);
    free(pool->indetifiers);
}