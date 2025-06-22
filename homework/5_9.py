names = ['admin','jaden','job','x','cawd']
names=names.clear()
if names:
    for name in names:
        if name == 'admin':
            print(f"hello {name.title()},would you like to see a status report!")
        else:
            print(f"hello {name.title()},thank you for logging in again.")
else:
    print("We need to find somes users!")