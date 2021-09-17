# Task 1.6
#Write a program which makes a pretty print of a part of the multiplication table.
a = 2
b = 4
c = 3
d = 7
for i in range(c, d+1):
    print("\t", i, end = "")
print()
for j in range(a, b+1):
    print(j, end = "\t")
    for g in range(c, d+1):
        print(j * g, end = "\t")
    print() 
    