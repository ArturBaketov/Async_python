from time import time
#генераторы - это функции, отдающая результат
#Передача контроля выполнения программы

def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

        sum = 234 + 234
        print(sum)

def gen():
    yield 1
    yield 2
    yield 3

gen = gen_filename()


#Round Robin событийный цикл Карусель

def gen1(s):
    for i in s:
        yield i

g = gen('Me')

def gen2(n):
    for i in range:
        yield i

g1 = gen1('Me')
g2 = gen2(4)

tasks = [g1, g2]

while task:
    task = task.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass