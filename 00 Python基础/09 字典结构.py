'''
animals=['cat','dog','rabbit']
if 'cat' in animals:
	print('Cat found')
'''

'''	
scores={} # type dict
scores['Jim']=85
scores['Sue']=88
scores['Lyndon']=99
print(scores)
print(scores.keys()) # 打出键值，结果随机
print(scores['Sue'])
'''

'''
scores={
	'Jim':85,
	'Sue':88
} # type dict

print(scores)
print(scores.keys()) # 打出键值，结果随机
print(scores['Sue'])
print('Sue' in scores)
'''

pantry=['a','b','a']
pantry_count={}
for item in pantry:
	if item in pantry_count:
		pantry_count[item]=pantry_count[item]+1
	else:
		pantry_count[item]=1
print(pantry_count)
