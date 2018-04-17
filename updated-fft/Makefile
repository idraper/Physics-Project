### Program to generate frequencies from signal ###

CC = g++
CFLAGS = -Og -Wall



FastFT.out : main.o FastFT.o
	$(CC) $(CPFLAGS) -o FastFT.out main.o FastFT.o

%.o : main.o FastFT.o
 
main.o : main.cpp FastFT.h
	$(CC) $(CPFLAGS) -c main.cpp FastFT.h	

FastFT.o : FastFT.h FastFT.cpp
	$(CC) $(CPFLAGS) -c FastFT.h FastFT.cpp

.PHONY: clean
clean:
	rm *.o *.h.gch FastFT.out
	



