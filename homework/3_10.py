list = ['宁静','山川','瓦尔登湖','自然','上海']

number = len(list)
print(f'原始数据\t{list}\n')

#弹出
tan_chu =list.pop()
print(f'现在弹出一个元素:{tan_chu}')
print(list)
print()

#末尾增加
list.append('自由')
print(list)

#插入
list.insert(1,'科学')
print(f"插入{list[2]}后列表:{list}\n")

#确定删除
a = list[3]
del list[3]
print(f'删除{a}后{list}\n')

#模糊
a = '科学'
list.remove(a)
print(f'模糊删除{a}后{list}\n')


'''
---  排序开始  --- 
'''
list_number=[1,6,7,23,5,7,-2]
print(list_number)
print()
#假性排序
    #顺
print(sorted(list_number))
    #逆
print(sorted(list_number,reverse=True))
print()

#真改变顺序排序
    #顺
list_number.sort()
print(list_number)
    #逆
list_number.sort(reverse=True)
print(list_number)
print()

#真反向输出
list_number.reverse()
print(list_number)

list_number.reverse()
print(list_number)