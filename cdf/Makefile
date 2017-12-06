CC=gcc
CFLAGS=-I.
# DEPS = hello.h
OBJ = cdf.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

cdf: $(OBJ)
	gcc -o $@ $^ $(CFLAGS)
