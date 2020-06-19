x = input("Please enter word you would like to oob: ")
vowel = ['a','e','i','o','u']
for y in x:
    if y in vowel:
        x=x.replace(y, "oob")
print(x)