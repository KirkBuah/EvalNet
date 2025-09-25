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
	$(CC) -O3 -march=native -mtune=native -ffast-math -fopenmp --std=gnu11 -I$(PYTHON_DIR)/include/python$(PYTHON_VERSION)/ -I$(VIRTUALENV_DIR)/lib/python$(PYTHON_VERSION)/site-packages/numpy/_core/include -fPIC --shared -o mmm_ops.so mmm_ops.c
