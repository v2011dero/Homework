#Task 1.4
#Create a program that asks the user for a number and then prints out a list of all thev[divisors] of that number
x = int(input())
divisors = []
for i in range(1, x + 1):
    if x % i == 0:
        divisors.append(i)
print(divisors)