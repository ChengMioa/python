current_users=['WAD','das','awq','WSa','KTY']
new_users=['WAD','awq','sdf','sdgf','swe']
copys=[]
for new_user in new_users:
    if new_user in current_users:
        print(f"已被使用{new_user}输入别的用户名")
    else:
        print(f"未被使用{new_user}")
        copys.append(new_user.lower())

for current_user in current_users:
    copys.append(current_user.lower())     
    
print(copys)