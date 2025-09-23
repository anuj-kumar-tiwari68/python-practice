# WAP to find max and min in a set
# a = {1,2,3,4,5}
# print(max(a))
# print(min(a))


# WAP to find common elements in three lists using sets
# a = [1,2,3,4,5,6]
# b = [5,6,7,8,9]
# c = [11,12,13,14,5,6]
# print(set(a) & set(b) & set(c))


# WAP to find difference between two sets
# a = {1,2,3,4,5,6}
# b = {5,6,7,8,9}
# print(a - b)
# print(a.difference(b))


# WAP to remove an item from a set if it is present in set
# a = {1,2,3,4,5,6}
# a.discard(3)
# print(a)


# WAP to check if a set is a subset of another set
a = {1,2,3,4,5}
b = {2,3,4}
print(b.issubset(a))
print(a.issubset(b))