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
test: ./obj/test.o ./obj/strlib.o
	gcc obj/test.o  obj/strlib.o -o bin/test

./obj/test.o: ./test/test.c 
	gcc -c test/test.c -o obj/test.o

# Run unit testing
runtest:
	@./bin/test

ifeq ($(OS), Windows_NT)
clear:
	del obj\*.o bin\*.exe
else
clear:
	rm obj/*.o bin/*
endif



