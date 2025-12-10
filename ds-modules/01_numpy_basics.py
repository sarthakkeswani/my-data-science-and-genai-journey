import numpy as np
print("NumPy Version:", np.__version__)

arr = np.array([1,2,3,4,5])
print(arr)
print("Type:",type(arr))
print("Data type:",arr.dtype)

print(arr + 5)
print (arr * 2)

matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)
print("Shape:",matrix.shape)
print("Rows:",matrix.shape[0])
print("Cols:",matrix.shape[1])

zeros = np.zeros((3,3))
ones = np.ones((2,4))
rand = np.random.rand(3,3)      # uniform distribution
rand_int = np.random.randint(1, 10, (3,3))

print(zeros)
print(ones)
print(rand)
print(rand_int)

arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(2,3)

print(arr)
print(reshaped)

data = np.array([10, 20, 25, 30, 40])

print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.var(data))
print(np.min(data))
print(np.max(data))