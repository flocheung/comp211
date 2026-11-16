import ctypes

# gcc add.c -o add.so -shared -fPIC

# Load compiled C library
lib = ctypes.CDLL("./add.so")

# Specify argument and return types
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

# Call C function
result = lib.add(10, 20)

print(result)  # 30