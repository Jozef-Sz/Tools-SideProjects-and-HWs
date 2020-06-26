#include <stdio.h>

#include "test.h"
#include "../src/strlib.h"


TESTRESULT str_test()
{
    TESTRESULT result;

    return result;
}

TESTRESULT strpush_test()
{
    TESTRESULT result = { 1, "safsdf asdf asd" };
    int number = 0;
    for (int i = 0; i < 10000; i++)
        number += 10;
    return result;
}

int main()
{
    TEST* testing = create_testpool();
    
    add_testsubject(testing, &str_test, "str_test");
    add_testsubject(testing, &strpush_test, "strpush_test");

    evaluate_testpool(testing);
    return 0;
}
