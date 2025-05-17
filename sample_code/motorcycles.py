motorcycle = ['honda','yamaha','suzuki']

print   ('\n')
print	( f'原本 {motorcycle}' )
motorcycle[0] = 'ducati'
print	(f'修改 {motorcycle}' )
print   ('\n')


print	("增加 [列表名].append('[value]')")
print	( f'原本 {motorcycle}' )
motorcycle.append('ducati')
print	(f'增加 {motorcycle}')
print   ('\n')

print	("插入 [列表名].insert(【index】，'[value]')           ---在index位置后，增加节点值为value")
print	( f'原本 {motorcycle}' )
motorcycle.insert(1,'ducati')
print	(f'插入 {motorcycle}')
print   ('\n')

print	("删除 del [列表名] [index]                           ---删除节点 [index],根据元素位置删除")
print	( f'原本 {motorcycle}' )
del motorcycle[0]
print	(f'删除 {motorcycle}       ---删除第一个节点del [列表名][0]')
print   ('\n')


print	("弹出  [列表名],pop()                                ---弹出列表最后一个元素，并原列表删除它")
print	( f'原本 {motorcycle}' )
a=motorcycle.pop()
print	(f'弹出 {motorcycle}                 ---弹出后的列表')
print	(f'      {a}                                        ---弹出的元素')
print   ('\n')

print	("  [列表名].remove('[value]')                                ---根据值删除，列表元素")
print	( f'原本 {motorcycle}' )
b = 'yamaha'
motorcycle.remove(b)
print	(f'删除 {motorcycle}                 ---弹出后的列表')
print	(f'      {b}                                        ---弹出的元素')
print   ('\n')

