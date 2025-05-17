#嘉宾名单
name_list=['XuJie','ZhangHua','LiLin','GuTianLei','ChengLei']

print (f"\n我最近搬新家了，\n \n诚挚的邀请你们： \n\n{name_list[0]},{name_list[1]},{name_list[2]},{name_list[3]},{name_list[4]} \n\n 来我新家吃饭\n\n ")
print ()


print (f'{name_list[2]}：不好意思我要缺席了,你换ChengMiao吧，他是乐子人，最合适去了（活跃气氛）。世事无常，十落九空，才是人生常态')
#print ()
print (f"{name_list[0]}: 那好吧,我就去邀请ChengMiao")
print ()

a = 'ChengMiao'
name_list[2] = a

print (f"\n我最近搬新家了，\n \n诚挚的邀请你们： \n\n{name_list[0]},{name_list[1]},{name_list[2]},{name_list[3]},{name_list[4]} \n\n 来我新家吃饭\n\n ")
print ()

print (f"{name_list[0]}:我找到一张大桌子，可以邀请更多的人\n我要邀请，WenLian,ZangTon,PaoLe")
a,b,c='WenLian','ZangTon','PaoLe'
name_list.insert(0,a)
d=len(name_list)//2
name_list.insert(d,b)
name_list.append(c)
print ()
print ()

print (f"\n我最近搬新家了，\n \n诚挚的邀请你们： \n\n{name_list[0]},{name_list[1]},{name_list[2]},{name_list[3]},{name_list[4]},{name_list[5]},{name_list[6]},{name_list[7]} \n\n 来我新家吃饭\n\n ")
print ()


