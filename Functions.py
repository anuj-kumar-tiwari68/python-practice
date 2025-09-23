# def hello():
#     print("Hello World")
# hello()

# def add(a,b): # parameters
#     print(a+b)
# add(1,2)# arguments
#
# def rectangle(length,width): print(length*width)
# rectangle(2,3)

# Arbitrary arguments
def hello(*name):
    print("hello, my name is ",name[1])
hello("John","lisa","arun")