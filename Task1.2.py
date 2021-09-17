#Task 1.2
#Write a python program to count the number of characters(characters frequency) in a string(ignore case of letters)
x = input()
dict = {}
for n in x:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)    