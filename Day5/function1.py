from random import randint

"""
    摇色子
    
    :param n: 色子的个数
    
    :return: n颗色子点数之和
"""

def roll_dice(n=2):
    factor = 0
    for _ in range(n):
        factor += randint(1, 6)
    return factor


total = int(input('n=: '))

print(roll_dice(total))
print()

def add(a=0, b=0, c=0):
    return a+b+c

print(add(1,2))
print(add(1,2,3))
print(add(1,2,4))
print(add(1,2, add(1,3,5)))
print()