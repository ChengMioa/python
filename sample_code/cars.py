cars = ['bmw', 'audi', 'toyota', 'subaru']

# 原始列表
print('原始列表：')
print(cars)
print()

# 永久正序排序
cars.sort()
print('永久正序排序后：')
print(cars)
print()

# 永久逆序排序
cars.sort(reverse=True)
print('永久逆序排序后：')
print(cars)
print()

# 临时正序排序
print('临时正序排序：')
print(sorted(cars))
print('排序后原列表：')
print(cars)
print()

# 临时逆序排序
print('临时逆序排序：')
print(sorted(cars, reverse=True))
print('排序后原列表：')
print(cars)
print()

# 反转列表
cars.reverse()
print('反转列表后：')
print(cars)
print()

# 再次反转，恢复原顺序
cars.reverse()
print('再次反转后（恢复原顺序）：')
print(cars)
print()

# 列表长度
print(f'列表长度：{len(cars)}')