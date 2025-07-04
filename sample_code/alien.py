alien_0 = {'color':'green','poits':5}
print(alien_0['color'])
print(alien_0['poits'])
#增加键值对
print(alien_0)
alien_0['x_poits'] = 0
alien_0['y_piits'] = 25
print(alien_0)
#修改键对值
print(f"old color is {alien_0['color']}")
alien_0['color'] = 'red'
print(f"Now color is {alien_0['color']}")