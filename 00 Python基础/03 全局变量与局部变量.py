
#局部变量 
i=5 #全局变量 
def func1(n):
	n=3
	# 打印结果 3
	print(n)
func1(i)
# 打印结果 5 （函数不影响传入的对象）
print(i)
print('--------------------')

def func2():
	#指定i为全局变量
	global i
	i=3
	# 打印结果 3
	print(i)
func2()
# 打印结果 5 （global指定了全局变量）
print(i)