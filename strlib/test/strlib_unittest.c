#include <stdio.h>

#include "test.h"
#include "../src/strlib.h"


TESTRESULT str_test()
{
    printf("If u're reading this, ur job today is finished\n");
    TESTRESULT result = { 0, "Failed at x y." };
    return result;
}

int main()
{
    TEST* testing = create_testpool();
    
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

    TESTRESULT a = testing->test_subjects[0]();

    printf("Success %d, status msg %s\n", a.success, a.status_msg);

    return 0;
}