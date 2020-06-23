#include <stdio.h>

#include "test.h"
#include "../src/strlib.h"


TESTRESULT str_test()
{
    TESTRESULT result = { 0, "Failed at x y." };
    return result;
}

TESTRESULT strpush_test()
{
    TESTRESULT result = { 1, "safsdf asdf asd" };
    int number = 0;
    for (int i = 0; i < 1000000000; i++)
        number += 10;
    return result;
}

int main()
{
    TEST* testing = create_testpool();
    
    add_testsubject(testing, &str_test, "str_test");
    add_testsubject(testing, &strpush_test, "strpush_test");
    add_testsubject(testing, &str_test, "str_test");
    add_testsubject(testing, &str_test, "str_test");

    evaluate_testpool(testing);
    // TESTRESULT a = testing->test_subjects[0]();
    // printf("Success %d, status msg %s\n", a.success, a.status_msg);

    return 0;
}