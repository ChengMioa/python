#嘉宾名单
name_list=['XuJie','ZhangHua','LiLin','GuTianLei','ChengLei']

print (f"\n我最近搬新家了，\n 诚挚的邀请你们： \n{name_list[0]},{name_list[1]},{name_list[2]},{name_list[3]},{name_list[4]} \n 来我新家吃饭\n\n ")
print ()


print (f'{name_list[2]}：不好意思我要缺席了,你换ChengMiao吧，他是乐子人，最合适去了（活跃气氛）。世事无常，十落九空，才是人生常态')
#print ()
print (f"{name_list[0]}: 那好吧,我就去邀请ChengMiao")
print ()

a = 'ChengMiao'
name_list[2] = a

print (f"\n我最近搬新家了，\n 诚挚的邀请你们： \n{name_list[0]},{name_list[1]},{name_list[2]},{name_list[3]},{name_list[4]} \n 来我新家吃饭\n\n ")
print ()

print (f"{name_list[0]}:我找到一张大桌子，可以邀请更多的人\n我要邀请，WenLian,ZangTon,PaoLe")
a,b,c='WenLian','ZangTon','PaoLe'
name_list.insert(0,a)
d=len(name_list)//2
name_list.insert(d,b)
name_list.append(c)
print ()
print ()

print (f"\n我最近搬新家了，\n 诚挚的邀请你们： \n{name_list[0]},{name_list[1]},{name_list[2]},{name_list[3]},{name_list[4]},{name_list[5]},{name_list[6]},{name_list[7]} \n 来我新家吃饭\n\n ")
print ()

print (f"{name_list[0]}:怎么回事只有两份餐具了，无法补充，好吧\n")

a = name_list.pop()
print (f"不好意思{a},特殊原因无法邀请您了，下次才能，我的朋友原谅我，按先后顺序只能邀请前两个人\n")

a = name_list.pop()
print (f"不好意思{a},特殊原因无法邀请您了，下次才能，我的朋友原谅我，按先后顺序只能邀请前两个人\n")

a = name_list.pop()
print (f"不好意思{a},特殊原因无法邀请您了，下次才能，我的朋友原谅我，按先后顺序只能邀请前两个人\n")

a = name_list.pop()
print (f"不好意思{a},特殊原因无法邀请您了，下次才能，我的朋友原谅我，按先后顺序只能邀请前两个人\n")

a = name_list.pop()
print (f"不好意思{a},特殊原因无法邀请您了，下次才能，我的朋友原谅我，按先后顺序只能邀请前两个人\n")

a = name_list.pop()
print (f"不好意思{a},特殊原因无法邀请您了，下次才能，我的朋友原谅我，按先后顺序只能邀请前两个人\n")
print ()



print (f"您好\n{name_list[0]},{name_list[1]}\n诚挚的邀请你们\n来我新家吃饭\n")

del name_list[1]
del name_list[0]
print ()
print (name_list)







