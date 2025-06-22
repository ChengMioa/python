print("年龄阶段判断")
age=int(input("输入年龄："))
print("现在的年龄阶段是:")
if age < 2:
    print("婴儿")
elif age >= 2 and age < 4:
    print("幼儿")
elif age >= 4 and age < 13:
    print("儿童")
elif age >= 13 and age < 18:
    print("少年")
elif age >= 18 and age < 65:
    print("中青年")
else:
    print("老年人")