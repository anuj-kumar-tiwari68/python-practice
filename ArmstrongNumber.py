n = int(input("enter a number"))
num = n
result = 0
nod = len(str(n))
while num > 0:
    ld = num % 10
    result = result + (ld**nod)
    num = num//10
print(result == n)



