# COMP211 - Checkoff 3

## Introduction

NumPy is a well-known Python library implemented in C that combines the friendly interface of Python with the high memory and exeuction efficiencies of C. I wanted to compare the performance of operations conducted via pure Python vs. Python with NumPy while also learning how libraries implemented in C are compiled for and called by Python. Through this exploration, I was able to clearly see the difference in time efficiency between Python and NumPy and noticed unique patterns in their performances. In general, NumPy performs better than Python, but when operations were performed on smaller arrays, Python began to outperform NumPy.

## Presentation

The presentation slides are stored in `slides.pdf`.

## Code Examples

### implement_add

I explored how C files are compiled into usable code for Python, and how Python calls functions from the compiled library.
This folder contains 2 files:
- `add.c`: returns the sum of 2 given numbers
- `add.py`: calls add() from `add.c` to add 10 & 20

`add.c` does not need to be run; the main focus is on `add.py`. Before running `add.py`, you must compile `add.c` properly by running the command "gcc add.c -o add.so -shared -fPIC" in the terminal.

### compare_add.py

I compared the performance of adding 2 arrays of various sizes in Python vs. NumPy. NumPy must be installed on your machine for the code to run properly. When `compare_add.py` is run, you will be prompted twice: first to enter an array siz, second to enter the number of trials. The array size is required, the number of trials is not and its default value is 1. For example, entering
- `100` then `10` will add arrays of size 100 ten times.
- `100` then `\n` will add arrays of size 100 one time.
- `\n` will immediately throw an error and will not prompt a second time.

After entering the prompts, `compare_add.py` will calculate the mean performance time of adding arrays in Python/NumPy across all trials. The means of both the Python and NumPy operations will be printed to the terminal.
