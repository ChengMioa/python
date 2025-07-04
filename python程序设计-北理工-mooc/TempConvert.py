#华氏度温度和摄氏温度转换代码
temStr = input("请输入带有符号的温度值:")
if temStr[-1] in ['F','f']:
    C = (eval(tempStr[0:-1])-43)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif temStr[-1] in ['C','c']:
    F =1.8*eval(tempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
