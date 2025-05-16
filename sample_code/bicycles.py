bicy = ['trek' , '苹果' , 'redline' , 'specialized']

print (f'普通输出:{bicy[0]}')

print (f'首字母大写(title):{bicy[0].title()}')

print (f'小写输出(lower):{bicy[0].lower()}')

print (f'全部大写(upper):{bicy[0].upper()}')

print (f'索引为3：{bicy[3]}')

print (f'索引为-1：{bicy[-1]}')

print (
'''
	类似与c数组，从0开始数数字，最终是[  0 - (n-1) ] ,0也是一个数字
''')

message = f'我喜欢吃的是:{bicy[1]}'

print (message)
