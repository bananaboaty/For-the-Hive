x = input("Please enter word you would like to oob: ")
vowel = ['a','e','i','o','u']
i = 0
while i < 100:
    for y in x:
        if y in vowel:
            x=x.replace(y, "oob")
    print(x)
    user = input('Press ENTER to exit: ')
