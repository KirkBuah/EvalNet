PYTHON_VERSION=3.9# main version; only the number, no space afterwards
PYTHON_DIR=/usr
VIRTUALENV_DIR=../.venv

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
	$(CC) -O3 -march=native -mtune=native -ffast-math -fopenmp --std=gnu11 -lpython3.9 -I/usr/include/python3.9/ -I../evalnet/lib/python3.9/site-packages/numpy/core -fPIC --shared -o mmm_ops.so mmm_ops.c
