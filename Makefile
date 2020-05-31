main: ./obj/sandbox.o ./obj/strlib.o
	gcc obj/sandbox.o obj/strlib.o -o bin/main

./obj/sandbox.o: ./src/sandbox.c
	gcc -c src/sandbox.c -o obj/sandbox.o

./obj/strlib.o: ./src/strlib.c ./src/strlib.h
	gcc -c src/strlib.c -o obj/strlib.o

run:
	@./bin/main

clear:
	del obj\*.o bin\main.exe

