import numpy

'''
world_alcohol=numpy.genfromtxt("world_alcohol.txt",delimiter=",",dtype=str)
print(type(world_alcohol))
print(world_alcohol)

print(world_alcohol[1,1])  #取出某个值
print(world_alcohol[1])  #取出某个数组
print(world_alcohol[0:1]) #取出某个范围数组（不含最后）
print(world_alcohol[:,0:1]) #取出某个列
print(world_alcohol[:,0:1]) #取出某个范围列
print(world_alcohol[0:1,0:1]) #取出某个范围列，某范围行
# print(help(numpy.genfromtxt))
'''

'''
vector = numpy.array([5,10,15,20])

matrix =numpy.array([[5,10,15,20],[5,10,15,20]])
print(vector)
print(matrix)

print(vector.shape)
print(matrix.shape)

matrix.dtype #numpy array 只能有一个类型
'''


'''
vector = numpy.array([5,10,15,20])
print(vector == 10)

matrix = numpy.array([[5,10,15,20],[25,30,45,50]])
print(matrix == 10)

# 可以当索引
index=(vector == 10)
print(vector[index])

second_column_25=(matrix[:,0] == 25)
print(second_column_25)
print(matrix[second_column_25, :])

'''


