my_pizza = ['pizza hut',"domino's",'papajohns',]
friend_pizza = my_pizza [:]
my_pizza.append('bigpizza')
friend_pizza.append("buitoni")
print('My favorite pizzas are:')
for value in my_pizza:
    print(value)
print()
print("My friend's favorite pizzas are:")
for value in friend_pizza:
    print(value)