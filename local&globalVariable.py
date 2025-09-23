# local Variable
x = 33
print(x)
def hello():
    global x
    x = 44
    return x
print(hello())
print(x)