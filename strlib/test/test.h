#ifndef TEST_H
#define TEST_H

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
    int amount;
    int cap;
} TEST;


TEST* create_testpool();

void add_testsubject(TEST* pool, testresult_func_ptr fn);

#endif