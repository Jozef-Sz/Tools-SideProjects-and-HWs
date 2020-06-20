main: ./obj/sandbox.o ./obj/strlib.o
	gcc obj/sandbox.o obj/strlib.o -o bin/main

./obj/sandbox.o: ./src/sandbox.c
	gcc -c src/sandbox.c -o obj/sandbox.o

./obj/strlib.o: ./src/strlib.c ./src/strlib.h
	gcc -c src/strlib.c -o obj/strlib.o

# Run sandox enviroment(dev testing)
run:
	@./bin/main

# Compile unit testing
test: ./obj/strlib_unittest.o ./obj/test.o ./obj/strlib.o
	gcc obj/strlib_unittest.o obj/test.o  obj/strlib.o -o bin/test

./obj/strlib_unittest.o: ./test/strlib_unittest.c 
	gcc -c test/strlib_unittest.c -o obj/strlib_unittest.o

./obj/test.o: ./test/test.c ./test/test.h
	gcc -c test/test.c -o obj/test.o

# Run unit testing
runtest:
	@./bin/test



ifeq ($(OS), Windows_NT)
# FYI: bar stands for "Build and Run"
bar: ./obj/sandbox.o ./obj/strlib.o 
	@gcc obj/sandbox.o obj/strlib.o -o bin/main && bin\main
	
bartest: ./obj/strlib_unittest.o ./obj/test.o ./obj/strlib.o 
	@gcc obj/strlib_unittest.o obj/test.o  obj/strlib.o -o bin/test && bin\test

clear:
	del obj\*.o bin\*.exe

else
# FYI: bar stands for "Build and Run"
bar: ./obj/sandbox.o ./obj/strlib.o 
	@gcc obj/sandbox.o obj/strlib.o -o bin/main && ./bin/main
	
bartest: ./obj/strlib_unittest.o ./obj/test.o ./obj/strlib.o 
	@gcc obj/strlib_unittest.o obj/test.o  obj/strlib.o -o bin/test && ./bin/test

clear:
	rm obj/*.o bin/*

endif