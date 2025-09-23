# a = {"Ironman","Thor","Smith","CaptainAmerica"}
#add
# a.add("SpiderMan")
# # print(a) # added on random places
#
# #pop
# a.pop()# removes random element
# print(a)

#remove => Removes element (Error if not present)
# a.remove("SpiderMan")
# print(a)

#discard => Removes element (No error if missing)
# a.discard("SpiderMan")
# print(a)

# copy()
# b = a.copy()
# print(b)


#**********************************PART 2******************************************

# a = {"Ironman","Thor","Hulk","CaptainAmerica"}
# b = {"Superman","batman","wonder-woman"}
# c = {"Thor","Hulk"}

# # isdisjoint()
# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# issubset
# print(a.issubset(b))
# print(c.issubset(a))

# issuperset
# print(a.issuperset(c))
#
# # update => unique values updated
# a.update(c)
# print(a)

# clear()
# a.clear()
# print(a)

# ++++++++++++++++++++++++++++++++++ part 3 ++++++++++++++++++++++++++++++++++

a = {"Ironman","Thor","Hulk","CaptainAmerica"}
b = {"Superman","batman","wonder-woman"}
c = {"Thor","Hulk"}

# union
# print(a.union(b))

# difference
# print(a.difference(c))

#difference_update()
# a.difference_update(c)
# print(a)

# intersection
# print(a.intersection(c))

# intersection_update
# a.intersection_update(c)
# print(a)

# symmetric_diffeence
# print(a.symmetric_difference(c))

# symmetric_difference_update
a.symmetric_difference_update(c)
print(a)