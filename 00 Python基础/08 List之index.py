int_month=[1,2,3,4,5]


'''
# 理解下标

index=len(int_month)-1
# list从零开始,如果取5报错
last_value=int_month[index]
print(len(int_month))
print(last_value)
# 倒着数
print(int_month[-2])
'''

'''
# 取片段

# 不含4
print(int_month[2:4])
# 如果取5不报错，因为不含5
print(int_month[2:5])
print(int_month[2:])
'''

