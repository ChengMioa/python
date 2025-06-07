my_foods = ['pizza','falafel','carrot cake']

friend_foods = my_foods[:]
print('My favorite foods are:')
my_foods.append('cannoli')
for i in my_foods:
    print(i)

print("\nMy friend's favorite foods are:")
friend_foods.append('ice-cream')
for i in friend_foods:
    print(i)