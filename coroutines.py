#Coourutines - сопрограммы - это генераторы, которые в процессе работы могут принимать какие-нибудь данные методом send(
#yield from
from sys import exception
from inspect import getgeneratorstate
"""
def subgen():
    x = 'ready to accept message'
    message = yield x
    print('Subgen: ', message)
"""
def coroutines(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class NewException(Exception):
    pass

@coroutines
def average():
    count = 0
    summa = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except NewException:
            print('-------------------------')
            break
        else:
            count += 1
            summa += x
            average = round(summa / count, 2)

    return average