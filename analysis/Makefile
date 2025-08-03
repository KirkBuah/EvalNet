PYTHON_VERSION=3.9# main version; only the number, no space afterwards

CC=gcc
CCFLAGS=

all: extension-functions.o percentile.o mmm_ops.so

clean:
	rm -f *.o *.so

extension-functions.o: extension-functions.c
	$(CC) $(CCFLAGS) -c $<

percentile.o: percentile.c
	$(CC) $(CCFLAGS) -c $<

mmm_ops.so: mmm_ops.c
	$(CC) -O3 -march=native -mtune=native -ffast-math -fopenmp --std=gnu11 -lpython$(PYTHON_VERSION) -I/usr/include/python$(PYTHON_VERSION)/ -fPIC --shared -o mmm_ops.so mmm_ops.c
