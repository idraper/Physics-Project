### Program to generate frequencies from signal ###

CC = g++
CPFLAGS = -Og -Wall



df_trans.out : main.o df_trans.o
	$(CC) $(CPFLAGS) -o df_trans.out main.o df_trans.o
 
main.o : main.cpp df_trans.h
	$(CC) $(CPFLAGS) -c main.cpp df_trans.h	

df_trans.o : df_trans.h df_trans.cpp
	$(CC) $(CPFLAGS) -c df_trans.h df_trans.cpp

.PHONY: clean
clean:
	rm *.o *.h.gch df_trans.out
	



