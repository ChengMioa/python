tests =['pong','ping','abs','ABS','delete','DELETE',
        1,3,6,7,'pong']
print(tests)
print("\n")
#---------检查两个字符串是否相等-----------#

print("Is 'pong' == 'ping'? I predict False.")
print(tests[0] == tests[1])

print("Is  'pong' =='pong'? I predict true.")
print(tests[0] == tests[-1])
print()
#---------用lower()方法的条件测试---------#

print("Is 'abs' ==('ABS').lower()? I predict true.")
print(tests[2] == tests[3].lower())

print("Is 'delete' ==('DELETE').lower()? I predict true.")
print(tests[4] == tests[5].lower())
print()

#涉及相等 大于 小于 大于等于 小于等于数值比较#
print("Is 1 == 3 ? I predict false.")
print(tests[-5]==tests[-4])
print("Is 3 > 1 ? I predict true.")
print(tests[-4]>tests[-5])
print("Is 1 < 3 ? I predict true.")
print(tests[-5]<tests[-4])
print("Is 6 <= 7 ? I predict true.")
print(tests[-3]<=tests[-2])
print("Is 1 >= 7 ? I predict false.")
print(tests[-5]>=tests[-2])
print()
#------使用关键字and 和 or 的条件判断------#
print("and:")
print("Is 1 != 3 and 1 < 3 I predict true.")
print(tests[-5]!=tests[-4] and tests[-5]<tests[-4])
print("Is 1 == 3 and 1 < 3 I predict flase.")
print(tests[-5]==tests[-4] and tests[-5]<tests[-4])
print("or:")
print("Is 1 != 3 or 1 < 3 I predict true.")
print(tests[-5]!=tests[-4] or tests[-5]<tests[-4])
print("Is 1 == 3 or 1 < 3 I predict true.")
print(tests[-5]==tests[-4] or tests[-5]<tests[-4])
print("Is 1 == 3 or 1 > 3 I predict false.")
print(tests[-5]==tests[-4] or tests[-5]>tests[-4])
print()
#------测试特定的值是否在列表------#
a=7
print(f"is {a} in the list,i predict true")
print(a in tests)
#-----测试特定的值是否不在列表------#
a='abact'
print(f"is {a} in the list,i predict false")
print(a in tests)
a='abact'
print(f"is {a} not in the list,i predict true")
print(a not in tests)