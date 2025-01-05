# Coourutines - сопрограммы - это генераторы, которые в процессе работы могут принимать какие-нибудь данные методом send(
# yield from
#Делегирующий генератор - генератор, вызывающий другой генератор (подгенератор) разбить 1 генератор на несколько
from sys import exception
from inspect import getgeneratorstate

def coroutines(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner

class NewException(Exception):
    pass

@coroutines
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('Exception')
            break
        else:
            print('-------', message)
    return 'Returned from subgen'

@coroutines
def delegator(g):
    """
    while True:
        try:
            data = yield
            g.send(data)
        except NewException as e:
            g.throw(e)
    """
    result = yield from g
    print(result)