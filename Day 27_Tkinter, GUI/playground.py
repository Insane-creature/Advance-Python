def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# print(add(5,2,4))

def calculator(**kwargs):
    # print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

def calculator2(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
   

calculator2(2,add = 3, multiply = 5)