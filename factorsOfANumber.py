
n = int(input("please enter a number: "))
from math import sqrt
result = []
# for i in range(1,n//2):
#     if n % i == 0:
#         # print(i)
#         result.append(i)
# result.append(n)
# print(result)
for i in range(1,int(sqrt(n)+1)):
    if n % i == 0:
        result.append(i)
        if n // i != i:
            result.append(n//i)
print(sorted(result))


