### Task 1.6
#Write a Python program to print all unique values of all dictionaries in a list.
#Examples:
#```
#Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
myDict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
values = []
for i in dict:
    if i.values not in values:
        values.extend(set(i.values()))
print(values)