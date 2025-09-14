# a = ["Ross","Rachel","Monica","Joe"]
# a[0],a[3]=a[3],a[0]
# print(a)
# a.insert(1,"Taylor")
# print(a)
# a.pop(2)
# print(a)

b = [1,7,12,100]
d = 1
for i in b:
    d *= i
print(d)


# c = 0
# for i in b:
#     if i > c:
#         c = i
# print(c)

smallest = b[0]
for i in range(1,len(b)):
    if b[i] < smallest:
        smallest = b[i]
print(smallest)




