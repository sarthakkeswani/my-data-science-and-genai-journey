import numpy as np

#1 array of num 1 to 20

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(arr[0:5])
print(arr[-5:])
print(arr[1::2])

matrix = np.random.randint(1,50,(3,3))
print(np.max(matrix))
row, col = np.unravel_index(np.argmax(matrix), matrix.shape)
print(matrix[row])
print(matrix[:,col])

reshaped = arr.reshape(4,5)
print(reshaped[0])
print(reshaped[:,-1])
print(np.median(reshaped))

stat=np.array([3, 5, 7, 11, 13, 17, 19])
print(np.mean(stat))
print(np.median(stat))
print(np.var(stat))