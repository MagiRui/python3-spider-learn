#coding:utf8
#author:MagiRui

def func():

    return 1

def gen():

    yield 1


print(type(func))
print(type(gen))

print(type(func()))
print(type(gen()))


def square():

    for x in range(4):

        yield x ** 2

square_gen = square()
for x in square_gen:
    print(x)



def yield_step():

    yield 1
    yield 2
    yield 3

testYield = yield_step()
for ty in testYield:

    print(ty)