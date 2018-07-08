"""

找出1~9999之间的所有完美数

能整除本身的所有不重复因子的和等于自己的数

ps: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

"""

import math

for x in range(1, 10000):
    sum = 0 
    for y in range(1 , int(math.sqrt(x)) + 1):
        if x % y == 0:
            sum += y
            if y > 1 and x / y != y:
                sum += x / y
    if x == sum:
        print(x)
