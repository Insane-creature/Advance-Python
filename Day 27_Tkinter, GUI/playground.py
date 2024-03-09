def add(*args):
    sum = 0
    print(type(args))
    for i in args:
        sum += i
    return sum

print(add(5,2,4))

# NOTE: In *args, args here store values in Tuple 
# NOTE: In **args, args here store values in Dictionary

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
   
# calculator(add = 3, multiply = 5)
# calculator2(2,add = 3, multiply = 5)
    
# def test(**args):
#     print(args)

# test()