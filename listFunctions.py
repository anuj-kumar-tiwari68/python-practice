# fruits = ['apple', 'banana', 'cherry',"orange"]
# print(fruits)
# # to find length of a list
# print(len(fruits))
# # to count an occurrences of a particular element
# print(fruits.count("apple"))
# # to add to the list
# fruits.append("papaya")
# print(fruits)
#
# # to add to a specific location
# fruits.insert(1,"guava")
# print(fruits)
# # to remove from a list
# fruits.remove("papaya")
# print(fruits)
# # to remove from a certain location
# print(fruits.pop(2))
# print(fruits)

# *********************** part 2 **********************

fruits = ['apple', 'banana', 'cherry',"orange"]

# to create a copy of list
b = fruits.copy()
print(b)
# to access an element
print(fruits.index('banana'))
# to extend the list
c = ["tomato","kiwi"]
fruits.extend(c)
# to reverse the list
fruits.reverse()
print(fruits)
# to sort the list
fruits.sort()
print(fruits)
# to clear all the data from the list
fruits.clear()
print(fruits)
