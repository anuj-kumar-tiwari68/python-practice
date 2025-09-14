# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# print(type(fruits))
# print(fruits[0:2])
# print(fruits[::-1])

# list iteration using for loop
fruits = ["apple", "banana", "cherry","orange","papaya"]
# for i in fruits:
#     print(i)

# iteration using for loop with range and length function
# for i in range(len(fruits)):
#     print(fruits[i])

# iteration using while loop
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i = i + 1
#
# shorthand for loop
# [print(i) for i in fruits] # way 1
[print(fruits[i]) for i in range(len(fruits))] #  way 2