#Task1.3
#Write a python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form
x = input()
words = sorted(set(x.split()))
print(words)