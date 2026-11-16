import numpy as np
import time

n = int(input("Enter array size: "))

x = input("Enter # trials (default = 1): ")
trials = int(x) if x.strip() else 1

a_py = list(range(n))
b_py = list(range(n))

a_np = np.arange(n)
b_np = np.arange(n)

py_times = []
np_times = []

for j in range(trials):
    # Pure Python
    start = time.perf_counter()
    result_py = [a_py[i] + b_py[i] for i in range(n)]
    py_time = time.perf_counter() - start

    # NumPy
    start = time.perf_counter()
    result_np = a_np + b_np
    np_time = time.perf_counter() - start

    py_times.append(py_time)
    np_times.append(np_time)

print("Python:", np.mean(py_times))
print("NumPy:", np.mean(np_times))